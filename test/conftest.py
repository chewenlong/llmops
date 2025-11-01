import pytest

from app.http.app import app


@pytest.fixture
def client():
    """获取flask应用的测试应用并返回"""
    app.testing = True
    with app.test_client() as client:
        yield client
