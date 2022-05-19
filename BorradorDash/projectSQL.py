def CollisionBeforeCovid():
    return """select -- as --, -- as --, -- as --
            from -- join -- on (-- = --)
            group by --, --
            order by -- desc"""

def CuatroBronx():
    return """SELECT p.person_age, s.sex, pt.person_type
FROM person p JOIN sex s ON (p.person_sex_id = sex_id)
JOIN person_type pt ON (p.person_type_id = pt.person_type_id)
JOIN involve i ON (p.person_unique_id = i.person_unique_id)
JOIN collision c ON (i.collision_id = c.collision_id)
JOIN borough b ON (b.borough = c.borough)
WHERE b.borough = 'BRONX';"""
