#Escenarios en Dash

#1er Escenario

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

#2do Escenario

def BronxByArea():
    return """SELECT c.borough, count( DISTINCT collision_id)/(area) as Accidentality
From collision c, borough b
WHERE c.borough = 'BRONX' and b.borough = 'BRONX'
Group by c.borough, b.area;"""

def BronxByPopulation():
    return """SELECT count( DISTINCT collision_id)::float/(population) as Accidentality
From collision c, borough b
WHERE c.borough = 'BRONX' and b.borough = 'BRONX'
Group by b.population;"""

def BrooklynByArea():
    return """SELECT count( DISTINCT collision_id)/(area) as Accidentality
From collision c, borough b
WHERE c.borough = 'BROOKLYN' and b.borough = 'BROOKLYN'
Group by b.area;"""

def BrooklynByPopulation():
    return"""SELECT count( DISTINCT collision_id)::float/(population) as Accidentality
From collision c, borough b
WHERE c.borough = 'BROOKLYN' and b.borough = 'BROOKLYN'
Group by b.population;"""

def ManhattanByArea():
    return """SELECT count( DISTINCT collision_id)/(area) as Accidentality
From collision c, borough b
WHERE c.borough = 'MANHATTAN' and b.borough = 'MANHATTAN'
Group by b.area;"""

def ManhattanByPopulation():
    return """SELECT count( DISTINCT collision_id)::float/(population) as Accidentality
From collision c, borough b
WHERE c.borough = 'MANHATTAN' and b.borough = 'MANHATTAN'
Group by b.population;"""

def QueensByArea():
    return """SELECT count( DISTINCT collision_id)/(area) as Accidentality
From collision c, borough b
WHERE c.borough = 'QUEENS' and b.borough = 'QUEENS'
Group by b.area;"""

def QueensByPopulation():
    return """SELECT count( DISTINCT collision_id)::float/(population) as Accidentality
From collision c, borough b
WHERE c.borough = 'QUEENS' and b.borough = 'QUEENS'
Group by b.population;"""

def StatenIByArea():
    return """SELECT count( DISTINCT collision_id)/(area) as Accidentality
From collision c, borough b
WHERE c.borough = 'STATEN ISLAND' and b.borough = 'STATEN ISLAND'
Group by b.area"""

def StatenIByPopulation():
    return """SELECT count( DISTINCT collision_id)::float/(population) as Accidentality
From collision c, borough b
WHERE c.borough = 'STATEN ISLAND' and b.borough = 'STATEN ISLAND'
Group by b.population;"""

#3er Escenario

def Bronx():
    return """SELECT p.person_age, count(p.person_age) as aQuantity, s.sex, count(s.sex) as sQuantity, pt.person_type, count(pt.person_type) as ptQuantity
FROM person p INNER JOIN sex s ON (p.person_sex_id = sex_id)
INNER JOIN person_type pt ON (p.person_type_id = pt.person_type_id)
INNER JOIN involve i ON (p.person_unique_id = i.person_unique_id)
INNER JOIN collision c ON (i.collision_id = c.collision_id)
INNER JOIN borough b ON (b.borough = c.borough)
WHERE b.borough = 'BRONX'
GROUP BY p.person_age, s.sex, pt.person_type
ORDER BY aQuantity, sQuantity, ptQuantity DESC;"""

def Brooklyn():
    return """SELECT p.person_age, count(p.person_age) as aQuantity, s.sex, count(s.sex) as sQuantity, pt.person_type, count(pt.person_type) as ptQuantity
FROM person p INNER JOIN sex s ON (p.person_sex_id = sex_id)
INNER JOIN person_type pt ON (p.person_type_id = pt.person_type_id)
INNER JOIN involve i ON (p.person_unique_id = i.person_unique_id)
INNER JOIN collision c ON (i.collision_id = c.collision_id)
INNER JOIN borough b ON (b.borough = c.borough)
WHERE b.borough = 'BROOKLYN'
GROUP BY p.person_age, s.sex, pt.person_type
ORDER BY aQuantity, sQuantity, ptQuantity DESC;"""

def Manhattan():
    return """SELECT p.person_age, count(p.person_age) as aQuantity, s.sex, count(s.sex) as sQuantity, pt.person_type, count(pt.person_type) as ptQuantity
FROM person p INNER JOIN sex s ON (p.person_sex_id = sex_id)
INNER JOIN person_type pt ON (p.person_type_id = pt.person_type_id)
INNER JOIN involve i ON (p.person_unique_id = i.person_unique_id)
INNER JOIN collision c ON (i.collision_id = c.collision_id)
INNER JOIN borough b ON (b.borough = c.borough)
WHERE b.borough = 'MANHATTAN'
GROUP BY p.person_age, s.sex, pt.person_type
ORDER BY aQuantity, sQuantity, ptQuantity DESC;"""

def Queens():
    return """SELECT p.person_age, count(p.person_age) as aQuantity, s.sex, count(s.sex) as sQuantity, pt.person_type, count(pt.person_type) as ptQuantity
FROM person p INNER JOIN sex s ON (p.person_sex_id = sex_id)
INNER JOIN person_type pt ON (p.person_type_id = pt.person_type_id)
INNER JOIN involve i ON (p.person_unique_id = i.person_unique_id)
INNER JOIN collision c ON (i.collision_id = c.collision_id)
INNER JOIN borough b ON (b.borough = c.borough)
WHERE b.borough = 'QUEENS'
GROUP BY p.person_age, s.sex, pt.person_type
ORDER BY aQuantity, sQuantity, ptQuantity DESC;"""

def StatenI():
    return """SELECT p.person_age, count(p.person_age) as aQuantity, s.sex, count(s.sex) as sQuantity, pt.person_type, count(pt.person_type) as ptQuantity
FROM person p INNER JOIN sex s ON (p.person_sex_id = sex_id)
INNER JOIN person_type pt ON (p.person_type_id = pt.person_type_id)
INNER JOIN involve i ON (p.person_unique_id = i.person_unique_id)
INNER JOIN collision c ON (i.collision_id = c.collision_id)
INNER JOIN borough b ON (b.borough = c.borough)
WHERE b.borough = 'STATEN ISLAND'
GROUP BY p.person_age, s.sex, pt.person_type
ORDER BY aQuantity, sQuantity, ptQuantity DESC;"""

#4to Escenario

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
