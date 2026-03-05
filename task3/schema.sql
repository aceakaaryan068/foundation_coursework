CREATE TABLE Student (
    StudentID   INT          PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    Email       VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE Club (
    ClubID     VARCHAR(5)   PRIMARY KEY,
    ClubName   VARCHAR(100) NOT NULL,
    ClubRoom   VARCHAR(20),
    ClubMentor VARCHAR(100)
);

-- links students to clubs (resolves many-to-many relationship)
CREATE TABLE Membership (
    MembershipID SERIAL       PRIMARY KEY,
    StudentID    INT          NOT NULL REFERENCES Student(StudentID),
    ClubID       VARCHAR(5)   NOT NULL REFERENCES Club(ClubID),
    JoinDate     DATE         NOT NULL
);