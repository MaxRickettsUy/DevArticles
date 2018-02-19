#ultimately server to interact with user to enter album reviews/data 
#into mongo db
from __future__ import print_function
import pymongo
from pymongo import MongoClient

if __name__ == "__main__":
	con = MongoClient() #connection to db running on local machine
	
	db = con.albums #albums is member var of con

	albums = db.albums_data #tables = collections, creating albums_data collection

	insert = True

	while insert:
		print("Enter album data? (Yes/No):", end='')
		answer = raw_input()
		if answer.lower() == "yes":
			print("Enter album name: ", end='') 		
			name = raw_input()
			print("Enter artist: ", end='')
			artist = raw_input()
			print("Enter review: ", end='')
			review = raw_input()
			albums.insert({"name":name, "artists":artist, "review":review})
		else:
			insert = False
	
	#selects all data in collection and stores in list
	album_data = albums.find() 

	for shrimp in album_data:
		print(shrimp)	
	
	db.albums_data.drop()	
