import logging

logger = logging.getLogger(__name__)

class PriceFeed:
    def __init__(self):
        pass
        
    async def get_price(self, token_symbol: str) -> float:
        logger.info(f"Fetching price for {token_symbol}")
        return 0.0
