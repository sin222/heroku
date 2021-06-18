import requests
from bs4 import BeautifulSoup

def main():
    ha = args.get("ha","로션")
    # name = "메이크업"
    lanking_name = list()
    top1 = ""
    top2 = ""
    top3 = ""

    if name == '선크림':
        url = "https://www.oliveyoung.co.kr/store/main/getBestList.do?dispCatNo=900000100100001&fltDispCatNo=10000010011&pageIdx=1&rowsPerPage=8"
    elif name == '스킨케어':
        url = "https://www.oliveyoung.co.kr/store/main/getBestList.do?dispCatNo=900000100100001&fltDispCatNo=10000010001&pageIdx=1&rowsPerPage=8"
    elif name == '메이크업':
        url = "https://www.oliveyoung.co.kr/store/main/getBestList.do?dispCatNo=900000100100001&fltDispCatNo=10000010002&pageIdx=1&rowsPerPage=8" 
    # print(cosmetics_name)
    res = requests.get(url)
    res.raise_for_status() # 문제 있으면 프로그램 종료되도록
    soup = BeautifulSoup(res.text, "lxml")

    cosmetics_name = soup.find_all("p", attrs={"class":"tx_name"})
    
    for i, cosmetic in enumerate(cosmetics_name):
        if i<3:
            tmp = cosmetic.get_text()
            lanking_name.append(tmp)
            # print(cosmetic.get_text())
        else:
            continue
    # return {"text":cosmetics_name}
    top1 = lanking_name[0]
    top2 = lanking_name[1]
    top3 = lanking_name[2]
    # print(top1, top2, top3)
    # print("1위 : "+top1+"\n2위 : "+top2+"\n3위 : "+top3)
    return {"text":"1위 : "+top1+"\n2위 : "+top2+"\n3위 : "+top3}
main()



# def main(args):
#     import requests
#     from bs4 import BeautifulSoup

#     url = "https://www.oliveyoung.co.kr/store/main/getBestList.do"
#     res = requests.get(url)
#     res.raise_for_status() # 문제 있으면 프로그램 종료되도록

#     soup = BeautifulSoup(res.text, "lxml")

#     cosmetics_name = soup.find("p", attrs={"class":"tx_name"}).get_text()
    
#     ha = args.get("ha")
    
#     if ha=='로션':
#         return {"text":cosmetics_name}


# import requests
# from bs4 import BeautifulSoup

# def main(args):
#     ha = args.get("ha","선크림")
#     # name = "메이크업"

#     if ha == '선크림':
#         url = "https://www.oliveyoung.co.kr/store/main/getBestList.do?dispCatNo=900000100100001&fltDispCatNo=10000010011&pageIdx=1&rowsPerPage=8"
#     elif ha == '스킨케어':
#         url = "https://www.oliveyoung.co.kr/store/main/getBestList.do?dispCatNo=900000100100001&fltDispCatNo=10000010001&pageIdx=1&rowsPerPage=8"
#     elif ha == '메이크업':
#         url = "https://www.oliveyoung.co.kr/store/main/getBestList.do?dispCatNo=900000100100001&fltDispCatNo=10000010002&pageIdx=1&rowsPerPage=8" 
#     # print(cosmetics_name)
#     res = requests.get(url)
#     res.raise_for_status() # 문제 있으면 프로그램 종료되도록
#     soup = BeautifulSoup(res.text, "lxml")

#     cosmetics_name = soup.find("p", attrs={"class":"tx_name"}).get_text()


#     return {"text":cosmetics_name}

    
    
    