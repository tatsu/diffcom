#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Compare DICOM files tag by tag.

"""

import os

import pydicom


def __check_file(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        print("%s is something wrong" % filepath, file=sys.stderr)
        return False
    return True


def __print_elem(element1=None, element2=None):
    if not element1 and not element2:
        return
    if element1 and element2:
        if element1.value != element2.value:
            mark = 'M'
        else:
            mark = '='
        elem = element1
    elif element1:
        mark = 'D'
        elem = element1
    else:
        mark = 'A'
        elem = element2

    print('[%s] ' % mark, end='')
    print('(%s,%s) ' % (format(elem.tag.group, '04x'),
                        format(elem.tag.element, '04x')), end='')
    print(elem.name.ljust(40), end='')
    print(' %s ' % elem.VR, end='')
    if elem.tag == 0x7FE00010:  # Pixel Data
        if mark == 'M':
            print('[1] {:,} bytes [2] {:,} bytes'.format(len(element1.value),
                                                         len(element2.value)),
                  end='')
        else:
            print('{:,} bytes'.format(len(elem.value)), end='')
    else:
        if mark == 'M':
            print('[1] "%s" [2] "%s"' % (element1.value, element2.value),
                  end='')
        else:
            print('"%s"' % elem.value, end='')
    print('')


def diffcom(file1, file2):
    """Compare DICOM file1 with DICOM file2.

    file1 is often the earlier, whereas file2 is the later.
    """

    if not __check_file(file1):
        return
    if not __check_file(file2):
        return
    ds1 = pydicom.dcmread(file1)
    ds2 = pydicom.dcmread(file2)
    it1 = iter(ds1)
    it2 = iter(ds2)
    EOD = pydicom.DataElement(0xFFFFFFFF, 'PN', 'Guard')
    elem1 = next(it1, EOD)
    elem2 = next(it2, EOD)
    while elem1 != EOD or elem2 != EOD:
        if elem1.tag == elem2.tag:
            __print_elem(elem1, elem2)
            elem1 = next(it1, EOD)
            elem2 = next(it2, EOD)
        while elem1.tag < elem2.tag:
            __print_elem(elem1)
            elem1 = next(it1, EOD)
        while elem1.tag > elem2.tag:
            __print_elem(element2=elem2)
            elem2 = next(it2, EOD)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3:
        diffcom(sys.argv[1], sys.argv[2])
    else:
        print('Usage: python diffcom.py file1 file2')
