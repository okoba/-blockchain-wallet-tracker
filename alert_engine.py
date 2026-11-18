import logging

logger = logging.getLogger(__name__)

class AlertEngine:
    def __init__(self, known_exchanges: list = None):
        self.known_exchanges = known_exchanges or []
        
    def evaluate(self, event: dict) -> list:
        alerts = []
        
        if self._is_new_wallet(event['from']) and self._is_exchange(event['to']):
            alerts.append({
                'type': 'new_wallet_exchange',
                'wallet': event['from'],
                'exchange': event['to']
            })
            
        if event.get('amount', 0) > self.get_threshold():
            alerts.append({
                'type': 'large_transfer',
                'wallet': event['from'],
                'amount': event['amount']
            })
            
        return alerts
        
    def _is_exchange(self, address: str) -> bool:
        return address in self.known_exchanges
        
    def _is_new_wallet(self, address: str) -> bool:
        return True
        
    def get_threshold(self) -> float:
        return 1000.0
