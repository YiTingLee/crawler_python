import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class":"propertyRow"})

for item in all:
    print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    try:
        print(item.find("span",{"class":"infoBed"}).find("b").text)
    except:
        print(None)
    try:
        print(item.find("span",{"class":"infoSqFt"}).find("b").text)
    except:
        print(None)
    try:
        print(item.find("span",{"class":"infoValueFullBath"}).find("b").text)
    except:
        print(None)
    try:
        print(item.find("span",{"class":"infoValueHalfBath"}).find("b").text)
    except:
        print(None)

    for col_group in item.find_all("div",{"class":"columnGroup"}):
        # print(col_group)
        for feature_Group,feature_Name in zip(col_group.find_all("span",{"class":"featureGroup"}), col_group.find_all("span",{"class":"featureName"})):
            # print(feature_Group.text, feature_Name.text)
            if "Lot Size" in feature_Group.text:
                print(feature_Name.text)

    print(" ")
