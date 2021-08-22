from flask import Flask, jsonify
import psutil

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/cpuusage', methods=['GET'])
def cpuusage():
    try:
        return jsonify({
            #Reports the % of cpu being used.
            'data': psutil.cpu_percent()
        }), 200
    except:
        return jsonify({
            'data': "Error!"
        }), 500

@app.route('/ramusage', methods=['GET'])
def ramusage():
    try:
        return jsonify({
            # The [2] just reports the % of ram being used.
            'data': psutil.virtual_memory()[2]
        }), 200
    except:
        return jsonify({
            'data': "Error!"
        }),500


@app.route('/temps', methods=['GET'])
def temps():
    try:
        return jsonify({
            # Reports the cpu's temperature.
            'data': psutil.sensors_temperatures()[0]
        }), 200
    except:
        return jsonify({
            'data': "Error!"
        }),500