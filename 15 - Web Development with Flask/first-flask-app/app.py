from flask import Flask, render_template, request, redirect, url_for

# 15 - Web Development with Flask
# 15.1 - Introduction to Flask
# 15.2 - Creating a Flask App
# 15.3 - Routing
# 15.4 - Templates
# 15.5 - Forms
# 15.6 - Database
# 15.7 - Deployment
# 15.8 - Testing
# 15.9 - Debugging
# 15.10 - Security
# 15.11 - Error Handling
# 15.12 - Logging


app = Flask(__name__)
posts = {0: {"title": "My First Post", "content": "This is my first post."}}


@app.route("/")
def home():
    return render_template("home.jinja2", posts=posts)


@app.route("/posts")
def get_posts():
    return posts


@app.route("/posts/<int:post_id>")
def get_post_by_id(post_id):
    # return posts[post_id]
    post = posts.get(post_id)
    # return f"Post {post['title']} - content: \n\n{post['content']}"
    if not post:
        return render_template(
            "404.jinja2", message=f"Post not found with post id:{post_id}"
        )
    return render_template("post.jinja2", post=post)


# @app.route("/posts/form")
# def form():
#     return render_template("form.jinja2")


@app.route("/posts/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        # print(title, content)
        # post_id = len(posts)
        posts[len(posts)] = {"title": title, "content": content}
        # return render_template("post.jinja2", post=posts[len(posts) - 1])
        return redirect(url_for("get_post_by_id", post_id=len(posts) - 1))
    return render_template("form.jinja2")


if __name__ == "__main__":
    app.run(debug=True)
