import uuid


import requests
from dataclasses import dataclass, field
from bs4 import BeautifulSoup

from models.model import Model


@dataclass(eq=False)
class Dolar(Model):
    collection: str = field(init=False, default="items")
    url: str
    tag_name: str
    precio_dolar: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def buscar_precio(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        element = soup.select(self.tag_name)
        dolarRava = element[0].getText().strip()
        dolarSplit = dolarRava.split(',')
        dolar = dolarSplit[0].replace(".", "")
        print(dolar)
        self.precio_dolar = float(dolar)
        print(dolar)
        return self.precio_dolar

    def json(self):
        return {
            "_id": self._id,
            "url": self.url,
            "precio_dolar": self.precio_dolar,
            "tag_name": self.tag_name,

        }





