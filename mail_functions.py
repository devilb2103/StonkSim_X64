import random
import string
from mailjet_rest import Client

class mailFunctions():

    def checkMailID(self, email):
        return True
    
    def generateVerificationCode(self):
        code = "".join(random.choices(string.digits + string.ascii_uppercase, k=8))
        return(code)
    
    def sendVerificationMail(self, username, targetMailID, code):
        api_key = '9e64d676b099b1ada3532e3a5e87276c'
        api_secret = 'de24dd36a1f0f736077e77b16f76f048'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
            'Messages': [
                {
                "From": {
                    "Email": "stonksimbot@gmail.com",
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
    