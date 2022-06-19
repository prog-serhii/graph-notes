from uuid import uuid4

from notes.domain.entities import Note


def test_note_string_representation(faker):
    note_id = uuid4()
    note = Note(note_id, faker.pystr(), faker.sentence())

    assert str(note) == f'Note {note_id}'


def test_note_representation(faker):
    note_id = uuid4()
    title = faker.pystr()
    content = faker.sentence()
    note = Note(note_id, title, content)

    expected_representation = (
        f'<Note id={note_id}, title={title}, content={content}, tags=[]>'
    )
    assert repr(note) == expected_representation


def test_note_hash(faker):
    note_id = uuid4()
    note = Note(note_id, faker.pystr(), faker.sentence())

    assert hash(note) == hash(note_id)


def test_notes_with_the_same_content_are_not_equal(faker):
    title = faker.pystr()
    content = faker.sentence()

    note_1 = Note(uuid4(), title, content)
    note_2 = Note(uuid4(), title, content)

    assert note_1 != note_2


def test_notes_with_the_same_id_and_different_content_are_equal(faker):
    note_id = uuid4()

    note_1 = Note(note_id, faker.unique.pystr(), faker.unique.sentence())
    note_2 = Note(note_id, faker.unique.pystr(), faker.unique.sentence())

    assert note_1 == note_2


def test_notes_with_same_id_and_content_but_different_types_are_note_equal(
    faker
):
    note_id = uuid4()
    title = faker.pystr()
    content = faker.sentence()

    assert Note(note_id, title, content) != (note_id, title, content)


def test_can_add_tag_if_its_is_not_added(faker):
    note = Note(uuid4(), faker.pystr(), faker.sentence())

    assert note.can_add_tag(uuid4())


def test_cannot_add_tag_if_its_is_added(faker):
    tag_id = uuid4()

    note = Note(uuid4(), faker.pystr(), faker.sentence())
    note.tags = [tag_id]

    assert note.can_add_tag(tag_id) is False


def test_add_not_added_tag(faker):
    tag_id = uuid4()
    note = Note(uuid4(), faker.pystr(), faker.sentence())

    note.add_tag(tag_id)

    assert note.tags == [tag_id]


def test_add_already_added_tag(faker):
    tag_id = uuid4()
    note = Note(uuid4(), faker.pystr(), faker.sentence())

    note.add_tag(tag_id)
    note.add_tag(tag_id)

    assert note.tags == [tag_id]


def test_can_remove_tag_if_its_is_added(faker):
    tag_id = uuid4()

    note = Note(uuid4(), faker.pystr(), faker.sentence())
    note.tags = [tag_id]

    assert note.can_remove_tag(tag_id)


def test_cannot_remove_tag_if_its_is_not_added(faker):
    tag_id = uuid4()

    note = Note(uuid4(), faker.pystr(), faker.sentence())

    assert note.can_remove_tag(tag_id) is False


def test_remove_already_added_tag(faker):
    tag_id = uuid4()

    note = Note(uuid4(), faker.pystr(), faker.sentence())
    note.remove_tag(tag_id)

    assert note.tags == []


def test_remove_not_added_tag(faker):
    tag_id = uuid4()

    note = Note(uuid4(), faker.pystr(), faker.sentence())
    note.tags = [tag_id]
    note.remove_tag(uuid4())

    assert note.tags == [tag_id]
