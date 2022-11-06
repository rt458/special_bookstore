import requests
import streamlit as st
def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    response=response.json()
    # 將 response 轉換成 json 格式
    return response

def getCountyOption(items):
    optionList = []
    # 創建一個空的 List 並命名為 optionList
    for item in items:
        name=item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList

    # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
    # hint: 想辦法處理 item['cityName'] 的內容

    # 如果 name 不在 optionList 之中，便把它放入 optionList
    # hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
def getDistrictOption(items, target):
    optionList = []
    #print(target)
    for item in items:
        name = item['cityName']
        if target not in name: continue

        # 如果 name 裡面不包含我們選取的縣市名稱(target) 則略過該次迭代
        # hint: 使用 if-else 判斷式並且用 continue 跳過
        name.strip()
        district = name[5:]
        if len(district) == 0: continue
        if district not in optionList:
            optionList.append(district)

        # 如果 district 不在 optionList 裡面，將 district 放入 optionList
        # hint: 使用 if-else 判斷式並使用 append 將內容放入 optionList
    return optionList
def getSpecificBookstore(items, county, districts):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county not in name: continue
        for district in districts:
            if district not in name: continue
            specificBookstoreList.append(item)
    
    # 如果 name 不是我們選取的 county 則跳過
    # hint: 用 if-else 判斷並用 continue 跳過

    # districts 是一個 list 結構，判斷 list 每個值是否出現在 name 之中
    # 判斷該項目是否已經出現在 specificBookstoreList 之中，沒有則放入
    # hint: 用 for-loop 進行迭代，用 if-else 判斷，用 append 放入
    return specificBookstoreList
def app():
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)

    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))

    county = st.selectbox('請選擇縣市', countyOption) 
    DsitrictOption=getDistrictOption()
    # 呼叫 getDistrictOption 並將回傳值賦值給變數 districtOption
    district = st.multiselect('請選擇區域', DsitrictOption) 
    # 將['a', 'b', 'c', 'd']替換成縣市選項
def app():
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption) 
    districtOption = getDistrictOption(bookstoreList, county)
    district = st.multiselect('請選擇區域', districtOption) 
    # 呼叫 getSpecificBookstore 並將回傳值賦值給變數 specificBookstore
    num = len(specificBookstore)


def app():
    bookstorelist=getAllBookstore()
    bookcity=getCountyOption(bookstorelist)


    # 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
    st.header('特色書店地圖')
    st.metric('Total bookstore',len(bookstorelist) ) # 將 118 替換成書店的數量
    county = st.selectbox('請選擇縣市',bookcity)
    boo = getDistrictOption(bookstorelist, county)
    district = st.multiselect('請選擇區域', boo)

if __name__ == '__main__':
    app()
    