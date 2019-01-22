# -*- coding: utf-8 -*-

import random
import os
import numpy as nd
import pandas as pd
import sys
import re

##print ('checksum'.center(20, '*'))
#PASSWORDS={'email':'FX88ssjehk',
#			'vault':'Ix88787d',
#			'phone':'eekc9eed'}
#
#if len(sys.argv)<2:
#    print('copy secure password')
#    sys.exit()
#account=sys.argv[1]
#if account in PASSWORDS:
#    print(account)
#else:
#    print("no account")
#    
#preg=re.compile(r'future(credit|fx|rate|commodity)')   
#preg=re.compile(r'(\(\d\d\d\)?-\d\d-\d)')
preg=re.compile(r'-\d\d-\d$')
#mo=preg.findall('trade number is (137)-34-874 another trade is (237)-73-873')
#('futurecredit heding with futurerate')    #
mo=preg.search('trade1 is 58-898 trade2 is 59-83-8')
#print('trade found is ' +mo.group()) #+ mo.group()
df_tmp=pd.DataFrame()
cwd=os.getcwd()
fn='auto1.py'
lu=os.path.join(cwd, fn)
out1=os.path.getsize(lu)
out2=os.listdir(cwd)
out3=os.path.exists (lu)
fh=open(os.path.join(cwd, 'new2.txt'), 'w')
fh.write('update to 2nd password file,\n')
fh.close()
fh=open(os.path.join(cwd, 'new2.txt'), 'a')
fh.write('penetration testing to follow up')
fh.close()
fh=open(os.path.join(cwd, 'new2.txt'))
out4=fh.read()
fh.close()
#print (out4)

import shutil as sh
#os.makedirs(os.path.join(cwd, 'newdir'))
#sh.move(os.path.join(cwd, 'new2.txt'), os.path.join(cwd, 'newdir3'))

for filen in os.listdir(os.path.join(cwd, 'newdir2')):
    if filen.endswith('.txt'):
 #       os.unlink(filen)
        print('file removed: %s'%filen)
#os.unlink(os.path.join(cwd,'newdir2','new4.txt'))

#for fdn, subfdns, fns in os.walk(os.path.join(cwd,'newdir')):
#    print('folder: ' + fdn)
#    for subfdn in subfdns:
#        print('sfders: ' + subfdn)
#    for fn in fns:
#            print('file : ' + fn)
import zipfile as zip
os.chdir(os.path.join(cwd, 'dir_test'))
#ez=zip.ZipFile('t2.zip')
#print(ez.namelist())
#ez.extractall()
#ez.close()
#ez=zip.ZipFile('newzip','w')

import traceback
try:
    raise Exception("File cannot be found")
except:
    loc=os.path.join(cwd,'error.txt')
    errfile=open(loc,'w')
    errfile.write(traceback.format_exc())
    errfile.close()
    print("error logged in error.log")
    
import requests as req
url='http://www.navigator.bns/'
r=req.get(url)
#print(r.status_code==req.codes.ok)
size=len(r.text)
#print ('size is :  %s'%size)
try:
    r.raise_for_status()
except Exception as exc:
    print("error code is: ", exc)
#fw=open(os.path.join(cwd, 'file_web.txt'), 'wb')
#for chunk in r.iter_content(100000):
#    fw.write(chunk)
#fw.close()
#print(cwd, "done")
import bs4 as bs
soup=bs.BeautifulSoup(r.text, "lxml")
elems=soup.select('a')
#print(elems[0].getText())
#print(elems[2].get('href'))
#import selenium
import csv
csvobj=open(os.path.join(cwd,'new1.txt'))
robj=csv.reader(csvobj)
lrobj=list(robj)
#try:
#    for row in csv1r:
#        print(str(csv1r.line_num)+'  '+str(row))
#except:
#    print('error')
crow=[]
for row in robj:
    if robj.line_num ==1:
        continue
    
    crow.append(row)
csvobj.close()
import json
jdata='{"coredb":"wssdb", "reportdb":"ordfx","hist db":null}'
jpdata=json.loads(jdata)
jpjdata=json.dumps(jpdata)
#print(jpjdata)
import time, datetime
dt1=datetime.datetime(2017,11,6)
dt1s=dt1.strftime('%Y %m %d')
dt1st=datetime.datetime.strptime(dt1s, '%Y %m %d')
import threading
import smtplib
#try:
#    smtpobj=smtplib.SMTP_SSL('smtp.gmail.com',465)
#    print(type(smtpobj))










