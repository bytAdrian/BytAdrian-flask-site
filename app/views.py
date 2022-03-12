from app import app
from app import r
from app import q
from app.tasks import scrape_synomyns
from time import strftime
import time

from flask import render_template, request, session
from flask_socketio import SocketIO
from flask_session import Session

Session(app)
sio = SocketIO(app, manage_session=False)

@app.route("/")
def home():
  return render_template("public/home.html")


@app.route("/passwordgenerator")
def password_generator( methods=["GET", "POST"]):

  jobs = q.jobs
  message = None
  syns = None

  if request.args:
    keyword = request.args.get("keyword")
    task = q.enqueue(scrape_synomyns, keyword, result_ttl=86400)
    jobs = q.jobs
    q_len = len(q)
    message = f"task queued at {task.enqueued_at.strftime('%a %d %b %Y %H : %M : %S')}, {q_len} jobs queued"
    syns = task.result

    print(f'synonyms here >> {syns}')
    
    
  return render_template("public/passwordGenerator.html", message=message, jobs=jobs, syns=syns)

@app.route("/chatroom", methods=['GET', 'POST'])
def chatroom():

  return render_template("public/chatroom.html")

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@sio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

  