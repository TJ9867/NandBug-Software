#!/usr/bin/env python3

from amaranth import *
from amaranth.lib import wiring

class Blinker(wiring.Component):

    def __init__(self, s, period):
        """
        Simple blinker module

            Parameters:
                s : A signal
                period (int): The blink period (seconds)
        """
        self.s = s
        self.period = period

    def elaborate(self, platform):
        m = Module()

        max_value = int(self.period * platform.default_clk_frequency/2 + 1)

        counter = Signal(range(max_value))

        with m.If(counter == max_value):
            m.d.sync += self.s.o.eq(~self.s.o)
            m.d.sync += counter.eq(0)
        with m.Else():
            m.d.sync += counter.eq(counter + 1)

        return m
