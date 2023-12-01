import redis
from decouple import config

# Load Redis credentials from .env file
REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT', cast=int)
REDIS_PASSWORD = config('REDIS_PASSWORD')

# Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

# Test the connection
try:
    r.set('test_key', 'hello')
    value = r.get('test_key')
    print(f"Value from Redis: {value}")
except Exception as e:
    print(f"Redis connection error: {e}")
