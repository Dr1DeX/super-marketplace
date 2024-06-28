from dataclasses import dataclass
import httpx
import logging

from app.settings import Settings
from app.users.auth.schema import GoogleUserData


@dataclass
class GoogleClient:
    settings: Settings
    async_client: httpx.AsyncClient

    async def get_user_info(self, code: str):
        access_token = await self._get_user_access_token(code=code)
        print(access_token)
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://www.googleapis.com/oauth2/v1/userinfo",
                headers={"Authorization": f"Bearer {access_token}"}
            )
            user_info = response.json()
            return GoogleUserData(**user_info)

    async def _get_user_access_token(self, code: str):
        data = {
            "code": code,
            "client_id": self.settings.GOOGLE_CLIENT_ID,
            "client_secret": self.settings.GOOGLE_SECRET_KEY,
            "redirect_uri": self.settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code"
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.settings.GOOGLE_TOKEN_URL, data=data)
            json_response = response.json()
            logging.debug(f"Google token response: {json_response}")
            print(json_response)
            return json_response['access_token']
