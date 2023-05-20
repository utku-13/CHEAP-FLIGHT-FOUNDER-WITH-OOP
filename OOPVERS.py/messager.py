from twilio.rest import Client

ACCOUNT_SID = "AC7ccc7e2a92ee8d457474decef65bfc4d"
AUTH_TOKEN = "c470a8b755084a3263e99e493ca0d114"

TW_NUM = "+12546154628"
MY_NUM = "+905332088834"
class Message:
    def message(self, bodyy):
        client = Client(ACCOUNT_SID,AUTH_TOKEN)
        message = client.messages \
                            .create(
                        body=bodyy,
                        from_=TW_NUM,
                        to=MY_NUM,
                        )
        print(message.sid)
        