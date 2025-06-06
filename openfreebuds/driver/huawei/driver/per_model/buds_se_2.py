from openfreebuds.driver.huawei.driver.generic import OfbDriverHuaweiGeneric
from openfreebuds.driver.huawei.handler import *


class OfbDriverHuaweiSe2(OfbDriverHuaweiGeneric):
    def __init__(self, address):
        super().__init__(address)
        self._spp_service_port = 1
        self.handlers = [
            OfbHuaweiLogsHandler(),
            OfbHuaweiInfoHandler(),
            OfbHuaweiBatteryHandler(),
            OfbHuaweiActionDoubleTapHandler(w_in_call=True),
            OfbHuaweiActionTripleTapHandler(),
            OfbHuaweiActionLongTapSplitHandler(w_left=False, w_anc=False, w_in_call=True),
            OfbHuaweiEqualizerPresetHandler(w_presets={
                1: "default",
                2: "hardbass",
                3: "treble",
                9: "voices",
            }),
            OfbHuaweiLowLatencyPreferenceHandler(),
        ]
