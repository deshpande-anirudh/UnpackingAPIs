from datetime import datetime
from threading import RLock
import time


class TokenBucket:
    _unique_instance = None
    _lock = RLock()

    def __new__(cls, burst_rate, replenishment_rate):
        if not cls._unique_instance:
            cls._unique_instance = super().__new__(cls)
            cls._unique_instance.__init__(burst_rate, replenishment_rate)
        return cls._unique_instance

    def __init__(self, burst_rate, replenishment_rate):
        if not hasattr(self, 'tokens'):
            self.burst_rate = burst_rate
            self.replenishment_rate = replenishment_rate
            self.tokens = burst_rate
            self.filled_at = datetime.now()

    def consume(self, tokens) -> int:
        with self._lock:
            self.refill()
            if self.tokens <= tokens:
                if self.tokens > 1:
                    cur_tokens = self.tokens
                    self.tokens = 0
                    return cur_tokens
                else:
                    return 0

            self.tokens -= tokens
            return tokens

    def refill(self):
        with self._lock:
            elapsed_time = (datetime.now() - self.filled_at).total_seconds()
            tokens_to_add = self.replenishment_rate * elapsed_time
            self.tokens = min(
                self.burst_rate,
                self.tokens + tokens_to_add
            )

            self.filled_at = datetime.now()


if __name__ == "__main__":
    bucket = TokenBucket(2, 1)
    while True:
        if not bucket.consume(1):
            print('Rate exceeded')
        else:
            print('Consumed')
        time.sleep(0.2)
