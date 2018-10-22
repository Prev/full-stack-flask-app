from models import db
from datetime import datetime


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text, nullable=False)
	author_email = db.Column(db.String(100), nullable=False)
	created_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

	def as_dict(self):
		return {
			'content': self.content,
			'author_email': self.author_email,
			'created_time': self.created_time,
		}