import random
import time

# ======================================
# 플레이어 MBTI 선택
# ======================================
print("🎮 MBTI 포켓몬 배틀 게임!")
print("당신의 MBTI를 입력하세요 (예: ENFP, INTJ 등)")

mbti = input("👉 MBTI: ").upper()

# ======================================
# 포켓몬 데이터
# ======================================
pokemon = {
    "INTJ": "뮤츠 🧬",
    "INFP": "이브이 🌸",
    "ENFP": "피카츄 ⚡",
    "ENTJ": "리자몽 🔥",
    "INFJ": "루기아 🌊",
    "ISTP": "한카리아스 🐉"
}

enemy = ["야생 팬텀 👻", "야생 리자몽 🔥", "야생 갸라도스 🌊", "야생 망나뇽 🐉"]

# ======================================
# 기본 값
# ======================================
hp = 100
enemy_hp = 100

player = pokemon.get(mbti, "피카츄 ⚡")
wild = random.choice(enemy)

print("\n🎯 당신의 포켓몬:", player)
print("⚔️ 상대:", wild)

print("\n🔥 배틀 시작!")

# ======================================
# 게임 루프
# ======================================
while hp > 0 and enemy_hp > 0:

    print("\n====================")
    print(f"❤️ 내 HP: {hp}")
    print(f"💀 적 HP: {enemy_hp}")
    print("====================")

    print("\n행동 선택:")
    print("1️⃣ 공격")
    print("2️⃣ 방어")
    print("3️⃣ 회복")

    choice = input("👉 선택: ")

    # 플레이어 행동
    if choice == "1":
        damage = random.randint(10, 25)
        enemy_hp -= damage
        print(f"🔥 공격 성공! {damage} 데미지!")

    elif choice == "2":
        block = random.randint(5, 15)
        print(f"🛡️ 방어 자세! 피해 감소 효과 {block}")

    elif choice == "3":
        heal = random.randint(10, 20)
        hp += heal
        print(f"💖 회복! HP +{heal}")

    else:
        print("❌ 잘못된 입력!")

    # 적 공격
    if enemy_hp > 0:
        enemy_damage = random.randint(8, 20)
        hp -= enemy_damage
        print(f"💥 적의 공격! -{enemy_damage} HP")

    time.sleep(1)

# ======================================
# 결과
# ======================================
print("\n====================")

if hp > 0:
    print("🏆 승리!")
    print(f"🎉 {player}가 전투에서 승리했습니다!")
else:
    print("💀 패배...")
    print("다음엔 더 강해지세요!")

print("====================")
