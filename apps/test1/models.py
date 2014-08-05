#! /usr/bin/env python
#coding=utf-8

from uliweb.orm import *

class A(Model):
    a1 = Field(str)

class B(Model):
    a = ManyToMany('A', collection_name='b')
    b1 = Field(str)
    b2 = Field(str)
