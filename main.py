from flask import Flask, render_template
import requests
from post import Post

get_post = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []

for post in get_post:
    post_content = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_content)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", posts=post_objects, num=num)

if __name__ == "__main__":
    app.run(debug=True)
