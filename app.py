import streamlit as st
import pandas as pd
from pathlib import Path
import datetime

path = Path(__file__).parent / 'data.csv'

# Title of the app
st.title("山宝宝成长记录1.0")

df = pd.read_csv(path, encoding='utf-8')
st.dataframe(df)
@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8-sig')

csv = convert_df(df)
st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

items = {'记录时间': [datetime.datetime.now()], '项目时间': [None], '项目': [None], '哺乳方式': [None], '哺乳方位': [None], '哺乳时间': [None], '哺乳量': [None],
         '大小便': [None], '大小便性状': [None], '大小便颜色': [None], '大小便量': [None], '体重': [None], '身高': [None], '其他': [None]}

# Input fields
item_time = st.text_input("项目时间", value=datetime.datetime.now())
items['项目时间'] = [item_time]

option = st.selectbox("选择项目", ["选择", "哺乳", "换尿布", "体重", "身高", "其他"])
items['项目'] = [option]

if option == "哺乳":
    feed = st.selectbox("方式", ["选择", "直接母乳", "瓶喂母乳", "配方奶粉"])
    items['哺乳方式'] = [feed]

    if feed == "直接母乳":
        item = st.selectbox("方位", ["选择", "双侧", "左侧", "右侧"])
        items['哺乳方位'] = [item]

        time = st.text_input("时间(min)")
        items['哺乳时间'] = [time]

    elif feed == "瓶喂母乳":
        amount = st.text_input("哺乳量(ml)")
        items['哺乳量'] = [amount]

    elif feed == "配方奶粉":
        amount = st.text_input("哺乳量(ml)")
        items['哺乳量'] = [amount]

elif option == "换尿布":
    excretion = st.selectbox("选择", ["选择", "大便", "小便"])
    items['大小便'] = [excretion]

    status = st.text_input("性状", value="正常")
    items['大小便性状'] = [status]

    color = st.text_input("颜色", value="黄色")
    items['大小便颜色'] = [color]

    amount = st.selectbox("排便量", ["正常", "大量", "少量"])
    items['大小便量'] = [amount]

elif option == "体重":
    weight = st.text_input("体重(kg)")
    items['体重'] = [weight]

elif option == "身高":
    height = st.text_input("身高(cm)")
    items['身高'] = [height]

elif option == "其他":
    other = st.text_input("其他")
    items['其他'] = [other]

# st.markdown(items)

# Button to submit
if st.button("Submit"):
    # Create a DataFrame
    data = pd.DataFrame(items)

    # Append to CSV
    data.to_csv(path, mode='a', encoding='utf-8', header=False, index=False)
    st.success("Data successfully recorded!")

else:
    st.error("Please fill all fields correctly.")

