from DMX.profiles.defaults import Vdim


class LED_Par_36(Vdim):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._register_channel('mode')
        self._register_channel('red', vdim=True)
        self._register_channel('green', vdim=True)
        self._register_channel('blue', vdim=True)
        self._register_channel('speed')
