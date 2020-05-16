from app.api.v1 import api_v1

@api_v1.route('/heartbeat', methods=['GET'])
def heartbeat():
    return "I am still alive"