import logging
import asyncio

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.is_running = False
        
    async def start(self):
        logger.info("Telegram bot starting...")
        self.is_running = True
        logger.info("Telegram bot started.")
        
    async def stop(self):
        self.is_running = False
        logger.info("Telegram bot stopped.")
        
    async def send_alert(self, chat_id: str, message: str):
        if not self.is_running:
            return
        logger.info(f"Sending alert to {chat_id}: {message}")
