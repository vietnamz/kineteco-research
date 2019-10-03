from research.models.solar import SolarPanel


class SolarService(object):
    """Service for interacting with solar-related activities
       Currently limited to SolarPanels"""

    POWER_OF_THE_SUN = 1000  # measured in watts per square meter
    EFFICIENCY_LABELS = {
        0: 'Known Inefficient',
        1: 'Known Efficient',
        2: 'Exceeds Efficiency Standards'
    }

    def __init__(self, panel_data):
        self.data = panel_data

    @property
    def name(self):
        return self.data.get('name', 'Unknown')

    @staticmethod
    def _is_efficient(efficiency):
        """Computes whether or not a provided decimal is efficient
           A normal solar cell will exhibit between 10-20% efficiency"""
        return efficiency > .1

    @staticmethod
    def _get_efficiency_label(efficiency_status):
        return SolarService.EFFICIENCY_LABELS[efficiency_status]

    # TODO: Fix me, I don't include panel width and length
    def _panel_efficiency(self):
        """Calculate the efficiency of a solar panel, based on the data provided"""
        useful_cell_power = self.data.get('voltage') * self.data.get('current')
        total_power_in = SolarService.POWER_OF_THE_SUN

        return useful_cell_power / total_power_in

    def meets_efficiency_standards(self):
        """Determines whether or not a panel is efficient as determined by useful power over total power input
            Returns data about both the panel data provided as well as known data about the solar panel model"""
        efficiency = self._panel_efficiency()
        panel_model = SolarPanel.get_by_name(self.data.get('name'))

        if panel_model is not None:
            return self._is_efficient(efficiency), self._get_efficiency_label(panel_model.efficiency_status)
        else:
            raise Exception('Panel model not found in database')
