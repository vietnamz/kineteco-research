from flask import jsonify, request
from flask_restplus import Resource

from research import solar_namespace
from research.services.solar import SolarService


@solar_namespace.route('/panel_efficiency')
class PanelEfficiency(Resource):
    @solar_namespace.param('current', type=float, description='The electrical current')
    @solar_namespace.param('name', type=str, description='The name of the solar panel model')
    @solar_namespace.param('voltage', type=float, description='The voltage of the solar panel')
    def get(self):
        data = request.args.to_dict()
        print(data)
        if _validate_request_data(data):
            try:
                data = _translate_request_data(data)
            except ValueError:
                return return_non_200(400, 'You must provide valid numeric data for voltage and current')

            solar_service = SolarService(data)

            try:
                is_efficient, is_model_efficient = solar_service.meets_efficiency_standards()
            except Exception as e:
                return return_non_200(500, str(e))

            return jsonify({
                'model': solar_service.name,
                'model_efficiency': is_model_efficient,
                'panel_efficiency': "Efficient" if is_efficient else "Inefficient"
            })
        else:
            return return_non_200(400, 'You must provide data')


def _validate_request_data(data):
    if 'current' in data.keys() and 'voltage' in data.keys() and 'name' in data.keys():
        return True
    return False


def _translate_request_data(request_data):
    translated_data = {}
    for key, value in request_data.items():
        if key in ('current', 'voltage'):
            value = float(value)
        translated_data[key] = value
    return translated_data


def return_non_200(error_code, error_message):
    response = jsonify({
        'error': error_message
    })
    response.status_code = error_code
    return response