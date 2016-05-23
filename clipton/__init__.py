import platform

__version__ = '1.0.0'


def get_clipboard(handle=None):
    system = platform.system().lower()
    if 'windows' == system:
        from . import win_clipboard
        clip = win_clipboard.Clipboard(handle)

    elif 'darwin' == system:
        raise NotImplementedError("Clipboard not available for MacOS yet")

    else:
        try:
            from . import gtk_clipboard
            clip = gtk_clipboard.Clipboard(handle)
        except:
            raise NotImplementedError("Clipboard for Qt, XFCE, not available yet")      

    return clip
