#Escenarios en Dash

#1er Escenario __________________________________________________________________________________________________________

def CovidBronx():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'BRONX' and date <= '2022-03-01' and '2019-03-01' <=date
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def BeforeCovidBronx():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'BRONX' and '2019-03-01' <= date and date < '2020-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def DuringCovidBronx():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'BRONX' and '2020-03-01' <= date and date < '2021-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def AfterCovidBronx():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'BRONX' and date >= '2021-03-01' and date < '2022-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def CovidBrooklyn():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'BROOKLYN' and date <= '2022-03-01' and '2019-03-01' <=date
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def BeforeCovidBrooklyn():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'BROOKLYN' and '2019-03-01' <= date and date < '2020-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def DuringCovidBrooklyn():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'BROOKLYN' and '2020-03-01' <= date and date < '2021-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def AfterCovidBrooklyn():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'BROOKLYN' and date >= '2021-03-01' and date < '2022-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def CovidManhattan():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'MANHATTAN' and date <= '2022-03-01' and '2019-03-01' <=date
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def BeforeCovidManhattan():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'MANHATTAN' and '2019-03-01' <= date and date < '2020-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def DuringCovidManhattan():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'MANHATTAN' and '2020-03-01' <= date and date < '2021-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def AfterCovidManhattan():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'MANHATTAN' and date >= '2021-03-01' and date < '2022-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def CovidQueens():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
    WHERE c.borough = 'QUEENS' and date <= '2022-03-01' and '2019-03-01' <=date
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def BeforeCovidQueens():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'QUEENS' and '2019-03-01' <= date and date < '2020-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def DuringCovidQueens():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'QUEENS' and '2020-03-01' <= date and date < '2021-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def AfterCovidQueens():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'QUEENS' and date >= '2021-03-01' and date < '2022-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def CovidStatenI():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
    WHERE c.borough = 'STATEN ISLAND' and date <= '2022-03-01' and '2019-03-01' <=date
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def BeforeCovidStatenI():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'STATEN ISLAND' and '2019-03-01' <= date and date < '2020-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def DuringCovidStatenI():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'STATEN ISLAND' and '2020-03-01' <= date and date < '2021-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

def AfterCovidStatenI():
    return """select extract(hour from c.time) as time, count(c.collision_id) as num_accidents
from collision c, borough b 
WHERE c.borough = 'STATEN ISLAND' and date >= '2021-03-01' and date < '2022-03-01'
group by extract(hour from c.time)
order by extract(hour from c.time) ASC;"""

#2do Escenario __________________________________________________________________________________________________________
def accidentRPopulation():
    return """select c.borough, count(c.collision_id)::float/b.population as accidentality_rate_population
from collision as c INNER JOIN borough as b ON (c.borough=b.borough)
group by c.borough, b.population;"""

def accidentRArea():
    return"""select c.borough, count(c.collision_id)::float/b.area as accidentality_rate_area
from collision as c INNER JOIN borough as b ON (c.borough=b.borough)
group by c.borough, b.area;"""


#3er Escenario __________________________________________________________________________________________________________

def typePerson():
    return """SELECT pt.person_type as tipo_persona, count(pt.person_type) as cantidad_personas
FROM person p INNER JOIN person_type pt ON (p.person_type_id = pt.person_type_id)
INNER JOIN involve i ON (p.person_unique_id = i.person_unique_id)
INNER JOIN collision c ON (i.collision_id = c.collision_id)
GROUP BY pt.person_type
ORDER BY cantidad_personas DESC;"""

def sexPerson():
    return """SELECT s.person_sex as sexo_persona, count(s.person_sex) as cantidad_personas
FROM person p INNER JOIN sex s ON (p.person_sex_id = s.person_sex_id)
INNER JOIN involve i ON (p.person_unique_id = i.person_unique_id)
INNER JOIN collision c ON (i.collision_id = c.collision_id)
GROUP BY s.person_sex
ORDER BY cantidad_personas DESC;"""


#4to Escenario __________________________________________________________________________________________________________

def damageVehicle():
    return """SELECT d.vehicle_damage as daño_vehiculo, count(d.vehicle_damage) as cantidad_vehiculos
FROM vehicle_type as vt INNER JOIN vehicle v ON (vt.vehicle_type_id = v.vehicle_type_id)
INNER JOIN damage as d ON (d.vehicle_damage_id = v.vehicle_damage_id)
GROUP BY d.vehicle_damage
ORDER BY cantidad_vehiculos DESC;"""

def typeVehicle():
    return """SELECT vt.vehicle_type as tipo_vehiculo, count(vt.vehicle_type) as cantidad_vehiculos
FROM vehicle_type as vt INNER JOIN vehicle v ON (vt.vehicle_type_id = v.vehicle_type_id)
INNER JOIN damage as d ON (d.vehicle_damage_id = v.vehicle_damage_id)
GROUP BY vt.vehicle_type
ORDER BY cantidad_vehiculos DESC;"""
