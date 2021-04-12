# coding=utf-8

#list of locations a traveler (user) can go to
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

#example user data to test functions with
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

#one list of attractions to correspond with each travel spot
#will be populated later
attractions = [[], [], [], [], []]

#given a location as a string, search destinations[] and return
#index
def get_destination_index(destination):
	destination_index = destinations.index(destination) 
	return destination_index

#parse user data to return their destination's index in destinations[]
def get_traveler_location(traveler):
	traveler_destination = traveler[1]
	traveler_destination_index = get_destination_index(traveler_destination)
	return traveler_destination

#populate attractions for a given destination	
def add_attraction(destination, attraction):
	#search for destination, get index from list
	try:
		destination_index = get_destination_index(destination)
	except ValueError:
		print('Destination not found')
		return
	
	#use destination index to target correct attraction list 
	attractions_for_destination = attractions[destination_index]
	
	#update attraction list
	attractions_for_destination.append(attraction)
	
	return attractions_for_destination

#given where a user is going, and a list of their interests
#recommend attractions they would like
def find_attractions(destination, interests):
	#get index of destination
	destination_index = get_destination_index(destination)
	#find corresponding list of attractions
	attractions_in_city = attractions[destination_index]
	#list to store available attractions that match interests
	attractions_with_interest = []
	for possible_attraction in attractions_in_city:
		#retrieve attraction tags
		attraction_tags = possible_attraction[1]
		for interest in interests:
			#check if interest matches tags
			if interest in attraction_tags:
				attractions_with_interest.append(possible_attraction[0])
	return attractions_with_interest

#update attractions for each destination
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#search for arts attractions in LA
la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)