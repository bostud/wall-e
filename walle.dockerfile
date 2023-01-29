FROM python:3.10
ENV PYTHONUNBUFFERED=1
RUN mkdir app
COPY . /app

WORKDIR /app

RUN python -m pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt
CMD ["uvicorn", "start_app:app", "--reload", "--host", "0.0.0.0", "--port", "8899"]
