# Service Registry & Discovery using Consul

## Registry

```python
consul = Consul(host="consul", port=consul_port)
```
Where
- `consul` in `host="consul"` is the hostname of the container running consul server.
- `consul_port` in `port=consul_port` is 8500 (the default consul port).

<br />

```python
check = Check.http(f"http://{ip}:{service_port}/", interval="10s", timeout="5s", deregister="1s")
```
Where
- `ip` is the current service address (which we are registering).
- `service_port` is the current service port.
- Ending the url with simply `/` means it will check the default url.
    - So we should have something like this in fast api code:
    ```python
    @app.get("/")
    def index():
        return "Service1"
    ```
- `interval="10s"` means that the health check will occur each 10 seconds.
- `timeout="5s` 5 seconds is the response timeout.
- `deregister="1s"` after how much time will the service go from 'critical state' to 'deregistered'.
    - Note however that consul takes a minimum of around 1 minute to perform such action.
    - So putting anything less than that won't change consul's default.
- Check more details [in the official consul docs](https://www.consul.io/api/agent/check.html#parameters-1).

<br />

```python
service.register(service_name, service_id=service_name, address=ip, port=service_port, check=check)
```
Where
- `service_name` is the service name and id so it should be unique.
- `ip` is the same we used in the check, that is, the current service address.
- `service_port`, same story for this one.
- `check` is the check we created earlier.

### Note
- To get the local ip address (which we do in `get_ip()`) we use a configuration file.
- If you plan on using this only inside docker, then you can simply use `eth0` as a network interface.
- In windows it is different so we provide a config file but it won't work on your device as it is different in every machine.

## Discovery

```python
service_list = agent.services()
service_info = service_list[service_id]
```
- `agent.services()` returns the registered services.
- `service_id` is the service we are searching for its address and port (or other details).

```python
return service_info['Address'], service_info['Port']
```
- Since `service_info` is `dict` object so we can get the response details as shown.
- Other attributes that can be used can be found in the [official docs](https://www.consul.io/api/agent/service.html#sample-response-1).

## Building it

```commandline
docker-compose up -d
```
We suggest using the simple docker compose file.

If you want to use python consul in your project, here is how you can do it:

- First you need to use `pip freeze > requirements.txt` to add the dependencies.
    - Note that we did this in a virtual environment so we only had the dependencies we used in the project.
- We provide a Dockerfile which copies the needed files and runs the app using uvicorn.
- To build it into a docker image use `docker build . -t service-name`.
- Don't forget to change the service name in the docker compose file with your image.

## Consul UI (Dashboard)
- Available on [localhost:8500/ui/](http://localhost:8500/ui/).
- Here you can see all the services and their health status.

## Endpoints
We host
- service1 on [localhost:8010](http://localhost:8010/).
- service2 on [localhost:8020](http://localhost:8020/).

### Service1 Endpoints
- `/` index page, used by the health check.
- `/sentence-dependent` calls service2 using consul.
- `/sentence-independent` gets called by service2 using consul.

### Service2 Endpoints
- `/` index page, used by the health check.
- `/text` calls service1 using consul.
- `/words` gets called by service1 using consul.
