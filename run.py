#serves as an entry point to our application
#it gets a copy of the app package and runs it

import os

from app import create_app
config_name = os.getenv('APP_SETTINGS')

app = create_app(config_name)


if __name__ == '__main__':
  app.run()
# app.run(host='0.0.0.0',port=8080)













# '''single delivery order API'''
	# def get(self, order_id):
	# 	"""find an order by order_id and assign it to one_order"""
	# 	"""call the get_one method from order models"""
	# one_order = Parcels.get_one(self, order_id) # import from
	# models(Parcels.get_one)

		# return make_response(jsonify(
    #   {"status": "ok",
    #   "order": one_order}), 200)
# order_id = self.order_id,