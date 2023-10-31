


database = {
	1: "Mocked Alice",
	2: "Alice",
	3: "Tom",
	4: "Samy",
	5: "Yami"
}

def get_user_from_db(user_id):
	return database.get(user_id)

