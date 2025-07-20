import psutil
from flask import Flask, jsonify  

app = Flask(__name__)

@app.route('/metrics')
def system_metrics():
    cpu = psutil.cpu_percent(interval=1)  
    memory = psutil.virtual_memory().percent

    print(f"CPU Utilization: {cpu}%")
    print(f"Memory Utilization: {memory}%")

    return jsonify({
        'cpu_percent': cpu,
        'memory_percent': memory
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5276)
