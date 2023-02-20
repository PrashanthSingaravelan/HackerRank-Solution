select sum(t1.population) from city t1 
inner join country t2 on t1.countrycode = t2.code
where continent = "Asia"