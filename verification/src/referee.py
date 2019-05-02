from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "sun_angle"
    FUNCTION_NAMES = {
        "python_3": "sun_angle",
        "js_node": "sunAngle"
    }
    ENV_COVERCODE = {
        
    }