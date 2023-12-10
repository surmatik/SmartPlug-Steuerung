from flask import Flask, render_template, jsonify
from pyW215.pyW215 import SmartPlug, ON, OFF

app = Flask(__name__)

# Erstelle Instanzen der Smart Plugs für Lampe 1 und Lampe 2
sp_lampe1 = SmartPlug('192.168.1.31:', '740169')
sp_lampe2 = SmartPlug('192.168.1.32:', '397381')

# Funktionen zum Ein- und Ausschalten der Lampen
def turn_on(plug):
    plug.state = ON

def turn_off(plug):
    plug.state = OFF

# Routen für die Web-Seiten
@app.route('/')
def index():
    return render_template('index.html')

# Routen zum Steuern von Lampe 1
@app.route('/on_lampe1', methods=['POST'])
def switch_on_lampe1():
    turn_on(sp_lampe1)
    return jsonify({'status': 'Lampe 1 eingeschaltet'})

@app.route('/off_lampe1', methods=['POST'])
def switch_off_lampe1():
    turn_off(sp_lampe1)
    return jsonify({'status': 'Lampe 1 ausgeschaltet'})

# Routen zum Steuern von Lampe 2
@app.route('/on_lampe2', methods=['POST'])
def switch_on_lampe2():
    turn_on(sp_lampe2)
    return jsonify({'status': 'Lampe 2 eingeschaltet'})

@app.route('/off_lampe2', methods=['POST'])
def switch_off_lampe2():
    turn_off(sp_lampe2)
    return jsonify({'status': 'Lampe 2 ausgeschaltet'})

if __name__ == '__main__':
    app.run(debug=True)
