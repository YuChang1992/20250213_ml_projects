# https://docs.streamlit.io/library/cheatsheet
# streamlit run app.py
import streamlit as st
import numpy as np
import joblib

# load model
clf2 = joblib.load('penguins.joblib')  # 載入先前訓練好的機器學習模型
scaler = joblib.load('scaler.joblib')  # 載入標準器，用來對輸入的特徵進行縮放處理

# 定義映射字典
y_dict = {0:'Adelie', 1:'Chinstrap', 2:'Gentoo'}  # 將模型的預測結果映射到企鵝品種
island_dict = {'Torgersen':0, 'Biscoe':1, 'Dream':2}  # 將島嶼名稱映射到數值（0、1、2），可以將文字型別的資料轉換為數字型別，便於模型處理
sex_dict = {'Female':0, 'Male':1}  # 將性別映射到數值

# 畫面設計
st.markdown('# 企鵝品種預測系統')  # 顯示主標題

col1, col2 = st.columns(2)
with col1:
    island = st.selectbox('島嶼', island_dict.keys())  # st.selectbox() 使用下拉選單讓用戶選擇島嶼
    bill_length = st.slider('嘴巴長度', 30, 60, 40)  # st.slider() 使用拉桿讓用戶選擇嘴巴長度，範圍為 30 到 60，預設值為 40
    bill_depth = st.slider('嘴巴寬度', 10, 25, 15)
with col2:
    flipper_length = st.slider('翅膀長度', 170, 230, 200)
    body_mass = st.slider('體重', 2500, 6500, 4000)
    sex = st.radio('性別', sex_dict.keys())  # st.radio() 使用單選框讓用戶選擇性別
    
if st.button('預測'):  # 創建一個按鈕，用戶點擊時會觸發
    # predict
    X=np.array([[island_dict[island], bill_length, bill_depth, flipper_length,
                 body_mass, sex_dict[sex]]])  # 將用戶輸入的特徵組合成數組（每個特徵都經過映射字典轉換）
    X=scaler.transform(X)  # 對輸入特徵進行標準化處理
    st.markdown(f'預測結果： **{y_dict[int(clf2.predict(X))]}**')  # 使用模型對標準化後的特徵進行預測，並回傳預測的類別（0、1、2），再將預測結果轉換為對應的企鵝品種名稱