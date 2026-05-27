import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="🎮",
    layout="centered"
)

# 제목
st.title("🎮 MBTI 포켓몬 추천기")
st.markdown("### ✨ 당신의 MBTI와 가장 잘 어울리는 포켓몬은?!")

st.write("---")

# MBTI 데이터
pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠 🧬",
        "desc": "전략적이고 독립적인 당신! 강력한 카리스마의 뮤츠와 닮았어요.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"
    },
    "INFP": {
        "pokemon": "이브이 🌸",
        "desc": "감성적이고 따뜻한 당신은 무한한 가능성의 이브이와 찰떡!",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png"
    },
    "ENFP": {
        "pokemon": "피카츄 ⚡",
        "desc": "에너지 넘치고 사랑스러운 당신! 모두의 인기스타 피카츄!",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    },
    "ENTP": {
        "pokemon": "팬텀 👻",
        "desc": "장난기 많고 창의적인 당신은 신비로운 팬텀 스타일!",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png"
    },
    "ISFJ": {
        "pokemon": "해피너스 🩷",
        "desc": "배려심 넘치는 당신은 모두를 행복하게 만드는 해피너스!",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png"
    },
    "ESTP": {
        "pokemon": "리자몽 🔥",
        "desc": "열정과 추진력 폭발! 무대 체질 리자몽!",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"
    },
    "INFJ": {
        "pokemon": "루기아 🌊",
        "desc": "신비롭고 깊은 통찰력을 가진 당신은 루기아 타입!",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png"
    },
    "ESFP": {
        "pokemon": "푸린 🎤",
        "desc": "사람들을 즐겁게 하는 매력쟁이! 귀여운 푸린!",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png"
    }
}

# MBTI 선택
mbti = st.selectbox(
    "🎭 당신의 MBTI를 선택하세요!",
    list(pokemon_data.keys())
)

st.write("")

# 버튼
if st.button("✨ 내 포켓몬 확인하기!"):
    result = pokemon_data[mbti]

    st.balloons()

    st.success(f"당신과 어울리는 포켓몬은 바로 **{result['pokemon']}**!")

    st.image(result["img"], width=220)

    st.markdown(
        f"""
        ## 💬 성격 분석
        
        {result['desc']}
        """
    )

    st.write("---")

    st.markdown("### 🌟 오늘의 한마디")
    
    quotes = [
        "포켓몬 마스터의 길은 오늘도 계속된다! 🚀",
        "당신의 매력은 이미 전설급! ✨",
        "피카츄도 반할 성격이에요 ⚡",
        "오늘도 귀엽게 힘내봐요 🌈"
    ]

    import random
    st.info(random.choice(quotes))

# 하단
st.write("")
st.caption("Made with ❤️ using Streamlit")
