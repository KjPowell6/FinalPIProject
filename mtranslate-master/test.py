#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate


def main():
    to_translate = 'What is your name?'
    print(translate(to_translate))
    #print(translate(to_translate, 'sp'))
    print(translate(to_translate, 'es', 'auto'))


if __name__ == '__main__':
    main()
