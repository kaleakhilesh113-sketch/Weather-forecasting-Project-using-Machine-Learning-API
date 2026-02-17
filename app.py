# import streamlit as st
# import joblib
# import numpy as np
# from datetime import datetime
# from weather_api import get_coordinates, get_live_weather

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Premium Weather App",
#     layout="wide"
# )

# model = joblib.load("weather_model.pkl")

# # ---------------- CSS ----------------
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #eef2f7, #dfe7ef);
# }

# .section {
#     background: white;
#     border-radius: 18px;
#     padding: 20px;
#     margin-bottom: 20px;
#     box-shadow: 0 10px 25px rgba(0,0,0,0.08);
# }

# .card {
#     background: linear-gradient(135deg, #2b5876, #4e4376);
#     border-radius: 20px;
#     padding: 20px;
#     color: white;
#     box-shadow: 0 15px 35px rgba(0,0,0,0.25);
# }

# .title {
#     font-size: 26px;
#     font-weight: 600;
# }

# .big {
#     font-size: 54px;
#     font-weight: 700;
# }

# .small {
#     opacity: 0.85;
#     font-size: 14px;
# }

# .center {
#     text-align: center;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- HEADER ----------------
# st.markdown("## 🌦 AI Weather Forecast")
# st.caption("Live weather • AI prediction • Google-style experience")

# place = st.text_input(
#     "📍 Enter city, village, or region",
#     placeholder="Example: Kashmir, Pune, Mumbai"
# )

# # ---------------- MAIN ----------------
# if st.button("Get Weather"):
#     try:
#         loc = get_coordinates(place)
#         current, forecast = get_live_weather(loc["lat"], loc["lon"])

#         temp = current["temp"]
#         wind = current["wind"]
#         humidity = current["humidity"]
#         pressure = current["pressure"]
#         rain = current["rain"]

#         # ML prediction
#         sample = np.array([[temp-3, temp+3, rain, wind, pressure, temp]])
#         tomorrow_temp = model.predict(sample)[0]

#         # ======================================================
#         # 1️⃣ CLEAN METRIC SECTION (LIKE YOUR SCREENSHOT)
#         # ======================================================
#         st.markdown(
#             f"### 🌍 Current Weather in {loc['city']}, {loc['state']}"
#         )

#         m1, m2, m3 = st.columns(3)
#         m1.metric("🌡 Temperature", f"{temp} °C")
#         m2.metric("🤗 Feels Like", f"{temp - 0.7:.1f} °C")
#         m3.metric("💧 Humidity", f"{humidity} %")

#         m4, m5, m6 = st.columns(3)
#         m4.metric("🌬 Wind Speed", f"{wind} km/h")
#         m5.metric("🌍 Pressure", f"{pressure} hPa")
#         m6.metric("🌧 Rainfall", f"{rain} mm")

#         st.metric(
#             "🤖 AI Predicted Temperature (Tomorrow)",
#             f"{tomorrow_temp:.2f} °C"
#         )

#         st.divider()

#         # ======================================================
#         # 2️⃣ PREMIUM DASHBOARD (PHOTO-2 STYLE)
#         # ======================================================
#         st.markdown("### 📊 Weather Overview")

#         col1, col2, col3 = st.columns([2,1,1])

#         with col1:
#             st.markdown(f"""
#             <div class="card">
#                 <div class="title">{loc['city']}, {loc['state']}</div>
#                 <div class="small">{datetime.now().strftime("%A")}</div>
#                 <div class="big">{temp}°C</div>
#                 <div class="small">Partly cloudy</div>
#             </div>
#             """, unsafe_allow_html=True)

#         with col2:
#             st.markdown(f"""
#             <div class="card center">
#                 <div class="title">TODAY</div>
#                 <div class="big">{temp}°C</div>
#                 <div class="small">Humidity {humidity}%</div>
#             </div>
#             """, unsafe_allow_html=True)

#         with col3:
#             st.markdown(f"""
#             <div class="card center">
#                 <div class="title">TOMORROW</div>
#                 <div class="big">{tomorrow_temp:.1f}°C</div>
#                 <div class="small">AI Prediction</div>
#             </div>
#             """, unsafe_allow_html=True)

#         st.markdown("")

#         d1, d2, d3 = st.columns(3)

#         with d1:
#             st.markdown(f"""
#             <div class="card center">
#                 <div class="title">MORNING</div>
#                 <div class="big">{temp-2}°C</div>
#                 <div class="small">Cool</div>
#             </div>
#             """, unsafe_allow_html=True)

#         with d2:
#             st.markdown(f"""
#             <div class="card center">
#                 <div class="title">AFTERNOON</div>
#                 <div class="big">{temp+1}°C</div>
#                 <div class="small">Warm</div>
#             </div>
#             """, unsafe_allow_html=True)

#         with d3:
#             st.markdown(f"""
#             <div class="card center">
#                 <div class="title">EVENING</div>
#                 <div class="big">{temp-1}°C</div>
#                 <div class="small">Pleasant</div>
#             </div>
#             """, unsafe_allow_html=True)

