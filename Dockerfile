FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

RUN yum install -y gcc gcc-c++ make libffi-devel openssl-devel wget tar \
    && yum clean all

RUN pip install --upgrade pip \
    && pip install prophet pandas

COPY lambda_function.py .

CMD ["lambda_function.lambda_handler"]
