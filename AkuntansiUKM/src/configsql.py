import mysql.connector

class MySQL():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connectors()

    def connectors(self):
        try:
            self.dataBase = mysql.connector.connect(
                    host=self.host,
                    user = self.user,
                    password = self.password,
                    database = self.database
                )
            if self.dataBase.is_connected():
                db_Info = self.dataBase.get_server_info()
                print("Terhubung dengan database MariaDB versi", db_Info)
                self.cursor = self.dataBase.cursor()
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Mungkin ada yang salah dengan username, password database anda")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Tidak ada database")
            else:
                print(err)

    # Fungsi insert database
    def insert_data(self, tablename, target=()):
        self.target = target
        query = f"INSERT INTO {tablename} VALUES(%s,%s,%s,%s)"
        self.cursor.execute(query, self.target)
        hasil = self.dataBase.commit()
        if(hasil): print('Berhasil Insert Data')

    def read_data(self, tablename):
        query = f"SELECT * FROM {tablename}"
        self.cursor.execute(query)
        hasil = self.cursor.fetchall()
        for i in hasil:
            print(i)

# if __name__ == "__main__":
    # obj = MySQL('localhost', 'python', 'KaliLinux', 'ukm').read_table('detailperusahaan')
    # obj.insert_table('detailperusahaan', ('PT IDX','Surabaya', '4231', 'fsjhd@gmsk.com'))
