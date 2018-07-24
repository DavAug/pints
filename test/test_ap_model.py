#!/usr/bin/env python3
#
# Tests if the Beeler-Reuter AP (toy) model works.
#
# This file is part of PINTS.
#  Copyright (c) 2017-2018, University of Oxford.
#  For licensing information, see the LICENSE file distributed with the PINTS
#  software package.
#
import unittest
import numpy as np
import pints
import pints.toy


class TestActionPotentialModel(unittest.TestCase):
    """
    Tests if the Beeler-Reuter AP (toy) model works.
    """

    def test_ap(self):
        model = pints.toy.ActionPotentialModel()
        p0 = model.suggested_parameters()
        self.assertEqual(len(p0), model.n_parameters())
        times = model.suggested_times()
        self.assertTrue(np.all(times[1:] > times[:-1]))
        values = model.simulate(p0, times)
        self.assertEqual(len(times), len(values))

        # Test setting and getting init cond.
        self.assertFalse(np.all(model.initial_conditions() == [-80, 1e-5]))
        model.set_initial_conditions([-80, 1e-5])
        self.assertTrue(np.all(model.initial_conditions() == [-80, 1e-5]))

        # Initial conditions cannot be negative
        self.assertRaises(ValueError, pints.toy.ActionPotentialModel,
                          [-80, -1])


if __name__ == '__main__':
    unittest.main()
