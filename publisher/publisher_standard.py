import os
from dotenv import load_dotenv
import boto3

load_dotenv()  # .env 파일 로드

# SNS 클라이언트 생성
sns = boto3.client('sns', region_name='ap-northeast-2')
topic_arn = os.getenv('SNS_STANDARD_TOPIC_ARN')

def publish_message(message_body):
    response = sns.publish(
        TopicArn=topic_arn,
        Message=message_body
    )
    print("메시지 발행 완료:", response.get('MessageId'))

if __name__ == "__main__":
    publish_message("안녕하세요! SNS Standard 테스트 메시지입니다.") 