import psycopg2


class Connection:

    def __init__(self):
        self.connection = None

    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="****",
                                               database="COLLISION_DB",
                                               host="localhost",
                                               port="5432")
        except Exception as e:
            print(e)

    def closeConnection(self):
        self.connection.close()
