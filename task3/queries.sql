INSERT INTO Student VALUES
    (1, 'Asha',   'asha@email.com'),
    (2, 'Bikash', 'bikash@email.com'),
    (3, 'Nisha',  'nisha@email.com'),
    (4, 'Rohan',  'rohan@email.com'),
    (5, 'Suman',  'suman@email.com'),
    (6, 'Pooja',  'pooja@email.com'),
    (7, 'Aman',   'aman@email.com');

-- insert clubs
INSERT INTO Club VALUES
    ('C1', 'Music Club',  'R101', 'Mr. Raman'),
    ('C2', 'Sports Club', 'R202', 'Ms. Sita'),
    ('C3', 'Drama Club',  'R303', 'Mr. Kiran'),
    ('C4', 'Coding Club', 'Lab1', 'Mr. Anil');

-- insert memberships
INSERT INTO Membership (StudentID, ClubID, JoinDate) VALUES
    (1, 'C1', '2024-01-10'),
    (2, 'C2', '2024-01-12'),
    (1, 'C2', '2024-01-15'),
    (3, 'C1', '2024-01-20'),
    (4, 'C3', '2024-01-18'),
    (5, 'C1', '2024-01-22'),
    (2, 'C3', '2024-01-25'),
    (6, 'C2', '2024-01-27'),
    (3, 'C4', '2024-01-28'),
    (7, 'C4', '2024-01-30');

-- add a new student
INSERT INTO Student VALUES (8, 'Priya', 'priya@email.com');

-- add a new club
INSERT INTO Club VALUES ('C5', 'Photography Club', 'R404', 'Ms. Lena');

-- show all students
SELECT * FROM Student;

-- show all clubs
SELECT * FROM Club;

-- JOIN: student name + club name + join date
SELECT s.StudentName, c.ClubName, m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club    c ON m.ClubID    = c.ClubID
ORDER BY s.StudentName;

-- bonus: how many members per club
SELECT c.ClubName, COUNT(m.StudentID) AS Members
FROM Club c
LEFT JOIN Membership m ON c.ClubID = m.ClubID
GROUP BY c.ClubName;