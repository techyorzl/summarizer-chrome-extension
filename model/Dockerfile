FROM pytorch/pytorch

RUN apt update && apt install -y curl net-tools iputils-ping

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "uvicorn" , "model_api:app" , "--host" , "0.0.0.0" , "--port" , "5000" ]