import pytest
from httpx import ASGITransport, AsyncClient

from ..api.utils import env
from ..main import app

@pytest.mark.anyio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url=f'http://{env.get('SERVER_HOST')}:{env.get('SERVER_PORT')}/'
    ) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
