from starlette.testclient import TestClient


def test_comic(client: TestClient) -> None:
    """Test `rsserpent_plugin_manhuagui.comic`."""
    response = client.get("/manhuagui/comic/29499")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
    assert response.text.count("看得见的女孩") == 1
