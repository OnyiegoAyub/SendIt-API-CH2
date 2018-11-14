from flask import Flask, jsonify, make_response, request, abort
from flask_restful import Resource


# internal import
from ..models.user_models import User

users = [{
    "user_id":1,
    "username": "Ayub",
    "role": "Admin",
    "email": "ayub@gmail.com",
    "password": "ayub"

}]

class AllUsers(Resource, User):

    def get(self):
        """gets all orders"""
        users = self.get_all_users()  # from paercel models
        return make_response(jsonify(
            {"message": "All Users", "orders": users, "status": "okay"}), 200)


class CreateUsers(Resource, User):

    def post(self):
        """posts an order"""
        data = request.get_json() or {}
        orders = self.create(
                               username=data['username'],
                               role=data['role'],
                               email=data['email'],
                               password=data['password']
                               )

        return make_response(jsonify(
            {"message": "success"}), 201)


class SingleUser(Resource, User):
    '''single delivery order API'''

    def get(self, user_id):
        """find an order by order_id and assign it destination one_order"""
        """call the get_one method from order models"""
        one_user = self.get_one_users(user_id)
        if one_user is not False:
            return make_response(jsonify(
            {"status": "ok", "User": one_user}), 200)
        return make_response(jsonify(
            {"status": "Not Found"}), 404)

