import requests
import json
from bs4 import BeautifulSoup as bs

def getURLs(
            keyword,
            where,
            start_date,
            end_date
        ):

    page = 1
    a_tags = []

    while True:
        URL = {
            "view": f"""https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start={page}&query={keyword}&nso=so:r,p:from{start_date}to{end_date},a:all&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&sm=tab_opt&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02465101&fgn_region=&fgn_city=&abt=&_callback=viewMoreContents""",
            "blog": f"""https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query={keyword}&rev=44&start={page}&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=&dkey=0&source_query=&nx_search_query={keyword}&spq=3&_callback=viewMoreContents""",
            "cafe": f"""https://s.search.naver.com/p/cafe/search.naver?where=article&ie=utf8&query={keyword}&prdtype=0&t=0&st=rel&srchby=text&dup_remove=1&cafe_url=&without_cafe_url=&sm=tab_opt&nso_open=0&rev=44&abuse=0&ac=0&aq=0&converted=0&is_dst=0&nqx_context=&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&people_sql=0&spq=3&x_tab_article=&is_person=0&start={page}&display=10&prmore=1&_callback=viewMoreContents"""
        }
        # print(page)

        data = requests.get(URL[where])
        soup = bs(data.text.strip(), "html.parser")

        results = soup.findAll("a", {'class': ['\\\"api_txt_lines']})

        a_tags.extend( results )

        if len(results) <= 1:
            break

        page += 30

    urls = set()

    for a in a_tags:
        h = a["href"]
        if h == "#":
            continue
        urls.add(h)

    result = list(urls)

    return result