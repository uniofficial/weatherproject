import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'weatherApp/index.html')


def get_travel_spots(region):
    # 여행 명소 데이터를 딕셔너리로 정의
    travel_spots_data = {
        '서울': ['경복궁', '남산타워'],
        '부산': ['해운대', '범어사'],
        '대구': ['이월드', '워터파크'],
        '인천': ['월미도', '차이나타운'],
        '광주': ['국립광주과학관', '국립광주박물관'],
        '대전': ['성심당', '한밭수목원'],
        '울산': ['명선도', '간절곶'],
        '경기도': ['에버랜드', '한국민속촌'],
        '강원도': ['대관령', '남이섬'],
        '충청북도': ['활옥동굴', '의림지'],
        '충청남도': ['국립생태원', '독립기념관'],
        '전라북도': ['전주한옥마을', '선유도'],
        '전라남도': ['오동도', '대흥사'],
        '경상북도': ['첨성대', '부석사'],
        '경상남도': ['지리산', '가야랜드'],
        '제주도': ['성산일출봉', '천지연폭포']
    }

    return travel_spots_data.get(region, [])  # 선택된 지역에 대한 여행 명소 반환



def check_weather(request):
    if request.method == 'POST':
        selected_region = request.POST['region']

        # OpenWeatherMap API 키
        api_key = '5bb284445cc3465dd776e8744699c132'

        # 선택한 지역에 대한 좌표 정보 (예시로 서울 좌표 사용)
        coordinates = {
            '서울': {'lat': 37.5665, 'lon': 126.9780},
            '부산': {'lat': 35.1796, 'lon': 129.0756},
            '대구': {'lat': 35.8714354, 'lon': 128.601445},
            '인천': {'lat': 37.4562557, 'lon': 126.7052062},
            '광주': {'lat': 35.1595454, 'lon': 126.8526012},
            '대전': {'lat': 36.3504119, 'lon': 127.3845475},
            '울산': {'lat': 35.5383773, 'lon': 129.3113596},
            '경기도': {'lat': 37.5670, 'lon': 127.1907},
            '강원도': {'lat': 37.8859, 'lon': 127.7293},
            '충청북도': {'lat': 36.6357, 'lon': 127.4912},
            '충청남도': {'lat': 36.5184, 'lon': 126.8000},
            '전라북도': {'lat': 35.7175, 'lon': 127.1446},
            '전라남도': {'lat': 34.8679, 'lon': 126.9910},
            '경상북도': {'lat': 36.4919, 'lon': 128.8889},
            '경상남도': {'lat': 35.2383, 'lon': 128.6922},
            '제주도': {'lat': 33.4889, 'lon': 126.4983}
        }

        # 선택한 지역의 좌표
        coords = coordinates.get(selected_region, {})

        if coords:
            # OpenWeatherMap API에서 기상 정보 가져오기
            weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
            response = requests.get(weather_api_url)
            weather_data = response.json()

            temperature = weather_data.get('main', {}).get('temp')
            humidity = weather_data.get('main', {}).get('humidity')

            suitable_for_travel = True

            if temperature is None or humidity is None or temperature <= -15 or temperature > 35 or humidity > 70:
                suitable_for_travel = False

            if suitable_for_travel:
                travel_spots = get_travel_spots(selected_region)
                return render(request, 'weatherApp/result.html', {'suitable_for_travel': True, 'temperature': temperature, 'humidity': humidity, 'travel_spots': travel_spots})
            else:
                return render(request, 'weatherApp/result.html', {'suitable_for_travel': False, 'temperature': temperature, 'humidity': humidity})

    return HttpResponse("Invalid request")
