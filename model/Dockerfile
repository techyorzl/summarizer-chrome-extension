FROM python:3.10-slim

WORKDIR /app

COPY /model .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "uvicorn" , "model_api:app " , "--host" , "0.0.0.0" , "--port" , "5000" ]