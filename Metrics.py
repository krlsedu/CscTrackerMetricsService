class Metrics:
    def __init__(self):
        self.map_metrics = {}

    def get_metrics(self):
        metrics = ""
        for metric_name in self.map_metrics:
            metric_ = self.map_metrics[metric_name]
            metric_id = "{application=\"" + str(metric_['metric']['appName']) + "\"" \
                        + ", method=\"" + str(metric_['metric']['method']) + "\"" \
                        + ", class=\"" + str(metric_['metric']['fullClassName']) + "\"" \
                        + "} "
            metrics += "execution_time_seconds_sum" + metric_id + str(metric_['sum'] / 1000) + "\n"
            metrics += "execution_time_seconds_avg" + metric_id + str(metric_['avg'] / 1000) + "\n"
            metrics += "execution_time_seconds_max" + metric_id + str(metric_['max'] / 1000) + "\n"
            metrics += "execution_time_seconds_count" + metric_id + str(metric_['count']) + "\n"
        return metrics

    def add_metric(self, metric):
        metric_name = metric['appName'] + "_" + \
                      metric['fullClassName'] + "_" + metric['method']
        metric_name = metric_name.replace(".", "_").lower()
        if metric_name in self.map_metrics:
            metrics = self.map_metrics[metric_name]
            metrics['sum'] += metric['executionTime']
            metrics['count'] += 1
            metrics['avg'] = metrics['sum'] / metrics['count']
            metrics['max'] = max(metrics['max'], metric['executionTime'])
            metrics['min'] = min(metrics['min'], metric['executionTime'])
            metrics['last'] = metric['executionTime']
            metrics['metric'] = metric
            self.map_metrics[metric_name] = metrics
        else:
            metrics = {'sum': metric['executionTime'], 'count': 1, 'avg': metric['executionTime'],
                       'max': metric['executionTime'], 'min': metric['executionTime'],
                       'last': metric['executionTime'],
                       'metric': metric}
            self.map_metrics[metric_name] = metrics
