from twilio.rest import Client
import datetime

def main():
    account_sid = 'ACCOUNT_SID'
    auth_token = 'AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    numbers=['+353871234567', '+353871234567']
    bins=['Waste', 'Recycling']
    
    # Get the current week number of the year at runtime 
    week_number=datetime.datetime.utcnow().isocalendar()[1]    
    
    # Recycling bin is collected on the even week. Waste on the odd week
    if week_number % 2 == 0:
        bin=bins[1]
    else:
        bin=bins[0]

    try:
        for number in numbers:
            message = client.messages \
                .create(
                     body="Bin reminder: %s bin will be collected tomorrow" % bin,
                     from_='ACCOUNT_PHONE_NUMBER',
                     to=number
                 )
        print("Message(s) sent successfully")
        print(message.sid)

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    main()
