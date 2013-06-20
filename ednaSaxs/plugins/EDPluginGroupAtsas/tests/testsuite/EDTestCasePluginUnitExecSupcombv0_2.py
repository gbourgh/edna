#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) DLS

#    Principal author:       irakli
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

__author__ = "irakli"
__license__ = "GPLv3+"
__copyright__ = "DLS"

from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataEdnaSaxs import XSDataInputSupcomb
from XSDataCommon import XSDataFile

class EDTestCasePluginUnitExecSupcombv0_2(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Supcombv0_2
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginExecSupcombv0_2")


    def testCheckParameters(self):
        xsDataInput = XSDataInputSupcomb()
        xsDataInput.templateFile = XSDataFile()
        xsDataInput.superimposeFile = XSDataFile()
        edPluginExecSupcomb = self.createPlugin()
        edPluginExecSupcomb.setDataInput(xsDataInput)
        edPluginExecSupcomb.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)



if __name__ == '__main__':

    edTestCasePluginUnitExecSupcombv0_2 = EDTestCasePluginUnitExecSupcombv0_2("EDTestCasePluginUnitExecSupcombv0_2")
    edTestCasePluginUnitExecSupcombv0_2.execute()
