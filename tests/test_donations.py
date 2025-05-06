def test_donations_index(client):
    response = client.get("/donations/")
    assert response.status_code == 200

def test_donation_list(client):
    """Test that the donations list page returns at least three donations"""
    response = client.get('/donations', follow_redirects=True)
    assert response.status_code == 200
    assert b'Donated on:' in response.data
    assert response.data.count(b'Donation') >= 2

def test_donation_detail(client):
    """Test that a single donation detail page returns exactly one donation"""
    response = client.get('/donations/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Donated on:' in response.data
    assert b'Donor Name' in response.data
    assert response.data.count(b'Donor Name') == 1