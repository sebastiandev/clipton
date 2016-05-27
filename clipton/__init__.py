import platform
from .clipboard import Clipboard


__version__ = '1.0.0'


def get_clipboard(handle=None):
    system = platform.system().lower()
    if 'windows' == system:
        from . import win_clipboard
        impl = win_clipboard.WinClipboard(handle)

    elif 'darwin' == system:
        raise NotImplementedError("Clipboard not available for MacOS yet")

    else:
        try:
            from . import gtk_clipboard
            impl = gtk_clipboard.GTKClipboard(handle)
        except:
            raise NotImplementedError("Clipboard for Qt not available yet")      

    return Clipboard(handle, impl)
