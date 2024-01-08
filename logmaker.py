import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_log_entry():
    ip_address = fake.ipv4()
    timestamp = datetime.now() - timedelta(days=random.randint(1, 365), hours=random.randint(1, 24))
    timestamp_str = timestamp.strftime("%d/%b/%Y:%H:%M:%S %z")
    method = random.choice(["GET", "POST", "PUT", "DELETE"])
    endpoint = fake.uri_path()
    protocol = "HTTP/1.0"
    status_code = random.choice([200, 201, 204, 400, 404, 500])
    response_size = random.randint(100, 2000)
    referer = fake.uri()
    user_agent = fake.user_agent()

    log_entry = f'{ip_address} - - [{timestamp_str}] "{method} {endpoint} {protocol}" {status_code} {response_size} "{referer}" "{user_agent}"'
    return log_entry

num_entries = 1000  # You can adjust the number of entries you want

log_data = [generate_log_entry() for _ in range(num_entries)]

with open("generated_log_data.txt", "w") as f:
    for log_entry in log_data:
        f.write(log_entry + "\n")

print(f"Generated {num_entries} log entries. Check 'generated_log_data.txt'.")
