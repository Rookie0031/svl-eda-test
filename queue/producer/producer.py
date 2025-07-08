import os
from dotenv import load_dotenv
import boto3

load_dotenv()  # .env 파일 로드

# SQS 클라이언트 생성
sqs = boto3.client('sqs', region_name='ap-northeast-2')
queue_url = os.getenv('SQS_URL')

def send_message(message_body):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    print("메시지 전송 완료:", response.get('MessageId'))

if __name__ == "__main__":
    send_message("안녕하세요! SQS 테스트 메시지입니다.") 
