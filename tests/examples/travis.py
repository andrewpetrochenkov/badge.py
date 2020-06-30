#!/usr/bin/env python
import badge

# https://github.com/owner/repo
# https://travis-ci.org/owner/repo


class Travis(badge.Badge):
    title = "Travis"
    image = "https://api.travis-ci.org/{fullname}.svg?branch={branch}"
    link = "https://travis-ci.org/{fullname}/"


fullname = "owner/repo"

travis = Travis(fullname=fullname)
assert str(travis) == '[![Travis](https://api.travis-ci.org/owner/repo.svg?branch=master)](https://travis-ci.org/owner/repo/)'


assert str(travis.rst) == """.. image:: https://api.travis-ci.org/owner/repo.svg?branch=master
    :target: https://travis-ci.org/owner/repo/"""
