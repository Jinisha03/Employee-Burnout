from datetime import datetime
from flask import Flask, render_template, request,jsonify
import mysql.connector  
from flask_sqlalchemy import SQLAlchemy   
import requests
import pickle

from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('cat_model_pickle.pkl', 'rb'))


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql + pymysql://root:Ananya162@localhost/employee_database'
# old method 
#ysql.connector.connect(host="http://sql6.freesqldatabase.com/", user="sql6459204", password="zUlrGmPcNT",database="sql6459204")
#mycur = mydb.cursor()



@app.route('/',methods= ['GET'])
def man():
    return render_template('predict.html')


# no errors till here 
@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':

        Employee_ID = request.form('Employee ID')
        Date_of_Joining = request.form('Date of Joining')

        Gender = request.form('Gender')       

        Company_Type = request.form('Company Type')    

        WFH_Setup_Available = request.form('WFH Setup Available')  

        Designation = request.form('Designation')
        
        Working_Hours = request.form('Resource Allocation')
      
        Mental_Fatigue_Score = request.form('Mental Fatigue Score')
     
        #mycur.execute("""INSERT INTO 'Employee'(`Employee_ID`,`Date_of_Joining`,`Gender`,`Company_Type`,`WFH_Setup_Available`,`Designation`,`Resource_Allocation`,`Mental_Fatigue_Score`) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')""".format(Employee_ID, Date_of_Joining, Gender, Company_Type,WFH_Setup_Available, Designation, Working_Hours, Mental_Fatigue_Score))
        #mycur.commit()
        #pred = model.predict([[ Employee_ID, Date_of_Joining, Gender, Company_Type,WFH_Setup_Available, Designation, Working_Hours, Mental_Fatigue_Score]])
        #output = round(pred[0],2)
        #return #mycur.execute("""SELECT 'Burn_Rate' FROM `Employee` WHERE `Employee_ID` LIKE '{}'""".format(Employee_ID))

        rate = model.predict([Employee_ID, Date_of_Joining, Gender, Company_Type,WFH_Setup_Available, Designation, Working_Hours, Mental_Fatigue_Score])
    return render_template('sub.html' )


if __name__ == "__main__":
    app.run(debug=True)
