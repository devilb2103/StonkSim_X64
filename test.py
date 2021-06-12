from mailjet_rest import Client
import os

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
          "Email": "devbhanushali21@gmail.com",
          "Name": "stonksim"
        }
      ],
      "Subject": "Greetings from StonkSim.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to myass!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())