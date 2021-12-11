 import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Employee ID':"fffe32003000360033003200", 'Date of Joining':2008-11-10, 'Gender':"Male", 'Company Type':"Service",'WFH Setup available':"Yes", 'Designation':2.0, 'Working Hours':4.0, 'Mental Fatigue Score': 5.6})

print(r.json())