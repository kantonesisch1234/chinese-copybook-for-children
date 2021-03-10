# chinese-copybook-for-children
A Python mini-program for creating a Chinese copybook in docx and pdf files for children. The maximum allowed number of Chinese characters for one word is 10.

Dependencies: packages `python-docx`, `google_trans_new`, `docx2pdf`, `bs4`, `requests`.

In case you haven't installed these packages, install them with `pip install ` + package name, e.g. `pip install python-docx`, or simply execute the batch file `install_dependencies.bat`.

There are two modes: the translation mode and the picture mode. The translation mode inserts multilingual translation of the word in the cell in the upper right hand corner of a copybook page; the picture mode inserts the corresponding picture in that cell. The pictures are directly scraped from Yahoo image search after queries are sent to the search engine.

The Python code can be run as follows in the command line:

The translation mode:
```
python copybook.py -t
```
The picture mode:
```
python copybook.py -p
```

To make the execution of the code even easier, batch files are included in the repository. The code can be executed directly by clicking on it.

By running the Python code,  a copybook `copybook.docx` and its converted pdf file `copybook.pdf` will be created.

The word list can be read by a text file.
It is assumed that you have a file `wordlist.txt` containing wordlists in the following format:
```
星星, Star
月亮, Moon
太陽, Sun
```

New features being worked on:
* English copybooks;
* Automatic generation of random arithmetic exercises for children;
* Automatic generation of maze games from children. 

This program is originally meant to be written for someone who has no programming knowledge at all, such that they can complete everything in one click, so flexibility is basically not taken into account. 

p.s. The code `download_images.py` is for direct downloading of images by scraping Yahoo image search without creating copybook documents. 
