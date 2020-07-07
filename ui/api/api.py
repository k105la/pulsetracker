import os
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import pulse as p

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome_screen():
    return render_template('index.html')

@app.route('/<string:uid>', methods=['GET'])
def view_heartrate(uid):
    pulse = p.Pulse()
    pulse.pulsebox_to_frames(uid)
    hr = pulse.bpm()
    os.system('rm -rf images')
    return jsonify({'pulse': hr})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
