from crawler.NaverCrawler import getURLs
from utils.FileControler import listToTXT

keywords = [
    "이불 관리",
    "이불 건조",
    "이불 먼지"
]
for keyword in keywords:
    start_date = "20190825"
    end_date = "20220825"

    where = "blog"

    result = getURLs(keyword, where, start_date, end_date)
    listToTXT(result, f"{keyword}_{start_date}_{end_date}_{where}.txt")
    print(f"{keyword} {where} 총 {len(result)}개 크롤링 완료")


    where = "cafe"

    result = getURLs(keyword, where, start_date, end_date)
    listToTXT(result, f"{keyword}_{start_date}_{end_date}_{where}.txt")
    print(f"{keyword} {where} 총 {len(result)}개 크롤링 완료\n")

zz