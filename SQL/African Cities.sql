select t1.name from city t1 
inner join country t2 on t1.countrycode = t2.code
where continent = "Africa"