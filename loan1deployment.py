# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:07:24 2021

@author: Nishi
"""

import pickle
import streamlit as st
 
# loading the trained model

pickle_in = open('loan_prediction_rf.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction( Married,Education,Property_Area, Credit_History, LoanAmount, AppCoAppIncome):   
 
    # Pre-processing user input    
     
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
        
    if Education == "Not Graduate":
        Education = 0
    else:
        Education = 1 
        
    if Property_Area == "Urban":
        Property_Area = 0
    elif Property_Area == "Rural":
         Property_Area = 1
    else:
        Property_Area = 2      
     
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    LoanAmount = LoanAmount / 1000
    AppCoAppIncome = AppCoAppIncome/1000
 
    # Making predictions 
    prediction = classifier.predict( 
        [[ Married,Education,Property_Area, Credit_History, LoanAmount, AppCoAppIncome]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:blue;padding:10px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    Education = st.selectbox('Education',("Not Graduate","Graduate"))
    Property_Area =st.selectbox('Property_Area',("Urban","Rural","Semiurban"))
    AppCoAppIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction( Married,Education,Property_Area, Credit_History, LoanAmount, AppCoAppIncome) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()