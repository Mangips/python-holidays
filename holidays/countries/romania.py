# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO, FR

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, \
    OCT, \
    NOV, DEC
from holidays.holiday_base import HolidayBase


class Romania(HolidayBase):

    def __init__(self, **kwargs):
        self.country = 'RO'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, JAN, 1)] = "New Year's Day"
        self[date(year, JAN, 2)] = "Day after New Year's Day"
        self[date(year, JAN, 24)] = "Unification Day"
        if year >= 2018:
            self[easter(year) - rd(weekday=FR)] = "Orthodox Good Friday"
        self[easter(year)] = "Orthodox Easter Day"
        self[easter(year) + rd(weekday=MO)] = "Orthodox Easter Monday"
        self[date(year, MAY, 1)] = "Labor Day"
        self[easter(year) + rd(days=50)] = 'Orthodox Pentecost'
        self[easter(year) + rd(days=51)] = 'Orthodox Pentecost Monday'
        self[date(year, AUG, 15)] = "St Mary's Day"
        self[date(year, NOV, 30)] = "St Andrew's Day"
        self[date(year, DEC, 1)] = "National holiday"
        self[date(year, DEC, 25)] =	"Christmas Eve"
        self[date(year, DEC, 25)] = "Christmas Day"
        self[date(year, DEC, 26)] = "Second day of Christmas"
        self[date(year, DEC, 31)] = "New Year's Eve"
        
class RO(Romania):
    pass
    
class ROM(Romania):
    pass
