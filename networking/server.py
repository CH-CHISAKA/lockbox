from flask import Flask, request, jsonify
import socket
import os

app = Flask(__name__)

# For persistent storage, consider using a database or Redis.
# For now, we'll use a simple in-memory solution.
message_store = {}

# @app.route('/receive', methods=['POST'])
# def receive():
#     try:
#         data = request.get_json()
#         encrypted_msg = data.get('encrypted_msg', '')
        
#         if not encrypted_msg:
#             return jsonify({"error": "Missing encrypted_msg"}), 400

#         # Here, for simplicity, we store it in-memory; you may want to store it in a DB.
#         message_store['encrypted_msg'] = encrypted_msg
#         return 'Received', 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/receive', methods=['POST'])
def receive():
    try:
        print(f"🔔 Incoming request: {request.json}")
        data = request.get_json()
        encrypted_msg = data.get('encrypted_msg', '')
        
        if not encrypted_msg:
            print("❌ Missing encrypted_msg")
            return jsonify({"error": "Missing encrypted_msg"}), 400

        message_store['encrypted_msg'] = encrypted_msg
        print("✅ Message received and stored.")
        return 'Received', 200
    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/get_message', methods=['GET'])
def get_message():
    try:
        encrypted_msg = message_store.get('encrypted_msg', None)
        
        if encrypted_msg is None:
            return jsonify({"message": "No message stored"}), 404
        
        return jsonify({'encrypted_msg': encrypted_msg}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/whoami', methods=['GET'])
def whoami():
    try:
        # Returns the device's hostname as the device name
        device_name = socket.gethostname()
        return jsonify({'device_name': device_name}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Setting a production config for better performance
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False  # Turn off debugging in production
    
    # Set a proper host and port, if needed
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    app.run(host=host, port=port, threaded=True)  # Enable threading for concurrent requests
