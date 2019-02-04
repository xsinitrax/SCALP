import psycopg2
import config


class DbConnection:

    def __init__(self):
        self._host = config.DATABASE_CONFIG['host']
        self._port = config.DATABASE_CONFIG['port']
        self._db = config.DATABASE_CONFIG['dbname']
        self._user = config.DATABASE_CONFIG['user']
        self._password = config.DATABASE_CONFIG['password']

    def getConnection(self):
        try:
            self.connection = psycopg2.connect(host=self._host,
                                               user=self._user,
                                               password=self._password,
                                               dbname=self._db)
            self.connection.autocommit = True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return self.connection

    def __del__(self):
        self.connection = None
