# Gems가 작성한 확장 가능한 클린 코드
import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="Gems 만능 단위 변환기", page_icon="🌐")

# --- 제목 ---
st.title("🌐 Gems 만능 단위 변환기")
st.write("길이, 온도, 속도 등 다양한 단위를 변환해 보세요.")


# --- 메인 카테고리 선택 ---
# st.tabs()를 사용해 각 변환기를 탭으로 분리하여 UI를 깔끔하게 만듭니다.
tab_length, tab_temp, tab_speed = st.tabs(["📏 길이", "🌡️ 온도", "🚀 속도"])


# --- 1. 길이 변환 탭 ---
with tab_length:
    st.header("📏 길이 변환기")

    # 단위와 변환 기준(미터)을 딕셔너리로 관리하면 코드가 깔끔해집니다.
    length_units = {
        '밀리미터(mm)': 0.001,
        '센티미터(cm)': 0.01,
        '미터(m)': 1.0,
        '킬로미터(km)': 1000.0,
        '인치(inch)': 0.0254
    }
    
    # st.columns로 위젯들을 가로로 정렬합니다.
    col1, col2 = st.columns(2)
    with col1:
        from_unit_len = st.selectbox("어떤 단위에서?", list(length_units.keys()), key='len_from')
    with col2:
        to_unit_len = st.selectbox("어떤 단위로?", list(length_units.keys()), key='len_to')

    # 숫자 입력 필드
    input_value_len = st.number_input("변환할 값을 입력하세요:", value=1.0, format="%.4f", key='len_input')

    # 변환 로직
    # 1. 입력값을 기본 단위(미터)로 변환합니다.
    value_in_meters = input_value_len * length_units[from_unit_len]
    # 2. 기본 단위(미터)에서 목표 단위로 다시 변환합니다.
    converted_value_len = value_in_meters / length_units[to_unit_len]

    # 결과 출력
    st.success(f"**결과: {converted_value_len:,.4f} {to_unit_len.split('(')[0]}**")


# --- 2. 온도 변환 탭 ---
with tab_temp:
    st.header("🌡️ 온도 변환기")

    temp_units = ('섭씨(℃)', '화씨(℉)', '절대온도(K)')
    
    col1, col2 = st.columns(2)
    with col1:
        from_unit_temp = st.selectbox("어떤 단위에서?", temp_units, key='temp_from')
    with col2:
        to_unit_temp = st.selectbox("어떤 단위로?", temp_units, key='temp_to')

    input_value_temp = st.number_input("변환할 값을 입력하세요:", value=0.0, format="%.2f", key='temp_input')

    # 변환 로직 (온도는 공식이 복잡해 if문으로 처리합니다)
    celsius = 0.0
    # 1. 어떤 단위든 먼저 '섭씨'로 변환합니다.
    if from_unit_temp == '섭씨(℃)':
        celsius = input_value_temp
    elif from_unit_temp == '화씨(℉)':
        celsius = (input_value_temp - 32) * 5/9
    elif from_unit_temp == '절대온도(K)':
        celsius = input_value_temp - 273.15

    # 2. '섭씨'에서 목표 단위로 다시 변환합니다.
    converted_value_temp = 0.0
    if to_unit_temp == '섭씨(℃)':
        converted_value_temp = celsius
    elif to_unit_temp == '화씨(℉)':
        converted_value_temp = (celsius * 9/5) + 32
    elif to_unit_temp == '절대온도(K)':
        converted_value_temp = celsius + 273.15

    # 결과 출력
    st.success(f"**결과: {converted_value_temp:,.2f} {to_unit_temp.split('(')[0]}**")


# --- 3. 속도 변환 탭 ---
with tab_speed:
    st.header("🚀 속도 변환기")

    # 속도의 기준은 'm/s'로 잡습니다.
    speed_units = {
        'm/s': 1.0,
        'm/min': 1/60,
        'km/h': 1/3.6,
        'km/s': 1000.0,
        'km/min': 1000/60,
    }

    col1, col2 = st.columns(2)
    with col1:
        from_unit_speed = st.selectbox("어떤 단위에서?", list(speed_units.keys()), key='speed_from')
    with col2:
        to_unit_speed = st.selectbox("어떤 단위로?", list(speed_units.keys()), key='speed_to')
        
    input_value_speed = st.number_input("변환할 값을 입력하세요:", value=1.0, format="%.4f", key='speed_input')

    # 변환 로직
    # 1. 입력값을 기본 단위(m/s)로 변환합니다.
    value_in_mps = input_value_speed * speed_units[from_unit_speed]
    # 2. 기본 단위(m/s)에서 목표 단위로 다시 변환합니다.
    converted_value_speed = value_in_mps / speed_units[to_unit_speed]
    
    # 결과 출력
    st.success(f"**결과: {converted_value_speed:,.4f} {to_unit_speed}**")
