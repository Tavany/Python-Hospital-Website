from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Table,
    Integer,
    String,
    text,
    )

from sqlalchemy.engine import Engine
from typing import List, Optional, Union

from sqlalchemy import create_engine

def get_engine():
    username = "root"
    hostname = "127.0.0.1"
    password = ""
    database_name = "medicare-db"

    database_url = f"mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}"

    engine = create_engine(database_url)

    return engine


def create_table(engine):
    metadata = MetaData()

    metadata.create_all(engine)

def run_query(query: Union[str, text], commit: bool = False) -> Optional[List[dict]]:

    engine = get_engine()

    if isinstance(query, str):
        query = text(query)

    with engine.connect() as conn:
        if commit:
            conn.execute(query)
            conn.commit()
            return None
        else:
            result_proxy = conn.execute(query)
            result_set = result_proxy.fetchall()
            return [dict(row) for row in result_set]
