import time 
from flask import Flask
from flask_cors import CORS
import pulse as p

app = Flask(__name__)
CORS(app)

@app.route('/<string:uid>')
def view_heartrate(uid):
    pulse = p.Pulse()
    pulse.pulsebox_to_frames(uid)
    hr = pulse.bpm()
    return f'{hr}bpm'



@app.route('/api/time')
def get_current_time():
    return (f'time: {time.time()}')
