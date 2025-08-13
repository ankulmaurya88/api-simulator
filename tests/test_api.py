from app.api import get_status

def test_get_status():
    assert get_status() == {"status": "ok"}
