import boto3
from botocore.exceptions import ClientError

class AmazonSES:
    def __init__(self, SENDER, RECIPIENT, SUBJECT, BODY_TEXT, BODY_HTML):
        self.SENDER = SENDER
        self.RECIPIENT = RECIPIENT
        self.AWS_REGION = "us-east-1"
        self.SUBJECT = SUBJECT
        self.BODY_TEXT = BODY_TEXT
        self.BODY_HTML = BODY_HTML
        self.CHARSET = "UTF-8"
        
    def output(self):
        print('This is simple console ouptut')
        self.send()
    
    def send(self):
        print('EMAIL SENT TO ' + self.RECIPIENT + ' FROM ' + self.SENDER)
        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=self.AWS_REGION)

        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self.RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.CHARSET,
                            'Data': self.BODY_HTML,
                        },
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': self.BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': self.SUBJECT,
                    },
                },
                Source=self.SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=CONFIGURATION_SET,
            )
            return True
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
            return False
        else:
            print("Email sent! Message ID:"),
            print(response['ResponseMetadata']['RequestId'])
            return False