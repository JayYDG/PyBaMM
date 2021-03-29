#
# Test full concentration submodel
#

import pybamm
import tests
import unittest


class TestFull(unittest.TestCase):
    def test_public_functions(self):
        param = pybamm.LeadAcidParameters()
        a = pybamm.Scalar(1)
        variables = {
            "Separator tortuosity": pybamm.FullBroadcast(
                a, "separator", "current collector"
            ),
            "Positive electrode tortuosity": pybamm.FullBroadcast(
                a, "positive electrode", "current collector"
            ),
            "Separator porosity": pybamm.FullBroadcast(
                a, "separator", "current collector"
            ),
            "Positive electrode porosity": pybamm.FullBroadcast(
                a, "positive electrode", "current collector"
            ),
            "Separator porosity change": pybamm.FullBroadcast(
                a, "separator", "current collector"
            ),
            "Positive electrode porosity change": pybamm.FullBroadcast(
                a, "positive electrode", "current collector"
            ),
            "Volume-averaged velocity": a,
            "Negative electrode interfacial current density": pybamm.FullBroadcast(
                a, "negative electrode", "current collector"
            ),
            "Positive electrode interfacial current density": pybamm.FullBroadcast(
                a, "positive electrode", "current collector"
            ),
            "Positive electrode oxygen interfacial current "
            "density": pybamm.FullBroadcast(
                a, "positive electrode", "current collector"
            ),
        }
        submodel = pybamm.oxygen_diffusion.Full(param)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
