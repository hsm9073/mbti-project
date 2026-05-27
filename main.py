import streamlit as st
import random

# =========================
# 페이지 기본 설정
# =========================
st.set_page_config(
    page_title="MBTI 포켓몬 추천기 🎮",
    page_icon="⚡",
    layout="centered"
)

# =========================
# 커스텀 CSS
# =========================
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom, #fff7f0, #ffeef8);
}

h1, h2, h3 {
    text-align: center;
}

.stButton>button {
    background-color: #ffcc00;
    color: black;
    border-radius: 15px;
    border: none;
    padding: 10px 25px;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #ffaa00;
    color: white;
}

.result-box {
    padding: 20px;
    border-radius: 20px;
    background-color: white;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =========================
# MBTI 데이터
# =========================
pokemon_data = {

    "INTJ": {
        "pokemon": "뮤츠 🧬",
        "type": "에스퍼 🔮",
        "desc": "전략적이고 독립적인 당신은 강력한 카리스마를 가진 뮤츠와 닮았어요!",
        "strength": "분석력 / 리더십 / 집중력",
        "color": "보라색 💜",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"
    },

    "INTP": {
        "pokemon": "후딘 🔮",
        "type": "에스퍼 🧠",
        "desc": "논리적이고 호기심 많은 당신은 천재 포켓몬 후딘 타입!",
        "strength": "창의력 / 분석력 / 아이디어",
        "color": "노란색 💛",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png"
    },

    "ENTJ": {
        "pokemon": "리자몽 🔥",
        "type": "불꽃 🔥",
        "desc": "카리스마 넘치는 리더! 모두를 이끄는 리자몽 스타일!",
        "strength": "추진력 / 리더십 / 자신감",
        "color": "주황색 🧡",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"
    },

    "ENTP": {
        "pokemon": "팬텀 👻",
        "type": "고스트 👻",
        "desc": "장난기 많고 창의적인 당신은 팬텀처럼 독특한 매력쟁이!",
        "strength": "아이디어 / 재치 / 유머",
        "color": "보라색 💜",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png"
    },

    "INFJ": {
        "pokemon": "루기아 🌊",
        "type": "에스퍼 🌊",
        "desc": "신비롭고 깊은 통찰력을 가진 당신은 전설의 루기아 타입!",
        "strength": "직관 / 공감 / 통찰력",
        "color": "하늘색 💙",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png"
    },

    "INFP": {
        "pokemon": "이브이 🌸",
        "type": "노말 🌈",
        "desc": "감성적이고 따뜻한 당신은 무한한 가능성의 이브이!",
        "strength": "감성 / 배려 / 상상력",
        "color": "핑크 🩷",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png"
    },

    "ENFJ": {
        "pokemon": "가디안 💖",
        "type": "페어리 ✨",
        "desc": "사람들을 챙기고 이끄는 당신은 가디안 같은 존재!",
        "strength": "배려 / 소통 / 리더십",
        "color": "초록색 💚",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/282.png"
    },

    "ENFP": {
        "pokemon": "피카츄 ⚡",
        "type": "전기 ⚡",
        "desc": "밝고 사랑스러운 인기쟁이! 피카츄와 찰떡!",
        "strength": "에너지 / 친화력 / 열정",
        "color": "노란색 💛",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    },

    "ISTJ": {
        "pokemon": "강철톤 ⛓️",
        "type": "강철 ⚙️",
        "desc": "묵묵하고 책임감 강한 당신은 강철톤처럼 든든해요!",
        "strength": "책임감 / 신뢰 / 성실함",
        "color": "회색 🩶",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/208.png"
    },

    "ISFJ": {
        "pokemon": "해피너스 🩷",
        "type": "노말 🌸",
        "desc": "배려심 넘치는 당신은 모두를 행복하게 만드는 해피너스!",
        "strength": "친절 / 공감 / 안정감",
        "color": "핑크 🩷",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png"
    },

    "ESTJ": {
        "pokemon": "보스로라 ⚙️",
        "type": "강철 ⛓️",
        "desc": "추진력과 책임감이 강한 당신은 보스로라 타입!",
        "strength": "통솔력 / 실행력 / 현실감각",
        "color": "은색 🤍",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/306.png"
    },

    "ESFJ": {
        "pokemon": "픽시 🌙",
        "type": "페어리 🌸",
        "desc": "친절하고 따뜻한 분위기의 당신은 픽시와 닮았어요!",
        "strength": "사교성 / 배려 / 친근함",
        "color": "연핑크 🌸",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png"
    },

    "ISTP": {
        "pokemon": "한카리아스 🦈",
        "type": "드래곤 🐉",
        "desc": "조용하지만 강력한 행동파! 한카리아스 스타일!",
        "strength": "도전정신 / 집중력 / 침착함",
        "color": "남색 💙",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/445.png"
    },

    "ISFP": {
        "pokemon": "라프라스 ❄️",
        "type": "물 💧",
        "desc": "온화하고 감성적인 자유로운 영혼! 라프라스 타입!",
        "strength": "감수성 / 자유로움 / 따뜻함",
        "color": "하늘색 💎",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png"
    },

    "ESTP": {
        "pokemon": "번치코 🥊",
        "type": "불꽃 🔥",
        "desc": "열정 넘치고 스릴을 즐기는 당신은 번치코 스타일!",
        "strength": "도전 / 자신감 / 에너지",
        "color": "빨간색 ❤️",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png"
    },

    "ESFP": {
        "pokemon": "푸린 🎤",
        "type": "노말 🎵",
        "desc": "사람들을 즐겁게 만드는 분위기 메이커! 푸린 타입!",
        "strength": "매력 / 밝음 / 친화력",
        "color": "핑크 🌸",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png"
    }
}

# =========================
# 제목
# =========================
st.title("🎮 MBTI 포켓몬 추천기")
st.markdown("## ✨ 당신과 가장 잘 어울리는 포켓몬은?!")
st.write("")

# =========================
# 설명
# =========================
st.info("""
💡 사용 방법

1️⃣ 자신의 MBTI를 선택하세요  
2️⃣ 버튼을 눌러 결과를 확인하세요  
3️⃣ 당신의 성격과 닮은 포켓몬을 만나보세요!
""")

# =========================
# MBTI 선택
# =========================
mbti = st.selectbox(
    "🎭 당신의 MBTI를 선택하세요!",
    list(pokemon_data.keys())
)

# =========================
# 버튼
# =========================
if st.button("⚡ 결과 확인하기!"):

    result = pokemon_data[mbti]

    st.balloons()

    st.write("")
    st.write("")

    st.markdown(
        "<div class='result-box'>",
        unsafe_allow_html=True
    )

    st.image(
        result["img"],
        width=250
    )

    st.success(
        f"🎉 당신과 가장 잘 어울리는 포켓몬은 {result['pokemon']} 입니다!"
    )

    st.markdown(f"""
### 📌 포켓몬 타입
{result['type']}

### 💬 성격 설명
{result['desc']}

### 🌟 당신의 강점
{result['strength']}

### 🎨 당신의 에너지 컬러
{result['color']}
""")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # 랜덤 명언
    quotes = [

        "포켓몬 마스터의 길은 오늘도 계속된다 🚀",
        "당신의 매력은 이미 전설급 ✨",
        "피카츄도 반할 성격이에요 ⚡",
        "오늘도 귀엽게 힘내봐요 🌈",
        "당신만의 특별한 능력을 믿어보세요 💖",
        "오늘의 행운 포켓몬이 당신과 함께합니다 🍀",
        "당신의 MBTI 에너지가 폭발 중 🔥",
        "행복은 포켓몬처럼 가까이에 있어요 🎈",
        "당신은 이미 최고의 트레이너 😎",
        "오늘도 반짝반짝 빛나는 하루 ✨"

    ]

    st.write("")
    st.markdown("## 🌟 오늘의 한마디")
    st.info(random.choice(quotes))

    # 궁합 추천
    st.write("")
    st.markdown("## 💞 잘 맞는 MBTI")

    compatibility = {
        "INTJ": "ENFP 💛",
        "INTP": "ENTJ 🔥",
        "ENTJ": "INFP 🌸",
        "ENTP": "INFJ 🌊",
        "INFJ": "ENTP 👻",
        "INFP": "ENFJ 💖",
        "ENFJ": "ISFP ❄️",
        "ENFP": "INTJ 🧬",
        "ISTJ": "ESFP 🎤",
        "ISFJ": "ESTP 🥊",
        "ESTJ": "ISFP 🌈",
        "ESFJ": "ISTP 🦈",
        "ISTP": "ESFJ 🌙",
        "ISFP": "ESTJ ⚙️",
        "ESTP": "ISFJ 🩷",
        "ESFP": "ISTJ ⛓️"
    }

    st.success(
        f"💘 당신과 잘 맞는 MBTI는 {compatibility[mbti]} 입니다!"
    )

    # 퍼센트 바
    st.write("")
    st.markdown("## 📊 포켓몬 싱크로율")

    sync = random.randint(80, 100)

    st.progress(sync)

    st.write(f"✨ 싱크로율: {sync}%")

    # 랜덤 능력치
    st.write("")
    st.markdown("## ⚔️ 당신의 능력치")

    power = random.randint(70, 100)
    speed = random.randint(70, 100)
    intelligence = random.randint(70, 100)
    charm = random.randint(70, 100)

    st.write(f"💪 힘: {power}")
    st.write(f"⚡ 스피드: {speed}")
    st.write(f"🧠 지능: {intelligence}")
    st.write(f"💖 매력: {charm}")

    # 타입 궁합
    st.write("")
    st.markdown("## 🌈 추천 포켓몬 타입")

    type_quotes = [
        "🔥 불꽃 타입 — 열정 넘치는 스타일!",
        "💧 물 타입 — 부드럽고 차분한 스타일!",
        "⚡ 전기 타입 — 활발하고 에너지 넘치는 스타일!",
        "🌿 풀 타입 — 따뜻하고 힐링되는 스타일!",
        "❄️ 얼음 타입 — 조용하지만 깊은 매력!",
        "👻 고스트 타입 — 신비로운 분위기!"
    ]

    st.warning(random.choice(type_quotes))

    # 재미 요소
    st.write("")
    st.markdown("## 🎲 오늘의 랜덤 운세")

    fortunes = [

        "🍀 오늘은 아주 운이 좋은 날!",
        "🎁 깜짝 행복이 찾아올지도?!",
        "⚡ 예상치 못한 좋은 일이 생겨요!",
        "🌈 웃을 일이 가득한 하루!",
        "💖 새로운 인연이 찾아올 가능성 UP!",
        "🔥 도전하면 성공 확률 상승!",
        "🎵 기분 좋은 하루가 될 예정!",
        "🌟 당신의 매력이 빛나는 하루!"

    ]

    st.success(random.choice(fortunes))

# =========================
# 하단 꾸미기
# =========================
st.write("")
st.write("---")

st.markdown("""
<div style='text-align:center;'>

🎮 Made with ❤️ using Streamlit  
✨ MBTI + Pokémon = 최고의 조합 ✨

</div>
""", unsafe_allow_html=True)
