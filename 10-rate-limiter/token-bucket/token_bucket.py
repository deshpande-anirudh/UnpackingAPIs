# max_tokens
# rate
from time import time, sleep

"""
- The burst capacity β is the maximum number of requests that the server is allowed to handle immediately for each key (the "bucket size"). 
- Each request consumes a token from the bucket. 
- When the bucket is empty, requests are rejected ("throttled"). 
- Tokens are added back to the bucket uniformly at rate r. 
- So the long-term average request rate is held close to r, while allowing periodic bursts of requests of up to size β.
"""


class TokenBucket:
    def __init__(self, refill_rate, burst_capacity):
        self.tokens = burst_capacity
        self.refill_rate = refill_rate
        self.max_capacity = burst_capacity
        self.filled_at = int(time())

    def refill(self):
        cur_time = int(time())

        # zero within the same second
        new_tokens = self.refill_rate * (cur_time - self.filled_at)
        self.filled_at = cur_time
        self.tokens = min(new_tokens + self.tokens, self.max_capacity)

    def consume(self, tokens):
        self.refill()
        if self.tokens <= tokens:
            cur_tokens = self.tokens
            self.tokens = 0
            return cur_tokens

        self.tokens -= tokens
        return tokens


token_bucket = TokenBucket(1, 5)
while True:
    sleep(0.2)
    print(f"Consuming {str(token_bucket.consume(2))} tokens")





