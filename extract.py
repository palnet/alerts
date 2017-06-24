#!/usr/bin/env python3

import os
from multiprocessing import Pool, cpu_count


def extract(year: int):
    os.nice(1)  # force high priority
    os.system("gunzip geojson/" + str(year) + ".geojson.gz")


pool = Pool(cpu_count()))
pool.map(extract, range(2017, 1985, -1))
