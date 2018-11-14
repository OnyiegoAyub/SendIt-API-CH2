from flask import Flask, jsonify, make_response, request, abort
from flask_restful import Resource

from ..models.parcel_order_models import Parcel


class AllOrders(Resource, Parcel):

    def get(self):
        """gets all orders"""
        par = Parcel()
        orders = self.get_all()  # from parcel models
        return make_response(jsonify(
            {"message": "All orders made", "orders": orders, "status": "okay"}), 200)

class CreateOrders(Resource, Parcel):

    def post(self):
        """posts an order"""
        data = request.get_json() or {}
        orders = self.create(
                               origin=data['origin'],
                               destination=data['destination'],
                               weight=data['weight'],
                               status=data['status']
                               )

        return make_response(jsonify(
            {"message": "success"}), 201)


class SingleOrder(Resource, Parcel):
    '''single delivery order API'''

    def get(self, parcel_id):
        """find an order by order_id and assign it destination one_order"""
        """call the get_one method from order models"""
        one_order = self.get_one(parcel_id)
        if one_order is not False:
            return make_response(jsonify(
            {"status": "ok", "order": one_order}), 200)
        return make_response(jsonify(
            {"status": "Not Found"}), 404)


class CancelOrder(Resource, Parcel):
    """This class cancels an order"""

    def put(self, parcel_id):
        """
        Updates the status of a parcel order destination canceled
        """
        change = self.cancel_parcel_order(parcel_id)

        if change is not False:
            return make_response(jsonify(
                {"Message": "success", "Order": change, "status": "Accepted"}), 202)

        return make_response(jsonify(
                {"Message": "The order requested does not exist",
                 "status": "Not Found"}), 404)

class UserOrders(Resource, Parcel):
    def get(self, user_id):
        user_order = self.get_order_by_user(user_id)
        if user_order is not False:
            return make_response(jsonify(
            {"status": "ok", "order": user_order}), 200)
        return make_response(jsonify(
            {"status": "Not Found"}), 404)
