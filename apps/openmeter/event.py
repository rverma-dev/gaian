import time
import uuid
import json
import random

# Generate a random CloudEvent in the specified format
def generate_random_cloudevent():
    event = {
        "id": str(uuid.uuid4()),
        "specversion": "1.0",
        "type": "api-request",
        "source": f"/example/source/{random.randint(1, 100)}",
        "subject": f"tenant-{random.randint(1, 10)}",
        "time": int(round(time.time() * 1000)),
        "datacontenttype": "application/json",
        "data": json.dumps({
            "method": random.choice(['GET', 'POST', 'PUT']),
            "path": "/demo",
            "region": f"us-east-{random.randint(1, 3)}",
            "zone": random.choice(['a', 'b', 'c']),
            "duration_ms": random.randint(1, 100)
        }),
    }
    return json.dumps(event)

for x in range(0, 600):
    random_cloudevent_json = generate_random_cloudevent()
    print(random_cloudevent_json)