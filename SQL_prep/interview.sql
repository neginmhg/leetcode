--1. What is Pattern Matching in SQL?
    -- Using the % wildcard to perform a simple search
    -- The % wildcard matches zero or more characters of any type and can be used to
    -- define wildcards both before and after the pattern. 
    -- Search a student in your database with first name STARTING with the letter K:
    SELECT *
    FROM students
    WHERE first_name LIKE 'K%'
    --Omitting the patterns using the NOT keyword
    SELECT *
    FROM students
    WHERE first_name NOT LIKE 'K%'

    --Matching a pattern ANYWHERE using the % wildcard twice
    --Search for a student in the database where he/she has a K in his/her first name.
    SELECT *
    FROM students
    WHERE first_name LIKE '%Q%'

    --Matching patterns for a specific length
    --The _ wildcard plays an important role as a limitation when it matches exactly one character. It limits the length and position of the matched results. For example - 

    SELECT *   /* Matches first names with three or more letters */
    FROM students
    WHERE first_name LIKE '___%'

    SELECT *   /* Matches first names with exactly four characters */
    FROM students
    WHERE first_name LIKE '____'



--2. How to create empty tables with the same structure as another table?

    --Creating empty tables with the same structure can be done smartly by fetching 
    --the records of one table into a new table using the INTO operator while fixing a 
    --WHERE clause to be false for all records. Hence, SQL prepares the new table with a 
    --duplicate structure to accept the fetched records but since no records get fetched due to the WHERE clause in action, 
    --nothing is inserted into the new table.
    SELECT * INTO Students_copy
    FROM Students WHERE 1 = 2;



--3. What is a Recursive Stored Procedure?
--A stored procedure that calls itself until a boundary condition is reached, is called a recursive stored procedure. 
    --This recursive function helps the programmers to deploy the same set of code several times as and when required. 
    --Some SQL programming languages limit the recursion depth to prevent an infinite loop of procedure calls 
    --from causing a stack overflow, which slows down the system and may lead to system crashes.

    DELIMITER $$     /* Set a new delimiter => $$ */
    CREATE PROCEDURE calctotal( /* Create the procedure */
    IN number INT,   /* Set Input and Ouput variables */
    OUT total INT
    ) BEGIN
    DECLARE score INT DEFAULT NULL;   /* Set the default value => "score" */
    SELECT awards FROM achievements   /* Update "score" via SELECT query */
    WHERE id = number INTO score;
    IF score IS NULL THEN SET total = 0;   /* Termination condition */
    ELSE
    CALL calctotal(number+1);   /* Recursive call */
    SET total = total + score;   /* Action after recursion */
    END IF;
    END $$     /* End of procedure */
    DELIMITER ;     /* Reset the delimiter */

-- 4. What is a Stored Procedure?
    --A stored procedure is a subroutine available to applications that access a relational database management system (RDBMS). 
    --Such procedures are stored in the database data dictionary. The sole disadvantage of stored procedure is that it can be executed nowhere except in the database and occupies more memory in the database server. 
    --It also provides a sense of security and functionality as users who can't access the data directly can be granted access via stored procedures.
    DELIMITER $$
    CREATE PROCEDURE FetchAllStudents()
    BEGIN
    SELECT *  FROM myDB.students;
    END $$
    DELIMITER ;

--5. What is User-defined function? What are its various types?
    --The user-defined functions in SQL are like functions in any other programming language that accept parameters, perform complex calculations, and return a value. 
    --They are written to use the logic repetitively whenever required. There are two types of SQL user-defined functions:
    --Scalar Function: As explained earlier, user-defined scalar functions return a single scalar value.
    --Table-Valued Functions: User-defined table-valued functions return a table as output.
        --Inline: returns a table data type based on a single SELECT statement.
        --Multi-statement: returns a tabular result-set but, unlike inline, multiple SELECT statements can be used inside the function body.

