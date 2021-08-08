#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:53:14 2020

@author: ganesh
"""

import astropy.io.fits as fits
from sys import argv, exit

def Edit_Header_HCT(hdul):
    hdr=hdul[0].header
    data=hdul[1].data
    primary_hdu= fits.PrimaryHDU(header=hdr,data=data)
    hdul=fits.HDUList(primary_hdu)
    hdul.writeto(argv[1]+'_modified.fits')

if __name__ == "__main__":
    hdul=fits.open(argv[1])
    Edit_Header_HCT(hdul)
    exit(0)
    
