import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students
grades = db.grades


def removeLowestScore():
	for i in range(200):
		query = {'student_id': i, 'type': 'homework'}
		cursor = grades.find(query)
		cursor.sort([
			('student_id', pymongo.ASCENDING),
			('score', pymongo.DESCENDING),
		])
		cursor.skip(1)

		for doc in cursor:
			# print(doc)
			result = grades.delete_many({'_id': doc['_id']})
			print('removed ', result)


removeLowestScore()
