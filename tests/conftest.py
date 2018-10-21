import pytest
from main import app
from models import db
from models.post import Post
import os
import csv


def load_model_fixtures(db, model, file_name):
	""" Load model fixtures in file.
	:param db: SQLAlchemy db instance
	:param model: Model class writen with SQLAlchemy
	:param file_name: File name of fixture (CSV)
	"""
	cur_dir = os.path.dirname(os.path.realpath(__file__))

	with open('%s/fixtures/%s' % (cur_dir, file_name), encoding='utf-8') as file:
		reader = csv.DictReader(file)
		for row in reader:
			attrs = dict(row.items())
			db.session.add(model(**attrs))

	db.session.commit()


@pytest.fixture
def client():
	client = app.test_client()

	with app.app_context():
		for table in reversed(db.metadata.sorted_tables):
			try:
				db.engine.execute(table.delete())
			except:
				pass

		db.create_all()
		load_model_fixtures(db, Post, 'posts.csv')

		yield client
