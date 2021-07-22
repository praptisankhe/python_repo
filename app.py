from typing import DefaultDict
from pywebio.input import *
from pywebio.output import *
from pywebio.exceptions import SessionClosedException
from flask import Flask,send_from_directory
from pywebio.platform.flask import start_server, webio_view
from pywebio import STATIC_PATH

# import pickle
# import numpy as np
# model=pickle.load(open('credit.pkl','rb'))
# app=Flask(__name__)

def demo():

    inputs = input_group("Credit Risk Scorecard Assessment", [
        select("Residential Status",options=[('Choose',0),('Home Owner', 73), ('Tenant', 91), ('Other', 62)],name='res_status'),
        select("Employee Status",options=[('Choose',0),('Employed', 87), ('Unknown',59)], name='emp_status'), 
        select("Other Credit Card",options=[('Choose',0),('Yes', 76), ('No', 50)], name='occ'),
        select("Age", options=[
               ('Choose', 0),('Upto 36',53), ('37 to 39', 60), ('40 to 45', 68), ('46 to 57', 81), ('58 & Above', 99)], name='age'),
        select("Income", options=[
               ('Choose', 0),('Upto 28999', 31), ('29000 to 32999', 57), ('33000 to 41999', 70), ('42000 to 46999', 82), ('47000 & above', 96)], name='income'),
        select("Time With Bank", options=[
              ('Choose', 0),('Upto 11', 51), ('12 to 44', 62), ('45 to 70', 93), ('71 & above', 133)], name='tmwb'),
        select("Average Monthly Balance", options=[
             ('Choose', 0),('Upto 558.87', 90), ('558.88 to 1597.43', 62), ('1797.44 & above', 49)], name='AvgM')
        
    ])
    res=inputs['res_status']+inputs['emp_status']+inputs['occ']+inputs['age']+inputs['income']+inputs['tmwb']+inputs['AvgM']

    put_text("Your score :",res).style('font-size: 50px;margin-top: 60px;text-align:center;background-color: #ff6600')
    if(res <=410 ):
          put_text("Your score is perilous. Regretfully we will not be considering your application.").style('color:red;font-size:28px;text-align:center;left-padding:50%')
    elif(res>410 and res<=499):
          put_text("Your score is mediocre. Unfortunately we will not advance your request.").style('color:red;font-size:38px;text-align:center;left-padding:50%')
    elif(res>499 and res<=519):
          put_text("Your score is adequate. You qualify our criteria.").style('color:green;font-size:38px;text-align:center;left-padding:50%')
    else:
          put_text("Your score is outstanding. Pre approved loan awaits.").style('color:green;font-size:38px;text-align:center;left-padding:50%')


if __name__ == "__main__":
    try:
        demo()
    except SessionClosedException:
        print("The session was closed unexpectedly")


# if __name__=='__main__':
#       parser=argparser.ArgumentParser()
#       parser.add_argument("-p","--port",type=int,default=8080)
#       args=parser.parse_args()
#       start_server(demo,port=args.port)



# app.add_url_rule('/','webio_view',webio_view(demo),methods=['GET','POST','OPTIONS'])
# app.run(host="localhost",port=5000)

# radio("Residential Status", options=[
#               ('Home Owner', 73), ('Tenant', 91), ('Other', 62)], name='res_status'),
#         radio("Employee Status", options=[
#               ('Employed', 87), ('Unknown',59)], name='emp_status'),
#         radio("Other Credit Card", options=[
#               ('Yes', 76), ('No', 50)], name='occ'),