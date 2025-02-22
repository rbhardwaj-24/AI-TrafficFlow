from flask import Flask, jsonify
from flask_cors import CORS
from ai_model import TrafficAI
from simulator import simulate_traffic
 
app = Flask(__name__)
CORS(app)
 
traffic_ai = TrafficAI()
 
@app.route('/get_traffic', methods=['GET'])
def get_traffic():
    traffic_data = simulate_traffic()
    light_times = {i: traffic_ai.predict_light_time(traffic_data[i]) for i in traffic_data}
    return jsonify({"traffic_data": traffic_data, "light_times": light_times})
 
if __name__ == '__main__':
app.run(debug=True)