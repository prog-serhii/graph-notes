from typing import List

from notes.application.repositories import UsersAbstractRepository
from notes.domain.entities import User
from notes.domain.value_objects import UserID


class UsersSqlAlchemyRepository(UsersAbstractRepository):

    def __init__(self, session) -> None:
        self.session = session

    def get(self, user_id: UserID) -> User:
        return self.session.query(User).filter_by(id=user_id).one()

    def save(self, user: User) -> None:
        self.session.add(user)

    def list(self) -> List[User]:
        return self.session.query(User).all()
