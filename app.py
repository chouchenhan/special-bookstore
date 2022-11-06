import streamlit as st
import requests

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' 
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res
def getCountyOption(items):
    optionlist = []
    for item in items:
        cityname=item['cityName']
        if cityname not in optionlist:
            optionlist.append(cityname)
        
    return optionlist
def getDistrictOption(items, target):
	optionList = []
    for item in items:
        name = item['cityName']
        if name not in target:
            continue
        else:
    # 如果 name 裡面不包含我們選取的縣市名稱(target) 則略過該次迭代
    # hint: 使用 if-else 判斷式並且用 continue 跳過
        name.strip()
        district = name[5:]
        if len(district) == 0: continue
        if district not in optionList:
            optionlist.append(district)
    # 如果 district 不在 optionList 裡面，將 district 放入 optionList
    # hint: 使用 if-else 判斷式並使用 append 將內容放入 optionList
    return optionList
def app():
    bookstorelist=getAllBookstore()
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstorelist))
    county = st.selectbox('請選擇縣市', getCountyOption(bookstorelist))
    district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

if __name__ =='__main__':
    app()