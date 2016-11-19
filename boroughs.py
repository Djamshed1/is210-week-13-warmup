#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week Thirteen Warmup task 01"""

import csv
import json

GRADES = {
    'A': float(1.00),
    'B': float(0.90),
    'C': float(0.80),
    'D': float(0.70),
    'F': float(0.60),
}
def get_score_summary(filename):
    """This fuction represent the filename whose data will be read and
    interpreted.

    Args:
        filename(str): This is a csv file.

    Returns:
        Returns a dictionary data.

    Examples:
        >>> get_score_summary('inspection_results.csv')
        {'BRONX': (156, 0.9762820512820514),
        'BROOKLYN': (417, 0.9745803357314141),
        'STATEN ISLAND': (46, 0.9804347826086955),
        'MANHATTAN': (748, 0.9771390374331531),
        'QUEENS': (414, 0.9719806763285017)}
    """
    data = {}
    fhandler = open(filename, 'r')
    csv_f = csv.reader(fhandler)
    for row in csv_f:
        if row[10] not in ['P', '', 'GRADE']:
            data[row[0]] = [row[1], row[10]]
            data.update(data)
    fhandler.close()
    buro_data = {}
    for value in data.itervalues():
        if value[0] not in buro_data:
            val1 = 1
            val2 = GRADES[value[1]]
        else:
            val1 = buro_data[value[0]][0] + 1
            val2 = buro_data[value[0]][1] + GRADES[value[1]]
        buro_data[value[0]] = (val1, val2)

    final_data ={}
    for key in buro_data.iterkeys():
        val1= buro_data[key][0]
        val2= buro_data[key][1]/float(buro_data[key][0])
        final_data [key]=(val1, val2)
    return final_data

def get_market_density(filename):
    """This function takes only one argument which is a filename.

    Args:
        filename(file): This is a csv file.

    Return:
        Returns a dictionary data.

    Examples:
       >>> get_market_density('green_markets.json')
      {u'STATEN ISLAND': 2, u'BROOKLYN': 48, u'BRONX': 32,
       u'MANHATTAN': 39, u'QUEENS': 16}
    """
    fhandler = open(filename, 'r')
    all_data = json.load(fhandler)
    buro_data = all_data["data"]
    final_data = {}
    fhandler.close()
    for data in buro_data:
        data[8] = data[8].strip()
        if data[8] not in final_data.iterkeys():
            val = 1
        else:
            val = final_data[data[8]] + 1
        final_data[data[8]] = val
       
    return final_data

def correlate_data(file1='inspection_results.csv',
                    file2='green_markets.json',
                    file3='result.json'
                   ):
    """This function takes three arguments and it will combine above two datas.

    Args:
        file1(file): First argument is the name of a file with restaurant scores data.
        file2(file): Next argument is the name of a JSON file with green_market data.
        file3(file): The final argument is the name of a file that will contain the output of this function.

    Returns:
        Returns an output of above two arguments.
    """
    data1 = get_score_summary(file1)
    data2 = get_market_density(file2)
    result = {}
    for key2 in data2.iterkeys():
        for key1 in data1.iterkeys():
            if key1 == str(key2).upper():
                val1 = data1[key1][1]
                val2 =(data2[key2])/float(data1[key1][0])
                result[key2] = (val1, val2)
                
    fhandler = open(file3, 'w')
    json.dump(result,fhandler)
    fhandler.close() 
