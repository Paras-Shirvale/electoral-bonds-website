from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Par1095#'
app.config['MYSQL_DB'] = 'dcc'

mysql = MySQL(app)

@app.route('/', methods=["POST", "GET"])
def main_page():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT distinct(`Name of the Purchaser`) FROM individual")
    data = cursor.fetchall()
    cursor.close()
    return render_template("home.html", data=data)
    
@app.route('/a1', methods=['POST'])
def a1():
    if request.method == 'POST':
        query = request.form["query"]
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM individual WHERE `Bond Number` = %s", (query,))
        data1 = list(cursor.fetchall())
        cursor.execute("SELECT * FROM political_party WHERE `Bond Number` = %s", (query,))
        data2 = list(cursor.fetchall())
        cursor.close()

    for i in range(len(data1)):
        data1[i] = list(data1[i]) + list(data2[i][1:4]) + list(data2[i][6:])

    return render_template("index.html", ans_1=data1)

@app.route('/result', methods=['POST'])
def result():
    name = request.form['company']
    years = ['2019', '2020', '2021', '2022', '2023', '2024']
    cursor = mysql.connection.cursor()
    results = []

    for year in years:
        cursor.execute("SELECT SUM(CAST(REPLACE(`Denominations`, ',', '') AS UNSIGNED)) FROM political_party WHERE `Name of the Political Party` = %s and `Date of Encashment` LIKE %s", (name, "%"+year))
        data = cursor.fetchall()
        if data[0][0] is None:
            DATA = 0
        else:
            DATA = int(data[0][0])
        
        results.append((year, DATA))
    cursor.close()

    return render_template('result.html', name=name, data=results)

@app.route('/result2', methods=['POST'])
def result2():
    name = request.form['company']
    years = ['2019', '2020', '2021', '2022', '2023', '2024']
    cursor = mysql.connection.cursor()
    results = []

    for year in years:
        cursor.execute("SELECT SUM(CAST(REPLACE(`Denominations`, ',', '') AS UNSIGNED)) FROM individual WHERE `Name of the Purchaser` = %s and `Date of Purchase` LIKE %s", (name, "%"+year))
        data = cursor.fetchall()
        if data[0][0] is None:
            DATA = 0
        else:
            DATA = int(data[0][0])
        
        results.append((year, DATA))
    cursor.close()

    return render_template('result2.html', name=name, data=results)

@app.route('/result4',methods=['POST'])
def result4():
    if request.method=="POST":
        cursor=mysql.connection.cursor()
        value=request.form['party']
        cursor.execute('select `Name of the Purchaser`, individual.Denominations from individual inner join political_party on individual.`Bond Number` = political_party.`Bond Number` and substring(`Journal Date`, 8, 4) = substring(`Date of Encashment`, 8, 4) where `Name of the Political Party` = %s and `Status` = "Paid"', (value,))
        data1=cursor.fetchall()
        cursor.execute("select SUM(CAST(REPLACE(individual.Denominations, ',', '') AS UNSIGNED)) from individual inner join political_party on individual.`Bond Number` = political_party.`Bond Number` and substring(`Journal Date`, 8, 4) = substring(`Date of Encashment`, 8, 4) where `Name of the Political Party` = %s and `Status` = 'Paid'", (value,))
        total = cursor.fetchall()
    cursor.close()
    print(data1)
    return render_template('result4.html',total=total[0][0], result_4=data1, value = value)

@app.route('/result5',methods=['POST'])
def result5():
    if request.method=="POST":
        cursor=mysql.connection.cursor()
        value=request.form['company']
        cursor.execute('select `Name of the Political Party`, political_party.Denominations from individual inner join political_party on individual.`Bond Number` = political_party.`Bond Number` and substring(`Journal Date`, 8, 4) = substring(`Date of Encashment`, 8, 4) where `Name of the Purchaser` = %s', (value,))
        data1=cursor.fetchall()
        cursor.execute("select SUM(CAST(REPLACE(political_party.Denominations, ',', '') AS UNSIGNED)) from individual inner join political_party on individual.`Bond Number` = political_party.`Bond Number` and substring(`Journal Date`, 8, 4) = substring(`Date of Encashment`, 8, 4) where `Name of the Purchaser` = %s", (value,))
        total = cursor.fetchall()
    cursor.close()
    return render_template('result5.html',total=total[0][0], result_5=data1, value = value)

@app.route('/result6',methods=['POST'])
def result6():
    if request.method=="POST":
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT `Name of the political party`, SUM(CAST(REPLACE(political_party.Denominations, ',', '') AS UNSIGNED)) FROM political_party group by `Name of the political party`")
        data=cursor.fetchall()
        cursor.close()
        party = []
        value = []
        for i in data:
            party.append(i[0])
            value.append(i[1])
    return render_template('pie_chart.html', party=party, value=value)

if __name__ == '__main__':
    app.run(debug=True)