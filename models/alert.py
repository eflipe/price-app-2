import uuid
from dataclasses import dataclass, field
from common.database import Database
from libs.mailgun import Mailgun
from models.item import Dolar
from models.model import Model
from models.user import User


@dataclass(eq=False)
class Alert(Model):
    collection: str = field(init=False, default="alerts")
    name: str
    item_id: str
    price_limit: float
    user_email: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Dolar.get_by_id(self.item_id)
        self.user = User.find_by_email(self.user_email)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "price_limit": self.price_limit,
            "item_id": self.item_id,
            "user_email": self.user_email
        }

    def load_item_price(self):
        self.item.buscar_precio()
        return self.item.precio_dolar

    def notify_if_price_reached(self):
        print(self.item.precio_dolar)
        print(self.price_limit)
        if self.item.precio_dolar > self.price_limit:
            print(f' Alerta: el precio subiò de {self.price_limit}. El valor actual es de {self.item.precio_dolar}')
            Mailgun.send_mail(
                ['infelipe@yandex.ru'],
                f'Hello, notificacion de {self.name}',
                f'Alerta: el precio subiò de {self.price_limit}. El valor actual es de {self.item.precio_dolar}',
                f'<p>Your alert {self.name} has reached a price subiò {self.price_limit}.</p><p>El precio actual es de {self.item.precio_dolar}. Check your item out <a href="{self.item.url}>here</a>.</p>',
                       )
