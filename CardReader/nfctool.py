import sys
import datetime
import json
from flask import Flask

app = Flask(__name__)

@app.route("/readcard")
def read_card():
    r = readers()
    if len(r) < 1:
        return "Error: No readers available!"

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    cmd = "getuid"
    if cmd == "getuid":
        COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00]
    else:
        return "Error: Undefined command: " + cmd

    data, sw1, sw2 = connection.transmit(COMMAND)
    if (sw1, sw2) == (0x90, 0x0):
        DT = datetime.datetime.now()
        date_time = DT.strftime("%m/%d/%Y, %H:%M:%S")
        figure = 4
        record = {
            "getuid": toHexString(data),
            "date": date_time,
            "amount": figure
        }
        result = json.dumps(record)
        print(result)
        with open('../pages/transaction_data.json', 'w') as json_file:
            json_file.write(result)  # Write the JSON string directly
        return result

    elif (sw1, sw2) == (0x63, 0x0):
        return "Error: The operation failed."
    else:
        return "Error: Unknown error occurred."

if __name__ == "__main__":
    from smartcard.System import readers
    from smartcard.util import toHexString
    from smartcard.ATR import ATR
    from smartcard.CardType import AnyCardType

    app.run()
