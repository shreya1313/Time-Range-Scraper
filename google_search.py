from googleapiclient.discovery import build


class GoogleSearch():

    def __init__(self):
        self.my_api_key = 'AIzaSyCp_4LQAU4Ip-5dhHnXmE4Gp8LfvpgzSz8'
        self.my_cse_id = '008598541419257952679:-da4afc_nm8'

    def google_search(self, search_term, api_key, cse_id, **kwargs):
        service = build(
            "customsearch", "v1", developerKey=api_key, cache_discovery=False
        )
        fin_search = []
        i = 0
        while(1):
            if(i != 0):
                res = service.cse().list(
                    q=search_term, cx=cse_id, start=(i * 10), **kwargs
                ).execute()
            else:
                res = service.cse().list(
                    q=search_term, cx=cse_id, **kwargs
                ).execute()
            i = i + 1
            if 'items' not in res:
                break
            fin_search.append(res['items'])
        return fin_search

    def get_slide_url(self, search_results):
        slide_urls = []
        for result in search_results:
            slide_urls.append(result['link'])
        return(slide_urls)

    def search_slideshare(self, search_term, result_count):
        search_results = self.google_search(
            'site:slideshare.net intitle:' + search_term,
            self.my_api_key, self.my_cse_id, num=result_count
        )
        return(self.get_slide_url(search_results))

    def search_blogs(self, search_term, result_count):
        search_results = self.google_search(
            'intext:(' + search_term + ' AND blog) -inanchor:blog ' +
            '-site:slideshare.net -site:youtube.com', self.my_api_key,
            self.my_cse_id, num=result_count
        )

        return(self.get_slide_url(search_results))

    def filter_by_time(self, search_term, start_date, end_date, result_count):
        """
        searches for a specific term based on time
        """
        fin_res = []
        start_date = start_date.strftime('%Y%m%d')
        end_date = end_date.strftime('%Y%m%d')

        search_results = self.google_search(
            search_term, self.my_api_key, self.my_cse_id,
            sort='date:r:{}:{}'.format(start_date, end_date),
            num=result_count
        )
        for search_result in search_results:
            fin_res.append(self.get_slide_url(search_result))
        return fin_res
