# Online Literature Scraper

This repository serves the purpose of creating a simple scraper which
can convert html pages on online-literature.com to markdown files. As
it currently stands, the scraper takes a page link as input and creates
a markdown file for every chapter found on the provided page.

# Install

Simply clone this repository and run the script. Its only external 
dependency is the `bs4` module. This can be installed using pip or
a similar python module installer:

```shell
$ pip install bs4
```

# How to use

For basic use, simply run:

```shell
$ python3 ol-scraper.py [hyperlink]
```

For instance, to download the book [Democracy: An American Novel](http://www.online-literature.com/henry-adams/democracy-an-american-novel/) by [Henry Adams](http://www.online-literature.com/henry-adams/) simply run:

```shell
$ python3 ol-scraper.py http://www.online-literature.com/henry-adams/democracy-an-american-novel/
```

Additional options include:
```
usage: ol-scraper.py [-h] [-o --output-path out-path] [-d --directory-name dir-name]
                     [-p --path-and-name full-path]
                     hyperlink

Pull books from online-literature.com

positional arguments:
  hyperlink             Hyperlink to main page of the book. Like: http://www.online-
                        literature.com/author/book-name/

options:
  -h, --help            show this help message and exit
  -o --output-path out-path
                        Path of output directory (default ./)
  -d --directory-name dir-name
                        Name of output directory (default: Title-Of-Book/ (dynamically
                        dertermined))
  -p --path-and-name full-path
                        Set path and name to output directory at once with one single string
                        (instead of setting output path and directory name seperately.)
```

# License

This repository is published under the MIT License.
