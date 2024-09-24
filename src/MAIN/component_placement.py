import gdsfactory as gf
from gdsfactory.typings import ComponentSpec

import MAIN

def component_placement(
    die: gf.Component,
) -> gf.Component:
    """This function places the components in the DIE"""

    die = gf.get_component(die)
