import json
import pandas as pd
import base64
import io
from prophet import Prophet

def lambda_handler(event, context):
    try:
        # Read file
        if event.get("isBase64Encoded"):
            file_bytes = base64.b64decode(event["body"])
        else:
            file_bytes = event["body"].encode("utf-8")

        df = pd.read_csv(io.StringIO(file_bytes.decode("utf-8")))

        # Validate columns
        if 'date' not in df.columns or 'demand' not in df.columns:
            return {"statusCode": 400, "body": json.dumps({"error": "CSV must contain 'date' and 'demand' columns."})}

        # Format for Prophet
        df['ds'] = pd.to_datetime(df['date'], errors='coerce')
        df['y'] = pd.to_numeric(df['demand'], errors='coerce')
        df = df[['ds', 'y']].dropna()

        if len(df) < 30:
            return {"statusCode": 400, "body": json.dumps({"error": "Not enough data for Prophet model."})}

        # Train Prophet model
        model = Prophet()
        model.fit(df)

        # Forecast next 7 days
        future = model.make_future_dataframe(periods=7)
        forecast = model.predict(future)

        # Prepare result
        result_df = forecast[['ds', 'yhat']].tail(7)
        forecast_data = {
            "date": result_df['ds'].dt.strftime("%Y-%m-%d").tolist(),
            "forecast": result_df['yhat'].round().astype(int).tolist()
        }

        return {
            "statusCode": 200,
            "body": json.dumps(forecast_data),
            "headers": {"Content-Type": "application/json"}
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
