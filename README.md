# Full-stack Flask App

[![CircleCI](https://circleci.com/gh/Prev/full-stack-flask-app.svg?style=svg&circle-token=7c1762ae7cafe9271773f32c098292814ee3c851)](https://circleci.com/gh/Prev/full-stack-flask-app)

Sample project using Flask + MySQL + SQLAlchemy + PyTest + Docker.  
Run tests is automated with [CircleCI](https://circleci.com).

> 포스트 [높은 품질의 Flask 웹 애플리케이션 설계하기](https://prev.kr/posts/%EB%86%92%EC%9D%80-%ED%92%88%EC%A7%88%EC%9D%98-Flask-%EC%9B%B9-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0/)를 작성하며 만든 레파지토리 입니다.

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
