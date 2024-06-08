from fastapi import APIRouter, Depends, Request, Body, Query
from typing import Dict
import tomli
from cat.auth.utils import AuthPermission, AuthResource 
from cat.auth.headers import http_auth, session

from cat.convo.messages import CatMessage

router = APIRouter()


# server status
@router.get("/", dependencies=[Depends(http_auth(AuthResource.STATUS, AuthPermission.READ))])
async def home() -> Dict:
    """Server status""" 
    with open("pyproject.toml", "rb") as f:
        project_toml = tomli.load(f)["project"]

    return {
        "status": "We're all mad here, dear!",
        "version": project_toml['version']
    }


@router.post("/message", dependencies=[Depends(http_auth(AuthResource.CONVERSATION, AuthPermission.WRITE))], response_model=CatMessage)
async def message_with_cat(
    payload: Dict = Body({"text": "hello!"}),
    stray = Depends(session),
) -> Dict:
    """Get a response from the Cat"""
    answer = await stray({"user_id": stray.user_id, **payload})
    return answer