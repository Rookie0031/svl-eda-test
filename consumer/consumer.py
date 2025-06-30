import os
from dotenv import load_dotenv
import boto3

load_dotenv()  # .env 파일 로드

# SQS 클라이언트 생성
sqs = boto3.client('sqs', region_name='ap-northeast-2')
queue_url = os.getenv('QUEUE_URL')

def receive_message():
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )
    messages = response.get('Messages', [])
    for message in messages:
        print("받은 메시지:", message['Body'])
        # 메시지 삭제 (중복 소비 방지)
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
        print("메시지 삭제 완료")

if __name__ == "__main__":
    receive_message() 
