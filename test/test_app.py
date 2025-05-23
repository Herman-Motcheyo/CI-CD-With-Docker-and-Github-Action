import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from app import app

def test_home():
    response = app.test_client().get("/")
    
    assert response.status_code == 200
    assert b"Welcome to My First CI/CD Project!" in response.data
    assert b"Hello, World!" in response.data
