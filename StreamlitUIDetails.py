import streamlit as st
import pandas as pd

def PublishHeading():
    st.markdown("<h1 style='text-align: center; color: purple;'>Energy Demand Forecasting</h1>", unsafe_allow_html=True)

def PublishSideBars(mlModel):
    data = st.sidebar.selectbox("Please Explore...", ['About Us',"Energy Consumption",'Developed By'])
    ImplementBasedOnSideBars(data, mlModel)

def ImplementBasedOnSideBars(option, mlModel):
    if option == 'Developed By':
        PostDevelopedByInUI()
    elif option == 'About Us':
        PostAboutUs()
    elif option == "Energy Consumption":
        PostForecast(mlModel)
    else:
        pass

def PostAboutUs():
    st.write('''
    ##### 
    ##### This application has been developed with a purpose to demonstrate the usage of Auto Time Series forecasting to predict stock prices direction based on the market sentiments on news headlines at the same time.
    ##### We have developed this as a part of a college project.
    ##### Here, we have chosen a specific stock for our project : SBIN ( State Bank of India – This is an Indian multinational public sector bank & financial services statutory body headquartered in Mumbai ,Maharashtra)
    ##### 
    #### -------------------------------------Caution-----------------------------------------
    ##### 
    ##### This project has only been used for demonstrative purpose.
    ##### We don’t encourage anyone to make decisions based on the forecasted data.
    ''')
def PostDevelopedByInUI():
    st.write('''
    ## _Developed By_ -
    ### _AMPBA Batch-17 - Group 15_
    ##### 1. 12120011 - Harsimar Singh Arora
    ##### 2. 12120032 - Tipu Thakur
    ##### 3. 12120040 - Rohit Thakur
    ##### 4. 12120050 - Anuj Verma
    ##### 5. 12120084 - Swati Yadav
    ''')

def PostForecast(mlModel):
    InputData = mlModel['InputNaturalGas']
    InputData = InputData[['ConsumptionData']]
    InputData.index = mlModel['InputNaturalGas'].TimePeriod
    InputData.columns = ['PreviousConsumption']
    OutputData = mlModel['OutputNaturalGas']
    OutputData.index.Name = 'TimePeriod'
    OutputData.columns = ['ForecastedConsumption']
    st.line_chart(pd.concat([InputData,OutputData], axis=1))
    st.write(InputData)
    st.write(OutputData)


