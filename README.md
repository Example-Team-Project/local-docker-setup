# Docker setup

This repository contains a docker-setup for the DVD Rental Quarkus Learning project.

## Parts

* Prometheus
* Grafana
* Elasticsearch
* Fluentd
* Kibana
* PostgreSQL
* [Jaeger](https://www.jaegertracing.io/)
* [NodeExporter](https://github.com/prometheus/node_exporter) - Prometheus exporter for hardware and OS metrics
* [Cadvisor](https://github.com/google/cadvisor) - provides container users an understanding of the resource usage and performance characteristics of their running containers
* [Locust](https://locust.io/) - Python based load test generator
  * master
  * worker
* Zookeeper + Broker for Kafka - TBD

## Problems

There were some issues during setup:

### Jaeger and ulimits

The local setup uses Rancher Desktop on WSL for docker environment, and it was really hard to start Jaeger because it always complained about `too many open files`.

The regular solution is to add the following to the `docker-compose.yaml`:
```yaml
  jaeger:
    ...
    ulimits:
      nofiles:
        soft: 90000
        hard: 90000
```

However, it didn't solve my issue but the [documentation of Rancher Desktop](https://docs.rancherdesktop.io/how-to-guides/increasing-open-file-limit#windows-steps) contains the solution for raising the open file limit.

### Jaeger and Elasticsearch

The current version of Jaeger does not support Elasticsearch 8. Due to this issue the setup doesn't use this connection and leaves Jaeger working with in memory db.


### Locust and host

The `docker-compose.yaml` contains the `--host=http://172.29.233.138:8080` parameter for the `locust` service.

However if the test itself contains the full URL it will work also: 

```python
self.client.get("http://172.29.233.138:18180/api/v1/films")
```

### ELK security

Currently, Elasticsearch and Kibana are used with security turned off. It is easier to set it up locally. 
