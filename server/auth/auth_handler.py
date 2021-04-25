import time
from typing import Dict
from jose import jwt, JWTError

from server.config import JWT_SECRET, JWT_ALGORITHM


def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(username: str) -> Dict[str, str]:
    payload = {
        "username": username,
        "expires": time.time() + 3600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload if payload["expires"] > time.time() else None
    except JWTError:
        return {}
