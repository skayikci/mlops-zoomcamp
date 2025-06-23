FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

WORKDIR /app

COPY starter.py .

RUN pip install --no-cache-dir pandas pyarrow scikit-learn

ENTRYPOINT ["python", "starter.py"]

# build with 
# docker build -t duration-predictor .

# run with 
# docker run --platform linux/amd64 -it \
#   -v $(pwd)/data:/app/data \
#   duration-predictor \
#   --year 2023 --month 5

