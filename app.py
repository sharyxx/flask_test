from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
  return "b<h1> Hello World</h1>"
@app.route("/login")



if __name__ == "__main__":
  app.run(debug=True,port=80)
