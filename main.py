import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.op.gg/champion/statistics")
con = req.content
html = BeautifulSoup(con,"html.parser")

champion_table = html.find("table",{"class":"champion-index-table tabItems"})

print("Data by op.gg")
lane_select = input("Select lane:")
if lane_select == "top" or lane_select == "TOP" or lane_select == "탑":
    tbody = champion_table.find("tbody",{"class":"tabItem champion-trend-tier-TOP"})
elif lane_select == "jng" or lane_select == "JNG" or lane_select == "정글":
    tbody = champion_table.find("tbody",{"class":"tabItem champion-trend-tier-JUNGLE"})
elif lane_select == "mid" or lane_select == "MID" or lane_select == "미드":
    tbody = champion_table.find("tbody", {"class": "tabItem champion-trend-tier-MID"})
elif lane_select == "adc" or lane_select == "ADC" or lane_select == "원딜":
    tbody = champion_table.find("tbody", {"class": "tabItem champion-trend-tier-ADC"})
elif lane_select == "sup" or lane_select == "SUP" or lane_select == "서폿":
    tbody = champion_table.find("tbody", {"class": "tabItem champion-trend-tier-SUPPORT"})

tr = tbody.find_all("tr")

champion_name_list = []
champion_position_list = []
champion_win_late_list = []
champion_tier_list = []

for i in tr:
    champion_info = i.find("td",{"class":"champion-index-table__cell champion-index-table__cell--champion"})

    name = champion_info.find("div",{"class":"champion-index-table__name"}).text.strip()
    position = champion_info.find("div",{"class":"champion-index-table__position"}).text.replace("\t","").replace("\n","")

    win_late = i.find("td",{"class":"champion-index-table__cell champion-index-table__cell--value"}).text.strip()

    champion_name_list.append(name)
    champion_position_list.append(position)
    champion_win_late_list.append(win_late)

for i in range(len(champion_name_list)):
    print("{}".format(i+1)+"\t"+champion_name_list[i]+"\t"+champion_position_list[i]+"\t"+champion_win_late_list[i])