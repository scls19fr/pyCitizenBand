#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some tools for Citizen Band users

Copyright (C) 2015 by
Sébastien Celles <s.celles@gmail.com>
All rights reserved.

"""

import numpy as np
import pandas as pd
import decimal

class CitizenBand(object):
    """
    A Python class for Citizen Band users

    >>> cb = CitizenBand()
    >>> cb.frequency(19)
    Decimal('27.185')

    >>> cb.frequency(19, 1)
    Decimal('27.635')

    >>> cb.frequency(19, -1)
    Decimal('26.735')

    >>> cb.channel('26.185')
    19
    """

    def __init__(self, bands=None, mask=None):
        self.nb_channels = 40
        self.channels = np.arange(1, self.nb_channels + 1)

        self._frequencies = pd.Series(
            ['26.965', '26.975', '26.985', '27.005', '27.015', '27.025', '27.035', '27.055', '27.065', '27.075', 
             '27.085', '27.105', '27.115', '27.125', '27.135', '27.155', '27.165', '27.175', '27.185', '27.205', 
             '27.215', '27.225', '27.255', '27.235', '27.245', '27.265', '27.275', '27.285', '27.295', '27.305', 
             '27.315', '27.325', '27.335', '27.345', '27.355', '27.365', '27.375', '27.385', '27.395', '27.405'],
            index=self.channels)
        self._frequencies = self._frequencies.map(decimal.Decimal)

        self.band_offset = decimal.Decimal('0.450')

        if bands is None:
            bands = np.array([-2, -1, 0, 1, 2])
            #bands = np.array([-3, -2, -1, 0, 1, 2])
        self.bands = bands

        self._df_freq = pd.DataFrame(index=self.channels)

        for band in bands:
            self._df_freq[band] = self._frequencies + band * self.band_offset

        if mask is None:
            mask = self._df_freq < decimal.Decimal('28')
    
        self._df_freq = self._df_freq[mask]

    @property
    def frequencies(self):
        return self._df_freq

    def frequency(self, channel, band=0):
        return self._df_freq.loc[channel, band]

    def channel(self, frequency):
        return NotImplementedError


def main():
    #cb = CitizenBand()
    #print(cb.frequencies)
    #print(cb.frequency(19))
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()