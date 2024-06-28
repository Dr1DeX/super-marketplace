from dataclasses import dataclass

import pytest

from app.users.user_profile.schema import UserCreateSchema
from tests.fixtures.users.user_model import UserProfileFactory


@dataclass
class FakerUserRepository:
    async def create_user(self, user_data: UserCreateSchema):
        return UserProfileFactory()


@pytest.fixture
def user_repository():
    return FakerUserRepository()
