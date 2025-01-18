#!/usr/bin/env python3

from amaranth import *
from amaranth.lib import wiring
from amaranth.lib.wiring import In, Out

class Blinker(wiring.Component):
    led_sig: Out(1)
    def __init__(self, period_s):
        super().__init__()  # is this maybe incorrect?
        self.period = period_s

    def elaborate(self, platform):
        m = Module()

        max_value = int(self.period * platform.default_clk_frequency/2 + 1)

        counter = Signal(range(max_value))

        with m.If(counter == max_value):
            m.d.sync += self.led_sig.eq(~self.led_sig)
            m.d.sync += counter.eq(0)
        with m.Else():
            m.d.sync += counter.eq(counter + 1)

        return m


class PlatformBlinker(Elaboratable):
    def __init__(self, period):
        self.period = period

    def elaborate(self, platform):
        m = Module()

        blink_led = platform.request("led", 0) # options are 0,1,2 
        blinker = Blinker(0.5)

        m.d.comb += blink_led.o.eq(blinker.led_sig) # complains about two driving sources (makes sense)? 
        m.submodules += blinker

        return m