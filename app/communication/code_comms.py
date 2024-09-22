# Author: Ujwal N K
# Date: 2024-09-20
# Communication from the user to the bot handled by the server

from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status, UploadFile

from datetime import datetime, timedelta, timezone

from ..database import operations as ds
from ..core.schema import Token, TokenData, User, UserInDB

from ..core.core import get_current_active_user

router = APIRouter(
    prefix="/bot"
)

@router.post("/iot/code")
async def push_code(
    current_user: Annotated[User, Depends(get_current_active_user)],
    file: UploadFile
):
    """
    Function to save the code to a temp folder. Code that is sent by the user. 
    The sent code needs to be dumped into the IoT Bot
    """
    try:
        # Intentionally changing the file extension to ensure no accidental runs
        file_path = f"/tmp/iot/iot_bot.code"
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )

@router.get("/iot/stop")
async def stop_iot_bot(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """Emergency stop for the IoT BOT"""
    # TODO: Implement stop message over socket stream
    pass


@router.post("/ros/code")
async def push_code(
    current_user: Annotated[User, Depends(get_current_active_user)],
    file: UploadFile
):
    """
    Function to save the code to a temp folder. Code that is sent by the user. 
    The sent code needs to be dumped into the ROS Bot
    """
    try:
        # Intentionally changing the file extension to ensure no accidental runs
        file_path = f"/tmp/ros/ros_bot.code"
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )

@router.get("/ros/stop")
async def stop_ros_bot(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """Emergency stop for the ROS Bot"""
    # TODO: Implement stop message over socket stream
    pass