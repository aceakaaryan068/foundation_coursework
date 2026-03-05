import base64
import urllib.parse
import hashlib
import hmac
import json
import os
from datetime import datetime

# SECTION 1 — BASE64 ENCODING
# ─────────────────────────────────────────────────────────────

def demo_base64():
    print("=" * 60)
    print("SECTION 1: Base64 Encoding")
    print("=" * 60)

    # Basic text encoding
    original = "Hello, this is a secret message!"
    encoded = base64.b64encode(original.encode("utf-8"))
    decoded = base64.b64decode(encoded).decode("utf-8")

    print(f"\nOriginal text  : {original}")
    print(f"Base64 encoded : {encoded.decode()}")
    print(f"Decoded back   : {decoded}")
    print(f"Size overhead  : {len(encoded)} bytes vs {len(original)} bytes "
          f"(+{round((len(encoded)/len(original)-1)*100)}%)")

    # Simulating HTTP Basic Auth header
    username = "student@softwarica.edu.np"
    password = "MyPassword123"
    credentials = f"{username}:{password}"
    auth_token = base64.b64encode(credentials.encode()).decode()
    print(f"\n--- HTTP Basic Auth Header Simulation ---")
    print(f"Credentials    : {credentials}")
    print(f"Authorization  : Basic {auth_token}")
    print(f"NOTE: Base64 is NOT encryption — decode it back easily:")
    print(f"Decoded        : {base64.b64decode(auth_token).decode()}")

    # Base64 encoding a binary file (simulated with bytes)
    fake_binary = os.urandom(12)   # 12 random bytes simulating binary data
    b64_binary = base64.b64encode(fake_binary).decode()
    print(f"\n--- Binary Data (e.g. image attachment) ---")
    print(f"Raw bytes (hex): {fake_binary.hex()}")
    print(f"Base64 encoded : {b64_binary}")

    # Base64URL (used in JWTs / OAuth)
    jwt_payload = {"sub": "user123", "role": "student", "exp": 9999999999}
    payload_json = json.dumps(jwt_payload)
    jwt_b64url = base64.urlsafe_b64encode(payload_json.encode()).decode().rstrip("=")
    print(f"\n--- Base64URL (used in JWT tokens / OAuth 2.0) ---")
    print(f"JWT Payload    : {payload_json}")
    print(f"Base64URL      : {jwt_b64url}")
    print(f"Note: '+' replaced with '-', '/' replaced with '_' for URL safety")