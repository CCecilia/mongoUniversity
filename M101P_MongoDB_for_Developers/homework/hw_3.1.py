import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
students = db.students

def gatherSudentScores():
	query = {}
	projection = {'scores': 1}
	cursor = students.find(query, projection)



	for doc in cursor:
		# get lowest hw grade
		ordered_hw_scores = sorted([i for i in doc['scores'] if i['type'] == 'homework'], key=lambda k: k['score'])
		lowest_hw = ordered_hw_scores[0]
		# prune scores
		doc['scores'].remove(lowest_hw)
		# place old with ne wupdated doc
		students.replace_one({'_id': doc['_id']}, doc)


gatherSudentScores()