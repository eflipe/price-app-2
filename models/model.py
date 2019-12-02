from abc import ABCMeta, abstractmethod

from common.database import Database


class Model(metaclass=ABCMeta):
    collection = str
    _id = str

    def __init__(self, *args, **kwargs):
        pass

    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})

    @classmethod
    def get_by_id(cls, _id: str):
        return cls(**Database.find_one(cls.collection, {"_id": _id}))

    @classmethod
    def get_by_email(cls, email: str):

        return cls(**Database.find_one(cls.collection, {"email": email}))

    @abstractmethod
    def json(self):
        raise NotImplementedError

    @classmethod
    def all(cls):
        elements_from_db = Database.find(cls.collection, {})
        return [cls(**elem) for elem in elements_from_db]

    @classmethod
    def find_one_by(cls, attribute, value):


        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls, attribute, value):
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]