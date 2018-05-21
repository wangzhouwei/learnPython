import mysql.connector
dbconfig = {
    'host': 'localhost',
    'user': 'vsearch',
    'password': '123456',
    'database': 'vsearchlogDB',
}
def connect_db(req,res):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    # _sql = """show tables"""
    # _sql = """describe log"""
    _sql = """insert into log
    (phrase,letters,ip,browser_string,results)
    values
    (%s,%s,%s,%s,%s)"""
    cursor.execute(_sql, (req.form['phrase'],req.form['letters'],req.remote_addr,req.user_agent.browser,res,))
    conn.commit()
    # _sql = """select * from log"""
    # res = cursor.fetchall()
    # for target_list in res:
    #     print(target_list)
    cursor.close()
    conn.close()
