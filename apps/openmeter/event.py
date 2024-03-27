import time
import uuid
import json
import random

# Generate a random CloudEvent in the specified format
def generate_random_cloudevent():
    event = {
        "id": str(uuid.uuid4()),
        "specversion": "1.0",
        "type": "request",
        "source": f"/example/source/{random.randint(1, 100)}",
        "subject": "customer-2",
        "time": int(round(time.time() * 1000)),
        "datacontenttype": "application/json",
        "data": json.dumps({
            "method": "POST",
            "path": "/",
            "region": "us-east-1",
            "zone": "a",
            "duration_ms": random.randint(1, 100)
        }),
    }
    return json.dumps(event)

for x in range(0, 600):
    random_cloudevent_json = generate_random_cloudevent()
    print(random_cloudevent_json)