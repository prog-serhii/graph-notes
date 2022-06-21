import abc

from notes.domain.entities import User
from notes.domain.value_objects import UserID


class UsersAbstractRepository(abc.ABC):

    @abc.abstractclassmethod
    def get(self, user_id: UserID) -> User:
        raise NotImplementedError

    @abc.abstractclassmethod
    def save(self, user: User) -> None:
        raise NotImplementedError
