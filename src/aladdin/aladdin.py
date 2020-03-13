import requests
from fastapi import FastAPI
from lorem.text import TextLorem
from consul import Consul


def register_to_consul():
    consul = Consul(host="3.17.67.170", port=8500)

    agent = consul.agent

    service = agent.service

    service.register("aladdin", service_id="aladdin",
                     address='localhost', port=8010)


def get_service(service_id):
    consul = Consul(host="3.17.67.170", port=8500)

    agent = consul.agent

    service_list = agent.services()

    service_info = service_list[service_id]

    return service_info['Address'], service_info['Port']


app = FastAPI()

register_to_consul()


@app.get("/")
def index():
    return "Usage "  # TODO


@app.get("/gary")
def get_gary():
    address, port = get_service("gary")
    meow = requests.get(f"http://{address}:{port}/meow")
    return meow.json()


@app.get("/spongebob")
def get_spongebob():
    address, port = get_service("gary")
    spongebob = requests.get(f"http://{address}:{port}/spongebob")
    return spongebob.json()


@app.get("/sentence")
def get_sentence(word_separator=' ', sentence_separator=' ', paragraph_separator='\n\n',
                 sentence_range=(4, 8), paragraph_range=(5, 10), text_range=(3, 6),
                 words=None):
    lorem = TextLorem(wsep=word_separator,
                      ssep=sentence_separator,
                      psep=paragraph_separator,
                      srange=sentence_range,
                      prange=paragraph_range,
                      trange=text_range,
                      words=words)

    return {"sentence": lorem.sentence()}


@app.get("/paragraph")
def get_paragraph(word_separator=' ', sentence_separator=' ', paragraph_separator='\n\n',
                  sentence_range=(4, 8), paragraph_range=(5, 10), text_range=(3, 6),
                  words=None):
    lorem = TextLorem(wsep=word_separator,
                      ssep=sentence_separator,
                      psep=paragraph_separator,
                      srange=sentence_range,
                      prange=paragraph_range,
                      trange=text_range,
                      words=words)

    return {"paragraph": lorem.paragraph()}


@app.get("/text")
def get_text(word_separator=' ', sentence_separator=' ', paragraph_separator='\n\n',
             sentence_range=(4, 8), paragraph_range=(5, 10), text_range=(3, 6),
             words=None):
    lorem = TextLorem(wsep=word_separator,
                      ssep=sentence_separator,
                      psep=paragraph_separator,
                      srange=sentence_range,
                      prange=paragraph_range,
                      trange=text_range,
                      words=words)

    return {"text": lorem.text()}
