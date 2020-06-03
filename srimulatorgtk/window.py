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


import pygtk
pygtk.require( '2.0' )
import gtk
import gobject

# import gui classes
from .viewer import Viewer


class SobotRimulatorWindow:

  def __init__( self, rimulator ):
    
    self.rimulator = rimulator

    # create the GUI
    self.viewer = Viewer( self )

    self.rimulator.add_viewer(self.viewer)
    
    # gtk simulation event source - for simulation control
    self.sim_event_source = gobject.idle_add( self.initialize_sim, True ) # we use this opportunity to initialize the sim
    
    
  def initialize_sim( self, random=False ):
    # reset the viewer
    self.viewer.control_panel_state_init()
    
    # create the simulation world
    self.rimulator.initialize_sim( random )
    
    # render the initial world
    self.draw_world()
    
    
  def play_sim( self ):
    self.rimulator.play_sim()
    self.run_sim()
    self.viewer.control_panel_state_playing()
    
    
  def pause_sim( self ):
    if self.rimulator.pause_sim():
      gobject.source_remove( self.sim_event_source )
      self.viewer.control_panel_state_paused()
    
    
  def step_sim_once( self ):
    self.rimulator.pause_sim()
    self.step_sim()
    
    
  def end_sim( self, alert_text='' ):
    self.rimulator.end_sim()
    gobject.source_remove( self.sim_event_source )
    self.viewer.control_panel_state_finished( alert_text )
    
    
  def reset_sim( self ):
    self.pause_sim()
    self.initialize_sim()
    
    
  def save_map( self, filename ):
    self.rimulator.save_map( filename )
    
    
  def load_map( self, filename ):
    self.rimulator.load_map( filename )
    self.reset_sim()
    
    
  def random_map( self ):
    self.pause_sim()
    self.initialize_sim( random = True )
    
    
  def draw_world( self ):
    self.viewer.new_frame()                 # start a fresh frame
    self.rimulator.draw_world( )   # draw the world onto the frame
    self.viewer.draw_frame()                # render the frame
    
    
  def run_sim( self ):
    self.sim_event_source = gobject.timeout_add( int( self.rimulator.period * 1000 ), self.run_sim )
    self.step_sim()
    
    
  def step_sim( self ):
    # increment the simulation
    self.rimulator.step_sim()
      
    # draw the resulting world
    self.draw_world()

  def start_sobot_rimulator(self):
    # start gtk
    gtk.main()