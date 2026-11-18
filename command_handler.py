import logging

logger = logging.getLogger(__name__)

class CommandHandler:
    def __init__(self, telegram_bot, config):
        self.telegram_bot = telegram_bot
        self.config = config
        self.alert_engine = config.alert_engine
        
    async def process_onchain_event(self, event: dict):
        alerts = self.alert_engine.evaluate(event)
        for alert in alerts:
            await self._notify_users(alert)
            
    async def _notify_users(self, alert: dict):
        logger.info(f"Alert generated: {alert}")
        
    async def handle_command(self, chat_id: str, command: str):
        if command == '/start':
            await self.telegram_bot.send_alert(
                chat_id, 
                "Welcome! You are now subscribed to wallet alerts."
            )
        elif command == '/mute':
            await self.telegram_bot.send_alert(
                chat_id,
                "You have been muted."
            )