#         # ======================================================
#         # 3️⃣ 7-DAY FORECAST
#         # ======================================================
#         st.divider()
#         st.markdown("### 📅 7-Day Outlook")

#         days = st.columns(7)
#         for i, day in enumerate(forecast):
#             with days[i]:
#                 st.markdown(f"""
#                 <div class="section center">
#                     <div>{day['date'][-5:]}</div>
#                     <div style="font-size:32px;">🌤</div>
#                     <div><b>{day['max']}°</b></div>
#                     <div class="small">{day['min']}°</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#     except Exception:
#         st.error("❌ Unable to fetch weather. Try another nearby city.")


import streamlit as st
import joblib
import numpy as np
from datetime import datetime
from weather_api import get_coordinates, get_live_weather

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Weather", layout="wide")

model = joblib.load("weather_model.pkl")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef2f7, #dfe7ef);
    font-family: Segoe UI, sans-serif;
}

.hero {
    background: linear-gradient(135deg, #2b5876, #4e4376);
    padding: 70px 40px;
    border-radius: 32px;
    color: white;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0 30px 70px rgba(0,0,0,0.3);
}

.card {
    background: linear-gradient(135deg, #2b5876, #4e4376);
    border-radius: 22px;
    padding: 22px;
    color: white;
    box-shadow: 0 18px 40px rgba(0,0,0,0.25);
}

.card-light {
    background: white;
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.1);
}

.big {
    font-size: 56px;
    font-weight: 700;
}

.mid {
    font-size: 22px;
    font-weight: 600;
}

.small {
    font-size: 14px;
    opacity: 0.85;
}

.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1 style="font-size:44px;">🌦 Weather Forecast Using ML And API</h1>
    <p style="font-size:20px; opacity:0.9;">
        Smart forecasts powered by <b>AI</b> & real-time data
    </p>
    <p style="margin-top:20px; opacity:0.8;">
        Clean design. Accurate results. Google-style experience.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- SEARCH ----------------
place = st.text_input(
    "📍 Enter city or region",
    placeholder="Example: Kashmir, Pune, Mumbai"
)

# ---------------- MAIN ----------------
if st.button("Get Weather"):
    try:
        loc = get_coordinates(place)
        current, forecast = get_live_weather(loc["lat"], loc["lon"])

        temp = current["temp"]
        wind = current["wind"]
        humidity = current["humidity"]
        pressure = current["pressure"]
        rain = current["rain"]

        # ML prediction
        sample = np.array([[temp-3, temp+3, rain, wind, pressure, temp]])
        tomorrow = model.predict(sample)[0]

        # ================= CURRENT WEATHER =================
        st.markdown(f"""
        <div class="card">
            <div class="mid">{loc['city']}, {loc['state']}</div>
            <div class="small">{datetime.now().strftime("%A")}</div>
            <div class="big">{temp}°C</div>
            <div class="small">Feels like {temp-0.7:.1f}°C</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")

        # ================= DETAILS =================
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"<div class='card center'><div class='mid'>💧 Humidity</div><div class='big'>{humidity}%</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='card center'><div class='mid'>🌬 Wind</div><div class='big'>{wind} km/h</div></div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='card center'><div class='mid'>🌍 Pressure</div><div class='big'>{pressure} hPa</div></div>", unsafe_allow_html=True)

        st.markdown("")

        # ================= AI =================
        st.markdown(f"""
        <div class="card center">
            <div class="mid">🤖 AI Predicted Temperature (Tomorrow)</div>
            <div class="big">{tomorrow:.2f}°C</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")

        # ================= DAY PARTS (ADDED) =================
        st.markdown("### ⏰ Day-wise Breakdown")

        d1, d2, d3 = st.columns(3)

        with d1:
            st.markdown(f"""
            <div class="card center">
                <div class="mid">🌅 Morning</div>
                <div class="big">{temp-2}°C</div>
                <div class="small">Cool & fresh</div>
            </div>
            """, unsafe_allow_html=True)

        with d2:
            st.markdown(f"""
            <div class="card center">
                <div class="mid">🌞 Afternoon</div>
                <div class="big">{temp+1}°C</div>
                <div class="small">Warm</div>
            </div>
            """, unsafe_allow_html=True)

        with d3:
            st.markdown(f"""
            <div class="card center">
                <div class="mid">🌇 Evening</div>
                <div class="big">{temp-1}°C</div>
                <div class="small">Pleasant</div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        # ================= 7-DAY FORECAST =================
        st.markdown("### 📅 7-Day Outlook")

        days = st.columns(7)
        for i, day in enumerate(forecast):
            with days[i]:
                st.markdown(f"""
                <div class="card-light center">
                    <div class="mid">{day['date'][-5:]}</div>
                    <div style="font-size:32px;">🌤</div>
                    <div class="mid">{day['max']}°</div>
                    <div class="small">{day['min']}°</div>
                </div>
                """, unsafe_allow_html=True)

    except Exception:
        st.error("❌ Unable to fetch weather. Try another nearby city.")
