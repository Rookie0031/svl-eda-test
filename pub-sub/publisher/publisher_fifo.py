import os
import uuid
from dotenv import load_dotenv
import boto3

load_dotenv()  # .env 파일 로드

# SNS 클라이언트 생성
sns = boto3.client('sns', region_name='ap-northeast-2')
topic_arn = os.getenv('SNS_FIFO_TOPIC_ARN')

def publish_message(message_body):
    response = sns.publish(
        TopicArn=topic_arn,
        Message=message_body,
        MessageGroupId="test-group",  # FIFO 필수
        MessageDeduplicationId=str(uuid.uuid4())  # FIFO 필수, 중복 방지
    )
    print("메시지 발행 완료:", response.get('MessageId'))

if __name__ == "__main__":
    publish_message("안녕하세요! SNS FIFO 테스트 메시지입니다.") 