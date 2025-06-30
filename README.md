## Inspiration: I wanted make the powerful prophet algorithm available to everyone. By simply uploading your data we can forecast with one click.

## What it does : It takes in demand data in csv format and runs prophet algorithm in aws lambda returns the forecasted data for next seven days in a plot form.

## How we built it : Ui : used streamlit (python)
                                    backend: aws lambda, api gateway
                                    packages used: pandas, prophet

## Challenges we ran into : Bundling the packages required for running the prophet algorithm into lambda function caused a lot problems.  We needed to create a docker container and upload it to aws ecr to resolve. Using docker also caused a lot of problems since iam using windows. The docker images created(oci format) were not compatible with aws lambda. To resolve this we tried many things but finally running  it in aws cloud shell resolved the issues.

## Accomplishments that we're proud of: Its simple and user friendly interface and quickness in getting back results. 

## What we learned: Best way to get all the dependencies in lambda function is using docker, using cloudshell is recommend if on windows.

## What's next for Demand prediction: Give a option for users to edit the type plots that are visible. Or use a different and more powerful algorithm for forecasting.
