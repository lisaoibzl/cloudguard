import ctypes
from ctypes import wintypes
import sys

# Constants for Windows API
SPI_GETBEEP = 0x0001
SPI_SETBEEP = 0x0002
SPI_GETSCREENREADER = 0x0046
SPI_SETSCREENREADER = 0x0047
SPI_GETFILTERKEYS = 0x0032
SPI_SETFILTERKEYS = 0x0033

# Structures for filter keys
class FILTERKEYS(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.UINT),
        ("dwFlags", wintypes.DWORD),
        ("iWaitMSec", wintypes.DWORD),
        ("iDelayMSec", wintypes.DWORD),
        ("iRepeatMSec", wintypes.DWORD),
        ("iBounceMSec", wintypes.DWORD)
    ]

# Initialize SPI_SETFILTERKEYS
def set_filter_keys():
    # Initialize FILTERKEYS structure
    fk = FILTERKEYS()
    fk.cbSize = ctypes.sizeof(FILTERKEYS)
    fk.dwFlags = 0x00000001  # FKF_FILTERKEYSON
    fk.iWaitMSec = 1000
    fk.iDelayMSec = 1000
    fk.iRepeatMSec = 1000
    fk.iBounceMSec = 1000

    # Call SystemParametersInfo to set filter keys
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETFILTERKEYS, fk.cbSize, ctypes.byref(fk), 0)

def enhance_display_readability():
    try:
        # Enable Windows screen reader
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETSCREENREADER, True, None, 0)
        # Set filter keys for better accessibility
        set_filter_keys()
        print("Display readability enhanced successfully for visual impairments.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if sys.platform != "win32":
        print("CloudGuard is only supported on Windows.")
    else:
        enhance_display_readability()