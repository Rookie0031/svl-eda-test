import os
from dotenv import load_dotenv
import requests

# .env 파일에서 환경변수 불러오기
load_dotenv()

# 환경변수에서 엔드포인트와 리소스 경로 읽기
ENDPOINT = os.getenv("API_GATEWAY_ENDPOINT")
RESOURCE_PATH = os.getenv("API_GATEWAY_RESOURCE_PATH")

# 전체 URL 생성
url = f"{ENDPOINT}{RESOURCE_PATH}"

try:
    response = requests.get(url)
    response.raise_for_status()  # 오류 발생 시 예외 처리
    print("응답 코드:", response.status_code)
    print("응답 데이터:", response.text)
except requests.exceptions.RequestException as e:
    print("API 호출 중 오류 발생:", e)