--6.What is a UNIQUE constraint?
    -- A UNIQUE constraint ensures that all values in a column are different. 
    --This provides uniqueness for the column(s) and helps identify each row uniquely. Unlike primary key, 
    --there can be multiple unique constraints defined per table. The code syntax for UNIQUE is quite similar to 
    --that of PRIMARY KEY and can be used interchangeably.

    CREATE TABLE Students (   /* Create table with a single field as unique */
    ID INT NOT NULL UNIQUE
    Name VARCHAR(255)
    );

    CREATE TABLE Students (   /* Create table with multiple fields as unique */
    ID INT NOT NULL
    LastName VARCHAR(255)
    FirstName VARCHAR(255) NOT NULL
    CONSTRAINT PK_Student
    UNIQUE (ID, FirstName)
    );

    ALTER TABLE Students   /* Set a column as unique */
    ADD UNIQUE (ID);
    ALTER TABLE Students   /* Set multiple columns as unique */
    ADD CONSTRAINT PK_Student   /* Naming a unique constraint */
    UNIQUE (ID, FirstName);


-- 7.What is the difference between Clustered and Non-clustered index?
--The differences can be broken down into three small factors -
    --Clustered index modifies the way records are stored in a database based on the indexed column. A non-clustered index creates a separate entity within the table which references the original table.
    --Clustered index is used for easy and speedy retrieval of data from the database, whereas, fetching records from the non-clustered index is relatively slower.
    --In SQL, a table can have a single clustered index whereas it can have multiple non-clustered indexes.


-- 8. What is an Index? Explain its different types.
    --A database index is a data structure that provides a quick lookup of data in a column or columns of a table. 
    --It enhances the speed of operations accessing data from a database table at the cost of additional writes and memory 
    --to maintain the index data structure.

    CREATE INDEX index_name   /* Create Index */
    ON table_name (column_1, column_2);

    DROP INDEX index_name;   /* Drop Index */

    --There are different types of indexes that can be created for different purposes:
        -- 1. Unique Index:
                --Unique indexes are indexes that help maintain data integrity by ensuring that no two rows of data in a table have identical key values. 
                --Once a unique index has been defined for a table, uniqueness is enforced whenever keys are added or changed within the index.
                CREATE UNIQUE INDEX myIndex
                ON students (enroll_no);
            
        --2.Non-Unique Index: 
                --Non-unique indexes are not used to enforce constraints on the tables with which they are associated. 
                --Instead, non-unique indexes are used solely to improve query performance by maintaining a sorted order of data values that are
                -- used frequently.

        -- 2. Clustered and Non-Clustered Index:
                --Clustered indexes are indexes whose order of the rows in the database corresponds to the order of the rows in the index. 
                --This is why only one clustered index can exist in a given table, whereas, multiple non-clustered indexes can exist in the table.
                --The only difference between clustered and non-clustered indexes is that the database manager attempts to keep the data in the database in the same order as the corresponding keys appear in the clustered index.
                --Clustering indexes can improve the performance of most query operations because they provide a linear-access path to data stored in the database.



-- 9. What is a Cross-Join?
    --Cross join can be defined as a cartesian product of the two tables included in the join. 
    --The table after join contains the same number of rows as in the cross-product of the number of rows in the two tables. 
    --If a WHERE clause is used in cross join then the query will work like an INNER JOIN.
    SELECT stu.name, sub.subject 
    FROM students AS stu
    CROSS JOIN subjects AS sub;


--- 10. 4 different types of JOINs in SQL:
    --(INNER) JOIN: Retrieves records that have matching values in both tables involved in the join. This is the widely used join for queries.
        SELECT *
        FROM Table_A
        JOIN Table_B;
        SELECT *
        FROM Table_A
        INNER JOIN Table_B;
    --LEFT (OUTER) JOIN: Retrieves all the records/rows from the left and the matched records/rows from the right table.
        SELECT *
        FROM Table_A A
        LEFT JOIN Table_B B
        ON A.col = B.col;
    --RIGHT (OUTER) JOIN: Retrieves all the records/rows from the right and the matched records/rows from the left table.
        SELECT *
        FROM Table_A A
        RIGHT JOIN Table_B B
        ON A.col = B.col;
    --FULL (OUTER) JOIN: Retrieves all the records where there is a match in either the left or right table.
        SELECT *
        FROM Table_A A
        FULL JOIN Table_B B
        ON A.col = B.col;

