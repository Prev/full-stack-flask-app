# Full-stack Flask App

[![CircleCI](https://circleci.com/gh/Prev/full-stack-flask-app.svg?style=svg&circle-token=7c1762ae7cafe9271773f32c098292814ee3c851)](https://circleci.com/gh/Prev/full-stack-flask-app)

Sample project using Flask + MySQL + SQLAlchemy + PyTest + Docker.  
Run tests is automated with [CircleCI](https://circleci.com).

### How to build & run

```bash
$ docker build -t my_flask_app .
$ docker run -p 8080:80 \
 	-e MYSQL_USER=<username> \
 	-e MYSQL_PASS=<password> \
 	-e MYSQL_DB=<database> \
 	--rm my_flask_app
```


### How to run tests

```bash
$ PYTHONPATH=app \
	MYSQL_USER=test_user \
	MYSQL_PASS=<some-other-pass> \
	MYSQL_DB=<my_app_test_db> \
	pytest tests
```