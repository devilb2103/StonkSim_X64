import random
import string
from validate_email import validate_email
from mailjet_rest import Client

class mailFunctions():

    def checkMailID(self, email):
        cleanEmail = str(email).rstrip(" ")
        cleanEmail = str(cleanEmail).lstrip(" ")
        return(validate_email(email_address=cleanEmail, check_format=True, check_blacklist=False, check_dns=True, dns_timeout=10, check_smtp=False, smtp_timeout=10))
    
    def generateVerificationCode(self):
        code = "".join(random.choices(string.digits + string.ascii_uppercase, k=8))
        return(code)
    
    def sendVerificationMail(self, username, targetMailID, code):
        api_key = 'd6904e7bd3a00b4e8e4242357ff46812'
        api_secret = '13bc15d6b759688f52d701a36d5c0923'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
            'Messages': [
                {
                "From": {
                    "Email": "thestonksimbot@gmail.com",
                    "Name": "TheStonkSimBot"
                },
                "To": [
                    {
                    "Email": f"{targetMailID}",
                    "Name": f"{username}"
                    }
                ],
                "Subject": "Greetings from StonkSim.",
                "TextPart": "",
                "HTMLPart": f"<h4>A forgot password request was recieved from username: {username}, and your verification code is:<h4><h3>{code}</h3><br/>"
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print("mail status: " + result.json()["Messages"][0]["Status"])
        return(code)

if __name__ == '__main__':
    print(mailFunctions.generateVerificationCode(mailFunctions))
    