##########################################################################
#  
#  Copyright (c) 2011, Image Engine Design Inc. All rights reserved.
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#  
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#  
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
##########################################################################

from __future__ import with_statement

import IECore

import Gaffer
import GafferUI

class ParameterisedHolderNodeUI( GafferUI.NodeUI ) :

	def __init__( self, node ) :
	
		GafferUI.NodeUI.__init__( self, node )

	def _build( self ) :
		
		infoRow = GafferUI.ListContainer( orientation = GafferUI.ListContainer.Orientation.Horizontal )
		
		infoRow.append( GafferUI.Spacer( IECore.V2i( 10 ) ), expand=True )
		
		infoIcon = GafferUI.Image( "info.png" )
		infoIcon.setToolTip( self._node().getParameterised()[0].description )
		infoRow.append( infoIcon )
		
		self._addWidget( infoRow )
		
		with self._scrollable() :
			with self._collapsible( label = "Parameters", collapsed = False ) :
				self._addParameterWidgets()

	def _addParameterWidgets( self ) :
	
		for p in self._node()["parameters"].children() :
			self.__addParameterWidgetsWalk( p )
	
	def __addParameterWidgetsWalk( self, plug ) :
	
		if plug.typeId()==Gaffer.CompoundPlug.staticTypeId() :
			with self._collapsible( label = IECore.CamelCase.toSpaced( plug.getName() ), collapsed=True ) :
				for p in plug.children() :
					self.__addParameterWidgetsWalk( p )
		else :
			self._addPlugWidget( plug )
			
GafferUI.NodeUI.registerNodeUI( Gaffer.ParameterisedHolderNode.staticTypeId(), ParameterisedHolderNodeUI )