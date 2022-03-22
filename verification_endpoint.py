from flask import Flask, request, jsonify
from flask_restful import Api
import json
import eth_account
from eth_account.messages import encode_defunct
import algosdk

app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False

@app.route('/verify', methods=['GET','POST'])
def verify():
    content = request.get_json(silent=True)
    #print(type(content))
    print(content)
    #y = json.loads(content)
    #print(y)
    sig = content.get('sig')
    payload = content.get('payload')
    
    platform = payload.get('platform')
    message = payload.get('message')
    pk = payload.get('pk')
    result = False
    if platform == "Ethereum":
        print("Ethereum")
        eth_encoded_msg = eth_account.messages.encode_defunct(json.json_dumps(payload))
        print(type(sig))
        #if eth_account.Account.recover_message(message = encode_defunct(payload),signature=sig) == pk:
        #    result = True
    elif platform == "Algorand":
        pass
    
    #Check if signature is valid
    #result = True #Should only be true if signature validates

    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
