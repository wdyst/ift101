# Rest API stuff
from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(_name_)
api = Api(app), Resource

a_language = api.model('Language', {'language': fields.String('The language.')})

languages = []
python = {'language': 'Python'}
languages.append(python)

@api.route('/language')
class Language(Resource):
    def get(self):
        return {'hey': 'there'}
    @api.expect(a_language)
    def post(self):
    languages.append(api.payload)
    return {'result': 'Language added'}, 201

if __name__ == '_main_':
    app.run(debug=True)
# End of file