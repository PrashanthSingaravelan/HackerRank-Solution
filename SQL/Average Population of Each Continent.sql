select t2.continent, floor(avg(t1.population))
from city t1 
inner join country t2 on t1.countrycode = t2.code
group by t2.continent