from flask import Flask
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def Home():
  return('Hello world!')


if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
  
  