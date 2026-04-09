-- 1 Вывести id департамента , в котором работает сотрудник, в зависимости от Id сотрудника

delimiter $$

create procedure id_dep(in emp_id int)
begin
	select department
    from employees_procedures
    where id = emp_id;
    end $$
    
    delimiter ;
    
    call id_dep(3);
    
-- 2 Создайте хранимую процедуру get_employee_age, которая принимает id сотрудника (IN-параметр) и возвращает его возраст через OUT-параметр.

delimiter $$
create procedure get_employee_age(
	in emp_id INT,
    out emp_age int
    )
    begin
		select age
        into emp_age
        from employees_procedures
        where id = emp_id;
		end $$
    
    delimiter ;
set @emp_age = 0;
call get_employee_age(4,@emp_age);
select @emp_age;
drop procedure get_employee_age;
-- 3 Создайте хранимую процедуру decrease_salary, которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%.

delimiter $$
create procedure decrease_salary(
inout emp_salary decimal(10, 2)
)
begin
	set emp_salary = emp_salary * 0.9;
    end $$

delimiter ;

set @salary = 100000;
call decrease_salary(@salary);
select @salary;