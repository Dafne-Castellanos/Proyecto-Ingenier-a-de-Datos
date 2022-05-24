import psycopg2

class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user="usuario",
                                               password="clave",
                                               database="collision_db",
                                               host="localhost", 
                                               port="puerto")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()
