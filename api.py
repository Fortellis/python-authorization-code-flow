from wsgiref import headers
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class Tokens(Resource):
  def options(self):
      return "We appreciate your request."
  def post(self):
    app.logger.debug('Body: %s', request.get_data())

    authorizationCode = request.get_data().decode()
    response = requests.post('https://identity.fortellis.io/oauth2/aus1p1ixy7YL8cMq02p7/v1/token', data = 'grant_type=authorization_code&redirect_uri=http://localhost:80/&code=' + authorizationCode , headers= {'Authorization':'Basic base64encoded{yourAPIKey:yourAPISecret}', 'Accept':'application/json', 'content-type':'application/x-www-form-urlencoded' })
    print(response.json())
    print(response.request.body)
    return response.json()


api.add_resource(Tokens, '/v1/token')

if __name__ == "__main__":
  app.run(debug=True)
