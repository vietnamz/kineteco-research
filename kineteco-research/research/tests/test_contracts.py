import requests
import atexit

from pact import Consumer, Provider
from pytest import mark


PANEL_EFFICIENCY = 'http://localhost:5000/solar/panel_efficiency'


def get_panel_efficiency(model):
    """Fetch the panel efficiency of a known inefficient panel"""
    payload = {"voltage": 50, "current": 0, "name": model}
    return requests.get(
        PANEL_EFFICIENCY,
        params=payload,
        headers={'Content-Type': 'application/json'}
    ).json()


pact = Consumer('Installation Support Service').has_pact_with(Provider('Research Service'), port=5000)
pact.start_service()
atexit.register(pact.stop_service)


@mark.contract
def test_panel_efficiency_contract():
    model = 'fake'
    model_efficiency = 'Known Inefficient'
    panel_efficiency = 'Inefficient'

    expected = {
        "model": model,
        "model_efficiency": model_efficiency,
        "panel_efficiency": panel_efficiency
    }

    pact.given(
        'a url'
    ).upon_receiving(
        'a request for fake panel with voltage 50 and current 0'
    ).with_request(
         'get',
         '/solar/panel_efficiency',
         headers={'Content-Type': 'application/json'}
     ).will_respond_with(200, body=expected)

    with pact:
      result = get_panel_efficiency('fake')

    assert result == expected