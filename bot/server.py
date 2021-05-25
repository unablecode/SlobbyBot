from flask import Flask, redirect, url_for, render_template
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/get_toggled_status') 
def toggled_status():
  current_status = flask.request.args.get('status')
  return 'Toggled' if current_status == 'Untoggled' else 'Untoggled'

def run():
  app.run(host='0.0.0.0', port=8080)

def server():
  server = Thread(target=run)
  server.start()
