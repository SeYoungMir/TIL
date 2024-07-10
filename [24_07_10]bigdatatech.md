# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 2. 공개 데이터 사용
### 1. 공개 데이터란?
3. 공개 데이터 활용
   - korea_data_scrap.py
   - ```python
     """특정 지역의 미세먼지 정보를 크롤링"""
     import urllib
     import requests
     from bs4 import BeautifulSoup
     import json

     # URL 관련 정보 선언
     service_key = "자신의 서비스키 입력"
     end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnTnforInqquireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=" + service_key
     default_options = {
        "numOfRows": 1, 
        "pageNo": 1,
        "dataTerm":"Daily",
        "ver": 1.3
     }
     def get_dust_info(region):
        """특정 지역의 미세먼지 수치 추출"""
        
        # URL 생성
        default_options["stationName"]=region
        params =urllib.parse.urlencode(default_options)
        url = end_point+"&"+params

        # 요청
        r = requests.get(url)
        xml = r.text

        # 필요한 정보 스크레이핑
        soup = BeautifulSoup(xml,'html.parser')
        pm_10 = soup.select('item>pm10Value')[0].text
        pm_25 = soup.select('item > pm25Value')[0].text

        return {
            "region": region,
            "pm_10": pm_10,
            "pm_25": pm_25,

        }

     if __name__ == '__main__':
        output_A = get_dust_info("강서구")
        print(json.dumps(output_a, ensure_ascii=False))
        output_a =get_dust_info("강남구")
        print(json.dumps(output_a,ensure_ascii=False))

     ```
     - 지금까지 살펴본 코드들과 대부분 유사함.