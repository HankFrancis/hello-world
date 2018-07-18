from urllib.request import urlopen,Request
import json


def dust_all_cities(cities,dust_info):

    if cities[0]=="전국":
        print("-----------전국 미세먼지 정보-------------")
        for i,j in dust_info.items():
            if j >=0 and j <=15:
                print (i,"미세먼지 : 좋음\n")
            elif j>=16 and j<=35:
                print (i,"미세먼지 : 보통\n")
            elif j>=37 and j<=75:
                print (i,"미세먼지 : 나쁨\n")
            else:
                print (i,"미세먼지 : 최악\n")

    else:
        for i in cities:

            j = dust_info[i]
            print("-----------"+i+" 미세먼지 정보-------------")
            if j >=0 and j <=15:
                print (i,"미세먼지 : 좋음\n")
            elif j>=16 and j<=35:
                print (i,"미세먼지 : 보통\n")
            elif j>=37 and j<=75:
                print (i,"미세먼지 : 나쁨\n")
            else:
                print (i,"미세먼지 : 최악\n")

    


city = {"seoul":'서울'
,"gwangju":'광주'
,"gyeonggi":'경기'
,"gangwon":'강원'
,"jeju":'제주'
,"busan":'부산'
,"incheon":'인천'
,"chungnam":'충남'
,"jeonnam":'전남'
,"chungbuk":'충북'
,"daegu":'대구'
,"gyeongnam":'경남'
,"daejeon":'대전'
,"gyeongbuk":'경북'
,"ulsan":'울산'
,"jeonbuk":'전북'
}



#환경공단 미세먼지 api
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/'
key = '%2FV4gL3%2FtnGiX2zU26VaqKWAzZ9smSjhZnjQvq3uXF01deRtLj%2FHfY4YXEGNqWKNfx5G57x3aNrWBbC%2BmqUn9nw%3D%3D'


#도시별 평균 실시간 미세먼지


#도시별 평균 미세먼지 api operation
cityAvg_operation = 'getCtprvnMesureLIst?'

#도시별 평균 미세먼지 api url
cityAvg_url = url+cityAvg_operation

#도시별 평균 미세먼지 api parameter

cityAvg_api={}

#한 페이지 결과 수
cityAvg_api['rows'] = 'numOfRows=1'
#페이지 번호
cityAvg_api['pages'] = 'pageNo=1'
#데이터 형식
cityAvg_api['return_type'] = '_returnType=json'
#미세먼지 측정 기준
cityAvg_api['item'] = 'itemCode=PM25'
#데이터 기간
cityAvg_api['time'] = 'dataGubun=HOUR'
#key
cityAvg_api['key'] = 'ServiceKey='+key

#request
request = Request(cityAvg_url+'&'.join(list(cityAvg_api.values())))


#api call
raw_dust = urlopen(request).read()

#json
parse_dust = json.loads(raw_dust)
print(parse_dust)


#make dust info of all cities
dust_all ={}

for i in parse_dust["list"][0]:
    if i in city.keys():
        dust_all[city[i]] = int(parse_dust["list"][0][i])
        


sen = input("도시를 알려주세요")
cities = sen.split()


dust_all_cities(cities,dust_all)





























