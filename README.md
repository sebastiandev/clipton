# clipton
A cross platform clipboard that makes it easy and transparent to access and interact with the native clipboard

Currently supported clipboards:
- [x] Windows
- [x] Linux Gtk
- [ ] Linux Qt

## Examples

### Getting the clipboard
```python
import clipton
clipboard = clipon.get_clipboard()
````

### Adding content to the clipboard
```python
import clipton
clipboard = clipon.get_clipboard()
c.copy("hello clipton!")  # default expects unicode text
c.copy("<html><body><p>texto html</p></body></html>", c.HTML)  # specifying the data format (html)
```

### Checking the available formats of clipboard's data
```python
import clipton
clipboard = clipon.get_clipboard()
clipboard.formats()
>> [(13, 'unicodetext'),
>> (16, 'locale'),
>> (1, 'text'),
>> (7, 'oemtext')]
```

### Retrieving clipboard data as text
```python
import clipton
clipboard = clipon.get_clipboard()
c.text()
>> u"hello clipton!"
```

### Retrieving clipboard data in a specific format
```python
import clipton
clipboard = clipon.get_clipboard()
c.paste(c.TEXT)  # unicode
>> u"hello clipton!"
```

### Retrieving clipboard contents in all formats
```python
import clipton
clipboard = clipon.get_clipboard()
c.contents()
>> {'locale': '\n,',
>> 'oemtext': 'hello clipton!',
>> 'text': 'hello clipton!',
>> 'unicodetext': u'hello clipton!'}
```

