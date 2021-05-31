worker: python bot/main.py
web: gunicorn -w 4 server:app --preload
heroku ps:scale web=1
