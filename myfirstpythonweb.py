from flask import Flask,render_template,request,escape
from vowels import search4letters
from threading import Thread
import mysql.connector
# import connectDB
from DBcm import UseDatabase
dbconfig = {
    'host': 'localhost',
    'user': 'vsearch',
    'password': '123456',
    'database': 'vsearchlogDB',
}
app = Flask(__name__)
# @app.route('/l')
# def hello()->'302':
#     return redirect('/entry')
def log_request(req:'flask_request',res:str)->None:
    # with open('todos.txt','a') as log:
    #     print(str((req.form,req.remote_addr,req.user_agent)),res,file = log)
    # connectDB.connect_db(req,res)
    with UseDataBase(dbconfig) as cursor:
        _sql = """insert into log
        (phrase,letters,ip,browser_string,results)
        values
        (%s,%s,%s,%s,%s)"""
        cursor.execute(_sql, (req.form['phrase'], req.form['letters'],
                            req.remote_addr, req.user_agent.browser, res,))
def show_list()->None:
    with UseDatabase(dbconfig) as cursor:
        _sql = """select * from log"""
        cursor.execute(_sql)
        res = cursor.fetchall()
        for target_list in res:
            print(target_list)
@app.route('/search',methods=['POST'])
def do_search()->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search4letters(phrase, letters))
    # return str(search4letters(phrase, letters))
    # log_request(res=result, req=request)
    show_list()
    return render_template(
        'result.html', the_phrase=phrase,
        the_letters=letters,
        the_title='Here are your results:',
        the_results=result,)


@app.route('/l')
@app.route('/entry')
def enter_page()->'html':
    return render_template('entry.html',the_title='Welcome to searchletters on the web!')


@app.route('/viewlog')
def view_log()->str:
    # with open('todos.txt') as log:
    #     contant = log.read()
    # return escape(contant)
    """Display the contents of the log file as a HTML table."""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results
                  from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)
        
app.run(debug=True)
