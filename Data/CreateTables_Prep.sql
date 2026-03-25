


use MIST460_RDB_Prep;

go

IF OBJECT_ID('Student')        IS NOT NULL DROP TABLE Student;
IF OBJECT_ID('AppUser')        IS NOT NULL DROP TABLE AppUser;

go

CREATE TABLE AppUser (
    AppUserID       INT IDENTITY(1,1) CONSTRAINT PK_AppUser PRIMARY KEY,
    FullName        NVARCHAR(100)  NOT NULL,
    Email           NVARCHAR(320)  NOT NULL CONSTRAINT UQ_AppUser_Email UNIQUE,
    PasswordHash    VARBINARY(64)  NOT NULL,      -- store salted hash
    UserRole        NVARCHAR(20)   NOT NULL,      -- 'Student','Advisor','Instructor','Alum' (from diagram)
    CreatedAt    DATETIME2(3)   NOT NULL CONSTRAINT DF_AppUser_CreatedAt DEFAULT SYSUTCDATETIME(),
    CONSTRAINT CK_AppUser_UserRole CHECK (UserRole IN (N'Student',N'Advisor',N'Instructor',N'Alum'))
);
GO

CREATE TABLE Student (
    StudentID               INT CONSTRAINT PK_Student PRIMARY KEY,
    TotalCreditsCompleted   INT NOT NULL CONSTRAINT DF_Student_TCC DEFAULT (0),
    CONSTRAINT FK_Student_AppUser FOREIGN KEY (StudentID)
        REFERENCES AppUser(AppUserID) ON DELETE CASCADE,
    CONSTRAINT CK_Student_TCC CHECK (TotalCreditsCompleted >= 0)
);
GO
