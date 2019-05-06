FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

ENV FLASK_APP=echo.py

CMD ["python", "-m", "flask", "run", "-h", "0.0.0.0"]
