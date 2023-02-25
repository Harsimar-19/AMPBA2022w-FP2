import streamlit as st
import pandas as pd

def PublishHeading():
    st.markdown("<h1 style='text-align: center; color: purple;'>Energy Demand Forecasting</h1>", unsafe_allow_html=True)

def PublishSideBars(mlModel):
    ReqList = ['About Us']
    ReqList.extend(list(mlModel['TrainData'].keys()))
    ReqList.append('Developed By')
    data = st.sidebar.selectbox("Please Explore...", ReqList)
    ImplementBasedOnSideBars(data, mlModel)

def ImplementBasedOnSideBars(option, mlModel):
    if option == 'Developed By':
        PostDevelopedByInUI()
    elif option == 'About Us':
        PostAboutUs()
    elif option == "Energy Consumption":
        PostForecast(mlModel)
    else:
        PostDataVariety(mlModel, option)
        pass

def PostAboutUs():
    st.write('''
    ##### 
    ##### Forecasting energy demand is a complicated task that necessitates a thorough understanding of the elements that impact energy use, such as population increase, economic activity, weather patterns, and technology advancements. To examine historical data and forecast future energy consumption, advanced statistical modelling and machine learning techniques are frequently applied.
    ##### We have developed this as a part of a college project.
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

def PostDataVariety(mlModel, source):
    InputData = mlModel['InputData'][source]
    TrainData = mlModel['TrainData'][source]
    TestData = mlModel['TestData'][source]
    ForecastedTestData = mlModel['ForecastedTestData'][source]
    ForecastedData = mlModel['FinalForecastedData'][source]
    IpVsFore, TeVsAte = st.tabs(["Input And Forecasted", "Test Vs Forecasted Test"])
    IpVsFore.subheader("Graph - ")
    InputData.columns = ['Actual Data']
    ForecastedData.columns = ['Forecasted Data']
    IpVsFore.line_chart(pd.concat([InputData,ForecastedData], axis=1))
    IpVsFore.subheader("Forecasted Data - ")
    IpVsFore.table(ForecastedData)
    IpVsFore.subheader("Input Data - ")
    IpVsFore.table(InputData)
    
    TeVsAte.subheader("Graph - ")
    TestData.columns = ['Test Data']
    ForecastedTestData.columns = ['Forecasted Test Data']
    TeVsAte.line_chart(pd.concat([TestData,ForecastedTestData], axis=1))
    TeVsAte.subheader("Forecasted Test Data - ")
    TeVsAte.table(ForecastedTestData)
    TeVsAte.subheader("Test Data - ")
    TeVsAte.table(TestData)
    
    