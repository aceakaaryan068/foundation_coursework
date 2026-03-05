# foundation_coursework
testing
Task 1 — Encoding Formats and Secure Data Exchange
File: task1_encoding_demo.py
This script demonstrates all encoding formats discussed in the report:

Base64 — encoding binary data and HTTP Basic Auth credentials
Base64URL — used in JWT tokens and OAuth 2.0
URL Encoding — percent encoding for safe HTTP transmission
ASCII — character-to-integer mapping and limitations
Hex Encoding — SHA-256 hash output in hexadecimal
Obfuscation Risk — encoding stacking attack (simulating Log4Shell-style evasion)
Secure Pipeline — simulated Base64 + HMAC data transmission flow
How to Run
bash# No external libraries required — uses Python standard library only
python task1_encoding_demo.py
Expected Output
The script prints each encoding format in turn, showing original input, encoded output, decoded output, and size overhead. Section 5 demonstrates how attackers stack encoding layers to bypass security scanners.