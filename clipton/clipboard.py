
class BaseClipboard(object):

    TEXT = 'text'
    HTML = 'html'
    IMAGE = 'image'
    RTF = 'richtext'
    
    def has_changed(self):
        raise NotImplementedError()
        
    def formats(self):
        """
        Retrieves all available formats for the current content in the clipboard
        """
        raise NotImplementedError()
    
    def contents(self):
        """
        Retrieves the content of the clipboard in all available formats
        """
        raise NotImplementedError()
    
    def copy(self, data, format):
        """
        Copies the data in the specified format to the clipboard
        """
        raise NotImplementedError()
    
    def paste(self, format):
        """
        Retrieves the data from the clipboard in the specified format
        """
        raise NotImplementedError()
    
    def text(self):
        """
        Retrieves the data from the clipboard as text
        """
        raise NotImplementedError()

    def html(self): 
        """
        Retrieves the data from the clipboard as html
        """
        raise NotImplementedError()

    def rtf(self):
        """
        Retrieves the data from the clipboard as rich text
        """
        raise NotImplementedError()
        
    def image(self):
        """
        Retrieves the data from the clipboard as image bytes
        """
        raise NotImplementedError()


class BaseClipboardImplementator(BaseClipboard):

    def __init__(self, handle=None):
        self.handle = handle

        
class Clipboard(BaseClipboard):

    def __init__(self, handle=None, implementation=None):
        """
        Initializes de clipboard and uses the provided handle, if any, as the owner.
        
        :param handle: Handler to be used as owner for the clipboard.
        """
        self._handle = handle
        self._impl = implementation
        
        if not self._impl.handle:
            self._impl.handle = handle
        
    def has_changed(self):
        return self._impl.has_changed()
        
    def formats(self):
        """
        Retrieves all available formats for the current content in the clipboard
        """
        return self._impl.formats()
    
    def contents(self):
        """
        Retrieves the content of the clipboard in all available formats
        """
        return self._impl.contents()
    
    def copy(self, data, format):
        """
        Copies the data in the specified format to the clipboard
        """
        return self._impl.copy(data, format)
    
    def paste(self, format):
        """
        Retrieves the data from the clipboard in the specified format
        """
        return self._impl.paste(format)
    
    def text(self):
        """
        Retrieves the data from the clipboard as text
        """
        return self._impl.text()

    def html(self): 
        """
        Retrieves the data from the clipboard as html
        """
        return self._impl.html()

    def rtf(self):
        """
        Retrieves the data from the clipboard as rich text
        """
        return self._impl.rtf()

    def image(self):
        """
        Retrieves the data from the clipboard as image bytes
        """
        return self._impl.image()