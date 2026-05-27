import streamlit as st
import random
import time

# =========================================
# 페이지 설정
# =========================================
st.set_page_config(
    page_title="✨ MBTI Pokémon Universe ✨",
    page_icon="⚡",
    layout="centered"
)

# =========================================
# 커스텀 CSS
# =========================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Pretendard', sans-serif;
}

.main {
    background: linear-gradient(to bottom, #fff5f7, #eef7ff);
}

.title {
    text-align: center;
    font-size: 55px;
    font-weight: 800;
    color: #ff4b6e;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: gray;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.1);
    margin-top: 20px;
}

.type-box {
    padding: 10px;
    border-radius: 15px;
    text-align: center;
    font-weight: bold;
    background: linear-gradient(to right, #ffe259, #ffa751);
    color: black;
}

.power-box {
    background: #f4f4f4;
    padding: 15px;
    border-radius: 15px;
    margin-top: 10px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
    font-size: 14px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #ff512f, #dd2476);
    color: white;
    border-radius: 15px;
    border: none;
    height: 55px;
    font-size: 20px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(to right, #dd2476, #ff512f);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# 포켓몬 데이터
# =========================================
pokemon_data = {

    "INTJ": {
        "pokemon": "뮤츠 🧬",
        "type": "에스퍼 🔮",
        "desc": "전략적이고 독립적인 완벽주의자!",
        "skill": "사이코 브레이크 💥",
        "color": "💜 보라색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"
    },

    "INTP": {
        "pokemon": "후딘 🔮",
        "type": "에스퍼 🧠",
        "desc": "논리적이고 분석적인 천재!",
        "skill": "염동력 ✨",
        "color": "💛 노란색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"
    },

    "ENTJ": {
        "pokemon": "리자몽 🔥",
        "type": "불꽃 🔥",
        "desc": "강력한 리더십과 카리스마!",
        "skill": "화염방사 🔥",
        "color": "🧡 주황색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"
    },

    "ENTP": {
        "pokemon": "팬텀 👻",
        "type": "고스트 👻",
        "desc": "창의적이고 장난기 가득!",
        "skill": "섀도볼 🌑",
        "color": "💜 보라색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"
    },

    "INFJ": {
        "pokemon": "루기아 🌊",
        "type": "전설 🌊",
        "desc": "깊은 통찰력과 신비로운 분위기!",
        "skill": "에어로블라스트 🌪️",
        "color": "💙 하늘색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/249.png"
    },

    "INFP": {
        "pokemon": "이브이 🌸",
        "type": "노말 🌈",
        "desc": "따뜻하고 감성적인 힐링러!",
        "skill": "애교부리기 💖",
        "color": "🩷 핑크색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"
    },

    "ENFJ": {
        "pokemon": "가디안 💖",
        "type": "페어리 ✨",
        "desc": "사람들을 이끄는 따뜻한 리더!",
        "skill": "문포스 🌙",
        "color": "💚 초록색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"
    },

    "ENFP": {
        "pokemon": "피카츄 ⚡",
        "type": "전기 ⚡",
        "desc": "밝고 사랑스러운 인기쟁이!",
        "skill": "100만볼트 ⚡",
        "color": "💛 노란색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
    },

    "ISTJ": {
        "pokemon": "강철톤 ⛓️",
        "type": "강철 ⚙️",
        "desc": "믿음직하고 책임감 있는 타입!",
        "skill": "아이언테일 ⛓️",
        "color": "🩶 회색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/208.png"
    },

    "ISFJ": {
        "pokemon": "해피너스 🩷",
        "type": "노말 🌸",
        "desc": "배려심 넘치는 천사 타입!",
        "skill": "치유의파동 ✨",
        "color": "🩷 핑크색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png"
    },

    "ESTJ": {
        "pokemon": "보스로라 ⚙️",
        "type": "강철 🛡️",
        "desc": "추진력 강한 현실주의자!",
        "skill": "메탈버스트 ⚡",
        "color": "🤍 은색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/306.png"
    },

    "ESFJ": {
        "pokemon": "픽시 🌙",
        "type": "페어리 🌸",
        "desc": "친절하고 따뜻한 분위기 메이커!",
        "skill": "코멧펀치 ☄️",
        "color": "🌸 연핑크",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/36.png"
    },

    "ISTP": {
        "pokemon": "한카리아스 🦈",
        "type": "드래곤 🐉",
        "desc": "조용하지만 강력한 행동파!",
        "skill": "드래곤클로 🐲",
        "color": "💙 남색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/445.png"
    },

    "ISFP": {
        "pokemon": "라프라스 ❄️",
        "type": "물 💧",
        "desc": "감성적이고 자유로운 영혼!",
        "skill": "하이드로펌프 🌊",
        "color": "💎 하늘색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/131.png"
    },

    "ESTP": {
        "pokemon": "번치코 🥊",
        "type": "불꽃 🔥",
        "desc": "열정 넘치는 액션파!",
        "skill": "블레이즈킥 👟",
        "color": "❤️ 빨간색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png"
    },

    "ESFP": {
        "pokemon": "푸린 🎤",
        "type": "노말 🎵",
        "desc": "사람들을 행복하게 만드는 엔터테이너!",
        "skill": "노래하기 🎶",
        "color": "🌸 핑크색",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"
    }
}

# =========================================
# 제목
# =========================================
st.markdown("<div class='title'>🎮 MBTI Pokémon Universe</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>✨ 당신의 영혼과 연결된 포켓몬을 찾아보세요 ✨</div>", unsafe_allow_html=True)

# =========================================
# 사이드바
# =========================================
with st.sidebar:

    st.header("🌟 메뉴")

    st.write("🎭 MBTI 기반 포켓몬 추천")
    st.write("⚡ 랜덤 능력치 분석")
    st.write("💖 궁합 MBTI 확인")
    st.write("🎲 오늘의 운세")
    st.write("🏆 전설 등급 테스트")

    st.write("---")

    st.subheader("🎵 오늘의 기분")

    mood = st.radio(
        "현재 기분은?",
        ["😆 신남", "😴 피곤", "🥰 행복", "🔥 의욕 MAX"]
    )

    if mood == "😆 신남":
        st.success("오늘은 피카츄처럼 에너지 폭발 ⚡")

    elif mood == "😴 피곤":
        st.info("잠만보와 함께 쉬어가요 😴")

    elif mood == "🥰 행복":
        st.balloons()

    else:
        st.warning("오늘 당신의 열정이 불타오른다 🔥")

# =========================================
# MBTI 선택
# =========================================
mbti = st.selectbox(
    "🎭 당신의 MBTI를 선택하세요!",
    list(pokemon_data.keys())
)

# =========================================
# 버튼
# =========================================
if st.button("⚡ 포켓몬 소환하기!"):

    # 로딩 연출
    with st.spinner("포켓몬 세계와 연결 중... 🌌"):

        time.sleep(2)

    st.snow()

    result = pokemon_data[mbti]

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.image(result["img"], width=300)

    st.markdown(f"# {result['pokemon']}")

    st.markdown(
        f"<div class='type-box'>{result['type']}</div>",
        unsafe_allow_html=True
    )

    st.write("")

    st.success(f"✨ 당신과 가장 잘 어울리는 포켓몬은 {result['pokemon']} 입니다!")

    st.markdown(f"""
## 💬 성격 설명

{result['desc']}

---

## ⚔️ 대표 기술

{result['skill']}

---

## 🎨 당신의 에너지 컬러

{result['color']}
""")

    # =========================================
    # 능력치
    # =========================================
    st.markdown("## 📊 능력치 분석")

    hp = random.randint(70, 100)
    attack = random.randint(70, 100)
    defense = random.randint(70, 100)
    speed = random.randint(70, 100)
    iq = random.randint(70, 100)
    charm = random.randint(70, 100)

    st.write("❤️ 체력")
    st.progress(hp)

    st.write("⚔️ 공격력")
    st.progress(attack)

    st.write("🛡️ 방어력")
    st.progress(defense)

    st.write("⚡ 스피드")
    st.progress(speed)

    st.write("🧠 지능")
    st.progress(iq)

    st.write("💖 매력")
    st.progress(charm)

    # =========================================
    # 희귀도
    # =========================================
    rarity = random.choice([
        "🌟 일반",
        "💎 레어",
        "👑 에픽",
        "🔥 전설",
        "🌈 신화"
    ])

    st.markdown("## 🏆 당신의 희귀도")
    st.info(rarity)

    # =========================================
    # 오늘의 운세
    # =========================================
    fortune = random.choice([
        "🍀 엄청난 행운이 찾아옵니다!",
        "💖 새로운 인연이 생길지도 몰라요!",
        "⚡ 오늘은 도전하면 성공 확률 UP!",
        "🎁 깜짝 선물이 기다리고 있어요!",
        "🌈 행복한 일이 가득한 하루!"
    ])

    st.markdown("## 🎲 오늘의 운세")
    st.success(fortune)

    # =========================================
    # 궁합
    # =========================================
    compatibility = {
        "INTJ": "ENFP ⚡",
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

    st.markdown("## 💞 최고의 MBTI 궁합")

    st.warning(
        f"당신과 최고의 궁합은 {compatibility[mbti]} 입니다!"
    )

    # =========================================
    # 랜덤 포켓몬 친구
    # =========================================
    friends = [
        "꼬부기 💧",
        "이상해씨 🌿",
        "파이리 🔥",
        "토게피 🥚",
        "냐옹 😺",
        "잠만보 😴"
    ]

    st.markdown("## 🧸 당신의 포켓몬 친구")

    st.info(random.choice(friends))

    # =========================================
    # 한줄 명언
    # =========================================
    quotes = [
        "✨ 당신의 가능성은 무한합니다!",
        "⚡ 오늘도 반짝반짝 빛나는 하루!",
        "🔥 포기하지 않는 당신은 이미 챔피언!",
        "🌈 당신만의 특별한 매력을 믿어보세요!",
        "🎮 인생은 모험! 오늘도 레벨업!"
    ]

    st.markdown("## 🌟 오늘의 한마디")
    st.success(random.choice(quotes))

    # =========================================
    # 최종 메시지
    # =========================================
    st.write("")
    st.write("---")

    st.markdown("""
# 🎉 분석 완료!

당신은 포켓몬 세계에서도 특별한 존재입니다 ✨  
오늘도 자신만의 매력을 믿고 앞으로 나아가세요 🌈
""")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================
# 하단
# =========================================
st.write("")
st.write("---")

st.markdown("""
<div class='footer'>

🎮 MBTI Pokémon Universe  
Made with ❤️ using Streamlit

✨ Pokémon + MBTI + Emotion = Perfect ✨

</div>
""", unsafe_allow_html=True)
