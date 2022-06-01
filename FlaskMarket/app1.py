from flask import Flask, render_template , request 
import numpy as np 

app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql + pymysql://root:Ananya162@localhost/employee_database'
# old method 
#ysql.connector.connect(host="http://sql6.freesqldatabase.com/", user="sql6459204", password="zUlrGmPcNT",database="sql6459204")
#mycur = mydb.cursor()



@app.route('/')
def man():
    return render_template("index.html")

@app.route('/sub', methods = ['POST'])
def submit():
    if request.method=="POST":
        Employee_ID = request.form('Employee ID')
        Date_of_Joining = request.form('Date of Joining')

        Gender = request.form('Gender')  

        Company_Type = request.form('Company Type')   

        WFH_Setup_Available = request.form('WFH Setup Available')

        Designation = request.form('Designation')
        
        Working_Hours = request.form('Resource Allocation')
      
        Mental_Fatigue_Score = request.form('Mental Fatigue Score')
        val = np.array(data[[Employee_ID, Date_of_Joining, Gender, Company_Type,WFH_Setup_Available, Designation, Working_Hours, Mental_Fatigue_Score]])
        rate = model.predict(val)
    return render_template('sub.html',score = rate)

if __name__ == "__main__":
    app.run(debug=True)
