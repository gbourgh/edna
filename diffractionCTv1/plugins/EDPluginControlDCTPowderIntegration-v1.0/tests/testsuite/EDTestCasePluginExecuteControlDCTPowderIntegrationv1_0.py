#
#    Project: DiffractionCTv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jerome Kieffer (kieffer@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
#from EDUtilsPath                         import EDUtilsPath
from EDUtilsFile                         import EDUtilsFile

class EDTestCasePluginExecuteControlDCTPowderIntegrationv1_0( EDTestCasePluginExecute ):
    """
    """
    
    def __init__( self, _edStringTestName = None):
        """
        """
        EDTestCasePluginExecute.__init__( self, "EDPluginControlDCTPowderIntegrationv1_0", "EDPluginControlDCTPowderIntegration-v1.0", _edStringTestName )

        self.setDataInputFile( os.path.join( self.getPluginTestsDataHome(), \
                                                      "XSDataInputPowderIntegration_reference.xml" ) )
        
        self.setReferenceDataOutputFile( os.path.join( self.getPluginTestsDataHome(), \
                                                                "XSDataResultPowderIntegration_reference.xml"))

        self.m_edObtainedOutputDataFile = self.getPluginName() + "_output.xml"
        
        self.m_iNoErrorMessages = 0
        self.m_iNoWarningMessages = 0        
                 

    def preProcess( self ):
        """
        """
        EDTestCasePluginExecute.preProcess( self )
        self.loadTestImage( [ "test_completed.edf" ] )

        
    def testExecute( self ):
        """
        """ 
        self.run()
        
        # Checks that there are no error messages
        
        plugin = self.getPlugin()

        EDVerbose.DEBUG("Checking error messages...")
        EDAssert.equal( self.m_iNoErrorMessages, self.getErrorMessages().getNumberObjects() )
            
        EDVerbose.DEBUG("Checking warning messages...")
        EDAssert.equal( self.m_iNoWarningMessages, self.getWarningMessages().getNumberObjects() )
        # Checking obtained results
        xsDataResults = plugin.getDataOutput()
        edStringPathToOutput = xsDataResults.getIntegratedIntensities().getPath().getValue()
        edStringDataObtained = EDUtilsFile.readFile( edStringPathToOutput )
        edStringDataReference = EDUtilsFile.readFile( os.path.join( self.getPluginTestsDataHome(), \
                                                                             "Reference_powder_diffraction.cif" ) )
        #too pointilleux
        #EDAssert.equal( edStringDataReference, edStringDataObtained )


##############################################################################

    def process( self ):
        """
        """
        self.addTestMethod( self.testExecute )

        
        
##############################################################################


if __name__ == '__main__':

    edTestCasePluginExecuteControlDCTPowderIntegrationv1_0 = EDTestCasePluginExecuteControlDCTPowderIntegrationv1_0( "EDTestCasePluginExecuteControlDCTPowderIntegrationv1_0" )
    edTestCasePluginExecuteControlDCTPowderIntegrationv1_0.execute()
