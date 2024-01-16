import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'weatherApp/index.html')


def get_travel_spots(region):
    # 여행 명소 데이터를 딕셔너리로 정의 (이 데이터는 예시일 뿐, 실제 데이터를 사용해야 합니다.)
    travel_spots_data = {
        '서울': ['경복궁', '남산타워'],
        '부산': ['해운대 해수욕장', '범어사'],
        # ... 다른 지역에 대한 여행 명소 추가
    }

    return travel_spots_data.get(region, [])  # 선택된 지역에 대한 여행 명소 반환



def check_weather(request):
    if request.method == 'POST':
        selected_region = request.POST['region']

        # OpenWeatherMap API 키
        api_key = 'YOUR_OPENWEATHERMAP_API_KEY'

        # 선택한 지역에 대한 좌표 정보 (예시로 서울 좌표 사용)
        coordinates = {
            '서울': {'lat': 37.5665, 'lon': 126.9780},
            '부산': {'lat': 35.1796, 'lon': 129.0756},
            # 나머지 지역들의 좌표 추가
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
