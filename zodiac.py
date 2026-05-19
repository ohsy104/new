#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌟 별자리 알려주는 프로그램 (우주 스타일) 🌟
생년월일을 입력하면 별자리와 운세를 알려주는 프로그램입니다.
"""

import streamlit as st
import random
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="🌟 Cosmic Zodiac Fortune", layout="wide")

# ==================== 우주 스타일 디자인 요소 ====================

class CosmicDesign:
    """우주 테마 디자인을 담당하는 클래스"""
    
    # 우주 테마 색상 및 문자
    STAR = "⭐"
    STAR_SPARKLE = "✨"
    CONSTELLATION = "🔷"
    MOON = "🌙"
    PLANET = "🪐"
    COMET = "☄️"
    SUN = "☀️"
    SPACE = "🌌"
    GALAXY = "🌠"


# ==================== 별자리 정보 데이터베이스 ====================

ZODIAC_INFO = {
    "물병자리": {
        "symbol": "♒",
        "period": "1월 20일 ~ 2월 18일",
        "characteristics": "독창적이고 혁신적인 사고를 가진 자유로운 영혼",
        "color": "파란색",
        "lucky_number": 7,
    },
    "물고기자리": {
        "symbol": "♓",
        "period": "2월 19일 ~ 3월 20일",
        "characteristics": "직관력 있고 감정이 풍부한 예술가 기질",
        "color": "초록색",
        "lucky_number": 3,
    },
    "양자리": {
        "symbol": "♈",
        "period": "3월 21일 ~ 4월 19일",
        "characteristics": "용감하고 열정적인 추진력의 소유자",
        "color": "빨간색",
        "lucky_number": 9,
    },
    "황소자리": {
        "symbol": "♉",
        "period": "4월 20일 ~ 5월 20일",
        "characteristics": "안정적이고 신뢰할 수 있는 현실적인 사람",
        "color": "녹색",
        "lucky_number": 6,
    },
    "쌍둥이자리": {
        "symbol": "♊",
        "period": "5월 21일 ~ 6월 20일",
        "characteristics": "호기심 많고 소통 능력이 뛰어난 지적 존재",
        "color": "노란색",
        "lucky_number": 5,
    },
    "게자리": {
        "symbol": "♋",
        "period": "6월 21일 ~ 7월 22일",
        "characteristics": "섬세하고 감정적으로 돌보는 따뜻한 마음",
        "color": "흰색",
        "lucky_number": 2,
    },
    "사자자리": {
        "symbol": "♌",
        "period": "7월 23일 ~ 8월 22일",
        "characteristics": "자신감 있고 창의적인 리더십의 소유자",
        "color": "금색",
        "lucky_number": 1,
    },
    "처녀자리": {
        "symbol": "♍",
        "period": "8월 23일 ~ 9월 22일",
        "characteristics": "완벽주의자이며 분석적이고 신중한 실리주의자",
        "color": "갈색",
        "lucky_number": 4,
    },
    "천칭자리": {
        "symbol": "♎",
        "period": "9월 23일 ~ 10월 22일",
        "characteristics": "균형감각 있고 외교적인 평화의 중재자",
        "color": "분홍색",
        "lucky_number": 6,
    },
    "전갈자리": {
        "symbol": "♏",
        "period": "10월 23일 ~ 11월 21일",
        "characteristics": "집중력 있고 강한 의지의 신비로운 존재",
        "color": "검은색",
        "lucky_number": 8,
    },
    "사수자리": {
        "symbol": "♐",
        "period": "11월 22일 ~ 12월 21일",
        "characteristics": "낙관적이고 모험을 좋아하는 자유로운 영혼",
        "color": "보라색",
        "lucky_number": 3,
    },
    "염소자리": {
        "symbol": "♑",
        "period": "12월 22일 ~ 1월 19일",
        "characteristics": "야심찬 목표의식과 책임감 있는 현실가",
        "color": "회색",
        "lucky_number": 8,
    },
}

# 별자리별 운세 데이터베이스
FORTUNES = {
    "물병자리": [
        "새로운 아이디어가 떠오르는 날입니다. 창의력을 발휘하세요!",
        "친구들과의 만남이 좋은 기회를 가져올 것 같습니다.",
        "혁신적인 변화가 당신을 기다리고 있습니다.",
        "독립심이 강해지는 시기입니다. 자신의 길을 걸으세요!",
        "예상치 못한 좋은 소식이 날아올 것 같습니다.",
    ],
    "물고기자리": [
        "직관력이 좋은 날입니다. 마음의 목소리를 들으세요.",
        "창의적인 작업에서 영감을 받을 것 같습니다.",
        "감정이 풍부해지는 시기, 예술 활동을 추천합니다.",
        "대인관계가 부드러워질 것 같은 좋은 에너지입니다.",
        "상상력이 현실이 되는 날입니다. 꿈꾸세요!",
    ],
    "양자리": [
        "용감함이 필요한 순간입니다. 도전하세요!",
        "에너지가 가득한 날, 새로운 프로젝트를 시작해도 좋습니다.",
        "열정이 전염되는 하루가 될 것 같습니다.",
        "첫 발을 내딛는 것이 성공의 시작이 됩니다.",
        "누구보다 빠르게 행동하세요. 운이 함께합니다!",
    ],
    "황소자리": [
        "안정적인 계획이 현실화될 좋은 날입니다.",
        "신중한 결정이 좋은 결과를 가져올 것 같습니다.",
        "자신의 능력을 믿고 천천히 나아가세요.",
        "물질적인 운이 좋은 시기입니다.",
        "견고한 기초를 다지는 것이 중요합니다.",
    ],
    "쌍둥이자리": [
        "소통이 빛나는 날입니다. 많은 사람을 만나세요!",
        "호기심을 따라 움직이면 좋은 일이 생깁니다.",
        "정보와 아이디어가 풍부해질 것 같습니다.",
        "말 한 마디가 큰 변화를 일으킬 수 있는 날입니다.",
        "새로운 연결고리가 당신의 미래를 밝혀줄 것 같습니다.",
    ],
    "게자리": [
        "가정이 따뜻해질 것 같은 좋은 기운입니다.",
        "감정이 안정되는 시기, 중요한 결정을 해도 좋습니다.",
        "배려심이 깊어지는 날, 주변 사람을 돌보세요.",
        "직관과 감정의 조화가 이루어질 것 같습니다.",
        "내면의 안정이 외적 성공을 가져올 것 같습니다.",
    ],
    "사자자리": [
        "당신의 리더십이 빛나는 날입니다!",
        "자신감이 최고조에 이르는 시기입니다.",
        "창의적인 표현이 주목받을 것 같습니다.",
        "누군가의 존경과 인정을 받게 될 것 같습니다.",
        "주인공처럼 당당하게 앞으로 나아가세요!",
    ],
    "처녀자리": [
        "세부사항에 집중하세요. 완벽함이 가능합니다.",
        "분석적인 사고가 문제 해결을 도울 것 같습니다.",
        "신중한 계획이 좋은 결과를 가져올 것입니다.",
        "작은 개선이 큰 변화를 만들 것 같습니다.",
        "정확한 판단과 실행이 성공의 열쇠입니다.",
    ],
    "천칭자리": [
        "균형감각이 좋아질 것 같은 날입니다.",
        "인간관계가 부드러워질 것 같습니다.",
        "공정한 판단이 높이 평가받을 것 같습니다.",
        "아름다운 것에 끌릴 것 같은 좋은 기운입니다.",
        "평화롭고 조화로운 하루가 될 것 같습니다.",
    ],
    "전갈자리": [
        "집중력이 최고조에 이르는 시기입니다.",
        "깊은 통찰력이 문제의 핵심을 꿰뚫을 것 같습니다.",
        "신비로운 기운이 당신을 감싸고 있습니다.",
        "숨겨진 진실이 드러날 것 같습니다.",
        "강한 의지가 모든 장애물을 극복하게 할 것 같습니다.",
    ],
    "사수자리": [
        "낙관적인 기운이 모든 것을 긍정적으로 변화시킬 것 같습니다.",
        "모험심이 발동하는 시기, 새로운 경험을 즐기세요!",
        "큰 꿈을 꾸어도 좋을 것 같습니다.",
        "자유로운 영혼이 새로운 길을 개척할 것 같습니다.",
        "운이 좋아서 예상치 못한 행운이 올 것 같습니다.",
    ],
    "염소자리": [
        "계획이 현실화되는 시기입니다.",
        "인내심과 노력이 결실을 맺을 것 같습니다.",
        "책임감 있는 행동이 신뢰를 쌓을 것 같습니다.",
        "야심찬 목표를 세워도 좋을 시기입니다.",
        "현실적인 판단이 큰 성공을 가져올 것 같습니다.",
    ],
}


# ==================== 별자리 판별 함수 ====================

def is_valid_date(year, month, day):
    """입력된 날짜가 유효한지 확인하는 함수"""
    try:
        if year < 1:
            return False, "연도는 양수여야 합니다."
        if month < 1 or month > 12:
            return False, "월은 1~12 사이여야 합니다."
        if day < 1 or day > 31:
            return False, "일은 1~31 사이여야 합니다."
        
        datetime(year, month, day)
        return True, "유효한 날짜입니다."
    except ValueError:
        return False, "유효하지 않은 날짜입니다. 다시 확인해주세요."


def get_zodiac_sign(month, day):
    """월과 일을 입력받아 별자리를 반환하는 함수"""
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "물병자리"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "물고기자리"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "양자리"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "황소자리"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "쌍둥이자리"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "게자리"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "사자자리"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "처녀자리"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "천칭자리"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "전갈자리"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "사수자리"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "염소자리"


def get_zodiac_fortune(zodiac_sign):
    """별자리의 운세를 무작위로 반환하는 함수"""
    fortunes = FORTUNES[zodiac_sign]
    return random.choice(fortunes)


# ==================== 메인 Streamlit 앱 ====================

def main():
    # 헤더
    st.markdown(f"<div style='text-align: center;'>{CosmicDesign.SPACE} " * 8 + "</div>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center;'>{CosmicDesign.MOON} 별자리 운세 알려주는 프로그램 {CosmicDesign.SUN}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: #9370DB;'>{CosmicDesign.GALAXY} Cosmic Zodiac Fortune {CosmicDesign.GALAXY}</h3>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # 사용 설명서
    with st.expander(f"📖 {CosmicDesign.STAR} 사용 방법 {CosmicDesign.STAR}"):
        st.markdown(f"""
        #### {CosmicDesign.CONSTELLATION} 1단계: 생년월일 입력
        - 연도 입력 (예: 2010)
        - 월 입력 (1~12, 예: 7월)
        - 일 입력 (1~31, 예: 23일)
        
        #### {CosmicDesign.CONSTELLATION} 2단계: 당신의 별자리와 운세 확인
        - 별자리 기호
        - 별자리 특징
        - 오늘의 운세
        - 행운의 색과 숫자
        
        #### {CosmicDesign.CONSTELLATION} 3단계: 다시 입력하기
        - 다른 생년월일로 별자리를 확인해보세요!
        
        💡 **팁**: 페이지를 새로고침할 때마다 다른 운세가 나옵니다!
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 입력 폼
    st.subheader(f"📍 생년월일을 입력해주세요.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        year = st.number_input("연도 입력 (예: 2010)", min_value=1, max_value=2025, value=2000, step=1)
    
    with col2:
        month = st.number_input("월 입력 (1-12)", min_value=1, max_value=12, value=1, step=1)
    
    with col3:
        day = st.number_input("일 입력 (1-31)", min_value=1, max_value=31, value=1, step=1)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 버튼
    if st.button(f"🌟 별자리와 운세 확인하기", use_container_width=True):
        # 날짜 유효성 검사
        is_valid, message = is_valid_date(int(year), int(month), int(day))
        
        if not is_valid:
            st.error(f"❌ {message}")
        else:
            # 별자리 계산
            zodiac_sign = get_zodiac_sign(int(month), int(day))
            zodiac_data = ZODIAC_INFO[zodiac_sign]
            fortune = get_zodiac_fortune(zodiac_sign)
            
            # 결과 출력
            st.markdown("<hr>", unsafe_allow_html=True)
            
            # 우주로부터의 메시지
            st.markdown(f"<div style='text-align: center; font-size: 20px;'>{CosmicDesign.PLANET} 우주로부터의 메시지 {CosmicDesign.PLANET}</div>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.info(f"**생년월일**\n{year}년 {month}월 {day}일")
            
            with col2:
                st.success(f"**당신의 별자리**\n{CosmicDesign.CONSTELLATION} {zodiac_sign} {CosmicDesign.CONSTELLATION}\n{zodiac_data['symbol']}")
            
            with col3:
                st.warning(f"**기간**\n{zodiac_data['period']}")
            
            # 별자리 특징
            st.markdown(f"### {CosmicDesign.STAR} 별자리 특징")
            st.write(f"> {zodiac_data['characteristics']}")
            
            # 오늘의 운세
            st.markdown(f"### {CosmicDesign.GALAXY} 오늘의 운세")
            st.write(f"> {fortune}")
            
            # 행운 정보
            st.markdown(f"### {CosmicDesign.STAR_SPARKLE} 행운 정보")
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"🎨 **행운의 색**: {zodiac_data['color']}")
            
            with col2:
                st.info(f"✨ **행운의 숫자**: {zodiac_data['lucky_number']}")
            
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 18px;'>{CosmicDesign.COMET} 우주의 신비로움이 당신의 운을 밝혀주길 {CosmicDesign.STAR_SPARKLE}</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
