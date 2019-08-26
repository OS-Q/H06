from platformio.managers.platform import PlatformBase


class Lattice_ice40Platform(PlatformBase):

    def is_embedded(self):
        return True
