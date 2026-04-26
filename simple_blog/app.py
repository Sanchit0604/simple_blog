# ============================================================
# Project Title : Simple Blog Platform (CRUD with Flask)
# Name          : [Your Name]
# Date          : April 2026
# Description   : A simple blog application using Flask that
#                 supports Create, Read, Update, and Delete
#                 operations on blog posts stored in memory.
# ============================================================

from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# -------------------------------------------------------
# In-memory storage for blog posts (no database required)
# Each post is a dictionary with: id, title, content
# -------------------------------------------------------
posts = [
    {
        "id": 1,
        "title": "Welcome to My Blog",
        "content": "This is my first blog post. I'm excited to share my thoughts here!"
    },
    {
        "id": 2,
        "title": "Learning Flask",
        "content": "Flask is a lightweight Python web framework. It's great for building simple web apps quickly."
    }
]

# Counter to generate unique IDs for new posts
next_id = 3


# -------------------------------------------------------
# Route: Home Page — Read all blog posts
# -------------------------------------------------------
@app.route("/")
def index():
    """Display all blog posts on the home page."""
    return render_template("index.html", posts=posts)


# -------------------------------------------------------
# Route: Create a new blog post (GET shows form, POST saves)
# -------------------------------------------------------
@app.route("/create", methods=["GET", "POST"])
def create():
    """Handle creation of a new blog post."""
    global next_id  # Access the global ID counter

    if request.method == "POST":
        # Retrieve form data submitted by the user
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        # Basic validation: ensure fields are not empty
        if title and content:
            new_post = {
                "id": next_id,
                "title": title,
                "content": content
            }
            posts.append(new_post)  # Add new post to storage
            next_id += 1            # Increment the ID counter

        return redirect(url_for("index"))  # Redirect back to home

    # GET request: render the blank create form
    return render_template("create.html")


# -------------------------------------------------------
# Route: Edit an existing blog post (GET pre-fills, POST saves)
# -------------------------------------------------------
@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    """Handle editing of an existing blog post by ID."""
    # Find the post that matches the given ID
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        # If the post doesn't exist, redirect to home
        return redirect(url_for("index"))

    if request.method == "POST":
        # Update the post fields with the new submitted data
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if title and content:
            post["title"] = title
            post["content"] = content

        return redirect(url_for("index"))  # Redirect to home after saving

    # GET request: render form pre-filled with the existing post data
    return render_template("edit.html", post=post)


# -------------------------------------------------------
# Route: Delete a blog post by ID
# -------------------------------------------------------
@app.route("/delete/<int:post_id>")
def delete(post_id):
    """Remove a blog post from the list by its ID."""
    global posts
    # Filter out the post with the matching ID
    posts = [p for p in posts if p["id"] != post_id]
    return redirect(url_for("index"))  # Redirect to home after deletion


# -------------------------------------------------------
# Run the Flask development server
# -------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
