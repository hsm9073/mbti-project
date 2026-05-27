import streamlit as st
import random
import time

# =========================================
# 페이지 설정
# =========================================
st.set_page_config(
    page_title="🔫 MBTI VALORANT 에이전트 추천기 🔫",
    page_icon="🎯",
    layout="centered"
)

# =========================================
# CSS
# =========================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Pretendard', sans-serif;
}

.main {
    background: linear-gradient(to bottom, #0f172a, #111827);
    color: white;
}

.title {
    text-align:center;
    font-size:55px;
    font-weight:900;
    color:#ff4655;
}

.subtitle {
    text-align:center;
    font-size:22px;
    color:#cbd5e1;
    margin-bottom:30px;
}

.card {
    background:#111827;
    padding:30px;
    border-radius:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.4);
    color:white;
}

.stButton>button {
    width:100%;
    height:60px;
    border:none;
    border-radius:18px;
    background:linear-gradient(to right,#ff4655,#ff7a59);
    color:white;
    font-size:22px;
    font-weight:bold;
}

.stButton>button:hover {
    background:linear-gradient(to right,#ff7a59,#ff4655);
}

.rank {
    padding:10px;
    border-radius:15px;
    background:linear-gradient(to right,#ff4655,#ffcc00);
    text-align:center;
    font-weight:bold;
    color:black;
}

.footer {
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# 발로란트 데이터
# =========================================
agents = {

    "INTJ": {
        "name": "CHAMBER 🕶️",
        "desc": "완벽한 계산형 킬러, 한 발로 끝내는 전략가",
        "role": "센티넬",
        "skill": "헤드헌터 🔫",
        "tier": "👑 프로픽",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltb3b1c3f0c2f7b2a3/Chamber.png"
    },

    "INTP": {
        "name": "KILLJOY 🤖",
        "desc": "기계처럼 분석하고 설계하는 방어 천재",
        "role": "센티넬",
        "skill": "나노스웜 💣",
        "tier": "💎 전략형",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltb3a3f0c2f7b2a3/Killjoy.png"
    },

    "ENTJ": {
        "name": "BRIMSTONE 🔥",
        "desc": "팀을 지휘하는 완벽한 리더",
        "role": "컨트롤러",
        "skill": "궤도폭격 ☄️",
        "tier": "🔥 지휘관",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltbrimstone.png"
    },

    "ENTP": {
        "name": "JETT 🌪️",
        "desc": "예측 불가, 자유로운 공격 스타일",
        "role": "듀얼리스트",
        "skill": "칼날 대시 ⚡",
        "tier": "💀 캐리형",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltjett.png"
    },

    "INFJ": {
        "name": "SAGE 💚",
        "desc": "팀을 살리는 조용한 수호자",
        "role": "센티넬",
        "skill": "부활 ✨",
        "tier": "💖 필수픽",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltsage.png"
    },

    "INFP": {
        "name": "REYNA 💜",
        "desc": "감정 기반 캐리형 솔로 플레이어",
        "role": "듀얼리스트",
        "skill": "영혼흡수 👁️",
        "tier": "🌈 하이리스크",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltreyna.png"
    },

    "ENFJ": {
        "name": "SKYE 🌿",
        "desc": "팀을 치유하고 이끄는 리더형 서포터",
        "role": "이니시에이터",
        "skill": "힐링 토템 🐺",
        "tier": "💚 팀버프",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltskye.png"
    },

    "ENFP": {
        "name": "PHOENIX 🔥",
        "desc": "불같은 에너지, 혼자도 팀도 캐리",
        "role": "듀얼리스트",
        "skill": "리바이브 🔥",
        "tier": "⚡ 인기픽",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltphoenix.png"
    },

    "ISTJ": {
        "name": "CYpher 🕵️",
        "desc": "정보를 완벽히 통제하는 분석가",
        "role": "센티넬",
        "skill": "트랩 와이어 🪤",
        "tier": "🧠 정보형",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltcypher.png"
    },

    "ISFJ": {
        "name": "SOVA 🏹",
        "desc": "팀을 위해 정보를 수집하는 지원형",
        "role": "이니시에이터",
        "skill": "정찰 화살 🎯",
        "tier": "💙 서포트",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltsova.png"
    },

    "ESTJ": {
        "name": "BREACH 💥",
        "desc": "강력한 진입형 파괴자",
        "role": "이니시에이터",
        "skill": "지진 충격 🌋",
        "tier": "🔥 돌격형",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltbreach.png"
    },

    "ESFJ": {
        "name": "ASTRA 🌌",
        "desc": "팀 전체를 조율하는 전략가",
        "role": "컨트롤러",
        "skill": "우주 조작 ✨",
        "tier": "💜 전략형",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltastra.png"
    },

    "ISTP": {
        "name": "YORU 👺",
        "desc": "혼자 침투하는 고독한 암살자",
        "role": "듀얼리스트",
        "skill": "차원 이동 🌌",
        "tier": "💀 변수",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltyoru.png"
    },

    "ISFP": {
        "name": "FADE 🌑",
        "desc": "감각적으로 적을 추적하는 사냥꾼",
        "role": "이니시에이터",
        "skill": "악몽 추적 👁️",
        "tier": "🌙 감각형",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltfade.png"
    },

    "ESTP": {
        "name": "RAZE 💣",
        "desc": "폭발적인 공격력의 러시형",
        "role": "듀얼리스트",
        "skill": "로켓 점프 🚀",
        "tier": "🔥 공격형",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltraze.png"
    },

    "ESFP": {
        "name": "NEON ⚡",
        "desc": "초고속 러시로 게임을 찢는 스타",
        "role": "듀얼리스트",
        "skill": "스피드 대시 ⚡",
        "tier": "🌟 캐리형",
        "img": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltneon.png"
    }
}

# =========================================
# UI
# =========================================
st.markdown("<div class='title'>🔫 MBTI VALORANT AGENT PICKER 🔫</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>🎯 당신의 플레이 스타일 에이전트는?</div>", unsafe_allow_html=True)

mbti = st.selectbox("🎭 MBTI 선택", list(agents.keys()))

if st.button("🔥 에이전트 소환!"):

    with st.spinner("스파이크 사이트 연결 중... 🌐"):
        time.sleep(2)

    st.snow()

    agent = agents[mbti]

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.image(agent["img"], use_container_width=True)

    st.markdown(f"# {agent['name']}")

    st.markdown(f"<div class='rank'>{agent['tier']}</div>", unsafe_allow_html=True)

    st.success(f"당신의 발로란트 에이전트는 {agent['name']}!")

    st.markdown(f"""
## 🧠 성향 분석
{agent['desc']}

## ⚔️ 대표 스킬
{agent['skill']}

## 🎮 포지션
{agent['role']}
""")

    st.markdown("## 📊 능력치")

    for stat in ["에임 🎯", "전략 🧠", "팀워크 🤝", "클러치 🔥"]:
        st.progress(random.randint(60, 100))

    st.markdown("## 🎲 오늘의 매치 운세")
    st.info(random.choice([
        "🔥 에임 각 미쳤습니다",
        "💎 랭크 상승 가능성 높음",
        "⚡ 클러치 게임 가능",
        "😈 팀운은 모르지만 당신은 잘함"
    ]))

    st.markdown("## 💞 듀오 추천")
    st.warning(random.choice(list(agents.keys())))

    st.markdown("</div>", unsafe_allow_html=True)

st.write("---")
st.caption("Made with ❤️ using Streamlit | VALORANT MBTI Edition 🔫")
