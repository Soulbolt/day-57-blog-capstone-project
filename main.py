from flask import Flask, render_template
import requests

BLOG_API_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(BLOG_API_ENDPOINT)
    response.raise_for_status
    all_post = response.json()
    return render_template("index.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)
