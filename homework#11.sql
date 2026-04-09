
delimiter //
create function radius(r decimal(10, 5))
returns decimal(10, 5)
deterministic
begin
	return pi() * (r * r);
end //

delimiter ;

select radius(5);




delimiter $$
create function gipo(a decimal(10, 2), b decimal(10,2))
returns decimal(10, 2)
deterministic
begin
	return  sqrt(a * a + b * b);
end $$

delimiter $$;

select gipo(5,6);







