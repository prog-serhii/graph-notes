import uuid

from sqlalchemy import Column, ForeignKey, MetaData, String, Table, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper, relationship

from notes.domain.entities.note import Note
from notes.domain.entities.tag import Tag
from notes.domain.entities.user import User

metadata = MetaData()


tags = Table(
    'tags', metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('name', String(255))
)

notes = Table(
    'notes', metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('title', String(255)),
    Column('content', Text)
)

tag_to_note = Table(
    'tag_to_note', metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('note_id', ForeignKey('notes.id')),
    Column('tag_id', ForeignKey('tags.id'))
)

users = Table(
    'users', metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
)

tag_to_user = Table(
    'tag_to_user', metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('tag_id', ForeignKey('tags.id')),
    Column('user_id', ForeignKey('users.id'))
)

note_to_user = Table(
    'note_to_user', metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('note_id', ForeignKey('notes.id')),
    Column('user_id', ForeignKey('users.id'))
)


def start_mappers() -> None:
    tags_mapper = mapper(Tag, tags)
    notes_mapper = mapper(Note, notes)
    mapper(
        Note, notes,
        properties={
            'tags': relationship(
                tags_mapper, secondary=tag_to_note, collection_class=list
            )
        }
    )
    mapper(
        User, users,
        properties={
            'tags': relationship(
                tags_mapper, secondary=tag_to_user, collection_class=list
            ),
            'notes': relationship(
                notes_mapper, secondary=note_to_user, collection_class=list
            )
        }
    )
