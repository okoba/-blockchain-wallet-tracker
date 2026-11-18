import asyncio
import logging
from typing import Callable, Dict, Any

logger = logging.getLogger(__name__)

class SolanaClient:
    """
    Connects to a Solana RPC node via WebSocket to stream raw transaction events.
    """
    
    def __init__(self, rpc_url: str):
        self.rpc_url = rpc_url
        self.on_new_event: Callable = None
        self.is_running = False
        
    async def start(self):
        logger.info(f"Connecting to Solana RPC: {self.rpc_url}")
        self.is_running = True
        logger.info("Solana client connected.")
        
    async def stop(self):
        self.is_running = False
        logger.info("Solana client stopped.")
        
    def process_log(self, log_data: Dict[str, Any]):
        if not self.is_running:
            return
            
        if self._is_transfer_event(log_data):
            normalized_event = self._normalize_event(log_data)
            if self.on_new_event:
                self.on_new_event(normalized_event)
                
    def _is_transfer_event(self, data: Dict) -> bool:
        return data.get('type') == 'transfer'
        
    def _normalize_event(self, data: Dict) -> Dict:
        return {
            'from': data.get('from'),
            'to': data.get('to'),
            'amount': data.get('amount'),
            'token': data.get('token_mint'),
            'signature': data.get('signature'),
            'timestamp': data.get('block_time')
        }
