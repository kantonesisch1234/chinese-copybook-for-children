# chinese-copybook-for-children
A Python mini-program for creating a Chinese copybook in docx file for children.

Example usage:
```
doc = docx.Document()
word_list = ["星星", "月亮", "太陽"]
eng_word_list = ["Star", "Moon", "Sun"]
copybook_obj_list = []
for words in zip(word_list, eng_word_list):
    copybook_obj_list.append(copybook_page(*words))
for page in copybook_obj_list:
    page.insert_to_document(doc)
```
This will create a copybook in `copybook.docx`.
