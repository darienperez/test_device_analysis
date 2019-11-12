#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:16:14 2019

@author: quantummech
"""

def file_extractor(file):
    # Declare filepaths
    IdVd_file = open(file)

    # Read files
    IdVd_read = reader(IdVd_file)

    # Convert to list
    IdVd_data = list(IdVd_read)
    IdVd_data_clean = IdVd_data[259:]
    
    return IdVd_data_clean