#!/usr/bin/python3 -tt
# -*- coding: utf-8 -*-

__all__ = ['Manager']

from twisted.internet.threads import deferToThread
from twisted.internet import task, reactor
from twisted.python import log

from legitimator.legitimator import Legitimator
class Manager(object):
    def __init__(self, db):
        self.db = db
        self.legitimator = Legitimator(self)

    def get_access(self, cardno):
        return {'Access': self.legitimator.get_access(cardno)}

# vim:set sw=4 ts=4 et:
