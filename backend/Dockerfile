FROM python:3.9-slim

RUN apt update && apt install -y curl net-tools iputils-ping

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "main:app" , "--host" , "0.0.0.0" , "--port" , "8000"]

