# LeetCode

# query employees whose managerId is not Null, if their salary > salary of employees with
#corresponding managaerId as Id.

#LeetCode 181



SELECT 
    a.Name AS 'Employee'  
FROM 
    Employee AS a, 
    Employee AS b
   
WHERE  
    a.ManagerId = b.Id 
          AND a.Salary > b.Salary 
          
;
