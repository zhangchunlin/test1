#! /usr/bin/env python
#coding=utf-8

from uliweb.orm import *
from test1.models import B

class B(B):
    #a = ManyToMany('A', collection_name='b')
    c1 = Field(str)
    c2 = Field(str)
