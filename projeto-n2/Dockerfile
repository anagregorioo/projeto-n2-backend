FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV FLASK_ENV=production
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
