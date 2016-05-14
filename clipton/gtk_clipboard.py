from gi.repository import Gtk, Gdk
from hashlib import sha1
from .clipboard import BaseClipboard


class Clipboard(BaseClipboard):

    CLIPBOARD = Gdk.SELECTION_CLIPBOARD
    PRIMARY = Gdk.SELECTION_PRIMARY

    def __init__(self, handle=None):
        super(Clipboard, self).__init__(handle)
        self._clipboard = Gtk.Clipboard.get(Clipboard.CLIPBOARD)
        self._primary = Gtk.Clipboard.get(Clipboard.PRIMARY)
        self._clipboard_hash = self._calculate_clipboard_hash()
        self._primary_hash = self._calculate_clipboard_hash(self.PRIMARY)

    def _calculate_clipboard_hash(self, mode=CLIPBOARD):
        return sha1(str(self.formats(mode)).encode()).hexdigest()

    def _get_format(self, user_format):
        if isinstance(user_format, tuple) and isinstance(user_format[0], Gdk.Atom):
            format = user_format[0]
        else:
            format = Gdk.Atom.intern(user_format, False)

        return format

    def _get_format_name(self, user_format):
        if isinstance(user_format, tuple) and isinstance(user_format[0], Gdk.Atom):
            format = user_format[0].name()
        else:
            format = user_format

        return format.lower()

    def formats(self, mode=CLIPBOARD):
        if mode == self.CLIPBOARD:
            targets = self._clipboard.wait_for_targets()
        else:
            targets = self._primary.wait_for_targets()

        return [(t, t.name().lower()) for t in targets[1]]

    def has_changed(self, mode=CLIPBOARD):
        clip_hash = self._clipboard_hash if mode == self.CLIPBOARD else self._primary_hash
        return clip_hash != self._calculate_clipboard_hash(mode)

    def copy(self, data, format, mode=CLIPBOARD):
        # Due to https://bugzilla.gnome.org/show_bug.cgi?id=656312
        # only set_text and set_image work in python
        if 'text' in format or 'string' in self._get_format_name(format):
            if mode == self.CLIPBOARD:
                self._clipboard.set_text(data, len(data))
            else:
                self._primary.set_text(data, len(data))

    def paste(self, format, mode=CLIPBOARD):
        target = self._get_format(format)
        content = self._clipboard.wait_for_contents(target) if mode == Clipboard.CLIPBOARD else \
            self._primary.wait_for_contents(target)

        return content.get_data() if isinstance(content, Gtk.SelectionData) else content

    def text(self, mode=CLIPBOARD):
        return self._clipboard.wait_for_text() if mode == Clipboard.CLIPBOARD else \
               self._primary.wait_for_text()

    def html(self, mode=CLIPBOARD):
        target = Gdk.Atom.intern('text/html', False)
        contents = self._clipboard.wait_for_contents(target) if mode == Clipboard.CLIPBOARD else \
            self._primary.wait_for_contents(target)

        return contents.get_data() if contents else ''

    def image(self, mode=CLIPBOARD):
        return self._clipboard.wait_for_image() if mode == Clipboard.CLIPBOARD else \
            self._primary.wait_for_image()

    def contents(self, mode=CLIPBOARD):
        content = {}

        for target_atom, target_name in self.formats(mode):
            contents_ = self._clipboard.wait_for_contents(target_atom) if mode == Clipboard.CLIPBOARD else \
               self._primary.wait_for_contents(target_atom)

            if contents_ and contents_.get_data():
                content[str(target_name)] = contents_.get_data()

        return content
