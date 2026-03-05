📁 Repository Structure
ST4015CMD-Foundation-CS/
│
├── task1_encoding_demo.py       # Task 1 — Encoding formats & secure data exchange
├── task2_seating_problem.py     # Task 2 — P vs NP seating arrangement solver
│
├── task3/
│   ├── schema.sql               # Table creation (3NF normalised schema)
│   ├── queries.sql              # Inserts, selects and JOIN queries
│   ├── docker-compose.yml       # Spins up PostgreSQL with Docker
│   └── README.md                # Task 3 Docker setup instructions
│
├── .gitignore
└── README.md

📌 Task 1 — Encoding Formats and Secure Data Exchange
File: task1_encoding_demo.py
Demonstrates all encoding formats covered in the report.
SectionWhat it shows1Base64 encoding, HTTP Basic Auth, JWT Base64URL2URL percent encoding, injection prevention3ASCII character mapping and limitations4Hex encoding, SHA-256 hash in hex5Encoding stacking — attacker obfuscation simulation6Secure pipeline with Base64 + HMAC integrity check
Run
bashpython task1_encoding_demo.py

📌 Task 2 — P vs NP: Classroom Seating Problem
File: task2_seating_problem.py
Solves the seating arrangement two ways and compares them.
ApproachComplexityDescriptionBrute ForceO(n!)Tries every permutationHeuristicO(n²)Seats most constrained students first
Run
bashpython task2_seating_problem.py
Sample output
Brute Force   (720 permutations, 0.049ms)
  Result: Asha -> Rohan -> Bikash -> Nisha -> Suman -> Pooja  (valid)

Heuristic     (0.058ms)
  Result: Pooja -> Suman -> Nisha -> Bikash -> Rohan -> Asha  (valid)

📌 Task 3 — College Club Membership Database
See task3/README.md for full Docker setup instructions.
Schema
┌──────────────┐         ┌─────────────────────┐         ┌──────────────┐
│   STUDENT    │         │     MEMBERSHIP       │         │     CLUB     │
├──────────────┤         ├─────────────────────┤         ├──────────────┤
│ StudentID PK │────1:M──│ MembershipID PK      │──M:1────│ ClubID PK    │
│ StudentName  │         │ StudentID FK         │         │ ClubName     │
│ Email        │         │ ClubID FK            │         │ ClubRoom     │
└──────────────┘         │ JoinDate             │         │ ClubMentor   │
                         └─────────────────────┘         └──────────────┘
Quick start (Docker)
bashcd task3
docker compose up -d
Without Docker (paste directly into MySQL Workbench or pgAdmin)
Run schema.sql first, then queries.sql.

⚙️ Requirements
ToolVersionPython3.8+Docker + Docker Composeany recent versionPostgreSQL (if not using Docker)13+

Tasks 1 and 2 only need Python — no external packages required.