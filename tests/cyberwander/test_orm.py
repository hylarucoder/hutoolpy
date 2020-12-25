from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

from cyberwander.orm import Model


class User(Model):
    __tablename__ = "users"

    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )


class Address(Model):
    __tablename__ = "addresses"
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


def test_orm():
    engine = create_engine("sqlite:///:memory:", echo=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    Model.metadata.create_all(engine)
    User._session = session
    Address._session = session
    session.add_all(
        [
            User(name="wendy", fullname="Wendy Williams", nickname="windy"),
            User(name="mary", fullname="Mary Contrary", nickname="mary"),
            User(name="fred", fullname="Fred Flintstone", nickname="freddy"),
        ]
    )
    session.commit()
    assert len(User.query.all()) == 3
