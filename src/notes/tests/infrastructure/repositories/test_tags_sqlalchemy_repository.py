from uuid import uuid4
import pytest

from notes.domain.entities import Tag
from notes.infrastructure.repositories import TagsSqlAlchemyRepository


pytestmark = pytest.mark.usefixtures('mappers')


def test_tags_sqlalchemy_repository_can_save_a_tag(session, faker):
    tag_id = uuid4()
    tag_name = faker.pystr()
    tag = Tag(id=tag_id, name=tag_name)

    repository = TagsSqlAlchemyRepository(session)
    repository.save(tag)
    session.commit()

    rows = list(session.execute('SELECT id, name FROM "tags"'))

    assert rows == [(tag_id, tag_name)]
