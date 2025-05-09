import streamlit as st
import requests
from datetime import datetime, timedelta

# OpenWeatherMap API 키
API_KEY = '2dd7ff7ea5b32023f96b6490b89ed94b'  # 본인의 키로 대체하세요.

# 앱 제목
st.set_page_config(page_title="날씨 앱", page_icon="🌤️")
st.title("🌤️ 실시간 날씨 앱")
st.write("도시 이름을 입력하면 현재 날씨와 현지 시간을 확인할 수 있어요.")

# 도시 입력
city = st.text_input("도시 이름을 입력하세요", "Seoul")

# 검색 버튼
if st.button("날씨 검색"):
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                st.error(f"도시를 찾을 수 없습니다: {data.get('message')}")
            else:
                # 날씨 정보 추출
                city_name = data["name"]
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]

                # 현지 시간 계산
                timezone_offset = data["timezone"]
                utc_now = datetime.utcnow()
                local_time = utc_now + timedelta(seconds=timezone_offset)
                local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")

                # 결과 표시
                st.subheader(f"📍 {city_name}")
                st.write(f"🌡️ 온도: **{temperature}°C**")
                st.write(f"🌥️ 상태: **{description}**")
                st.write(f"⏰ 현지 시간: **{local_time_str}**")
        except Exception as e:
            st.error(f"날씨 데이터를 가져오는데 실패했습니다.\n{e}")
    else:
        st.warning("도시 이름을 입력해주세요.")
