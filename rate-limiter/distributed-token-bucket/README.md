# Redis-Based Token Bucket for Rate Limiting

This project provides a scalable, distributed implementation of the Token Bucket algorithm using Redis. It allows you to efficiently limit the rate of API requests in high-concurrency environments.

## Features
- Scalable and distributed rate limiting using Redis.
- Thread-safe token consumption with Redis pipelines.
- Automatic token refilling based on elapsed time.
- Configurable burst capacity and replenishment rate.

## Prerequisites

### Installation
1. **Install Redis:**
   - On Linux:
     ```bash
     sudo apt update && sudo apt install redis
     sudo service redis-server start
     ```
   - On macOS (Homebrew):
     ```bash
     brew install redis
     brew services start redis
     ```
   - Alternatively, use Docker:
     ```bash
     docker run -d --name redis-server -p 6379:6379 redis
     ```

2. **Install Python Redis Library:**
   ```bash
   pip install redis
   ```

## Usage

### Code Example
```python
import time
import redis
from redis_token_bucket import RedisTokenBucket

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Create a token bucket with burst capacity of 5 tokens and refill rate of 1 token per second
bucket = RedisTokenBucket(redis_client, key="api_rate_limit", burst_rate=5, replenishment_rate=1)

# Consume tokens in a loop
while True:
    if bucket.consume():
        print("Request processed")
    else:
        print("Rate limit exceeded")
    time.sleep(0.5)
```

### Parameters
- `redis_client`: Redis client instance.
- `key`: Unique identifier for the bucket.
- `burst_rate`: Maximum capacity of the bucket.
- `replenishment_rate`: Number of tokens added per second.

### Output
```
Request processed
Request processed
Rate limit exceeded
```

## Redis Commands Used

| Redis Command | Description |
|---------------|-------------|
| `pipeline()` | Starts a pipeline to batch multiple Redis commands for atomic execution. |
| `watch(self.key)` | Monitors a key for changes to detect conflicts in concurrent transactions. |
| `hgetall(self.key)` | Fetches all fields and values of a hash stored at the key. |
| `multi()` | Marks the start of a transaction block. |
| `hset(self.key, mapping={"tokens": new_tokens, "last_refill": now})` | Sets multiple fields in a hash at the specified key. |
| `execute()` | Executes all commands in the transaction block atomically. |

## How It Works
1. **Token Storage:** Redis stores the token count and last refill timestamp.
2. **Token Consumption:** Tokens are deducted only if enough tokens are available.
3. **Token Refill:** Tokens are replenished based on the elapsed time since the last refill.
4. **Concurrency Handling:** Redis transactions (`watch`, `multi`, `execute`) ensure consistent state updates across multiple requests.

## Error Handling
- Handles concurrent modifications using Redis' `WatchError`.
- Ensures proper initialization of the token bucket.

## Performance Considerations
This implementation is suitable for high-traffic APIs, distributed environments, and scenarios requiring precise rate-limiting control.

## License
This project is open-source and available for modification and use.
