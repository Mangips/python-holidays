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


class Latvia(HolidayBase):

    def __init__(self, **kwargs):
        self.country = 'LV'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, JAN, 1)] = "New Year's Day"
        self[easter(year) - rd(weekday=FR)] = "Good Friday"
        self[easter(year)] = "Easter Sunday"
        self[easter(year) + rd(weekday=MO)] = "Easter Monday"
        self[date(year, MAY, 1)] = "Labor Day"
        self[date(year, MAY, 4)] = "Independence Restoration Day"
        self[date(year, MAY, 10)] = "Mothers' Day"
        self[easter(year) + rd(days=50)] = 'Whitsunday'
        self[date(year, JUN, 23)] = "Midsummer Eve"
        self[date(year, JUN, 24)] = "Midsummer Day"
        self[date(year, NOV, 18)] = "Republic of Latvia Proclamation Day"
        self[date(year, DEC, 25)] =	"Christmas Eve"
        self[date(year, DEC, 25)] = "Christmas Day"
        self[date(year, DEC, 26)] = "Second day of Christmas"
        self[date(year, DEC, 31)] = "New Year's Eve"
        
class LV(Latvia):
    pass

class LVA(Latvia):
    pass