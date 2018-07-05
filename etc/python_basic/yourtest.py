# -*- coding: utf-8 -*-

import re
import functools 
import json
import ast
import xml.etree.cElementTree as ET

def string_contains(source, dest):
    return source in dest

def clean_split(param):
    return list(''.join(param.split(' ')))

def re_match(reg, str):
    return None != re.match(reg, str)

def get_sum(inputs):
    return sum(inputs)

def average(inputs):
    return sum(inputs) // len(inputs)

def wc(s):
    s = s.split(' ')
    ret = {}
    for item in s:
        if None == ret.get(item):
            ret[item] = 1
        else:
            ret[item] += 1
    return ret
            
def get_user_city(xml):
    e = ET.fromstring(xml)

    def get_tech_contact(e):
        if 'techContact' == e.tag:
            return e
        else:
            for child in e:
                found = get_tech_contact(child)
                if found:
                    return found

            return None
                        
    tech_contact = get_tech_contact(e)
    import pdb; pdb.set_trace()
    tech_contact[1].text.strip()
    
    
def convert_from_json(param):
    return ast.literal_eval(param)

def sorter(inputs):
    return sorted(inputs)

def sortbyage(inputs):
    return [person['name'] for person in sorted(inputs, key=lambda x: x['birthyear'])]

class VideoGameCharacter(object):
    pass

class Megaman(VideoGameCharacter):
    def get_name(self):
        return 'Megaman'

    def get_company(self):
        return 'Capcom'

class Mario(VideoGameCharacter):
    def get_name(self):
        return 'Mario'

    def get_company(self):
        return 'Nintendo'

def memoize(func):
    memo = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        param = args[0]
        if None == memo.get(param):
            memo[param] = func(param)

        return memo[param]
    return wrapper