from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'KARTHIK PADIYAR UTA ID:1001508245!'

if __name__ == '__main__':
  app.run()
