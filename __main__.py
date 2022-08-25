from crawler.NaverCrawler import getURLs
from utils.FileControler import listToTXT

keyword = "이불 관리+이불 건조+이불 먼지"
start_date = "20190825"
end_date = "20220825"
where = "blog"

result = getURLs(keyword, where, start_date, end_date)

# print(f"{'='*20} {where} URL {'='*20}")
# for url in result:
#     print(url)
# print(f"{'='*50}\n")

print(f"총 {len(result)}개 크롤링 완료")

listToTXT(result, f"{keyword}_{start_date}_{end_date}_{where}.txt")