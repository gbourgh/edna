#
#coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, 2010
#
#    Principal author:       Jérôme Kieffer
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
from XSDataBioSaxsv1_0 import XSDataResultBioSaxsAzimutIntv1_0

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os, sys
from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute
from EDFactoryPluginStatic               import EDFactoryPluginStatic


EDFactoryPluginStatic.loadModule("EDInstallNumpyv1_3")
EDFactoryPluginStatic.loadModule("EDInstallSpecClient")
EDFactoryPluginStatic.loadModule("EDInstallEdfFile")
EDFactoryPluginStatic.loadModule("EDInstallPILv1_1_7")
EDFactoryPluginStatic.loadModule("EDInstallFabio_v0_0_7")

import EdfFile


class EDTestCasePluginExecuteBioSaxsAzimutIntv1_0(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginBioSaxsAzimutIntv1_0")
#        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
#                                               "XSConfiguration_<basePluginName>.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputBioSaxsAzimutIntv1_0_reference.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultBioSaxsAzimutIntv1_0_reference.xml"))

    def preProcess(self):
        """
        PreProcess of the execution test: download a set of images  from http://www.edna-site.org
        and remove any existing output file 
        """
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "bioSaxsMask.edf", "bioSaxsNormalized.edf", "bioSaxsIntegrated.dat", "bioSaxsIntegrated.edf", "bioSaxsCorrected.edf"])
        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
        EDVerbose.DEBUG("strExpectedOutput:" + strExpectedOutput)
        xsDataResultReference = XSDataResultBioSaxsAzimutIntv1_0.parseString(strExpectedOutput)
        self.integratedCurve = xsDataResultReference.getIntegratedCurve().getPath().getValue()
        EDVerbose.DEBUG("Output file is %s" % self.integratedCurve)
        if not os.path.isdir(os.path.dirname(self.integratedCurve)):
            os.makedirs(os.path.dirname(self.integratedCurve))
        if os.path.isfile(self.integratedCurve):
            EDVerbose.DEBUG(" Output Integrated Curve file exists %s, I will remove it" % self.integratedCurve)
            os.remove(self.integratedCurve)

        self.integratedImage = xsDataResultReference.getIntegratedImage().getPath().getValue()
        EDVerbose.DEBUG("Output Integrated Image file is %s" % self.integratedImage)
        if not os.path.isdir(os.path.dirname(self.integratedImage)):
            os.makedirs(os.path.dirname(self.integratedImage))
        if os.path.isfile(self.integratedImage):
            EDVerbose.DEBUG(" Output Integrated Image file exists %s, I will remove it" % self.integratedImage)
            os.remove(self.integratedImage)

        self.correctedImage = xsDataResultReference.getCorrectedImage().getPath().getValue()
        EDVerbose.DEBUG("Output Corrected Image file is %s" % self.correctedImage)
        if not os.path.isdir(os.path.dirname(self.correctedImage)):
            os.makedirs(os.path.dirname(self.correctedImage))
        if os.path.isfile(self.correctedImage):
            EDVerbose.DEBUG(" Output Corrected Image file exists %s, I will remove it" % self.correctedImage)
            os.remove(self.correctedImage)

    def testExecute(self):
        """
        """
        self.run()
        plugin = self.getPlugin()

################################################################################
# Compare XSDataResults
################################################################################

        strExpectedOutput = self.readAndParseFile (self.getReferenceDataOutputFile())
#        strObtainedOutput = self.readAndParseFile (self.m_edObtainedOutputDataFile)
        EDVerbose.DEBUG("Checking obtained result...")
        xsDataResultReference = XSDataResultBioSaxsAzimutIntv1_0.parseString(strExpectedOutput)
        xsDataResultObtained = plugin.getDataOutput()
        EDAssert.strAlmostEqual(xsDataResultReference.marshal(), xsDataResultObtained.marshal(), "XSDataResult output are the same", _strExcluded="bioSaxs")

################################################################################
# Compare spectrum ascii Files
################################################################################

        outputData = os.linesep.join([i for i in open(xsDataResultObtained.getIntegratedCurve().getPath().getValue()) if not i.startswith("#")])
        referenceData = os.linesep.join([i for i in open(os.path.join(self.getTestsDataImagesHome(), "bioSaxsIntegrated.dat")) if not i.startswith("#")])

        EDAssert.strAlmostEqual(referenceData, outputData, _strComment="3column ascii spectra files are the same", _fRelError=0.1, _fAbsError=0.1, _strExcluded="bioSaxs")

################################################################################
# Compare images 
################################################################################
        edfObt = EdfFile.EdfFile(xsDataResultObtained.getCorrectedImage().getPath().getValue())
        edfRef = EdfFile.EdfFile(os.path.join(self.getTestsDataImagesHome(), "bioSaxsCorrected.edf"))
        outputData = edfObt.GetData(0)
        referenceData = edfRef.GetData(0)
        EDAssert.arraySimilar(outputData, referenceData , _fAbsMaxDelta=0.1, _fScaledMaxDelta=0.05, _strComment="Corrected images are the same")

        headerRef = edfRef.GetHeader(0)
        headerObt = edfObt.GetHeader(0)
        keysRef = headerRef.keys()
        keysObt = headerObt.keys()
        keysRef.sort()
        keysObt.sort()
        for key in ["HeaderID", "Image", 'EDF_BinarySize', "EDF_DataBlockID", "EDF_HeaderSize", "filename" ]:
            if key in keysObt: keysObt.remove(key)
            if key in keysRef: keysRef.remove(key)
        EDAssert.equal(keysRef, keysObt, _strComment="Same keys in the header dictionary for Corrected Images")
        for key in keysRef:
            EDAssert.strAlmostEqual(headerRef[key], headerObt[key], _strComment="header value in Corrected %s are the same" % key, _strExcluded="bioSaxs")

        edfObt = EdfFile.EdfFile(os.path.join(self.getTestsDataImagesHome(), "bioSaxsIntegrated.edf"))
        edfRef = EdfFile.EdfFile(xsDataResultObtained.getIntegratedImage().getPath().getValue())
        outputData = edfObt.GetData(0)
        referenceData = edfRef.GetData(0)
        EDAssert.arraySimilar(outputData, referenceData , _fScaledMaxDelta=0.05, _strComment="Integrated images are the same")

        headerRef = edfRef.GetHeader(0)
        headerObt = edfObt.GetHeader(0)
        keysRef = headerRef.keys()
        keysObt = headerObt.keys()
        keysRef.sort()
        keysObt.sort()
        for key in ["HeaderID", "Image", 'EDF_BinarySize', "EDF_DataBlockID", "EDF_HeaderSize", "filename" ]:
            if key in keysObt: keysObt.remove(key)
            if key in keysRef: keysRef.remove(key)
        EDAssert.equal(keysRef, keysObt, _strComment="Same keys in the header dictionary for Integrated Images")
        for key in keysRef:
            EDAssert.strAlmostEqual(headerRef[key], headerObt[key], _strComment="header value in Integrated %s are the same" % key, _strExcluded="bioSaxs")




    def process(self):
        """
        """
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteBioSaxsAzimutIntv1_0 = EDTestCasePluginExecuteBioSaxsAzimutIntv1_0("EDTestCasePluginExecuteBioSaxsAzimutIntv1_0")
    edTestCasePluginExecuteBioSaxsAzimutIntv1_0.execute()
