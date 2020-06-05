# Sobot Rimulator - A Robot Programming Tool (Modified Version)
# Copyright (C) 2013-2014 Nicholas S. D. McCrea
# Modified by Lorena B. Bassani
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Email lorenabassani12@gmail.com for questions, comments, or to report bugs.


from srimulatorcore.rimulators_samples.rimulator import Rimulator
from srimulatorgtk.window import SobotRimulatorWindow
from srimulatorcore.sobots_samples.kheperaiii.kheperaiii import Kheperaiii

rimulator = Rimulator()
rimulator.add_robot([Kheperaiii, [1.0, -0.1]])
window = SobotRimulatorWindow(rimulator)
window.start_sobot_rimulator()