from flask import render_template, request, redirect, url_for
from forms import app
from forms.forms import PostForm

posts = []

@app.route("/", methods=["GET", "POST"])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = {
            "title": form.title.data,
            "content": form.content.data,
            "content1": form.content1.data,
            "content2": form.content2.data
        }
        posts.append(post)
        return redirect(url_for("index"))
    return render_template("blog.html", form=form, posts=posts)
