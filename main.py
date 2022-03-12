from app import app

if __name__ == "__main__":
  app.run()
  # sio.run(app, host='localhost', debug=True)
  # sio.connect('http://localhost:5000/chatroom')
  # sio.wait()