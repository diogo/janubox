from flask import Flask
from flask.ext import restful.Api
import janubox.server.add_resources
from janubox.server.database import database, DATABASE_URI

app = Flask(__name__)
api = restful.Api(app)

janubox.server.add_resources(api)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
database.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
