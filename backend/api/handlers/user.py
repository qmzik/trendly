import os
import json
import pymongo
import hashlib
import tornado.gen
from tornado.web import RequestHandler
from api.commons import users_collection
from jsonschema import validate
from jsonschema.exceptions import ValidationError


login_schema = {
    "type": "object",
    "properties": {
        "email": {"type":["string"]},
        "passwordHash": {"type":["string"]}
    },
    "required": ["email", "passwordHash"]
}

new_user_schema = {
    "type": "object",
    "properties": {
        "firstName": {"type":["string"]},
        "secondName": {"type":["string"]},
        "email": {"type":["string"]},
	    "passwordHash": {"type":["string"]}
    },
    "required": ["firstName", "secondName", "email", "passwordHash"]
}

user_publicpage_project_schema = {
    "type": "object",
    "properties": {
        "userId": {"type":["string"]},
        "accessToken": {"type":["string"]},
        "projectUrl": {"type":["string"]},
    },
    "required": ["userId", "accessToken", "projectUrl"]
}

class APIHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("access-control-allow-origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, PUT, DELETE, OPTIONS')
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type")

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class UserAuth(APIHandler):
    @tornado.gen.coroutine
    def post(self):
        request = json.loads(self.request.body.decode('utf-8'))
        try:
            validate(request, login_schema)
        except ValidationError as err:
            self.set_status(400, 'Wrong request schema')
            return
        this_user = users_collection.find_one({'email': request['email']})
        if (this_user != None):
            if (request['passwordHash'] == this_user['passwordHash']):
                access_token = str(hashlib.sha1(os.urandom(128)).hexdigest())
                this_user['currentToken'] = access_token
                users_collection.save(this_user)
                self.set_status(202, 'Successfuly authentificated')
                self.write({
                    'userId': this_user['userId'],
                    'accessToken': access_token
                })
                return
            else:
                self.set_status(406, 'Wrong credentials')
                return
        else:
            self.set_status(406, 'Wrong credentials')
            return


class UserRegister(APIHandler):
    @tornado.gen.coroutine
    def post(self):
        request = json.loads(self.request.body.decode('utf-8'))
        try:
            validate(request, new_user_schema)
        except ValidationError as err:
            self.set_status(400, 'Wrong request schema')
            return
        request = json.loads(self.request.body.decode('utf-8'))
        request['userId'] = int.from_bytes(os.urandom(4), byteorder='little')
        user_id = users_collection.insert_one(request).inserted_id
        if (user_id != None):
            self.set_status(201, 'Successfuly created')
            return


class AddProject(APIHandler):
    @tornado.gen.coroutine
    def post(self):
        request = json.loads(self.request.body.decode('utf-8'))
        try:
            validate(request, new_user_schema)
        except ValidationError as err:
            self.set_status(400, 'Wrong request schema')
            return
