## remove new cases 

#!flask/bin/python
from flask import Flask, jsonify, abort, request
#import pymysql
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)
#http://127.0.0.1:5000/corona/api/all
@app.route('/corona/api/all', methods=['GET'])
def get_all():
    connection = mysql.connector.connect(host='localhost', port=3307, database='pythonexam', user='dev',password="ax2")
    cursor = connection.cursor()
    query = ("SELECT country, total_cases, New_cases, Total_deaths, New_deaths, Total_recov from corona20200517")
    cursor.execute(query)
    tasks = []
    for country,total_cases,New_cases,Total_deaths,New_deaths,Total_recov in cursor:
        tasks.append(
        {
        'Country': country,
        'Total_cases': total_cases,
        'New_cases': New_cases,
        'Total_deaths': Total_deaths,
        'New_deaths': New_deaths,
        'Total_recov': Total_recov
        },
        )
    #print(tasks)
    cursor.close()
    connection.close()
    return jsonify({'tasks': tasks})
    
#http://127.0.0.1:5000/corona/api/country/USA
@app.route('/corona/api/country/<string:name>', methods=['GET'])
def get_countryByName(name):
    connection = mysql.connector.connect(host='localhost', port=3307, database='pythonexam', user='dev',password="ax2")
    cursor = connection.cursor()
    query = ("SELECT country, total_cases, New_cases, Total_deaths, New_deaths, Total_recov from corona20200517 WHERE country = %s")
    where = name, 
    cursor.execute(query, where)
    tasks = []
    for country,total_cases,New_cases,Total_deaths,New_deaths,Total_recov in cursor:
        tasks.append(
        {
        'Country': country,
        'Total_cases': total_cases,
        'New_cases': New_cases,
        'Total_deaths': Total_deaths,
        'New_deaths': New_deaths,
        'Total_recov': Total_recov
        },
        )
    #print(tasks)
    cursor.close()
    connection.close()
    return jsonify({'tasks': tasks})


a = """@app.route('/corona/api/data/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]}) """
if __name__ == '__main__':
    app.run(debug=True)


