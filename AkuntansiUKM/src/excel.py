from pymysql import*
import xlwt
import pandas.io.sql as sql

# connect the mysql with the python
def connecting():
    con=connect(user="python",password="KaliLinux",host="localhost",database="ukm")

    # read the data
    df=sql.read_sql('select * from laporanjurnal',con)

    # print the data
    print(df)

    # export the data into the excel sheet
    df.to_excel('/home/python/Tugas/AkuntansiUKM/src/documents/excel/jurnal.xls')
