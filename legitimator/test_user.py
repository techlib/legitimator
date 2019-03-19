#!/usr/bin/python3
from configparser import ConfigParser
from sys import stderr

from twisted.python import log

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlsoup import SQLSoup

from legitimator import Manager

if __name__ == '__main__':
    def do_start(config):

        log.startLogging(stderr)
        db_url = config.get('database', 'url')
        factory = sessionmaker(autocommit=False, autoflush=False)
        engine = create_engine(db_url)
        session = scoped_session(sessionmaker(
            autocommit=False, autoflush=False))
        db = SQLSoup(engine, session=session)
        manager_opts = dict(config.items('manager'))
        manager_pool = int(manager_opts.pop('pool_size', 2))
        manager = Manager(db, **manager_opts)
