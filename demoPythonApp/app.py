from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'Content of the post 1'
    },
    {
        'title': 'Post 2',
        'author': 'Midhun',
        'content': 'Content of the post 2'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/dynamic/<string:name>')
def dynamicPage(name):
    return 'This is an example of dynamic webpage '+ name 

if __name__ == '__main__':
    app.run(debug=True)

