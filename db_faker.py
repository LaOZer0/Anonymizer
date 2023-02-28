#! python
import argparse
import mysql.connector


def anonimize(db_link: str):

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='electronics',
                                             user='pynative',
                                             password='pynative@#29')

        sql_select_Query = "select * from Laptop"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        print("Total number of rows in table: ", cursor.rowcount)

        for row in range(cursor.rowcount):
            res = cursor.fetchone()
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Price  = ", row[2])
            print("Purchase date  = ", row[3], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Db faker')
    parser.add_argument('db_link', type=str,
                        help='link for MySQL connect')
    parser.add_argument('faker_db', type=str, help='from')
    args = parser.parse_args()
    print(args.indir)
