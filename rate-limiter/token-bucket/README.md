# Token Bucket Rate Limiter

## Overview
This implementation provides a thread-safe **Token Bucket** rate-limiting algorithm in Python. The Token Bucket algorithm allows controlled bursts of requests while maintaining a long-term average request rate. It is commonly used to limit network traffic or API calls.

## How It Works
1. **Bucket Initialization**: The token bucket has a capacity defined by `burst_rate`, which represents the maximum number of tokens the bucket can hold.
2. **Token Consumption**: Each request consumes a specified number of tokens. If enough tokens are available, the request is allowed; otherwise, it is rejected.
3. **Token Refill**: Tokens are refilled at a constant rate (`replenishment_rate`) over time.
4. **Thread Safety**: The implementation uses `RLock` to ensure safe concurrent access.

---

## Usage

### Initialization
Create a token bucket by specifying the maximum burst capacity (`burst_rate`) and the rate of replenishment (`replenishment_rate`).

```python
from token_bucket import TokenBucket

# Create a TokenBucket instance with burst capacity of 2 and replenishment rate of 1 token per second
bucket = TokenBucket(burst_rate=2, replenishment_rate=1)
```

### Consuming Tokens
Tokens can be consumed using the `consume()` method.

```python
if bucket.consume(1):
    print("Request allowed")
else:
    print("Rate limit exceeded")
```

### Example Program
```python
import time
from token_bucket import TokenBucket

bucket = TokenBucket(2, 1)  # Burst capacity of 2, refill rate of 1 per second

while True:
    if not bucket.consume(1):
        print("Rate exceeded")
    else:
        print("Request processed")
    time.sleep(0.2)  # Simulate a request every 200 ms
```

### Thread Safety
The `TokenBucket` implementation uses a `RLock` to allow concurrent access while preventing race conditions.

---

## Key Methods

### `__init__(burst_rate, replenishment_rate)`
Initializes the token bucket.

- **Parameters:**
  - `burst_rate (int)`: Maximum number of tokens the bucket can hold.
  - `replenishment_rate (float)`: Number of tokens added to the bucket per second.

### `consume(tokens) -> int`
Attempts to consume the specified number of tokens.

- **Parameters:**
  - `tokens (int)`: Number of tokens to consume.

- **Returns:**
  - `int`: Number of tokens successfully consumed (0 if insufficient tokens are available).

### `refill()`
Adds tokens to the bucket based on the elapsed time since the last refill.

---

## Important Notes
- **Singleton Design Pattern:** This implementation enforces a singleton pattern, ensuring only one instance of the token bucket is created.
- **Precision:** The use of `datetime.now()` ensures time-based refills but may not be suitable for high-precision real-time systems.

---

## Potential Enhancements
- Support for multiple independent token buckets.
- Add logging for better observability.
- Implement dynamic configuration for `burst_rate` and `replenishment_rate`.


