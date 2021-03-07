#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

from typing import List
import COMP9318.lab2.helper as helper
import COMP9318.lab2.submission as submission

if __name__ == '__main__':
    input_data = helper.read_data('./assert/a_.txt')
    output = submission.buc_rec_optimized(input_data)
    print(output)