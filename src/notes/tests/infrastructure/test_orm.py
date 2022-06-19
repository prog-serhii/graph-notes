from uuid import uuid4

import pytest

from notes.domain.entities import Note, Tag, User


pytestmark = pytest.mark.usefixtures('mappers')


def test_users_mapper_can_load_lines(session):
    user_1_id = uuid4()
    user_2_id = uuid4()
    user_3_id = uuid4()

    session.execute(
        'INSERT INTO users (id) VALUES (:id)',
        [{'id': user_1_id}, {'id': user_2_id}, {'id': user_3_id}]
    )
    expected = [User(id=user_1_id), User(id=user_2_id), User(id=user_3_id)]

    assert session.query(User).all() == expected

def test_users_mapper_can_save_lines(session):
    new_user_id = uuid4()
    new_user = User(id=new_user_id)

    session.add(new_user)
    session.commit()

    rows = list(session.execute('SELECT id FROM "users"'))

    assert rows == [(new_user_id)]


def test_tags_mapper_can_load_lines(session, faker):
    tag_1_id = uuid4()
    tag_1_name = faker.unique.pystr()

    tag_2_id = uuid4()
    tag_2_name = faker.unique.pystr()

    tag_3_id = uuid4()
    tag_3_name = faker.unique.pystr()

    session.execute(
        'INSERT INTO tags (id, name) VALUES (:id, :name)',
        [
            {'id': tag_1_id, 'name': tag_1_name},
            {'id': tag_2_id, 'name': tag_2_name},
            {'id': tag_3_id, 'name': tag_3_name}
        ]
    )
    expected = [
        Tag(tag_1_id, tag_1_name),
        Tag(tag_2_id, tag_2_name),
        Tag(tag_3_id, tag_3_name)
    ]

    assert session.query(Tag).all() == expected


# def test_tags_mapper_can_save_lines(session, faker):
#     pass

def test_notes_mappers_can_load_lines(session, faker):
    tag_1_data = {'id': uuid4(), 'name': faker.unique.pystr()}
    tag_1 = Tag(**tag_1_data)

    tag_2_data = {'id': uuid4(), 'name': faker.unique.pystr()}
    tag_2 = Tag(**tag_2_data)

    note_1_data = {
        'id': uuid4(),
        'title': faker.unique.pystr(),
        'content': faker.unique.sentence()
    }
    note_1 = Note(**note_1_data)
    note_1.add_tag(tag_1_data['id'])
    note_1.add_tag(tag_2_data['id'])

    note_2_data = {
        'id': uuid4(),
        'title': faker.unique.pystr(),
        'content': faker.unique.sentence()
    }
    note_2 = Note(**note_2_data)
    note_2.add_tag(tag_1_data['id'])

    note_3_data = {
        'id': uuid4(),
        'title': faker.unique.pystr(),
        'content': faker.unique.sentence()
    }
    note_3 = Note(**note_3_data)
    note_3.add_tag(tag_2_data['id'])

    session.execute(
        'INSERT INTO notes (id, title, content) VALUES (:id, :title, :content)',
        [note_1_data, note_2_data, note_3_data]
    )

    session.execute(
        'INSERT INTO tags (id, name) VALUES (:id, :name)',
        [tag_1_data, tag_2_data]
    )

    session.execute(
        'INSERT INTO tag_to_note (note_id, tag_id) VALUES (:note_id, :tag_id)',
        [
            {'note_id': note_1_data['id'], 'tag_id': tag_1_data['id']},
            {'note_id': note_1_data['id'], 'tag_id': tag_2_data['id']},
            {'note_id': note_2_data['id'], 'tag_id': tag_1_data['id']},
            {'note_id': note_3_data['id'], 'tag_id': tag_2_data['id']}
        ]
    )

    assert session.query(Note).all() == [note_1, note_2, note_3]
    assert session.query(Note).get(note_1_data['id']).tags == [tag_1, tag_2]
    assert session.query(Note).get(note_2_data['id']).tags == [tag_1]
    assert session.query(Note).get(note_3_data['id']).tags == [tag_2]

# def test_notes_mapper_can_save_lines(session, faker):
#     session.execute()
