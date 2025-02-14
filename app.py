# https://docs.streamlit.io/library/cheatsheet
# streamlit run app.py
import streamlit as st  # 建立 Web 應用的框架
import numpy as np  # 用於數學計算和數組操作
import joblib  # 載入儲存的機器學習模型
import base64  # 將圖片轉換為 Base64 編碼的格式，這樣可以將圖片內嵌於 HTML 頁面中顯示

def get_image_html(page_name, file_name):
    with open(file_name, "rb") as f:  # 以二進位的方式打開圖片
        contents = f.read()  # 讀取內容
    data_url = base64.b64encode(contents).decode("utf-8")  # 將圖片內容轉換成 Base64 編碼的字串
    return f'<a href="{page_name}"><img src="data:image/png;base64,{data_url}" style="width:300px"></a>'  # 回傳 HTML 字串，包含一個圖片標籤，圖片大小設為 300px

data_url = get_image_html("分類", "./iris.png")  # 呼叫 get_image_html 函數，將圖片轉為 Base64 編碼，並且生成 HTML 代碼
data_url_2 = get_image_html("迴歸", "./taxi.png")

st.set_page_config(  # 設定 Streamlit 網頁
    page_title="我的學習歷程",  # 網頁標題
    page_icon="👋",  # 網頁圖示emoji
)

st.title('Machine Learning 學習歷程')  # 頁面主標題

col1, col2 = st.columns(2)  # 創建兩個欄位
with col1:
    # url must be external url instead of local file
    # st.markdown(f"### [![分類]({url})](分類)")
    st.markdown('### [企鵝品種辨識－分類](分類)')  # 超連結「分類」指向「分類」頁面，顯示有關企鵝品種辨識模型的特徵和類別說明
    st.markdown('''
    ##### 特徵(X):
        - 島嶼
        - 嘴巴長度
        - 嘴巴寬度
        - 翅膀長度
        - 體重
        - 性別
    ##### 預測類別(Class):
        - Adelie
        - Chinstrap
        - Gentoo
        ''')
    # st.image('iris.png')
    st.markdown(data_url, unsafe_allow_html=True)  # 顯示嵌入的圖片
with col2:
    st.markdown('### [計程車小費預測－迴歸](迴歸)')  # 超連結「迴歸」指向「迴歸」頁面，顯示有關企鵝品種辨識模型的特徵和類別說明
    st.markdown('''
    ##### 特徵(X):
        - 車費
        - 性別
        - 吸菸
        - 星期
        - 時間
        - 同行人數
    ##### 目標：預測小費金額
        ''')
    # st.image('taxi.png')
    st.markdown(data_url_2, unsafe_allow_html=True)
