import psycopg2

try:
    conexion = psycopg2.connect(user="postgres",
                                password="dafneyjuli04",
                                database="COLLISION_DB",
                                host="localhost",
                                port="5432")
    print("Conexión correcta!")
    
    sql1 = """select *
         from borough;"""
    sql2 = """select *
         from collision
         limit 10;"""
    sql3 = """select *
         from crash
         limit 10;"""
    sql4 = """select vehicle_damage
         from damage
         limit 10;"""     
    sql5 = """select person_injury
         from injury;"""   
    #sql6 = """select collision_id, person_unique_id
    #     from involve
    #     limit 10;"""
    #sql7 = """select collision_id, person_unique_id, vehicle_unique_id
    #     from participate
    #     limit 10;"""
    sql8 = """select person_unique_id
         from person
         limit 10;"""
    sql9 = """select person_type_id
         from person_type;"""
    sql10 = """select sex_id
         from sex;"""
    sql11 = """select vehicle_unique_id
         from vehicle
         limit 10;"""
    sql12 = """select vehicle_type_id
         from vehicle_type;"""

    #CONSULTAR BOROUGH
    cursor = conexion.cursor() 
    cursor.execute(sql1) 
    borough = cursor.fetchone() 
    print("****DISTRITOS****")
    while borough:
        print(borough [0]) 
        borough = cursor.fetchone()
    #CONSULTAR COLLISION
    cursor2 = conexion.cursor() 
    cursor2.execute(sql2) 
    collision = cursor2.fetchone() 
    print("****COLISIONES****")
    while collision:
        print(collision [0]) 
        collision = cursor2.fetchone()
    #CONSULTAR CRASH
    cursor3 = conexion.cursor() 
    cursor3.execute(sql3) 
    crash = cursor3.fetchone() 
    print("****CRASH****")
    while crash:
        print(crash [0])
        crash = cursor3.fetchone()
    #CONSULTAR DAMAGE
    cursor4 = conexion.cursor() 
    cursor4.execute(sql4) 
    damage = cursor4.fetchone() 
    print("****DAMAGE****")
    while damage:
        print(damage [0])
        damage = cursor4.fetchone()
    #CONSULTAR INJURY
    cursor5 = conexion.cursor() 
    cursor5.execute(sql5) 
    injury = cursor5.fetchone() 
    print("****INJURY****")
    while injury:
        print(injury [0])
        injury = cursor5.fetchone()
    #CONSULTAR INVOLVE
    """cursor6 = conexion.cursor() 
    cursor6.execute(sql6) 
    involve = cursor6.fetchone() 
    print("****INVOLVE****")
    while involve:
        print(involve [0])
        involve = cursor6.fetchone()"""
    #CONSULTAR PARTICIPATE
    """cursor7 = conexion.cursor() 
    cursor7.execute(sql7) 
    participate = cursor7.fetchone() 
    print("****PARTICIPATE****")
    while participate:
        print(participate [0])
        participate = cursor7.fetchone()"""
    #CONSULTAR PERSON
    cursor8 = conexion.cursor() 
    cursor8.execute(sql8) 
    person = cursor8.fetchone() 
    print("****PERSON****")
    while person:
        print(person [0])
        person = cursor8.fetchone()
    #CONSULTAR PERSON TYPE
    cursor9 = conexion.cursor() 
    cursor9.execute(sql9) 
    person_type = cursor9.fetchone() 
    print("****PERSON TYPE****")
    while person_type:
        print(person_type [0])
        person_type = cursor9.fetchone()
    #CONSULTAR SEX
    cursor10 = conexion.cursor() 
    cursor10.execute(sql10) 
    sex = cursor10.fetchone() 
    print("****SEX****")
    while sex:
        print(sex [0])
        sex = cursor10.fetchone()
    #CONSULTAR VEHICLE
    cursor11 = conexion.cursor() 
    cursor11.execute(sql11) 
    vehicle = cursor11.fetchone() 
    print("****VEHICLE****")
    while vehicle:
        print(vehicle [0])
        vehicle = cursor11.fetchone()
    #CONSULTAR VEHICLE TYPE
    cursor12 = conexion.cursor() 
    cursor12.execute(sql12) 
    vehicle_type = cursor12.fetchone() 
    print("****VEHICLE TYPE****")
    while vehicle_type:
        print(vehicle_type [0])
        vehicle_type = cursor12.fetchone()
    
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)

finally:
    cursor.close()
    cursor2.close()
    cursor3.close()
    cursor4.close()
    cursor5.close()
    #cursor6.close()
    #cursor7.close()
    cursor8.close()
    cursor9.close()
    cursor10.close()
    cursor11.close()
    cursor12.close()
    conexion.close()
