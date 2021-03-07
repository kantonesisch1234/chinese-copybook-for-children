# chinese-copybook-for-children
A Python mini-program for creating a Chinese copybook in docx and pdf files for children. The maximum allowed number of Chinese characters for one word is 10.

Dependencies: packages `python-docx`, `google_trans_new`, `docx2pdf`.

Install the packages with `pip install python-docx`, `pip install google_trans_new` and `pip install docx2pdf` in Anaconda.

By running the Python code,  a copybook `copybook.docx` and its converted pdf file `copybook.pdf` will be created.

The word list can be read by a text file.
It is assumed that you have a file `wordlist.txt` containing wordlists in the following format:
```
星星, Star
月亮, Moon
太陽, Sun
```

You may want to remove translations to languages other than English, because Google Translation sometimes just really sucks. Just change the code and assign `false` to the keyword argument `translate` while creating `copybook_page` object. 
```
copybook_page(*words, translate=false).insert_to_document(doc)
```

New features being worked on:
* Automatic scraping of the first result of the word from Google image search and insert it to the document file (hard if API is not used because Google tried hard to stop us from scraping it ourselves)
* English copybooks;
* Automatic generation of random arithmetic exercises for children;
* Automatic generation of maze games from children. 

This program is originally meant to write for someone who has no programming knowledge at all, such that they can complete everything in one click, so flexibility is basically not taken into consideration. 
