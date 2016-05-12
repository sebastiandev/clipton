import platform

def get_clipboard(handle=None):
    system = platform.system().lower()
    if 'windows' == system:
        import win_clipboard
        clip = win_clipboard.Clipboard(handle)

    elif 'darwin' == system:
        raise NotImplementedError("Clipboard not available for MacOS yet")

    else:
        try:
            import gtk_clipboard
            clip = gtk_clipboard.Clipboard(handle)
        except:
            raise NotImplementedError("Clipboard for Qt, XFCE, not available yet")      

    return clip