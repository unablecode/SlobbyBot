worker: python bot/main.py
heroku ps:scale web=1
web: gunicorn -w 4 server:app 
