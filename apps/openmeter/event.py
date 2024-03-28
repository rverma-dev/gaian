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
        "subject": f"tenant-{random.randint(1, 10)}",
        "time": int(round(time.time())),
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

for x in range(0, 50):
    random_cloudevent_json = generate_random_cloudevent()
    print(random_cloudevent_json)
#  for i in {1..10}; do python3 apps/openmeter/event.py | kcat -b openmeter-kafka-bootstrap.metering.svc.cluster.local:9092 -t om_default_events -P -p $(($i % 2)) -l ; done
    
    