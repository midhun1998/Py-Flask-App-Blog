from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default='Unknown')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog Post ' + str(self.id)


# all_posts = [
#     {
#         'title': 'Post 1',
#         'content': 'Content of the post 1'
#     },
#     {
#         'title': 'Post 2',
#         'author': 'Midhun',
#         'content': 'Content of the post 2'
#     }
# ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        newPost = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(newPost)
        db.session.commit()
        return redirect('/posts')
    else: 
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == "POST":
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('editPost.html', post = post)
    

# @app.route('/dynamic/<string:name>')
# def dynamicPage(name):
#     return 'This is an example of dynamic webpage '+ name 

if __name__ == '__main__':
    app.run(debug=True)

