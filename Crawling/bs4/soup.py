from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request, urlretrieve
from urllib.parse import quote_plus
import logging


class gather():
    baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

    def loginit(self):
        '''
        로그를 관리
        :return:
        '''

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    def get_img(self, keyword=None, img_count=None):
        '''
        이미지 수집 코드
        :param keyword: 네이버에 수집할 이미지 검색어
        :param img_count: 수집할 이미지 갯수
        :return:
        '''

        logging.info('{} 페이지에서 이미지 수집을 시작합니다.'.format(self.baseUrl))

        plusUrl = keyword       # 이미지 검색어
        crawl_num = img_count   # 수집할 이미지 갯수

        while plusUrl is None:
            logging.info('검색어가 설정되지 않았습니다. 다시 한번 검색어를 입력해주세요.')
            plusUrl = input('검색할 이미지를 입력해주세요: ')

            if plusUrl is not None:
                break

        # 크롤링 할 이미지 갯수 지정을 하지 않을 시 크롤링 할 이미지 갯수 30개
        if crawl_num is None:
            crawl_num = 10

        logging.debug('수집할 이미지: {0}\n수집할 이미지 갯수: {1}'.format(plusUrl, crawl_num))


        # quote_plus()  한글 검색 자동 변환, header= 사용자 우회
        req = Request(self.baseUrl+quote_plus(plusUrl), headers={'User-Agent': 'Chrome/66.0.3359.181'})
        html = urlopen(req)  # 페이지 열기
        soup = bs(html, "html.parser")  # html 읽기
        imgs = soup.find_all('img')  # 모든 _img class 찾기

        cnt = 1     # 이미지 저장 개수 카운트

        for img in imgs:
            logging.info('{}번째 이미지'.format(cnt))

            imgsrc = img['src']     # 이미지 소스

            urlretrieve(imgsrc, 'images/{0}{1}.jpg'.format(plusUrl, str(cnt)))     # 이미지 저장

            if cnt < crawl_num:
                cnt += 1  # cnt 1 저장할때마다

            # 원하는 만큼 저장 후 종료
            elif cnt >= crawl_num:
                logging.info('{}개 이미지가 저장되었습니다.'.format(cnt))
                break





keyword = '바나나'
img_count = 5

cls = gather()
cls.loginit()
cls.get_img(keyword=keyword, img_count=img_count)

# gather(keyword=keyword, img_count=img_count)