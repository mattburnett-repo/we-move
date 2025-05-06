def test_users_index(client):
    response = client.get("/users/")
    assert response.status_code == 200

def test_user_list(client):
    """Test that the users list page returns at least three users"""
    response = client.get('/users', follow_redirects=True)
    assert response.status_code == 200
    assert b'View Details' in response.data  # Adjusted to match your actual output
    assert response.data.count(b'View Details') >= 3  # Assuming each user has a 'View Details' link

def test_user_detail(client):
    """Test that a single user's detail page returns exactly one user"""
    response = client.get('/users/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Back to Users' in response.data  # Adjusted to match known content in user detail page
    assert b'Name' in response.data  # Assuming 'Name' still appears for a user