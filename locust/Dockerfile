FROM locustio/locust:0.14.5
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY locustfile.py .
COPY data.py .
