# -*- coding: utf-8 -*-
"""
Created on Thu Sep 05 18:29:12 2019

@author: Ayman
"""
import csv
import json
from ibm_watson import ToneAnalyzerV3
from flask import Flask,request
app = Flask(__name__)


def AnalyzeToneforAHotel(HotelReview=[]):
    
    tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='CX5ULZg1Bn5b8IF6U6-3hgPdUnw0XNivs_mQEezPen03',
    url='https://gateway-syd.watsonplatform.net/tone-analyzer/api')
    
    
    TonesScores ={}
    TonesCount= {}
    for review in HotelReview:
            tone_analysis = tone_analyzer.tone({'text': review},content_type='application/json').get_result()
            for i in range (len(tone_analysis['document_tone']['tones'])):
                
                toneName= tone_analysis['document_tone']['tones'][i]['tone_name']
                Score= tone_analysis['document_tone']['tones'][i]['score']
                if(TonesScores.has_key(toneName)):
                    TonesScores[toneName]= TonesScores[toneName] + Score
                    TonesCount[toneName]= TonesCount[toneName]+1
                else:
                    TonesScores[toneName]= Score
                    TonesCount[toneName]= 1
    
    for key in TonesCount.keys():
        TonesScores[key]= TonesScores[key]/TonesCount[key]
    
    return TonesScores 
                    

@app.route('/AnalyzeAll', methods=['GET'])
def AnalyzeAll():
    HotelsReviews ={}
    HotelData ={}
    with open('hotels1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            hotel_name = row[6]
            if(HotelsReviews.has_key(hotel_name)):
                HotelsReviews[hotel_name].append(row[14])
            else:
                HotelsReviews[hotel_name]= [row[14]]
                HotelData[hotel_name] = row
        for key in HotelsReviews.keys():
           TonesScores= AnalyzeToneforAHotel(HotelsReviews[key])
           HotelData[key][14]= TonesScores
           # I couldn't run Elastic Search on my machine but If I could run it, 
           #I would have indexed each HotelData[key] elemment inside this for loop 
           #as josn string after adding the tones scores to it and of course index 
           #itself has to be created  earlier.
        return json.dumps(HotelData)
app.run()



