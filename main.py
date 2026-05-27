import streamlit as st
import random
import time

# =========================================
# 페이지 설정
# =========================================
st.set_page_config(
    page_title="🔥 MBTI 브롤스타즈 추천기 🔥",
    page_icon="🎮",
    layout="centered"
)

# =========================================
# CSS 디자인
# =========================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Pretendard', sans-serif;
}

.main {
    background: linear-gradient(to bottom, #fff4e6, #ffe8f3);
}

.title {
    text-align:center;
    font-size:55px;
    font-weight:900;
    color:#ff3d00;
}

.subtitle {
    text-align:center;
    font-size:22px;
    color:gray;
    margin-bottom:30px;
}

.card {
    background:white;
    padding:30px;
    border-radius:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.15);
}

.stButton>button {
    width:100%;
    height:60px;
    border:none;
    border-radius:18px;
    background:linear-gradient(to right,#ff512f,#dd2476);
    color:white;
    font-size:22px;
    font-weight:bold;
}

.stButton>button:hover {
    background:linear-gradient(to right,#dd2476,#ff512f);
    color:white;
}

.footer {
    text-align:center;
    color:gray;
    margin-top:50px;
}

.rank-box {
    background:linear-gradient(to right,#f7971e,#ffd200);
    padding:12px;
    border-radius:15px;
    text-align:center;
    color:black;
    font-weight:bold;
    font-size:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# 브롤스타즈 데이터
# =========================================
brawlers = {

    "INTJ": {
        "name": "스파이크 🌵",
        "desc": "조용하지만 엄청 강력한 전략가 타입!",
        "weapon": "가시 폭탄 💥",
        "rank": "👑 전설",
        "color": "💚 초록",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000006.png"
    },

    "INTP": {
        "name": "바이런 🧪",
        "desc": "분석적이고 지능적인 브레인 타입!",
        "weapon": "독약 샷 ☠️",
        "rank": "💎 신화",
        "color": "💜 보라",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000088.png"
    },

    "ENTJ": {
        "name": "팽 🥊",
        "desc": "카리스마 넘치는 리더형 브롤러!",
        "weapon": "킥 어택 👟",
        "rank": "🔥 크로마틱",
        "color": "❤️ 빨강",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000092.png"
    },

    "ENTP": {
        "name": "체스터 🎭",
        "desc": "장난기 많고 예측 불가능한 타입!",
        "weapon": "랜덤 궁극기 🎲",
        "rank": "🌈 전설",
        "color": "🩷 핑크",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000100.png"
    },

    "INFJ": {
        "name": "샌디 😴",
        "desc": "신비롭고 조용한 감성 브롤러!",
        "weapon": "모래 폭풍 🌪️",
        "rank": "🌙 전설",
        "color": "💛 노랑",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000052.png"
    },

    "INFP": {
        "name": "코델리우스 🍄",
        "desc": "몽환적이고 상상력 넘치는 타입!",
        "weapon": "버섯 공격 🍄",
        "rank": "💎 신화",
        "color": "💚 연두",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000111.png"
    },

    "ENFJ": {
        "name": "포코 🎸",
        "desc": "사람들을 행복하게 만드는 분위기 메이커!",
        "weapon": "뮤직 웨이브 🎵",
        "rank": "🎶 에픽",
        "color": "💜 보라",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000014.png"
    },

    "ENFP": {
        "name": "레온 🦎",
        "desc": "자유롭고 에너지 넘치는 인기쟁이!",
        "weapon": "스핀 블레이드 ⚡",
        "rank": "👑 전설",
        "color": "💚 초록",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000023.png"
    },

    "ISTJ": {
        "name": "샘 🔧",
        "desc": "묵묵하고 책임감 있는 브롤러!",
        "weapon": "너클 펀치 👊",
        "rank": "⚙️ 에픽",
        "color": "🩶 회색",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000098.png"
    },

    "ISFJ": {
        "name": "팸 🔩",
        "desc": "팀을 지켜주는 든든한 힐러!",
        "weapon": "스크랩 공격 🔧",
        "rank": "💖 영웅",
        "color": "🩷 핑크",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000038.png"
    },

    "ESTJ": {
        "name": "불 🔥",
        "desc": "강력한 추진력의 돌격대장!",
        "weapon": "샷건 폭발 💣",
        "rank": "🔥 초희귀",
        "color": "❤️ 빨강",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000002.png"
    },

    "ESFJ": {
        "name": "재키 ⛏️",
        "desc": "친화력 최고! 팀워크 장인!",
        "weapon": "지진 공격 🌍",
        "rank": "💛 초희귀",
        "color": "🧡 주황",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000058.png"
    },

    "ISTP": {
        "name": "에드거 🧣",
        "desc": "쿨하고 혼자 싸우는 암살자 스타일!",
        "weapon": "초고속 펀치 ⚡",
        "rank": "🌑 영웅",
        "color": "🖤 검정",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000080.png"
    },

    "ISFP": {
        "name": "재닛 🎤",
        "desc": "감성적이고 자유로운 아티스트 타입!",
        "weapon": "음파 공격 🎶",
        "rank": "🌈 크로마틱",
        "color": "💖 핑크",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000091.png"
    },

    "ESTP": {
        "name": "팽 🥋",
        "desc": "스릴을 즐기는 액션파 브롤러!",
        "weapon": "연속 킥 🔥",
        "rank": "🔥 크로마틱",
        "color": "❤️ 빨강",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000092.png"
    },

    "ESFP": {
        "name": "멜로디 🎧",
        "desc": "화려하고 주목받는 슈퍼스타!",
        "weapon": "뮤직 어택 🎵",
        "rank": "🌟 신화",
        "color": "💜 보라",
        "img": "https://cdn.brawlify.com/brawlers/borderless/16000119.png"
    }
}

# =========================================
# 제목
# =========================================
st.markdown("<div class='title'>🔥 MBTI 브롤스타즈 추천기 🔥</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>🎮 당신과 가장 잘 어울리는 브롤러를 찾아보세요!</div>", unsafe_allow_html=True)

# =========================================
# 사이드바
# =========================================
with st.sidebar:

    st.header("🌟 메뉴")

    st.write("🎭 MBTI 브롤러 분석")
    st.write("⚔️ 전투 능력치")
    st.write("🏆 브롤러 등급")
    st.write("🎲 오늘의 운세")
    st.write("🔥 스타 플레이어 테스트")

    st.write("---")

    mood = st.selectbox(
        "💭 현재 기분은?",
        ["😆 신남", "😴 피곤", "🔥 의욕 MAX", "🥰 행복"]
    )

    if mood == "😆 신남":
        st.success("오늘은 레온처럼 날아다닐 기세 ⚡")

    elif mood == "😴 피곤":
        st.info("샌디처럼 조금 쉬어가요 😴")

    elif mood == "🔥 의욕 MAX":
        st.warning("오늘 당신의 승률 폭발 예정 🔥")

    else:
        st.balloons()

# =========================================
# MBTI 선택
# =========================================
mbti = st.selectbox(
    "🎭 당신의 MBTI를 선택하세요!",
    list(brawlers.keys())
)

# =========================================
# 결과 버튼
# =========================================
if st.button("🔥 브롤러 소환하기!"):

    with st.spinner("브롤스타즈 서버 접속 중... 🎮"):
        time.sleep(2)

    st.snow()

    result = brawlers[mbti]

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.image(result["img"], width=300)

    st.markdown(f"# {result['name']}")

    st.markdown(
        f"<div class='rank-box'>{result['rank']}</div>",
        unsafe_allow_html=True
    )

    st.success(
        f"✨ 당신과 가장 잘 어울리는 브롤러는 {result['name']} 입니다!"
    )

    st.markdown(f"""
## 💬 성격 분석

{result['desc']}

---

## ⚔️ 대표 공격

{result['weapon']}

---

## 🎨 에너지 컬러

{result['color']}
""")

    # =========================================
    # 능력치
    # =========================================
    st.markdown("## 📊 브롤러 능력치")

    hp = random.randint(70, 100)
    attack = random.randint(70, 100)
    defense = random.randint(70, 100)
    speed = random.randint(70, 100)
    aim = random.randint(70, 100)
    teamwork = random.randint(70, 100)

    st.write("❤️ 체력")
    st.progress(hp)

    st.write("⚔️ 공격력")
    st.progress(attack)

    st.write("🛡️ 방어력")
    st.progress(defense)

    st.write("⚡ 스피드")
    st.progress(speed)

    st.write("🎯 에임")
    st.progress(aim)

    st.write("🤝 팀워크")
    st.progress(teamwork)

    # =========================================
    # 티어
    # =========================================
    tier = random.choice([
        "🏆 S 티어",
        "🔥 OP 티어",
        "⚡ A 티어",
        "💎 메타 브롤러",
        "👑 전설급"
    ])

    st.markdown("## 🌟 현재 메타 티어")
    st.info(tier)

    # =========================================
    # 운세
    # =========================================
    st.markdown("## 🎲 오늘의 브롤 운세")

    fortunes = [

        "🍀 오늘은 트로피 폭등 예정!",
        "🔥 연승 모드 발동!",
        "⚡ 스타 플레이어 가능성 UP!",
        "🎁 전설 브롤러 뽑을 운세!",
        "💎 오늘 운이 엄청 좋습니다!"
    ]

    st.success(random.choice(fortunes))

    # =========================================
    # 궁합
    # =========================================
    st.markdown("## 💞 최고의 듀오 궁합")

    duo = random.choice([
        "쉘리 🤠",
        "콜트 🔫",
        "스파이크 🌵",
        "레온 🦎",
        "멜로디 🎧",
        "팽 🥊"
    ])

    st.warning(f"당신과 최고의 듀오 브롤러는 {duo}")

    # =========================================
    # 명언
    # =========================================
    st.markdown("## 🌈 브롤 명언")

    quotes = [

        "🔥 패배는 다음 승리의 경험치!",
        "⚡ 오늘도 브롤러답게 싸워라!",
        "🎮 진짜 고수는 끝까지 포기하지 않는다!",
        "🏆 스타 플레이어는 바로 당신!",
        "💥 실력도 중요하지만 즐기는 게 최고!"
    ]

    st.info(random.choice(quotes))

    # =========================================
    # 최종 메시지
    # =========================================
    st.write("")
    st.write("---")

    st.markdown("""
# 🎉 분석 완료!

당신은 브롤스타즈 세계에서도 특별한 브롤러입니다 🔥  
오늘도 승리를 향해 돌진하세요 ⚡
""")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================
# 하단
# =========================================
st.write("")
st.write("---")

st.markdown("""
<div class='footer'>

🎮 MBTI Brawl Stars Universe  
Made with ❤️ using Streamlit

🔥 MBTI + Brawl Stars = PERFECT 🔥

</div>
""", unsafe_allow_html=True)
