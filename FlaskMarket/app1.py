from datetime import datetime
from flask import Flask, render_template, request,jsonify
import mysql.connector  
from flask_mysqldb import MySQL  
import requests
import pickle

from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('cat_model_pickle.pkl', 'rb'))

con = mysql.connector.connect(host="127.0.0.1", user="root", password="Ananya162", database="employee_database")
cursor = con.cursor()

@app.route('/',methods= ['GET'])
def man():
    return render_template('predict.html')

# no errors till here 

@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':

        Employee_ID = request.args['Employee ID']
        Date_of_Joining = datetime(request.form['Date of Joining'])

        Gender = request.form['Gender']       

        Company_Type = request.form['Company Type']    

        WFH_Setup_Available = request.form['WFH Setup Available']    

        Designation = float(request.form['Designation'])
        
        Working_Hours = float(request.form['Resource Allocation'])
      
        Mental_Fatigue_Score = float(request.form['Mental Fatigue Score'])
     
        cursor.execute("""INSERT INTO 'Employee'('Employee_ID','Date_of_Joining','Gender','Company_Type','WFH_Setup_Available','Designation','Resource_Allocation','Mental_Fatigue_Score') VALUES('{}','{}','{}','{}','{}','{}','{}','{}')""".format(Employee_ID, Date_of_Joining, Gender, Company_Type,WFH_Setup_Available, Designation, Working_Hours, Mental_Fatigue_Score))
        con.commit()
        #pred = model.predict([[ Employee_ID, Date_of_Joining, Gender, Company_Type,WFH_Setup_Available, Designation, Working_Hours, Mental_Fatigue_Score]])
        #output = round(pred[0],2)
        return cursor.execute("""SELECT 'Burn_Rate' FROM `Employee` WHERE `Employee_ID` LIKE '{}'""".format(Employee_ID))
    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
