from fastapi import FastAPI
from lorem.text import TextLorem


def register_to_consul():
    import consul

    consul = consul.Consul(host="3.17.67.170", port=8500)

    agent = consul.agent

    service = agent.service

    # first fast api app
    service.register("gary", service_id="gary",
                     address='localhost', port=8020)


app = FastAPI()

register_to_consul()


@app.get("/")
def index():
    return "Meow"


@app.get("/meow")
def meow():
    return {"Gary": "meow"}


@app.get("/spongebob")
def spongebob():
    return {"Spongebob": "I'm ready"}
