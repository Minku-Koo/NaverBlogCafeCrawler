import requests
import json
from bs4 import BeautifulSoup as bs

def getURLs(
            keyword,
            start_date,
            end_date
        ):
        
    page = 1
    a_tags = []

    while True:
        URL = f"""https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start={page}&query={keyword}&nso=so:r,p:from{start_date}to{end_date},a:all&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_opt&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02465101&fgn_region=&fgn_city=&lgl_lat=37.3279495&lgl_long=127.0949293&abt=&_callback=viewMoreContents"""

        data = requests.get(URL)
        data_dic = json.loads(data.text[18:-4])

        soup = bs(data_dic["html"], "html.parser")

        results = soup.findAll("a", {'class': ['api_txt_lines']})

        if len(results) == 0:
            break

        a_tags.extend( results )
        page += 30

    cafes = set()
    blogs = set()

    for a in a_tags:
        h = a["href"]
        if h == "#":
            continue
        elif "cafe.naver.com" in h:
            cafes.add(h)
        else:
            blogs.add(h)


    cafe_urls = list(cafes)
    blog_urls = list(blogs)
    result = {
        "count": len(cafe_urls)+len(blog_urls),
        "cafe_urls": cafe_urls,
        "blog_urls": blog_urls
    }

    return result