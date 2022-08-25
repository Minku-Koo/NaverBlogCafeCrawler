from crawler.NaverCrawler import getURLs

keyword = "스타 빨무"
start_date = "20210101"
end_date = "20220825"

result = getURLs(keyword, start_date, end_date)

print(f"{'='*20} 카페 URL {'='*20}")
for cafe in result.get("cafe_urls"):
    print(cafe)
print(f"{'='*50}\n")

print(f"{'='*20} 블로그 URL {'='*20}")
for cafe in result.get("blog_urls"):
    print(cafe)
print(f"{'='*50}\n")
print()

print(f"총 {result.get('count')}개 크롤링 완료")