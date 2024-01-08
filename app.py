from csctracker_py_core.starter import Starter

from Metrics import Metrics

starter = Starter()
app = starter.get_app()
http_repository = starter.get_http_repository()

service_metrics = Metrics()


@app.route('/services-metrics', methods=['GET'])
def get_metrics():
    get_metrics = service_metrics.get_metrics()
    return str(get_metrics), 200, {'Content-Type': 'text/plain'}


@app.route('/metric', methods=['POST'])
def post_metrics():
    json = http_repository.get_json_body()
    service_metrics.add_metric(json)
    return 'ok', 201, {'Content-Type': 'text/plain'}


starter.start()
