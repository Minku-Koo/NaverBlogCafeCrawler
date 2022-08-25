from crawler.NaverCrawler import getURLs

keyword = "스타 빨무"
start_date = "20220601"
end_date = "20220825"
where = "cafe"

result = getURLs(keyword, where, start_date, end_date)

print(f"{'='*20} {where} URL {'='*20}")
for url in result:
    print(url)
print(f"{'='*50}\n")

print(f"총 {len(result)}개 크롤링 완료")