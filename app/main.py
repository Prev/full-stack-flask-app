from flask import Flask, abort, jsonify, request
from werkzeug.exceptions import HTTPException
from datetime import datetime
from models import db
from models.post import Post
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.alchemy_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.errorhandler(Exception)
def handle_error(e):
	""" Handle all exceptions and always return json """
	code = 500
	if isinstance(e, HTTPException):
		code = e.code
	return jsonify(error=str(e), code=code), code


@app.route('/', methods=['GET'])
def index():
	return jsonify({
		'service': 'working',
	})


@app.route('/posts', methods=['GET'])
def get_post_list():
	""" Get paginated posts with url variable `page` and `per_page`
	"""
	page = int(request.args.get('page', 1))
	per_page = int(request.args.get('per_page', 10))

	posts = Post.query.order_by(Post.id.desc()).paginate(page, per_page, error_out=False)
	result = [post.as_dict() for post in posts.items]

	return jsonify({
		'page': page,
		'per_page': per_page,
		'total': posts.total,
		'result': result,
	})


@app.route('/post/<int:id>', methods=['GET'])
def get_post(id):
	""" Get the post with request URL arg `id`
	"""
	post = Post.query.get(id)
	if not post:
		return abort(404)

	return jsonify(post.as_dict())


@app.route('/post', methods=['POST'])
def create_post():
	""" Create post with request data
	"""
	params = request.get_json()

	if not params or 'content' not in params or 'author_email' not in params:
		return jsonify({'error': 'Arguments Missed'}), 400

	post = Post(
		content=params['content'],
		author_email=params['author_email'],
		created_time=datetime.now(),
	)
	db.session.add(post)
	db.session.commit()

	return jsonify({'result': 'success', 'id': post.id}), 201


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8080)
