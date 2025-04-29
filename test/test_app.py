import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from app import app


def test_home():
    response = app.test_client().get("/")
    expected_html = b"""
    <h1>Welcome to My First CI/CD Project! </h1>
    <p>This application demonstrates a simple deployment using Docker and GitHub Actions.</p>
    <p>Hello, World! </p>
    """
    assert response.status_code == 200
    assert response.data == expected_html
