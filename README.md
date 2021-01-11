# pdf-text-extract
This is a simple script to extract text from PDF documents, even if the text is included in images.

Beforehand we need to install 3 different packages using python 3 pip.
```
pip3 install pillow
pip3 install pytesseract
pip3 install pdf2image
```
The previous pytesseract requires that you have installed tesseract in your system.

In Linux Ubuntu and Debian distros is as simple as:
```
sudo apt-get install tesseract-ocr
```
In MacOS, at the time of this writing, you need to install it from [MacPorts](https://ports.macports.org/port/tesseract/summary)

The sample pdf included is property of Fujitsu.
https://www.fujitsu.com/global/support/products/computing/peripheral/scanners/scansnap/sample/sv600.html

**Make it Work**

Just clone this script, have the packages installed and run it passing the pdf file as argument.

Usage with the sample pdf:

```
python3 pdf-text-extract.py sv600_m_automatic.pdf
```

