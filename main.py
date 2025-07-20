from fastapi import FastAPI, BackgroundTasks, Request
from pydantic import BaseModel
import time
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NotificationRequest(BaseModel):
    user_id: int
    message: str

# Synchronous blocking function that simulates a slow operation (to be fixed)
def send_notification_sync(user_id: int, message: str):
    logger.info(f"Preparing to send notification to user {user_id}: {message}")
    time.sleep(5)  # This blocks the event loop if used in the main async endpoint
    logger.info(f"Notification sent to user {user_id}: {message}")

@app.post("/send_notification")
async def send_notification(
    notification: NotificationRequest, background_tasks: BackgroundTasks, request: Request
):
    # The original code calls send_notification_sync() directly, causing blocking
    # Correct implementation should offload to background_tasks.add_task instead
    # send_notification_sync(notification.user_id, notification.message)
    background_tasks.add_task(send_notification_sync, notification.user_id, notification.message)
    return {"detail": "Notification will be sent"}

@app.get("/health")
async def health():
    return {"status": "ok"}
