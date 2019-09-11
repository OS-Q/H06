from platformio.managers.platform import PlatformBase


class H4Platform(PlatformBase):

    def is_embedded(self):
        return True
