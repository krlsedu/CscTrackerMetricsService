from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

from Metrics import Metrics

app = Flask(__name__)

service_metrics = Metrics()
metrics = PrometheusMetrics(app, group_by='endpoint')


@app.route('/services-metrics', methods=['GET'])
def get_metrics():
    get_metrics = service_metrics.get_metrics()
    return str(get_metrics), 200, {'Content-Type': 'text/plain'}


@app.route('/metric', methods=['POST'])
def post_metrics():
    json = request.get_json()
    print(json)
    service_metrics.add_metric(json)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
