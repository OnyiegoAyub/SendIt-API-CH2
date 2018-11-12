class Parcel:

	parcels = [
        # {
        #     "parcel_id": 1,
        #     "user_id": 1,
        #     "origin": "Eldoret",
        #     "destination": "Kitale",
        #     "weight": 5,
        #     "status": "pending delivery"
        # },
        # {
        #     "parcel_id": 2,
        #     "user_id": 1,
        #     "origin": "Nairobi",
        #     "destination": "Mombasa",
        #     "weight": "1",
        #     "status": "pending delivery"
        # }
	]

	users = [{
	"user_id": 1,
    "username": "Ayub",
    "role": "Admin",
    "email": "ayub@gmail.com",
    "password": "ayub"

}]

	def create(self, origin, destination, weight, status):
		parcel = {
      		"parcel_id": len(Parcel.parcels) + 1,
            "user_id": len(Parcel.parcels) + 1,
            "origin": origin,
            "destination": destination,
            "weight": weight,
			"status": status
    	}

		Parcel.parcels.append(parcel)

		return parcel

"""   method calling all parcels """
	def get_all(self):
		return Parcel.parcels

  """ method calling one parcel"""
	def get_one(self, parcel_id):
		for parcel in Parcel.parcels:
			if parcel["parcel_id"] == parcel_id:
				return parcel
			return False

	def cancel_parcel_order(self, parcel_id):
		for parcel in Parcel.parcels:
			if parcel["parcel_id"] == parcel_id:
				parcel['status'] == "Cancelled"
				return parcel
			return False

	def get_order_by_user(self, user_id):
		for user in Parcel.parcels:
			if user["user_id"] == user_id:
				return user
			return False
