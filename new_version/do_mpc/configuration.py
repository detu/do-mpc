#
#   This file is part of do-mpc
#
#   do-mpc: An environment for the easy, modular and efficient implementation of
#        robust nonlinear model predictive control
#
#   Copyright (c) 2014-2019 Sergio Lucia, Alexandru Tatulea-Codrean
#                        TU Dortmund. All rights reserved
#
#   do-mpc is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as
#   published by the Free Software Foundation, either version 3
#   of the License, or (at your option) any later version.
#
#   do-mpc is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with do-mpc.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
from casadi import *
from casadi.tools import *
import pdb

class configuration:
    def __init__(self, simulator, optimizer, estimator, x0=None):
        self.simulator = simulator
        self.optimizer = optimizer
        self.estimator = estimator

        if x0:
            # Set global intial condition.
            self.simulator.data.update('_x', x0)
            self.optimizer.data.update('_x', x0)
            self.estimator.data.update('_x', x0)
        else:
            # Set individual initial condition.
            self.simulator.data.update(_x = self.simulator._x0.cat)
            self.optimizer.data.update(_x = self.simulator._x0.cat)
            self.estimator.data.update(_x =  self.simulator._x0.cat)


    def make_step_optimizer(self):
        None

    def make_step_simulator(self):
        tvp_now = self.simulator.tvp_fun(self.simulator._t0)
        p_now = self.simulator.p_fun(self.simulator._t0)
        x0 = self.simulator._x0




    def make_step_observer(self):
        None