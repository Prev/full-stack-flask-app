
def test_index(client):
	""" Test GET / """
	response = client.get('/')
	assert response.status_code == 200


def test_404(client):
	""" Test 404 Handling """
	response = client.get('/this_page_would_not_be_exist')
	assert response.status_code == 404


def test_get_post(client):
	""" Test GET /post/<id> """

	response = client.get('/post/1')
	assert response.status_code == 200

	response = client.get('/post/2')
	assert response.status_code == 200

	response = client.get('/post/3')
	assert response.status_code == 404
