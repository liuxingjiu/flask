from pymysql import Connection


def get_data():
    con = None

    try:
        # 创建数据库链接
        con = Connection(host="localhost",  # 主机名
                         port=3306,  # 端口
                         user="root",  # 账户
                         password="123456",  # 密码
                         database="db_python",  # 指定操作的数据库
                         autocommit=True  # 设置自动提交
                         )
        # 创建游标对象

        curser = con.cursor()
        curser.execute("select * from student")
        res = curser.fetchall()
        print(type(res), res)
    except Exception as e:
        print("异常：", e)
    finally:
        # 关闭链接
        con.close()
