# 한국복지패널 데이터 기반 인구통계학적 특성별 월급 차이 시각화

이 프로젝트는 Python의 **Streamlit** 프레임워크를 활용하여 공공 데이터를 시각화하는 웹 대시보드를 제작하는 실습 프로젝트입니다.

## 주요 내용
- **데이터셋**: 2015년 한국복지패널 데이터
- **주요 기능**:
  - 성별, 연령대, 지역별 필터링 기능
  - 성별에 따른 월급 차이 분석 (막대 그래프)
  - 나이와 월급의 관계 분석 (선 그래프)
  - 지역별 연령대 비율 분석 등

## 실행 방법
1. 필수 라이브러리 설치:
   ```bash
   pip install streamlit pandas matplotlib seaborn plotly openpyxl
   ```
2. 앱 실행:
   ```bash
   streamlit run app.py
   ```

## 프로젝트 구조
- `app.py`: Streamlit 메인 애플리케이션 코드
- `data/`: 데이터셋 파일 (`welfare_2015.csv`, `welfare_2015_codebook.xlsx`)
- `.gitignore`: Git 제외 설정 파일
