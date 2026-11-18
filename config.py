import os
from alert_engine import AlertEngine

class Config:
    def __init__(self):
        self.solana_rpc_url = os.getenv('SOLANA_RPC_URL')
        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.known_exchanges = [
            "placeholder_exchange_1",
            "placeholder_exchange_2"
        ]
        
        if not self.solana_rpc_url or not self.telegram_token:
            raise ValueError(
                "Missing environment variables: SOLANA_RPC_URL and TELEGRAM_BOT_TOKEN are required."
            )
            
        self.alert_engine = AlertEngine(known_exchanges=self.known_exchanges)
