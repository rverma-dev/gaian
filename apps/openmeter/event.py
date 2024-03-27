from datetime import datetime
import uuid
import json
import random

# Generate a random CloudEvent in the specified format
def generate_random_cloudevent():
    event = {
        "specversion": "1.0",
        "type": "com.example.type",
        "source": f"/example/source/{random.randint(1, 100)}",
        "id": str(uuid.uuid4()),
        "time": datetime.now().isoformat(),
        "datacontenttype": "application/json",
        "data": {
            "value": random.randint(1, 100)
        },
    }
    return json.dumps(event)

for x in range(0, 100):
    random_cloudevent_json = generate_random_cloudevent()
    print(random_cloudevent_json)