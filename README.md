## 📁 Repository Structure

```
ST4015CMD-Foundation-CS/
│
├── task1_encoding_demo.py       # Task 1 — Encoding formats & secure data exchange
├── task2_seating_problem.py     # Task 2 — P vs NP seating arrangement solver
├── task3_club_database.sql      # Task 3 — College club database schema & queries
├── .gitignore
└── README.md
```

---

## 📌 Task 1 — Encoding Formats and Secure Data Exchange

**File:** `task1_encoding_demo.py`

This script practically demonstrates all encoding formats covered in the written report, showing how each format works, its size overhead, and where it fits within secure web communication.

### What it covers

| Section | What it demonstrates |
|---------|----------------------|
| Section 1 | Base64 encoding/decoding, HTTP Basic Auth header, JWT Base64URL |
| Section 2 | URL percent encoding, injection prevention |
| Section 3 | ASCII character mapping and its limitations with non-Latin text |
| Section 4 | Hex encoding, SHA-256 hash output in hexadecimal |
| Section 5 | Encoding stacking — how attackers obfuscate malicious payloads |
| Section 6 | Simulated secure pipeline using Base64 + HMAC integrity check |

### How to run

```bash
python task1_encoding_demo.py
```

> No external packages needed — uses Python standard library only.

### Sample output

```
SECTION 1: Base64 Encoding
Original text  : Hello, this is a secret message!
Base64 encoded : SGVsbG8sIHRoaXMgaXMgYSBzZWNyZXQgbWVzc2FnZSE=
Decoded back   : Hello, this is a secret message!
Size overhead  : 44 bytes vs 32 bytes (+38%)
```

---

## 📌 Task 2 — P vs NP: Classroom Seating Problem

**File:** `task2_seating_problem.py`

Demonstrates why the seating arrangement problem belongs to the NP complexity class by solving it two ways and comparing the results directly.

### The Problem

A teacher must seat students in a single row such that:
- ❌ No two **friends** sit next to each other
- ❌ No two students from the **same city** sit next to each other

### Two approaches compared

| Approach | Time Complexity | Description |
|----------|----------------|-------------|
| **Brute Force** | O(n!) | Tries every possible permutation until a valid one is found |
| **Heuristic** | O(n²) | Degree-first greedy — seats most constrained students first |

### How to run

```bash
python task2_seating_problem.py
```

### Sample output

```
APPROACH 1: Brute Force (O(n!))
Permutations checked : 49
Total possible       : 720
Time taken           : 0.038 ms
Solution: Asha | Rohan | Bikash | Nisha | Suman | Pooja  ✓

APPROACH 2: Heuristic (O(n²))
Time taken  : 0.053 ms
Solution: Pooja | Suman | Nisha | Bikash | Rohan | Asha  ✓
Violations  : 0
```

### Why brute force fails at scale

| Students | Permutations | Time at 10⁶ checks/sec |
|----------|-------------|------------------------|
| 5 | 120 | 0.00 seconds |
| 10 | 3,628,800 | 3.6 seconds |
| 15 | 1,307,674,368,000 | 15 days |
| 20 | 2.43 × 10¹⁸ | 77,000 years |

---

## 📌 Task 3 — College Club Membership Database

**File:** `task3_club_database.sql`

Full relational database implementation for the college club management system, normalised to Third Normal Form (3NF).

### Schema

```
┌─────────────────┐         ┌──────────────────────┐         ┌─────────────────┐
│    STUDENT      │         │     MEMBERSHIP        │         │      CLUB       │
├─────────────────┤         ├──────────────────────┤         ├─────────────────┤
│ StudentID  (PK) │──────── │ MembershipID    (PK) │ ──────── │ ClubID     (PK) │
│ StudentName     │   1:M   │ StudentID       (FK) │   M:1   │ ClubName        │
│ Email           │         │ ClubID          (FK) │         │ ClubRoom        │
└─────────────────┘         │ JoinDate             │         │ ClubMentor      │
                            └──────────────────────┘         └─────────────────┘
```

### What the file includes

- ✅ `CREATE TABLE` — all three tables with primary keys, foreign keys, and constraints
- ✅ `INSERT` — all original data loaded from the unnormalised source table
- ✅ `SELECT` — display all students, display all clubs
- ✅ `INSERT` — add a new student and a new club
- ✅ `JOIN` — retrieves StudentName, ClubName, and JoinDate across all three tables
- ✅ Bonus queries — member counts per club, update demo, delete demo

### How to run

```bash
# Option 1: MySQL command line
mysql -u root -p < task3_club_database.sql

# Option 2: Paste directly into MySQL Workbench, DBeaver, or phpMyAdmin
```

### Anomalies eliminated by normalisation

| Anomaly | Problem in original table | Fixed in 3NF |
|---------|--------------------------|--------------|
| **Insert** | Couldn't add a club without a student | Club table is independent |
| **Update** | Changing a room required updating many rows | One row in Club table |
| **Delete** | Removing last student deleted the club | Club data is never lost |

---

## ⚙️ Requirements

| Tool | Version |
|------|---------|
| Python | 3.8 or above |
| MySQL / MariaDB | 8.0 or above |

> **No external Python packages required.** Tasks 1 and 2 use only the Python standard library (`base64`, `urllib.parse`, `hashlib`, `hmac`, `itertools`, `time`, `math`).

---
