from flask import Flask, abort, jsonify
from models import db
from models.post import Post
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.alchemy_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
	return 'Hello World!'

@app.route('/post/<int:id>', methods=['GET'])
def get_post(id):
	post = Post.query.get(id)
	if not post:
		return abort(404)

	return jsonify({
		'content': post.content,
		'author_email': post.author_email,
		'created_time': post.created_time,
	})


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8080)
