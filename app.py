from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL API
API_URL = "https://www.dbooks.org/api/recent"

@app.route("/")
def index():
  response = requests.get(API_URL)
  
  if response.status_code == 200:
    data = response.json()
    books = data.get("books", [])
  else:
    books =  []
  return render_template("index.html", books=books)

if __name__ == "__main__":
  app.run(debug=True)