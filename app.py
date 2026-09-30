import os

def login():
    user = os.environ.get("APP_USER")
    password = os.environ.get("APP_PASS")

    if not user or not password:
        raise RuntimeError("Missing credentials: APP_USER / APP_PASS not set")

    # Fake "authentication" for demo purposes
    return len(password) >= 6