--11. What is a Foreign Key?
    --A FOREIGN KEY comprises of single or collection of fields in a table that essentially refers to the PRIMARY KEY in another table. Foreign key constraint ensures referential integrity in the relation between two tables.
    --The table with the foreign key constraint is labeled as the child table, and the table containing the candidate key is labeled as the referenced or parent table.
        CREATE TABLE Students (   /* Create table with foreign key - Way 1 */
        ID INT NOT NULL
        Name VARCHAR(255)
        LibraryID INT
        PRIMARY KEY (ID)
        FOREIGN KEY (Library_ID) REFERENCES Library(LibraryID)
        );

        CREATE TABLE Students (   /* Create table with foreign key - Way 2 */
        ID INT NOT NULL PRIMARY KEY
        Name VARCHAR(255)
        LibraryID INT FOREIGN KEY (Library_ID) REFERENCES Library(LibraryID)
        );

        ALTER TABLE Students   /* Add a new foreign key */
        ADD FOREIGN KEY (LibraryID)
        REFERENCES Library (LibraryID);

--12. What are Constraints in SQL?
    --Constraints are used to specify the rules concerning data in the table. 
    --It can be applied for single or multiple fields in an SQL table during the creation of the table 
    --or after creating using the ALTER TABLE command. The constraints are:
        --NOT NULL - Restricts NULL value from being inserted into a column.
        --CHECK - Verifies that all values in a field satisfy a condition.
        --DEFAULT - Automatically assigns a default value if no value has been specified for the field.
        --UNIQUE - Ensures unique values to be inserted into the field.
        --INDEX - Indexes a field providing faster retrieval of records.
        --PRIMARY KEY - Uniquely identifies each record in a table.
        --FOREIGN KEY - Ensures referential integrity for a record in another table.


--13. What are the TRUNCATE, DELETE and DROP statements?

    --DELETE statement is used to delete rows from a table.
    DELETE FROM Candidates
    WHERE CandidateId > 1000;

    --TRUNCATE command is used to delete all the rows from the table and free the space containing the table.
    TRUNCATE TABLE Candidates;

    --DROP command is used to remove an object from the database. If you drop a table, all the rows in the table are deleted and the table structure is removed from the database.
    DROP TABLE Candidates;

--14. What is the difference between DELETE and TRUNCATE statements?
    --The TRUNCATE command is used to delete all the rows from the table and free the space containing the table.
    --The DELETE command deletes only the rows from the table based on the condition given in the where clause or deletes 
    --all the rows from the table if no condition is specified. But it does not free the space containing the table



-- 15. What are Aggregate and Scalar functions?
/*
    An aggregate function performs operations on a collection of values to return a single scalar value. 
    Aggregate functions are often used with the GROUP BY and HAVING clauses of the SELECT statement. 
    Following are the widely used SQL aggregate functions:
            AVG() - Calculates the mean of a collection of values.
            COUNT() - Counts the total number of records in a specific table or view.
            MIN() - Calculates the minimum of a collection of values.
            MAX() - Calculates the maximum of a collection of values.
            SUM() - Calculates the sum of a collection of values.
            FIRST() - Fetches the first element in a collection of values.
            LAST() - Fetches the last element in a collection of values.
            Note: All aggregate functions described above ignore NULL values except for the COUNT function.

    A scalar function returns a single value based on the input value. Following are the widely used SQL scalar functions:
            LEN() - Calculates the total length of the given field (column).
            UCASE() - Converts a collection of string values to uppercase characters.
            LCASE() - Converts a collection of string values to lowercase characters.
            MID() - Extracts substrings from a collection of string values in a table.
            CONCAT() - Concatenates two or more strings.
            RAND() - Generates a random collection of numbers of a given length.
            ROUND() - Calculates the round-off integer value for a numeric field (or decimal point values).
            NOW() - Returns the current date & time.
            FORMAT() - Sets the format to display a collection of values.
*/