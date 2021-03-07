# chinese-copybook-for-children
A Python mini-program for creating a Chinese copybook in docx file for children.

Example usage:
```
doc = docx.Document()
copybook_obj = copybook_page("太陽", "Sun")
copybook_obj.insert_to_document(doc)
```
This will create one page of copybook in `copybook.docx`.
