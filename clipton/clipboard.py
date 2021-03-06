
       
class Clipboard(object):

    TEXT = 'text'
    HTML = 'html'
    RTF = 'rtf'
    IMAGE = 'image'
    
    def __init__(self, handle=None):
        """
        Initializes de clipboard and uses the provided handle, if any, as the owner.
        
        :param handle: Handler to be used as owner for the clipboard.
        """
        self._handle = handle
        
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