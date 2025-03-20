import pytest
from httpx import ASGITransport, AsyncClient

from app.utils import env
from app.main import app

@pytest.mark.anyio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url=f'{env.get('SERVER_URI')}/'
    ) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
