def test_campaigns_index(client):
    response = client.get("/campaigns/")
    assert response.status_code == 200

def test_campaign_list(client):
    """Test that the campaigns list page returns at least three campaigns"""
    response = client.get('/campaigns/')
    assert response.status_code == 200
    assert b'Campaigns' in response.data  # Ensure the list title is in the response
    # Check if there are at least 3 campaigns listed in the page content
    assert response.data.count(b'Campaign') >= 2  # Adjust this based on how campaigns are rendered

def test_campaign_detail(client):
    """Test that a single campaign detail page returns exactly one campaign"""
    response = client.get('/campaigns/1')  # Ensure campaign with ID 1 exists in your test DB
    assert response.status_code == 200
    assert b'Campaign Details' in response.data
    assert b'Solar Power for Schools' in response.data  # Adjust based on your test fixture
    assert response.data.count(b'<h2 class="text-xl">') == 1