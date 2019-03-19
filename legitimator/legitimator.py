# -*- coding: utf-8 -*-

__all__ = ['Legitimator']

from datetime import date
from sqlalchemy import *

class Legitimator(object):
    def __init__(self, manager):
        self.manager = manager

    def get_ekv_group(self, cardno):
        users = self.manager.db.entity('users', schema='ntk')
        user = users.filter_by(cardno=cardno).first()

        if user is None:
            return 0

        return user.ekvgroup
	
    def get_access(self, cardno):
        return self.get_ekv_group(cardno) in [40,60,63,64,66,67,70,71,127,128,129,130,132,134,138,139,142,144]


# vim:set sw=4 ts=4 et:
