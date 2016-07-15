#!/bin/env python

import geopy
from geopy.geocoders import GoogleV3
import sys

gl = GoogleV3()
add = sys.argv[1]
l = gl.geocode(add)
print l.latitude, l.longitude
