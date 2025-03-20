from sqlalchemy import select
from sqlalchemy.orm import Session

from app.main import engine
from app.models.account import Account

def insert(entity):
    with Session(engine) as session:
        session.add(entity)
        session.commit()

def query_first(stmt):
    with Session(engine) as session:
        return session.execute(stmt).first()

def get_user_by_email(user_email):
    stmt = select(Account) \
                .filter_by(email = user_email)
    
    return query_first(stmt)

def get_user_by_public_id(public_id):
    stmt = select(Account) \
                .filter_by(public_id = public_id)

    return query_first(stmt)

def create_user_account(name, email):
    # database ORM object
    account = Account(
        name = name,
        email = email
    )
    # insert account
    insert(account)
