import time
import redis


class RedisTokenBucket:
    def __init__(self, redis_client, key, burst_rate, replenishment_rate):
        """
        A scalable Redis-based Token Bucket implementation.

        :param redis_client: Redis client instance.
        :param key: Unique key for this token bucket.
        :param burst_rate: Maximum burst capacity.
        :param replenishment_rate: Number of tokens added per second.
        """
        self.redis = redis_client
        self.key = key
        self.burst_rate = burst_rate
        self.replenishment_rate = replenishment_rate

        # Initialize bucket state if it doesn't exist
        if not self.redis.exists(self.key):
            self.redis.hset(self.key, mapping={"tokens": burst_rate, "last_refill": int(time.time())})

    def _current_time(self):
        """Return the current time in seconds."""
        return int(time.time())

    def consume(self, tokens=1) -> bool:
        """
        Consume tokens from the bucket.

        :param tokens: Number of tokens to consume.
        :return: True if tokens were successfully consumed, False if rate limited.
        """
        with self.redis.pipeline() as pipe:
            while True:
                try:
                    pipe.watch(self.key)

                    # Fetch current state
                    data = pipe.hgetall(self.key)

                    current_tokens = float(data.get("tokens", 0))
                    last_refill = int(data.get("last_refill", self._current_time()))

                    # Calculate elapsed time and refill
                    now = self._current_time()
                    elapsed_time = now - last_refill
                    new_tokens = min(self.burst_rate, current_tokens + elapsed_time * self.replenishment_rate)

                    if new_tokens < tokens:
                        return False

                    # Deduct tokens and update state
                    new_tokens -= tokens
                    pipe.multi()
                    pipe.hset(self.key, mapping={"tokens": new_tokens, "last_refill": now})
                    pipe.execute()
                    return True
                except redis.WatchError:
                    continue


# Example usage
if __name__ == "__main__":
    # Connect to Redis
    redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    # Create a token bucket with burst capacity 5 and refill rate of 1 token per second
    bucket = RedisTokenBucket(redis_client, key="api_rate_limit", burst_rate=5, replenishment_rate=1)

    while True:
        if bucket.consume():
            print("Request processed")
        else:
            print("Rate limit exceeded")
        time.sleep(0.5)
