from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url).json()


@app.route('/')
def home():
    return render_template("index.html",data = response)

@app.route('/post/<id>')
def get_post(id):
    k=int(id)-1
    new_blog = response[k]
    return render_template("post.html",blog = new_blog)




if __name__ == "__main__":
    app.run(debug=True)
