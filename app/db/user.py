from sqlalchemy.orm import sessionmaker
import uuid

from app.main import engine
from app.models.account import Account

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(user_email):
    return Account.query\
        .filter_by(email = user_email)\
        .first()

def get_user_by_public_id(public_id):
    return Account.query\
                .filter_by(public_id = public_id)\
                .first()

def create_user_account(username, email):
    # database ORM object
    account = Account(
        public_id = str(uuid.uuid4()),
        username = username,
        email = email
    )
    # insert account
    get_db().session.add(account)
    get_db().session.commit()
