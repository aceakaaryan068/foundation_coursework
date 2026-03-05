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


Task 2 — P vs NP: Classroom Seating Arrangement
File: task2_seating_problem.py
This script models the classroom seating problem with 6 students, 4 friend pairs, and city constraints, then solves it using two approaches:
Approach 1: Brute Force (O(n!))

Generates every possible permutation using itertools.permutations
Checks each permutation against both constraints
Returns the first valid arrangement found
Prints how many permutations were checked and time taken

Approach 2: Heuristic — Degree-First Greedy (O(n²))

Builds a constraint graph connecting constrained student pairs
Sorts students by number of constraints (most constrained seated first)
Greedily inserts each student at the position with fewest violations
Significantly faster than brute force

Scalability Table
The script also prints a table showing how n! grows catastrophically with class size, demonstrating why brute force becomes computationally impossible beyond small inputs.

How to Run
bash# No external libraries required
python task2_seating_problem.py
Sample Output
APPROACH 1: Brute Force (O(n!))
Permutations checked : 312
Total possible       : 720
Time taken           : 0.847 ms

APPROACH 2: Heuristic — Degree-First Greedy (O(n^2))
Time taken : 0.0312 ms


Task 3 — College Club Membership Database
File: task3_club_database.sql
This SQL file implements the fully normalised (3NF) relational schema for the college club membership system.
Schema Overview
Student (StudentID PK, StudentName, Email)
    |
    | 1 ──────── M
    |
Membership (MembershipID PK, StudentID FK, ClubID FK, JoinDate)
    |
    | M ──────── 1
    |
Club (ClubID PK, ClubName, ClubRoom, ClubMentor)
What the File Includes

CREATE TABLE statements for all three tables with primary keys, foreign keys, and constraints
INSERT statements loading all original data from the unnormalised table
Basic SELECT queries — display all students, display all clubs
INSERT queries — add a new student and a new club
JOIN query — retrieves StudentName, ClubName, and JoinDate across all three tables
Additional queries — club member counts, student club lookup, update demo (no anomaly), delete demo (no anomaly)