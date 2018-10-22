def test_get_post_list(client):
	""" Test GET /posts """

	response = client.get('/posts')
	assert response.status_code == 200

	data = response.get_json()
	assert data['page'] == 1
	assert data['per_page'] == 10
	assert data['total'] == 2
	assert len(data['result']) == 2


def test_get_post(client):
	""" Test GET /post/<id> """

	response = client.get('/post/1')
	assert response.status_code == 200

	response = client.get('/post/2')
	assert response.status_code == 200

	response = client.get('/post/3')
	assert response.status_code == 404


def test_create_post(client):
	""" Test POST /post """

	response = client.post('/post', json={
		'content': 'Hello!',
		'author_email': 'anonymous1@gmail.com',
	})
	assert response.status_code == 201

	data = response.get_json()
	assert data['id'] > 2

	# Then check with 'GET /post/<id>'
	response = client.get('/post/%d' % data['id'])
	assert response.status_code == 200
