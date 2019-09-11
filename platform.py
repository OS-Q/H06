from platformio.managers.platform import PlatformBase


class H4latform(PlatformBase):

    def is_embedded(self):
        return True
