### Getting started

```sh
python -m venv venv
pip install -r requirements.txt
openssl req -x509 -sha256 -nodes -newkey rsa:2048 -days 365 -keyout localhost.key -out localhost.crt
uvicorn main:app --reload --ssl-keyfile localhost.key  --ssl-certfile localhost.crt
```

Then visit https://127.0.0.1:8000 in your browser.
Enable location permission for the page
Click "Get Weather in my city"
