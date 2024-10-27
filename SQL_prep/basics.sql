Employees
+----+---------+-----------+---------+------------+
| id | name    | dept_id   | salary  | join_date  |
+----+---------+-----------+---------+------------+
| 1  | Alice   | 1         | 70000   | 2019-04-23 |
| 2  | Bob     | 1         | 80000   | 2020-03-17 |
| 3  | Charlie | 2         | 95000   | 2021-01-12 |
| 4  | Diana   | 3         | 62000   | 2018-11-10 |
| 5  | Evan    | 3         | 65000   | 2022-02-05 |
+----+---------+-----------+---------+------------+


Departments
+----+-------------+--------------------+
| id | dept_name   | manager_name       |
+----+-------------+--------------------+
| 1  | Engineering | Sarah Johnson      |
| 2  | Marketing   | Tom Ellis          |
| 3  | HR          | Rebecca Smith      |
+----+-------------+--------------------+


Salaries
+----------+--------+----------+------------+
| emp_id   | salary | bonus    | date       |
+----------+--------+----------+------------+
| 1        | 65000  | 3000     | 2019-04-23 |
| 1        | 70000  | 3500     | 2021-05-13 |
| 2        | 75000  | 4000     | 2020-03-17 |
| 2        | 80000  | 4500     | 2021-09-20 |
| 3        | 90000  | 2000     | 2021-01-12 |
| 3        | 95000  | 2500     | 2022-04-07 |
| 4        | 60000  | 1500     | 2018-11-10 |
| 4        | 62000  | 1600     | 2021-10-12 |
| 5        | 64000  | 1200     | 2022-02-05 |
+----------+--------+----------+------------+



SELECT * FROM Employees;

INSERT INTO Employees (id, name, dept_id, salary, join_date) 
VALUES (6, 'Frank', 2, 72000, '2023-01-15');

UPDATE Employees 
SET salary = 75000 
WHERE id = 4;

SELECT * FROM Employees WHERE salary > 70000;

SELECT * FROM Employees WHERE dept_id IN (1, 3);

SELECT * FROM Employees ORDER BY salary DESC;

--Count the number of employees in each department
SELECT dept_id, COUNT(*) AS num_employees
FROM Employees
GROUP BY dept_id;

--Calculate the average salary by department
SELECT dept_id, AVG(salary) AS avg_salary
FROM Employees
GROUP BY dept_id;

--Find departments with more than one employee
SELECT dept_id, COUNT(*) AS num_employees
FROM Employees
GROUP BY dept_id
HAVING COUNT(*) > 1;

--INNER JOIN Employees with Departments to display department names
SELECT Employees.name, Departments.dept_name
FROM Employees 
INNER JOIN Departments 
ON Employees.dept_id = Departments.id;

--LEFT JOIN to include all employees and show department names (including those without a department)
SELECT Employees.name, Departments.dept_name
FROM Employees
LEFT JOIN Departments 
ON Employees.dept_id = Departments.id;

--Select employees with the highest salar
SELECT * FROM Employees
WHERE salary = (SELECT MAX(salary) FROM Employees);

--Select employees in departments where the average salary is over 70,000
SELECT * FROM Employees
WHERE dept_id IN (
    SELECT dept_id
    FROM Employees
    GROUP BY dept_id
    HAVING AVG(salary) > 70000
);

--UNION to get all distinct department managers and employees
SELECT name AS person FROM Employees
UNION
SELECT manager_name AS person FROM Departments;

--UNION ALL to get all entries of employees and department managers with duplicates
SELECT name AS person FROM Employees
UNION ALL
SELECT manager_name AS person FROM Departments;

--Row number for each employee based on salary within their department
SELECT name, dept_id, salary,
       ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank
FROM Employees;



--Top 3 highest-paid employees
SELECT * FROM Employees
ORDER BY salary DESC
LIMIT 3;

--Select employees without a department assigned
SELECT * FROM Employees WHERE dept_id IS NULL;



--Replace NULL department IDs with a placeholder in output
SELECT name, COALESCE(dept_id, 'Not Assigned') AS dept_id
FROM Employees;

--Categorize employees based on their salary level
SELECT name, salary,
  CASE
    WHEN salary > 80000 THEN 'High'
    WHEN salary BETWEEN 60000 AND 80000 THEN 'Medium'
    ELSE 'Low'
  END AS salary_level
FROM Employees;

--Create a new table for project assignments
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    employee_id INT,
    start_date DATE
);

--Add a column to track last promotion date in the Employees table
ALTER TABLE Employees 
ADD COLUMN last_promotion_date DATE;

--Delete the Projects table
DROP TABLE Projects;
