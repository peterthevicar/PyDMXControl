from usb.core import USBError

from pyudmx import pyudmx
from .transmittingController import transmittingController


class uDMXController(transmittingController):

    def __init__(self, *args, **kwargs):
        self.__init()

        super().__init__(*args, **kwargs)

    def __init(self):
        try:
            self.udmx.close()
        except:
            pass

        self.udmx = pyudmx.uDMXDevice()
        self.udmx.open()

    def close(self):
        # uDMX
        self.udmx.close()
        print("CLOSE: uDMX closed")

        # Parent
        super().close()

        return

    def _send_data(self):
        data = self.get_frame()
        try:
            self.udmx.send_multi_value(1, data)
        except USBError:
            self.__init()
        except ValueError:
            pass
