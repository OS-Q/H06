from platformio.managers.platform import PlatformBase


class P01Platform(PlatformBase):

    def is_embedded(self):
        return True
