from pymysql import *


def main():
    conn = connect(host="127.0.0.1", port=3306, user='root', password='aptx4869..slj', database='test')
    cursor = conn.cursor()
    count = cursor.execute("select * from stu")  # 返回查到的信息数量
    for i in range(count):
        print(cursor.fetchone())  # 还有fetchmany(num)和fetchall()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
