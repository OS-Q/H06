from platformio.managers.platform import PlatformBase


class H06Platform(PlatformBase):

    def is_embedded(self):
        return True
