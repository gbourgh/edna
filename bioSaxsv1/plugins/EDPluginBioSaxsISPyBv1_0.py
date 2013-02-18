# coding: utf8
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 ESRF
#
#    Principal author:        Al. de Maria
#                             Jerome Kieffer
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
from __future__ import with_statement
__author__ = "Al. de Maria"
__license__ = "GPLv3+"
__copyright__ = "2012 ESRF"
__status__ = "Development"
__date__ = "20130124"

import os, shutil
from EDPluginControl        import EDPluginControl
from EDFactoryPlugin        import edFactoryPlugin
from EDConfiguration        import EDConfiguration
from suds.client            import Client
from suds.transport.http    import HttpAuthenticated
edFactoryPlugin.loadModule("XSDataBioSaxsv1_0")
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsISPyBv1_0, XSDataResultBioSaxsISPyBv1_0, XSDataBioSaxsSample, XSDataGnom
from XSDataEdnaSaxs         import XSDataAutoRg
from XSDataCommon           import XSDataInteger, XSDataDouble, XSDataString, XSDataFile, XSPluginItem, XSDataLength, XSDataBoolean, XSDataStatus


class EDPluginBioSaxsISPyBv1_0(EDPluginControl):

    URL = None
    CONF_URL_KEY = "url"
    CONF_URL_DEFAULT = "http://pcantolinos:8080/ispyb-ejb3/ispybWS/ToolsForBiosaxsWebService?wsdl"


    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsISPyBv1_0)
        self.dataBioSaxsSample = None
        self.dataAutoRg = None
        self.dataGnom = None

        # Params to be sent and I dont know them
        self.volume = None
        self.framesAverage = None
        self.framesMerged = None
        self.filename = None
        self.rg = None
        self.rgStdev = None
        self.i0 = None
        self.i0Stdev = None
        self.firstPointUsed = None
        self.lastPointUsed = None
        self.quality = None
        self.isagregated = None
        self.code = None
        self.concentration = None
        self.gnomFile = None
        self.rgGuinier = None
        self.rgGnom = None
        self.dmax = None
        self.total = None
        self.pyarchfiles = []
        self.lstError = []


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsISPyBv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.sample, "Sample is None")

    def configure(self):
        """
        Configures the ISPyB webservice access with the following parameters:
         - The "url" key from config file        
        """
        EDPluginControl.configure(self)
        if self.URL is None:
            self.DEBUG("EDPluginBioSaxsISPyBv1_0.configure")
            url = self.config.get(self.CONF_URL_KEY, None)
            if url:
                self.__class__.URL = url
            else:
                self.__class__.URL = self.CONF_URL_DEFAULT


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)

        # Initializing webservices
        self.DEBUG("EDPluginBioSaxsISPyBv1_0.preProcess")
        self.dataBioSaxsSample = self.dataInput.sample
        user = None
        password = ""
        if self.dataBioSaxsSample:
            if self.dataBioSaxsSample.login:
                user = self.dataBioSaxsSample.login.value
                password = self.dataBioSaxsSample.passwd.value
        if not user:
            self.ERROR("No login/password information in sample configuration. Giving up.")
            self.setFailure()
            return

        # I don't trust in this authentication....

        self.httpAuthenticatedToolsForBiosaxsWebService = HttpAuthenticated(username=user, password=password)
        self.client = Client(self.URL, transport=self.httpAuthenticatedToolsForBiosaxsWebService, cache=None)

        self.dataAutoRg = self.dataInput.autoRg
        self.dataGnom = self.dataInput.gnom

        # Params to be sent and I dont know them
        if self.dataInput.volume:
            self.volume = self.dataInput.volume.value
        if self.dataInput.frameAverage:
            self.framesAverage = self.dataInput.frameAverage.value
        if self.dataInput.frameMerged:
            self.framesMerged = self.dataInput.frameMerged.value
	if self.dataAutoRg:
           autoRg = self.dataAutoRg
           if autoRg.filename and autoRg.filename.path:
		self.filename = autoRg.filename.path.value
           if autoRg.rg:
                self.rg = autoRg.rg.value
           if autoRg.rgStdev:
                self.rgStdev = autoRg.rgStdev.value
           if autoRg.i0:
                self.i0 = autoRg.i0.value
           if autoRg.i0Stdev:
                self.i0Stdev = autoRg.i0Stdev.value
           if autoRg.firstPointUsed:
                self.firstPointUsed = autoRg.firstPointUsed.value
           if autoRg.lastPointUsed:
                self.lastPointUsed = autoRg.lastPointUsed.value
           if autoRg.quality:
                self.quality = autoRg.quality.value
           if autoRg.isagregated:
                self.isagregated = autoRg.isagregated.value
        if self.dataBioSaxsSample:
            if self.dataBioSaxsSample.code:
                self.code = self.dataBioSaxsSample.code.value
            if self.dataBioSaxsSample.concentration:
                self.concentration = self.dataBioSaxsSample.concentration.value
        if self.dataGnom:
            if self.dataGnom.gnomFile:
               self.gnomFile = self.dataGnom.gnomFile.path.value
            if self.dataGnom.rgGuinier:
               self.rgGuinier = self.dataGnom.rgGuinier.value
            if self.dataGnom.rgGnom:
               self.rgGnom = self.dataGnom.rgGnom.value
            if self.dataGnom.dmax:
               self.dmax = self.dataGnom.dmax.value
            if self.dataGnom.total:
               self.total = self.dataGnom.total.value


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsISPyBv1_0.process")
        try:
            self.copy_to_pyarch()
        except Exception as error:
            strErrorMessage = "Error while copying to pyarch: %s" % error
            self.ERROR(strErrorMessage)
            self.lstError.append(strErrorMessage)
        if self.dataInput.sample.collectionOrder is not None:
            collectionOrder = str(self.dataInput.sample.collectionOrder.value)
        else:
            collectionOrder = "-1"
        try:
            self.client.service.storeDataAnalysisResultByMeasurementId(
                                    self.dataBioSaxsSample.measurementID.value,
                                    self.filename,
                                    self.rg,
                                    self.rgStdev,
                                    self.i0,
                                    self.i0Stdev,
                                    self.firstPointUsed,
                                    self.lastPointUsed,
                                    self.quality,
                                    self.isagregated,
                                    self.code,
                                    self.concentration,
                                    self.gnomFile,
                                    self.rgGuinier,
                                    self.rgGnom,
                                    self.dmax,
                                    self.total,
                                    self.volume,
                                    self.framesAverage,
                                    self.framesMerged,
                                    ", ".join(self.pyarchfiles),
                                    collectionOrder,
                                    "param3",
                                    "param4"
                                    )
        except Exception, error:
            strError = "ISPyB error: %s" % error
            self.ERROR(strError)
            self.setFailure()


    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsISPyBv1_0.postProcess")
        # Create some output data

        xsDataResult = XSDataResultBioSaxsISPyBv1_0(status=XSDataStatus(executiveSummary=XSDataString(os.linesep.join(self.lstError))))
        self.setDataOutput(xsDataResult)

    def copy_to_pyarch(self):
        if self.dataInput.sample.ispybDestination:
            pyarch = os.path.join(self.dataInput.sample.ispybDestination.path.value, "1d")
            try:
                if not os.path.isdir(pyarch):
                    os.makedirs(pyarch)
            except IOError as error:
                ermsg = "Error while directory creation in pyarch: %s " % error
                self.lstError.append(ermsg)
                self.WARNING(errmsg)
            for xsdfile in self.dataInput.curves:
                if xsdfile:
                    afile = xsdfile.path.value
                    if os.path.exists(afile):
                        try:
                            shutil.copy(afile, pyarch)
                        except IOError as error:
                            ermsg = "Error while copying %s to pyarch: %s " % (afile, error)
                            self.lstError.append(ermsg)
                            self.WARNING(errmsg)
                        else:
                            self.pyarchfiles.append(os.path.join(pyarch, os.path.basename(afile)))
