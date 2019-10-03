PANELS = [
    {'name': 'fake', 'efficiency_status': 0},
    {'name': 'K-Eco 180', 'efficiency_status': 0},
    {'name': 'K-Eco 200', 'efficiency_status': 0},
    {'name': 'K-Eco 225', 'efficiency_status': 0},
    {'name': 'K-Eco 250', 'efficiency_status': 1},
    {'name': 'K-Eco 250x', 'efficiency_status': 1},
    {'name': 'K-Eco 275', 'efficiency_status': 0},
    {'name': 'K-Eco 300', 'efficiency_status': 1},
    {'name': 'K-Eco 325', 'efficiency_status': 1},
    {'name': 'K-Eco 325x', 'efficiency_status': 2},
    {'name': 'K-Eco 450', 'efficiency_status': 2},
    {'name': 'K-Eco 575', 'efficiency_status': 1},
    {'name': 'K-Eco 625', 'efficiency_status': 1},
    {'name': 'K-Eco 700', 'efficiency_status': 1},
    {'name': 'K-Eco Mini', 'efficiency_status': 1},
    {'name': 'K-Eco phone charger', 'efficiency_status': 0},
]


def main():
    from research.models.solar import SolarPanel

    for panel in PANELS:
        panel = SolarPanel(panel['name'], panel['efficiency_status'])
        panel.save()
