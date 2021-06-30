from flask import Flask,jsonify,request
import csv
allmovies=[]
with open('final.csv', encoding= 'utf-8') as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovies=data[1:]
likedmovies=[]
unlikedmovies=[]
didnotwatch=[]