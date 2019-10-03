from research.services.solar import SolarService


def test_solar_service_is_efficient_false():
    not_efficient = 0.07
    solar_service = SolarService('fake_data_dont_matter')
    assert solar_service._is_efficient(not_efficient) == False


def test_solar_service_is_efficient_true():
    efficient = .35
    solar_service = SolarService('fake_data_dont_matter')
    assert solar_service._is_efficient(efficient) == True


def test_solar_service_get_efficiency_labels():
    assert SolarService.EFFICIENCY_LABELS[0] == 'Known Inefficient'
    assert SolarService.EFFICIENCY_LABELS[1] == 'Known Efficient'
    assert SolarService.EFFICIENCY_LABELS[2] == 'Exceeds Efficiency Standards'


def test_solar_service_name_exists():
    fake_name = 'fake'
    solar_service = SolarService({'name': fake_name})
    assert solar_service.name == fake_name


# TODO: Finish me
def test_solar_service_panel_efficiency():
    sun_efficiency = 1000  # Should match SolarService.POWER_OF_THE_SUN
    sample_voltage = 50
    sample_current = 5

    known_efficiency = sun_efficiency
    pass
