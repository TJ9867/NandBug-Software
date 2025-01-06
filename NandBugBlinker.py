from nandbug_platform import NandBugPlatform
from bitstreams.modules.blinker import PlatformBlinker


if __name__ == "__main__":
    #from ...nandbug_platform import NandBugPlatform
    
    platform = NandBugPlatform()
    blinker = PlatformBlinker(0.5)
    print(blinker)
    platform.build(PlatformBlinker(0.5), do_program=True)