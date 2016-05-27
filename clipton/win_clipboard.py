import win32clipboard
import win32gui
import win32api
import contextlib
import time
from .clipboard import Clipboard
                            

class WinClipboard(Clipboard):

    CW_TEXT = win32clipboard.CF_UNICODETEXT
    CW_HTML = 49370
    CW_RTF = 49342
    CW_IMAGE = win32clipboard.CF_BITMAP
    CW_DIB = 2
    CW_DIBV5 = 17
    
    def __init__(self, handle=None):
        """
        Initializes de clipboard and uses the provided handle, if any, as the owner.
        
        :param handle: Handler to be used as owner for the clipboard.
        """
        super(WinClipboard, self).__init__(handle)
        self._custom_handle = False
        self._last_sequence = win32clipboard.GetClipboardSequenceNumber()
        self._standard_formats = self._get_standard_formats()
        
        if not handle:
            self._custom_handle = True
            self._handle = win32gui.CreateWindowEx(0, b"STATIC", None, 0, 0, 0, 0, 0,
                                                   None, None, None, None)
        with self._open():
            try:
                self.CW_RTF = win32clipboard.RegisterClipboardFormat("Rich Text Format")
            except:
                pass
        
    def __del__(self):
        if self._custom_handle:
            win32gui.DestroyWindow(self._handle)
    
    def _get_standard_formats(self):
        """Get the known formats by looking in win32clipboard"""
        formats = {}
        for define_name in win32clipboard.__dict__.keys():
            if define_name.startswith("CF_"):
                formats[getattr(win32clipboard, define_name)] = define_name.split('_')[1].lower()
        return formats
    
    @contextlib.contextmanager
    def _open(self):
        """open clipboard as a context"""
        tries = 0
        while tries < 5:
            try:
                win32clipboard.OpenClipboard(self._handle)
                break
                
            except win32api.error:
                tries += 1
                pass
            
        if tries > 5:
            raise Exception("Error calling OpenClipboard")

        try:
            yield
            
        finally:
            win32clipboard.CloseClipboard()
   
    @staticmethod
    def _windows_str(data):
        return data.rstrip('\x00')

    def _get_format(self, format):
        if format == self.TEXT:
            format = WinClipboard.CW_TEXT
        elif format == self.HTML:
            format = WinClipboard.CW_HTML
        elif format == self.RTF:
            format = WinClipboard.CW_RTF
        elif format == self.IMAGE:
            format = WinClipboard.CW_IMAGE

        return format

    def _get_clipboard_data(self, formats_to_try, default=None):
        with self._open():
            for data_format in formats_to_try:
                if win32clipboard.IsClipboardFormatAvailable(data_format):
                    data = win32clipboard.GetClipboardData(data_format)
                    break
                else:
                    data = default
        
        return data
    
    def has_changed(self):
        return self._last_sequence != win32clipboard.GetClipboardSequenceNumber()
       
    def formats(self):
        """retrieve all current data's available formats"""
        available_formats = []
        
        with self._open(): 
            current_format = 0
            while True:
                current_format = win32clipboard.EnumClipboardFormats(current_format)

                if not current_format:
                    break
                
                try:
                    if current_format in self._standard_formats:
                        format_name = self._standard_formats[current_format]
                    
                    else:
                        format_name = win32clipboard.GetClipboardFormatName(current_format)
                        
                except TypeError:
                    format_name = ''
                    
                available_formats.append((current_format, format_name.lower()))

        return available_formats

    def contents(self):
        return {format_name: self.paste(format_num) 
                for format_num, format_name in self.formats()}
        
    def copy(self, data, format=Clipboard.TEXT):
        """
        Puts data in the clipboard with the specified format
        
        :param data: data to store in the clipboard
        :param format: format of the data to be stored in the clipboard
        """
        format = self._get_format(format)
        
        with self._open():
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(format, data)
            self._last_sequence = win32clipboard.GetClipboardSequenceNumber()

    def paste(self, format):
        format = self._get_format(format)
        format_num = format if type(format) is int else format[0]
        
        data = self._get_clipboard_data([format_num])        
        return self._windows_str(data) if isinstance(data, (str, unicode)) else data
        
    def text(self):
        """
        Tries to retrieve data from clipboard as text or unicode
        """
        data = self._get_clipboard_data([win32clipboard.CF_UNICODETEXT, win32clipboard.CF_TEXT], default='')            
        return self._windows_str(data)
    
    def html(self):
        data = self._get_clipboard_data([WinClipboard.CW_HTML], default='')        
        return self._windows_str(data)

    def rtf(self):
        data = self._get_clipboard_data([WinClipboard.CW_RTF], default='')        
        return self._windows_str(data)
   
    def image(self):
        return self._get_clipboard_data([WinClipboard.CW_DIBV5, WinClipboard.CW_DIB, WinClipboard.CW_IMAGE])
 