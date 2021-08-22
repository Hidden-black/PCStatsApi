from flask import Flask, jsonify
import psutil

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/cpuusage', methods=['GET'])
def cpuusage():
    try:
        return jsonify({
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
            'data': psutil.virtual_memory()[2]
        }), 200
    except:
        return jsonify({
            'data': "Error!"
        }),500