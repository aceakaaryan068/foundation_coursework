# ST4015CMD — Foundation of Computer Science
### Investigation and Analysis of Computing Data for Data Management

---

## Repository Structure

```
ST4015CMD-Foundation-CS/
├── task1_encoding_demo.py
├── task2_seating_problem.py
├── task3/
│   ├── schema.sql
│   ├── queries.sql
│   ├── docker-compose.yml
│   ├── er_diagram.png
│   └── README.md
├── .gitignore
└── README.md
```

---

## Task 1 — Encoding Formats and Secure Data Exchange

**File:** `task1_encoding_demo.py`

Demonstrates all encoding formats covered in the report.

| Section | What it shows |
|---------|---------------|
| 1 | Base64 encoding, HTTP Basic Auth, JWT Base64URL |
| 2 | URL percent encoding, injection prevention |
| 3 | ASCII character mapping and limitations |
| 4 | Hex encoding, SHA-256 hash in hex |
| 5 | Encoding stacking — attacker obfuscation simulation |
| 6 | Secure pipeline using Base64 and HMAC integrity check |

**Run**

```bash
python task1_encoding_demo.py
```

---

## Task 2 — P vs NP: Classroom Seating Problem

**File:** `task2_seating_problem.py`

Solves the seating arrangement two ways and compares them.

| Approach | Complexity | Description |
|----------|------------|-------------|
| Brute Force | O(n!) | Tries every permutation until one works |
| Heuristic | O(n²) | Seats most constrained students first |

**Run**

```bash
python task2_seating_problem.py
```

**Sample output**

```
Brute Force   (720 permutations, 0.049ms)
  Result: Asha -> Rohan -> Bikash -> Nisha -> Suman -> Pooja  (valid)

Heuristic     (0.058ms)
  Result: Pooja -> Suman -> Nisha -> Bikash -> Rohan -> Asha  (valid)

Why brute force breaks down:
  n      n!                         time at 1M/sec
  5      120                        0.0s
  10     3,628,800                  3.6s
  15     1,307,674,368,000          15 days
  20     2,432,902,008,176,640,000  77,000 years
```

---

## Task 3 — College Club Membership Database

See [task3/README.md](task3/README.md) for full Docker setup instructions.

The database is split across two SQL files and runs inside a PostgreSQL Docker container.

| File | What it does |
|------|--------------|
| `schema.sql` | Creates the 3 normalised tables |
| `queries.sql` | Inserts data and runs all queries including JOIN |
| `docker-compose.yml` | Starts PostgreSQL and runs both SQL files automatically |

**ER Diagram**

![ER Diagram](task3/er_diagram.png)

**Quick start**

```bash
cd task3
docker compose up -d
```

**Without Docker** — run `schema.sql` then `queries.sql` in MySQL Workbench or pgAdmin.

---

## Requirements

| Tool | Version |
|------|---------|
| Python | 3.8+ |
| Docker and Docker Compose | any recent version |
| PostgreSQL without Docker | 13+ |

Tasks 1 and 2 only need Python — no external packages required.