from flask import Flask, render_template, request import numpy as np 
import pickle 

app=Flask(_name_) # our flask app
@app.route('/') # rendering the html template 
def home(): 
 return render_template('home.html')
@app.route('/predict')#rendering the html template 
def index() : return render_template("index. html") 
@app.route('/data_predict', methods=['POST']) # route for our prediction
def predict(): 
age = request. form[ 'age'] #requesting for age data gender = request.form['gender'] # requesting for gender data request. tb= request.form [' tb'] # requesting for Totat_Bilirubin data 
db = request. form ['db'] # requesting for Direct_ Bil irubin data 
ap = request.form  ['ap'] # requesttng for Alkaline_Phosphotase data aa1 = request. form['aa1'] #requesting for Alamine_Aminotransferase data
 aa2 = request. form['aa2'] requesting for Aspartate.Aminotransferase data 
tp = request. form['tp']# requesting for Total_Protiens data 
tp = request.form['tp'] a=request.forn['a'] #requesting for Albunin data 
agr = request . form[ 'agr'] # requesting for Albumin_and_Globulin_ ratio data
 # coverting data into float format 
data = [[Float (age), float (gender), float (tb), float(db) , Float (ap), float(aa1), float(aa2), float(tp),    
# loading model which we saved model pickle. load (open(" liver_analysis.pkl', rb'))
 prediction= model. predict (data) [0]
 if (prediction == 1): 
         return render template ('noChance.html', prediction='You have a liver desease problem, You must and')
 else: 
return render template(chance.html', prediction="You dont have a liver desease problem) 


if _ name== '_ main__':
app.run()