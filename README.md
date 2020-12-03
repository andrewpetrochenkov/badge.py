<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/badge.svg?maxAge=3600)](https://pypi.org/project/badge/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/badge.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/badge.py/actions)

### Installation
```bash
$ [sudo] pip install badge
```

#### Features
+   **md** (default), **rst**, **html**
+   autoformat strings
+   **minimalistic design**

#### Examples
```python
>>> class Travis(badge.Badge):
    title = "Travis"
    image = "https://api.travis-ci.org/{fullname}.svg?branch={branch}"
    link = "https://travis-ci.org/{fullname}/"

>>> Travis(fullname="owner/repo") # .md, Markdown by default
'[![Travis](https://api.travis-ci.org/owner/repo.svg?branch=master)](https://travis-ci.org/owner/repo/)'

>>> Travis(fullname="owner/repo").rst # .rst, reStructuredText
'.. image: : https://api.travis-ci.org/owner/repo.svg?branch=master
    : target: https://travis-ci.org/owner/repo/'
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
