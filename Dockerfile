FROM python:3

WORKDIR /ohhellno/my_container/Week13_RichMalloy_Project

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]

