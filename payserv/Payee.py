import json
import urllib.request
from flask import Flask


# Initialize the Flask application
app = Flask(__name__)
app.config['MIN_SJCX'] = 1000
app.config['DATABASE'] = '/db/payserv.db'


class Payee:

    def __init__(self, address):
        self.address = address

    def is_valid_address(self):
        """
        Does simple validation of a bitcoin-like address.
        Source: http://bit.ly/17OhFP5
        param : address : an ASCII or unicode string, of a bitcoin address.
        returns : boolean, indicating that the address has a correct format.
        """

        # The first character indicates the "version" of the address.
        chars_ok_first = "123"
        # alphanumeric characters without : l I O 0
        chars_ok = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

        # We do not check the high length limit of the address.
        # Usually, it is 35, but nobody knows what could happen in the future.
        if len(self.address) < 27:
            return False
        elif self.address[0] not in chars_ok_first:
            return False

        # We use the function "all" by passing it an enumerator as parameter.
        # It does a little optimization :
        # if one of the character is not valid, the next ones are not tested.
        return all((char in chars_ok for char in self.address[1:]))

    def get_addr_data(self):
        """
        Get the raw address data for the address from CounterPartyChain.
        :return: json, Raw data from CounterPartyChain.
        """
        api_url = 'https://counterpartychain.io/api/balances/'
        response = urllib.request.urlopen(api_url + self.address).read().decode("utf-8")
        json_response = json.loads(response)
        return json_response

    def get_balance(self):
        """
        Checks the balance of SJCX on the passed address from CounterPartyChain.
        :return: int, Number of SJCX in the address.
        """
        data = self.get_addr_data()
        if data["success"] == 0:
            return 0
        for asset in data["data"]:
            if asset["asset"] == "SJCX":
                return int(float(asset["amount"]))
        return 0

    def to_db(self):
        pass

    def save(self):
        if self.is_valid_address() or self.get_balance() == app.config['MIN_SJCX']:
            self.to_db()
            return True
        return False