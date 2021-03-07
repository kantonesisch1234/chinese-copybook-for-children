# chinese-copybook-for-children
A Python mini-program for creating a Chinese copybook in docx file for children.

Example usage:
```
doc = docx.Document()
word_list = ["星星", "月亮", "太陽"]
eng_word_list = ["Star", "Moon", "Sun"]
copybook_obj_list = []
for words in zip(word_list, eng_word_list):
    copybook_page(*words).insert_to_document(doc)
```
This will create a copybook in `copybook.docx`.

We can also read word pairs in a `.txt` file.
Assume that you have a file `wordlist.txt` containing wordlists in the following format:
```
星星, Star
月亮, Moon,
太陽, Sun
```
The Python code to read the file:
```
with open("wordlist.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
chinese_words = []
english_words = []
for line in lines:
    word_pair = line.strip('\n').split(',')
    chinese_words.append(word_pair[0].strip(' '))
    english_words.append(word_pair[1].strip(' '))

doc = docx.Document()
copybook_obj_list = []
for words in zip(chinese_words, english_words):
    copybook_page(*words).insert_to_document(doc)
```
