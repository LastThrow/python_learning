from pymysql import connect


class JD(object):
    def __init__(self):
        # 连接对象设置为实例属性
        self.conn = connect(host="127.0.0.1", port=3306, user='root', password='aptx4869..slj', database='test')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def menu():
        print("----京东商城----")
        print("1:所有的商品")
        print("2:所有的商品分类")
        print("3:所有的商品品牌")
        print("3:添加商品品牌")
        choice = input("输入您的选择:")
        return choice

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有的商品"""
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        """显示所有的商品种类"""
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        """显示所有的商品"""
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    # 删、改的操作只有sql语句不通过
    def add_brands(self):
        """插入商品品牌"""
        item_name = input("输入新商品的名称：")
        sql = """insert into goods_brands(name) values(%s)""" % item_name
        self.cursor.execute(sql)  # 若不commit，可以通过rollback()撤回这里执行的sql语句
        self.conn.commit()

    def get_info_by_name(self):
        name = input("输入要查询的商品名：")
        # sql = """select * from goods where name='%s';""" % name
        # print(sql)
        # self.execute_sql(sql)
        # 输入 ' or 1=1 '
        sql = "select * from goods where name=%s"
        self.cursor.execute(sql, [name])
        print(self.cursor.fetchall())

    def run(self):
        while True:
            choice = self.menu()
            if choice == "1":
                self.show_all_items()
            elif choice == "2":
                self.show_cates()
            elif choice == "3":
                self.show_brands()
            elif choice == "4":
                self.add_brands()
            else:
                print("输入有误，重新输入...")


def main():
    jd = JD()
    jd.run()


if __name__ == "__main__":
    main()
