import logging
from sqlalchemy.orm import scoped_session, Session, sessionmaker
from sqlalchemy.engine.base import Engine
from core.db_models.engine import engine as db_engine
from contextlib import contextmanager

log = logging.getLogger(__name__)


def create_scoped_session_for_engine(engine: Engine):
    return scoped_session(
        sessionmaker(autoflush=False, bind=engine)
    )


DBSession = create_scoped_session_for_engine(db_engine)


def create_db_session() -> Session:
    return DBSession()


@contextmanager
def create_autocommit_session() -> Session:
    session = create_db_session()
    try:
        yield session
        session.commit()
    except BaseException as e:
        log.error(e)
        session.rollback()
        raise e
    finally:
        session.close()
