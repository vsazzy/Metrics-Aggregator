import redis
import time
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST=os.getenv("REDIS_HOST", "localhost")
REDIS_PORT=int(os.getenv("REDIS_PORT", 6379))
STREAM_NAME=os.getenv("STREAM_NAME", "service_logs")

r=redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
services=["auth-api","payment-gateway", "inventory-service"]
print("Producer started, Pushing to stream:",STREAM_NAME)

while True:
    event={
        "service":random.choice(services),
        "timestamp":int(time.time()),
        "status":200 if random.random()>0.1 else 500,
        "latency":random.randint(50, 500)
    }
    
    try:
        r.xadd(STREAM_NAME, {"data":json.dumps(event)})
        time.sleep(0.1)
    except Exception as e:
        print("Error connecting to redis:", e)      
        time.sleep(2)
    
