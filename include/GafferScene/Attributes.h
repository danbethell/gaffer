//////////////////////////////////////////////////////////////////////////
//  
//  Copyright (c) 2012, John Haddon. All rights reserved.
//  
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//  
//      * Redistributions of source code must retain the above
//        copyright notice, this list of conditions and the following
//        disclaimer.
//  
//      * Redistributions in binary form must reproduce the above
//        copyright notice, this list of conditions and the following
//        disclaimer in the documentation and/or other materials provided with
//        the distribution.
//  
//      * Neither the name of John Haddon nor the names of
//        any other contributors to this software may be used to endorse or
//        promote products derived from this software without specific prior
//        written permission.
//  
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//  
//////////////////////////////////////////////////////////////////////////

#ifndef GAFFERSCENE_ATTRIBUTES_H
#define GAFFERSCENE_ATTRIBUTES_H

#include "GafferScene/SceneElementProcessor.h"
#include "GafferScene/ParameterListPlug.h"

namespace GafferScene
{

class Attributes : public SceneElementProcessor
{

	public :

		Attributes( const std::string &name=staticTypeName() );
		virtual ~Attributes();

		IE_CORE_DECLARERUNTIMETYPEDEXTENSION( Attributes, AttributesTypeId, SceneElementProcessor );
		
		GafferScene::ParameterListPlug *attributesPlug();
		const GafferScene::ParameterListPlug *attributesPlug() const;
		
		virtual void affects( const Gaffer::ValuePlug *input, AffectedPlugsContainer &outputs ) const;
		
	protected :
	
		/// Can be used by derived classes to declare an attributes plug which isn't dynamic, so
		/// they can add a predefined set of static attributes at construction.
		Attributes( const std::string &name, Gaffer::Plug::Flags attributesPlugFlags );
				
		virtual IECore::ConstCompoundObjectPtr processAttributes( const ScenePath &path, const Gaffer::Context *context, IECore::ConstCompoundObjectPtr inputAttributes ) const;
	
};

} // namespace GafferScene

#endif // GAFFERSCENE_ATTRIBUTES_H