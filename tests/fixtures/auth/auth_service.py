import pytest

from app.settings import Settings
from app.users.auth.service import AuthService


@pytest.fixture
def auth_service(user_repository):
    return AuthService(
        settings=Settings(),
        user_repository=user_repository,
    )
