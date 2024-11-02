# Write your MySQL query statement below
select EmployeeUNI.unique_id, Employees.name from Employees left join EmployeeUni on employees.id=employeeuni.id