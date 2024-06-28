import pytest
import datetime as dt
from app.settings import Settings
from app.users.auth.service import AuthService
from jose import jwt

pytestmark = pytest.mark.asyncio


async def test_generate_access_token__success(auth_service: AuthService, settings: Settings):
    user_id = '1'

    access_token = auth_service.generate_access_token(user_id=user_id)
    decoded_access_token = jwt.decode(
        access_token, settings.JWT_SECRET_KEY,
        algorithms=[settings.JWT_ENCODE_ALGORITHM])
    decoded_user_id = decoded_access_token.get('user_id')
    decoded_token_expire = dt.datetime.fromtimestamp(decoded_access_token.get('expire'), tz=dt.timezone.utc)

    assert (decoded_token_expire - dt.datetime.now(tz=dt.UTC) > dt.timedelta(days=6))
    assert decoded_user_id == user_id
