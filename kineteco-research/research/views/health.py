from flask import jsonify
from flask_restplus import Resource

from research import monitoring_namespace


@monitoring_namespace.route('/status')
class HealthCheck(Resource):
    def get(self):
        return jsonify({'status': 'OK'})