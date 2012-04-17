#!/usr/bin/env python

#
# Generated Tue Apr 17 10:23::00 2012 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
 "XSDataCommon": "Code/repos/edna/kernel/datamodel", \
}

try:
	from XSDataCommon import XSDataBoolean
	from XSDataCommon import XSDataDouble
	from XSDataCommon import XSDataFile
	from XSDataCommon import XSDataFloat
	from XSDataCommon import XSDataInput
	from XSDataCommon import XSDataInteger
	from XSDataCommon import XSDataResult
	from XSDataCommon import XSDataString
	from XSDataCommon import XSDataVectorDouble
except ImportError as error:
	if strEdnaHome is not None:
		for strXsdName in dictLocation:
			strXsdModule = strXsdName + ".py"
			strRootdir = os.path.dirname(os.path.abspath(os.path.join(strEdnaHome, dictLocation[strXsdName])))
			for strRoot, listDirs, listFiles in os.walk(strRootdir):
				if strXsdModule in listFiles:
					sys.path.append(strRoot)
	else:
		raise error
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataVectorDouble




#
# Support/utility functions.
#

# Compabiltity between Python 2 and 3:
if sys.version.startswith('3'):
	unicode = str
	from io import StringIO
else:
	from StringIO import StringIO


def showIndent(outfile, level):
	for idx in range(level):
		outfile.write(unicode('    '))


def checkType(_strClassName, _strMethodName, _value, _strExpectedType):
	if not _strExpectedType in ["float", "double", "string", "boolean", "integer"]:
		if _value != None:
			if _value.__class__.__name__ != _strExpectedType:
				strMessage = "ERROR! %s.%s argument is not %s but %s" % (_strClassName, _strMethodName, _strExpectedType, _value.__class__.__name__)
				print(strMessage)
				#raise BaseException(strMessage)
#	elif _value is None:
#		strMessage = "ERROR! %s.%s argument which should be %s is None" % (_strClassName, _strMethodName, _strExpectedType)
#		print(strMessage)
#		#raise BaseException(strMessage)


def warnEmptyAttribute(_strName, _strTypeName):
	pass
	#if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
	#		print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

class MixedContainer(object):
	# Constants for category:
	CategoryNone = 0
	CategoryText = 1
	CategorySimple = 2
	CategoryComplex = 3
	# Constants for content_type:
	TypeNone = 0
	TypeText = 1
	TypeString = 2
	TypeInteger = 3
	TypeFloat = 4
	TypeDecimal = 5
	TypeDouble = 6
	TypeBoolean = 7
	def __init__(self, category, content_type, name, value):
		self.category = category
		self.content_type = content_type
		self.name = name
		self.value = value
	def getCategory(self):
		return self.category
	def getContenttype(self, content_type):
		return self.content_type
	def getValue(self):
		return self.value
	def getName(self):
		return self.name
	def export(self, outfile, level, name):
		if self.category == MixedContainer.CategoryText:
			outfile.write(self.value)
		elif self.category == MixedContainer.CategorySimple:
			self.exportSimple(outfile, level, name)
		else:	 # category == MixedContainer.CategoryComplex
			self.value.export(outfile, level, name)
	def exportSimple(self, outfile, level, name):
		if self.content_type == MixedContainer.TypeString:
			outfile.write(unicode('<%s>%s</%s>' % (self.name, self.value, self.name)))
		elif self.content_type == MixedContainer.TypeInteger or \
				self.content_type == MixedContainer.TypeBoolean:
			outfile.write(unicode('<%s>%d</%s>' % (self.name, self.value, self.name)))
		elif self.content_type == MixedContainer.TypeFloat or \
				self.content_type == MixedContainer.TypeDecimal:
			outfile.write(unicode('<%s>%f</%s>' % (self.name, self.value, self.name)))
		elif self.content_type == MixedContainer.TypeDouble:
			outfile.write(unicode('<%s>%g</%s>' % (self.name, self.value, self.name)))

#
# Data representation classes.
#


class XSData2DCoordinates(object):
	def __init__(self, y=None, x=None):
		checkType("XSData2DCoordinates", "Constructor of XSData2DCoordinates", x, "XSDataFloat")
		self.__x = x
		checkType("XSData2DCoordinates", "Constructor of XSData2DCoordinates", y, "XSDataFloat")
		self.__y = y
	def getX(self): return self.__x
	def setX(self, x):
		checkType("XSData2DCoordinates", "setX", x, "XSDataFloat")
		self.__x = x
	def delX(self): self.__x = None
	# Properties
	x = property(getX, setX, delX, "Property for x")
	def getY(self): return self.__y
	def setY(self, y):
		checkType("XSData2DCoordinates", "setY", y, "XSDataFloat")
		self.__y = y
	def delY(self): self.__y = None
	# Properties
	y = property(getY, setY, delY, "Property for y")
	def export(self, outfile, level, name_='XSData2DCoordinates'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSData2DCoordinates'):
		pass
		if self.__x is not None:
			self.x.export(outfile, level, name_='x')
		else:
			warnEmptyAttribute("x", "XSDataFloat")
		if self.__y is not None:
			self.y.export(outfile, level, name_='y')
		else:
			warnEmptyAttribute("y", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'x':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setX(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'y':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setY(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSData2DCoordinates" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSData2DCoordinates' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSData2DCoordinates is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSData2DCoordinates.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSData2DCoordinates()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSData2DCoordinates" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSData2DCoordinates()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSData2DCoordinates

class XSDataXdsCompletenessEntry(object):
	def __init__(self, outer_isig=None, outer_rfactor=None, outer_complete=None, outer_res=None):
		checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_res, "XSDataFloat")
		self.__outer_res = outer_res
		checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_complete, "XSDataFloat")
		self.__outer_complete = outer_complete
		checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_rfactor, "XSDataFloat")
		self.__outer_rfactor = outer_rfactor
		checkType("XSDataXdsCompletenessEntry", "Constructor of XSDataXdsCompletenessEntry", outer_isig, "XSDataFloat")
		self.__outer_isig = outer_isig
	def getOuter_res(self): return self.__outer_res
	def setOuter_res(self, outer_res):
		checkType("XSDataXdsCompletenessEntry", "setOuter_res", outer_res, "XSDataFloat")
		self.__outer_res = outer_res
	def delOuter_res(self): self.__outer_res = None
	# Properties
	outer_res = property(getOuter_res, setOuter_res, delOuter_res, "Property for outer_res")
	def getOuter_complete(self): return self.__outer_complete
	def setOuter_complete(self, outer_complete):
		checkType("XSDataXdsCompletenessEntry", "setOuter_complete", outer_complete, "XSDataFloat")
		self.__outer_complete = outer_complete
	def delOuter_complete(self): self.__outer_complete = None
	# Properties
	outer_complete = property(getOuter_complete, setOuter_complete, delOuter_complete, "Property for outer_complete")
	def getOuter_rfactor(self): return self.__outer_rfactor
	def setOuter_rfactor(self, outer_rfactor):
		checkType("XSDataXdsCompletenessEntry", "setOuter_rfactor", outer_rfactor, "XSDataFloat")
		self.__outer_rfactor = outer_rfactor
	def delOuter_rfactor(self): self.__outer_rfactor = None
	# Properties
	outer_rfactor = property(getOuter_rfactor, setOuter_rfactor, delOuter_rfactor, "Property for outer_rfactor")
	def getOuter_isig(self): return self.__outer_isig
	def setOuter_isig(self, outer_isig):
		checkType("XSDataXdsCompletenessEntry", "setOuter_isig", outer_isig, "XSDataFloat")
		self.__outer_isig = outer_isig
	def delOuter_isig(self): self.__outer_isig = None
	# Properties
	outer_isig = property(getOuter_isig, setOuter_isig, delOuter_isig, "Property for outer_isig")
	def export(self, outfile, level, name_='XSDataXdsCompletenessEntry'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXdsCompletenessEntry'):
		pass
		if self.__outer_res is not None:
			self.outer_res.export(outfile, level, name_='outer_res')
		else:
			warnEmptyAttribute("outer_res", "XSDataFloat")
		if self.__outer_complete is not None:
			self.outer_complete.export(outfile, level, name_='outer_complete')
		else:
			warnEmptyAttribute("outer_complete", "XSDataFloat")
		if self.__outer_rfactor is not None:
			self.outer_rfactor.export(outfile, level, name_='outer_rfactor')
		else:
			warnEmptyAttribute("outer_rfactor", "XSDataFloat")
		if self.__outer_isig is not None:
			self.outer_isig.export(outfile, level, name_='outer_isig')
		else:
			warnEmptyAttribute("outer_isig", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outer_res':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setOuter_res(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outer_complete':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setOuter_complete(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outer_rfactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setOuter_rfactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'outer_isig':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setOuter_isig(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXdsCompletenessEntry" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXdsCompletenessEntry' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXdsCompletenessEntry is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXdsCompletenessEntry.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXdsCompletenessEntry()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXdsCompletenessEntry" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXdsCompletenessEntry()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXdsCompletenessEntry

class XSDataXscale(object):
	def __init__(self, res=None, path=None):
		checkType("XSDataXscale", "Constructor of XSDataXscale", path, "XSDataString")
		self.__path = path
		checkType("XSDataXscale", "Constructor of XSDataXscale", res, "XSDataFloat")
		self.__res = res
	def getPath(self): return self.__path
	def setPath(self, path):
		checkType("XSDataXscale", "setPath", path, "XSDataString")
		self.__path = path
	def delPath(self): self.__path = None
	# Properties
	path = property(getPath, setPath, delPath, "Property for path")
	def getRes(self): return self.__res
	def setRes(self, res):
		checkType("XSDataXscale", "setRes", res, "XSDataFloat")
		self.__res = res
	def delRes(self): self.__res = None
	# Properties
	res = property(getRes, setRes, delRes, "Property for res")
	def export(self, outfile, level, name_='XSDataXscale'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXscale'):
		pass
		if self.__path is not None:
			self.path.export(outfile, level, name_='path')
		else:
			warnEmptyAttribute("path", "XSDataString")
		if self.__res is not None:
			self.res.export(outfile, level, name_='res')
		else:
			warnEmptyAttribute("res", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setPath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'res':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRes(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXscale" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXscale' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXscale is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXscale.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXscale()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXscale" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXscale()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXscale

class XsDataXscaleInputFiles(object):
	def __init__(self, res=None, path=None):
		checkType("XsDataXscaleInputFiles", "Constructor of XsDataXscaleInputFiles", path, "XSDataString")
		self.__path = path
		checkType("XsDataXscaleInputFiles", "Constructor of XsDataXscaleInputFiles", res, "XSDataFloat")
		self.__res = res
	def getPath(self): return self.__path
	def setPath(self, path):
		checkType("XsDataXscaleInputFiles", "setPath", path, "XSDataString")
		self.__path = path
	def delPath(self): self.__path = None
	# Properties
	path = property(getPath, setPath, delPath, "Property for path")
	def getRes(self): return self.__res
	def setRes(self, res):
		checkType("XsDataXscaleInputFiles", "setRes", res, "XSDataFloat")
		self.__res = res
	def delRes(self): self.__res = None
	# Properties
	res = property(getRes, setRes, delRes, "Property for res")
	def export(self, outfile, level, name_='XsDataXscaleInputFiles'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XsDataXscaleInputFiles'):
		pass
		if self.__path is not None:
			self.path.export(outfile, level, name_='path')
		else:
			warnEmptyAttribute("path", "XSDataString")
		if self.__res is not None:
			self.res.export(outfile, level, name_='res')
		else:
			warnEmptyAttribute("res", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'path':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setPath(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'res':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRes(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XsDataXscaleInputFiles" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XsDataXscaleInputFiles' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XsDataXscaleInputFiles is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XsDataXscaleInputFiles.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XsDataXscaleInputFiles()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XsDataXscaleInputFiles" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XsDataXscaleInputFiles()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XsDataXscaleInputFiles

class XSDataXscaleInput(object):
	def __init__(self, bins=None, sg_number=None, unit_cell_constants=None, xds_files=None, friedels_law=None, merge=None):
		checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", merge, "XSDataBoolean")
		self.__merge = merge
		checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", friedels_law, "XSDataBoolean")
		self.__friedels_law = friedels_law
		if xds_files is None:
			self.__xds_files = []
		else:
			checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", xds_files, "list")
			self.__xds_files = xds_files
		if unit_cell_constants is None:
			self.__unit_cell_constants = []
		else:
			checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", unit_cell_constants, "list")
			self.__unit_cell_constants = unit_cell_constants
		checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", sg_number, "XSDataInteger")
		self.__sg_number = sg_number
		if bins is None:
			self.__bins = []
		else:
			checkType("XSDataXscaleInput", "Constructor of XSDataXscaleInput", bins, "list")
			self.__bins = bins
	def getMerge(self): return self.__merge
	def setMerge(self, merge):
		checkType("XSDataXscaleInput", "setMerge", merge, "XSDataBoolean")
		self.__merge = merge
	def delMerge(self): self.__merge = None
	# Properties
	merge = property(getMerge, setMerge, delMerge, "Property for merge")
	def getFriedels_law(self): return self.__friedels_law
	def setFriedels_law(self, friedels_law):
		checkType("XSDataXscaleInput", "setFriedels_law", friedels_law, "XSDataBoolean")
		self.__friedels_law = friedels_law
	def delFriedels_law(self): self.__friedels_law = None
	# Properties
	friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
	def getXds_files(self): return self.__xds_files
	def setXds_files(self, xds_files):
		checkType("XSDataXscaleInput", "setXds_files", xds_files, "list")
		self.__xds_files = xds_files
	def delXds_files(self): self.__xds_files = None
	# Properties
	xds_files = property(getXds_files, setXds_files, delXds_files, "Property for xds_files")
	def addXds_files(self, value):
		checkType("XSDataXscaleInput", "setXds_files", value, "XsDataXscaleInputFiles")
		self.__xds_files.append(value)
	def insertXds_files(self, index, value):
		checkType("XSDataXscaleInput", "setXds_files", value, "XsDataXscaleInputFiles")
		self.__xds_files[index] = value
	def getUnit_cell_constants(self): return self.__unit_cell_constants
	def setUnit_cell_constants(self, unit_cell_constants):
		checkType("XSDataXscaleInput", "setUnit_cell_constants", unit_cell_constants, "list")
		self.__unit_cell_constants = unit_cell_constants
	def delUnit_cell_constants(self): self.__unit_cell_constants = None
	# Properties
	unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
	def addUnit_cell_constants(self, value):
		checkType("XSDataXscaleInput", "setUnit_cell_constants", value, "XSDataFloat")
		self.__unit_cell_constants.append(value)
	def insertUnit_cell_constants(self, index, value):
		checkType("XSDataXscaleInput", "setUnit_cell_constants", value, "XSDataFloat")
		self.__unit_cell_constants[index] = value
	def getSg_number(self): return self.__sg_number
	def setSg_number(self, sg_number):
		checkType("XSDataXscaleInput", "setSg_number", sg_number, "XSDataInteger")
		self.__sg_number = sg_number
	def delSg_number(self): self.__sg_number = None
	# Properties
	sg_number = property(getSg_number, setSg_number, delSg_number, "Property for sg_number")
	def getBins(self): return self.__bins
	def setBins(self, bins):
		checkType("XSDataXscaleInput", "setBins", bins, "list")
		self.__bins = bins
	def delBins(self): self.__bins = None
	# Properties
	bins = property(getBins, setBins, delBins, "Property for bins")
	def addBins(self, value):
		checkType("XSDataXscaleInput", "setBins", value, "XSDataDouble")
		self.__bins.append(value)
	def insertBins(self, index, value):
		checkType("XSDataXscaleInput", "setBins", value, "XSDataDouble")
		self.__bins[index] = value
	def export(self, outfile, level, name_='XSDataXscaleInput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXscaleInput'):
		pass
		if self.__merge is not None:
			self.merge.export(outfile, level, name_='merge')
		else:
			warnEmptyAttribute("merge", "XSDataBoolean")
		if self.__friedels_law is not None:
			self.friedels_law.export(outfile, level, name_='friedels_law')
		else:
			warnEmptyAttribute("friedels_law", "XSDataBoolean")
		for xds_files_ in self.getXds_files():
			xds_files_.export(outfile, level, name_='xds_files')
		if self.getXds_files() == []:
			warnEmptyAttribute("xds_files", "XsDataXscaleInputFiles")
		for unit_cell_constants_ in self.getUnit_cell_constants():
			unit_cell_constants_.export(outfile, level, name_='unit_cell_constants')
		if self.getUnit_cell_constants() == []:
			warnEmptyAttribute("unit_cell_constants", "XSDataFloat")
		if self.__sg_number is not None:
			self.sg_number.export(outfile, level, name_='sg_number')
		else:
			warnEmptyAttribute("sg_number", "XSDataInteger")
		for bins_ in self.getBins():
			bins_.export(outfile, level, name_='bins')
		if self.getBins() == []:
			warnEmptyAttribute("bins", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'merge':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setMerge(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'friedels_law':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setFriedels_law(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'xds_files':
			obj_ = XsDataXscaleInputFiles()
			obj_.build(child_)
			self.xds_files.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unit_cell_constants':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.unit_cell_constants.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sg_number':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSg_number(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bins':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.bins.append(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXscaleInput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXscaleInput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXscaleInput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXscaleInput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXscaleInput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXscaleInput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXscaleInput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXscaleInput

class XSDataXscaleOutput(object):
	def __init__(self, output_file=None, succeeded=None):
		checkType("XSDataXscaleOutput", "Constructor of XSDataXscaleOutput", succeeded, "XSDataBoolean")
		self.__succeeded = succeeded
		checkType("XSDataXscaleOutput", "Constructor of XSDataXscaleOutput", output_file, "XSDataString")
		self.__output_file = output_file
	def getSucceeded(self): return self.__succeeded
	def setSucceeded(self, succeeded):
		checkType("XSDataXscaleOutput", "setSucceeded", succeeded, "XSDataBoolean")
		self.__succeeded = succeeded
	def delSucceeded(self): self.__succeeded = None
	# Properties
	succeeded = property(getSucceeded, setSucceeded, delSucceeded, "Property for succeeded")
	def getOutput_file(self): return self.__output_file
	def setOutput_file(self, output_file):
		checkType("XSDataXscaleOutput", "setOutput_file", output_file, "XSDataString")
		self.__output_file = output_file
	def delOutput_file(self): self.__output_file = None
	# Properties
	output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
	def export(self, outfile, level, name_='XSDataXscaleOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXscaleOutput'):
		pass
		if self.__succeeded is not None:
			self.succeeded.export(outfile, level, name_='succeeded')
		else:
			warnEmptyAttribute("succeeded", "XSDataBoolean")
		if self.__output_file is not None:
			self.output_file.export(outfile, level, name_='output_file')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'succeeded':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setSucceeded(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'output_file':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setOutput_file(obj_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXscaleOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXscaleOutput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXscaleOutput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXscaleOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXscaleOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXscaleOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXscaleOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXscaleOutput

class XSDataMatthewsCoeffIn(XSDataInput):
	def __init__(self, configuration=None, symm=None, gamma=None, beta=None, alpha=None, c=None, b=None, a=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", a, "XSDataDouble")
		self.__a = a
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", b, "XSDataDouble")
		self.__b = b
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", c, "XSDataDouble")
		self.__c = c
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", alpha, "XSDataDouble")
		self.__alpha = alpha
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", beta, "XSDataDouble")
		self.__beta = beta
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", gamma, "XSDataDouble")
		self.__gamma = gamma
		checkType("XSDataMatthewsCoeffIn", "Constructor of XSDataMatthewsCoeffIn", symm, "XSDataString")
		self.__symm = symm
	def getA(self): return self.__a
	def setA(self, a):
		checkType("XSDataMatthewsCoeffIn", "setA", a, "XSDataDouble")
		self.__a = a
	def delA(self): self.__a = None
	# Properties
	a = property(getA, setA, delA, "Property for a")
	def getB(self): return self.__b
	def setB(self, b):
		checkType("XSDataMatthewsCoeffIn", "setB", b, "XSDataDouble")
		self.__b = b
	def delB(self): self.__b = None
	# Properties
	b = property(getB, setB, delB, "Property for b")
	def getC(self): return self.__c
	def setC(self, c):
		checkType("XSDataMatthewsCoeffIn", "setC", c, "XSDataDouble")
		self.__c = c
	def delC(self): self.__c = None
	# Properties
	c = property(getC, setC, delC, "Property for c")
	def getAlpha(self): return self.__alpha
	def setAlpha(self, alpha):
		checkType("XSDataMatthewsCoeffIn", "setAlpha", alpha, "XSDataDouble")
		self.__alpha = alpha
	def delAlpha(self): self.__alpha = None
	# Properties
	alpha = property(getAlpha, setAlpha, delAlpha, "Property for alpha")
	def getBeta(self): return self.__beta
	def setBeta(self, beta):
		checkType("XSDataMatthewsCoeffIn", "setBeta", beta, "XSDataDouble")
		self.__beta = beta
	def delBeta(self): self.__beta = None
	# Properties
	beta = property(getBeta, setBeta, delBeta, "Property for beta")
	def getGamma(self): return self.__gamma
	def setGamma(self, gamma):
		checkType("XSDataMatthewsCoeffIn", "setGamma", gamma, "XSDataDouble")
		self.__gamma = gamma
	def delGamma(self): self.__gamma = None
	# Properties
	gamma = property(getGamma, setGamma, delGamma, "Property for gamma")
	def getSymm(self): return self.__symm
	def setSymm(self, symm):
		checkType("XSDataMatthewsCoeffIn", "setSymm", symm, "XSDataString")
		self.__symm = symm
	def delSymm(self): self.__symm = None
	# Properties
	symm = property(getSymm, setSymm, delSymm, "Property for symm")
	def export(self, outfile, level, name_='XSDataMatthewsCoeffIn'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMatthewsCoeffIn'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__a is not None:
			self.a.export(outfile, level, name_='a')
		else:
			warnEmptyAttribute("a", "XSDataDouble")
		if self.__b is not None:
			self.b.export(outfile, level, name_='b')
		else:
			warnEmptyAttribute("b", "XSDataDouble")
		if self.__c is not None:
			self.c.export(outfile, level, name_='c')
		else:
			warnEmptyAttribute("c", "XSDataDouble")
		if self.__alpha is not None:
			self.alpha.export(outfile, level, name_='alpha')
		else:
			warnEmptyAttribute("alpha", "XSDataDouble")
		if self.__beta is not None:
			self.beta.export(outfile, level, name_='beta')
		else:
			warnEmptyAttribute("beta", "XSDataDouble")
		if self.__gamma is not None:
			self.gamma.export(outfile, level, name_='gamma')
		else:
			warnEmptyAttribute("gamma", "XSDataDouble")
		if self.__symm is not None:
			self.symm.export(outfile, level, name_='symm')
		else:
			warnEmptyAttribute("symm", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'a':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setA(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'b':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setB(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'c':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setC(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'alpha':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setAlpha(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'beta':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBeta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'gamma':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setGamma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'symm':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setSymm(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMatthewsCoeffIn" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMatthewsCoeffIn' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMatthewsCoeffIn is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMatthewsCoeffIn.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMatthewsCoeffIn()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMatthewsCoeffIn" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMatthewsCoeffIn()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMatthewsCoeffIn

class XSDataMatthewsCoeffOut(XSDataResult):
	def __init__(self, status=None, best_sol=None, best_p=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataMatthewsCoeffOut", "Constructor of XSDataMatthewsCoeffOut", best_p, "XSDataDouble")
		self.__best_p = best_p
		checkType("XSDataMatthewsCoeffOut", "Constructor of XSDataMatthewsCoeffOut", best_sol, "XSDataString")
		self.__best_sol = best_sol
	def getBest_p(self): return self.__best_p
	def setBest_p(self, best_p):
		checkType("XSDataMatthewsCoeffOut", "setBest_p", best_p, "XSDataDouble")
		self.__best_p = best_p
	def delBest_p(self): self.__best_p = None
	# Properties
	best_p = property(getBest_p, setBest_p, delBest_p, "Property for best_p")
	def getBest_sol(self): return self.__best_sol
	def setBest_sol(self, best_sol):
		checkType("XSDataMatthewsCoeffOut", "setBest_sol", best_sol, "XSDataString")
		self.__best_sol = best_sol
	def delBest_sol(self): self.__best_sol = None
	# Properties
	best_sol = property(getBest_sol, setBest_sol, delBest_sol, "Property for best_sol")
	def export(self, outfile, level, name_='XSDataMatthewsCoeffOut'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMatthewsCoeffOut'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__best_p is not None:
			self.best_p.export(outfile, level, name_='best_p')
		else:
			warnEmptyAttribute("best_p", "XSDataDouble")
		if self.__best_sol is not None:
			self.best_sol.export(outfile, level, name_='best_sol')
		else:
			warnEmptyAttribute("best_sol", "XSDataString")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'best_p':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setBest_p(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'best_sol':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setBest_sol(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMatthewsCoeffOut" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMatthewsCoeffOut' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMatthewsCoeffOut is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMatthewsCoeffOut.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMatthewsCoeffOut()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMatthewsCoeffOut" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMatthewsCoeffOut()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMatthewsCoeffOut

class XSDataMinimalXDSIn(XSDataInput):
	def __init__(self, configuration=None, maxjobs=None, maxproc=None, job=None, input_file=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataMinimalXDSIn", "Constructor of XSDataMinimalXDSIn", input_file, "XSDataString")
		self.__input_file = input_file
		checkType("XSDataMinimalXDSIn", "Constructor of XSDataMinimalXDSIn", job, "XSDataString")
		self.__job = job
		checkType("XSDataMinimalXDSIn", "Constructor of XSDataMinimalXDSIn", maxproc, "XSDataInteger")
		self.__maxproc = maxproc
		checkType("XSDataMinimalXDSIn", "Constructor of XSDataMinimalXDSIn", maxjobs, "XSDataInteger")
		self.__maxjobs = maxjobs
	def getInput_file(self): return self.__input_file
	def setInput_file(self, input_file):
		checkType("XSDataMinimalXDSIn", "setInput_file", input_file, "XSDataString")
		self.__input_file = input_file
	def delInput_file(self): self.__input_file = None
	# Properties
	input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
	def getJob(self): return self.__job
	def setJob(self, job):
		checkType("XSDataMinimalXDSIn", "setJob", job, "XSDataString")
		self.__job = job
	def delJob(self): self.__job = None
	# Properties
	job = property(getJob, setJob, delJob, "Property for job")
	def getMaxproc(self): return self.__maxproc
	def setMaxproc(self, maxproc):
		checkType("XSDataMinimalXDSIn", "setMaxproc", maxproc, "XSDataInteger")
		self.__maxproc = maxproc
	def delMaxproc(self): self.__maxproc = None
	# Properties
	maxproc = property(getMaxproc, setMaxproc, delMaxproc, "Property for maxproc")
	def getMaxjobs(self): return self.__maxjobs
	def setMaxjobs(self, maxjobs):
		checkType("XSDataMinimalXDSIn", "setMaxjobs", maxjobs, "XSDataInteger")
		self.__maxjobs = maxjobs
	def delMaxjobs(self): self.__maxjobs = None
	# Properties
	maxjobs = property(getMaxjobs, setMaxjobs, delMaxjobs, "Property for maxjobs")
	def export(self, outfile, level, name_='XSDataMinimalXDSIn'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMinimalXDSIn'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__input_file is not None:
			self.input_file.export(outfile, level, name_='input_file')
		else:
			warnEmptyAttribute("input_file", "XSDataString")
		if self.__job is not None:
			self.job.export(outfile, level, name_='job')
		if self.__maxproc is not None:
			self.maxproc.export(outfile, level, name_='maxproc')
		if self.__maxjobs is not None:
			self.maxjobs.export(outfile, level, name_='maxjobs')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'input_file':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setInput_file(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'job':
			obj_ = XSDataString()
			obj_.build(child_)
			self.setJob(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxproc':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setMaxproc(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'maxjobs':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setMaxjobs(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMinimalXDSIn" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMinimalXDSIn' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMinimalXDSIn is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMinimalXDSIn.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMinimalXDSIn()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMinimalXDSIn" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMinimalXDSIn()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMinimalXDSIn

class XSDataMinimalXDSOut(XSDataResult):
	def __init__(self, status=None, succeeded=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataMinimalXDSOut", "Constructor of XSDataMinimalXDSOut", succeeded, "XSDataBoolean")
		self.__succeeded = succeeded
	def getSucceeded(self): return self.__succeeded
	def setSucceeded(self, succeeded):
		checkType("XSDataMinimalXDSOut", "setSucceeded", succeeded, "XSDataBoolean")
		self.__succeeded = succeeded
	def delSucceeded(self): self.__succeeded = None
	# Properties
	succeeded = property(getSucceeded, setSucceeded, delSucceeded, "Property for succeeded")
	def export(self, outfile, level, name_='XSDataMinimalXDSOut'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataMinimalXDSOut'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__succeeded is not None:
			self.succeeded.export(outfile, level, name_='succeeded')
		else:
			warnEmptyAttribute("succeeded", "XSDataBoolean")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'succeeded':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setSucceeded(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataMinimalXDSOut" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataMinimalXDSOut' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataMinimalXDSOut is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataMinimalXDSOut.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataMinimalXDSOut()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataMinimalXDSOut" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataMinimalXDSOut()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataMinimalXDSOut

class XSDataRBinsIn(XSDataInput):
	def __init__(self, configuration=None, high=None, low=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataRBinsIn", "Constructor of XSDataRBinsIn", low, "XSDataDouble")
		self.__low = low
		checkType("XSDataRBinsIn", "Constructor of XSDataRBinsIn", high, "XSDataDouble")
		self.__high = high
	def getLow(self): return self.__low
	def setLow(self, low):
		checkType("XSDataRBinsIn", "setLow", low, "XSDataDouble")
		self.__low = low
	def delLow(self): self.__low = None
	# Properties
	low = property(getLow, setLow, delLow, "Property for low")
	def getHigh(self): return self.__high
	def setHigh(self, high):
		checkType("XSDataRBinsIn", "setHigh", high, "XSDataDouble")
		self.__high = high
	def delHigh(self): self.__high = None
	# Properties
	high = property(getHigh, setHigh, delHigh, "Property for high")
	def export(self, outfile, level, name_='XSDataRBinsIn'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataRBinsIn'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__low is not None:
			self.low.export(outfile, level, name_='low')
		else:
			warnEmptyAttribute("low", "XSDataDouble")
		if self.__high is not None:
			self.high.export(outfile, level, name_='high')
		else:
			warnEmptyAttribute("high", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'low':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setLow(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'high':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.setHigh(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataRBinsIn" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataRBinsIn' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataRBinsIn is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataRBinsIn.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataRBinsIn()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataRBinsIn" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataRBinsIn()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataRBinsIn

class XSDataRBinsOut(XSDataResult):
	def __init__(self, status=None, bins=None):
		XSDataResult.__init__(self, status)
		if bins is None:
			self.__bins = []
		else:
			checkType("XSDataRBinsOut", "Constructor of XSDataRBinsOut", bins, "list")
			self.__bins = bins
	def getBins(self): return self.__bins
	def setBins(self, bins):
		checkType("XSDataRBinsOut", "setBins", bins, "list")
		self.__bins = bins
	def delBins(self): self.__bins = None
	# Properties
	bins = property(getBins, setBins, delBins, "Property for bins")
	def addBins(self, value):
		checkType("XSDataRBinsOut", "setBins", value, "XSDataDouble")
		self.__bins.append(value)
	def insertBins(self, index, value):
		checkType("XSDataRBinsOut", "setBins", value, "XSDataDouble")
		self.__bins[index] = value
	def export(self, outfile, level, name_='XSDataRBinsOut'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataRBinsOut'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for bins_ in self.getBins():
			bins_.export(outfile, level, name_='bins')
		if self.getBins() == []:
			warnEmptyAttribute("bins", "XSDataDouble")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bins':
			obj_ = XSDataDouble()
			obj_.build(child_)
			self.bins.append(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataRBinsOut" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataRBinsOut' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataRBinsOut is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataRBinsOut.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataRBinsOut()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataRBinsOut" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataRBinsOut()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataRBinsOut

class XSDataResCutoffResult(XSDataResult):
	def __init__(self, status=None, total_isig=None, total_rfactor=None, total_complete=None, bins=None, res=None):
		XSDataResult.__init__(self, status)
		checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", res, "XSDataFloat")
		self.__res = res
		if bins is None:
			self.__bins = []
		else:
			checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", bins, "list")
			self.__bins = bins
		checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", total_complete, "XSDataFloat")
		self.__total_complete = total_complete
		checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", total_rfactor, "XSDataFloat")
		self.__total_rfactor = total_rfactor
		checkType("XSDataResCutoffResult", "Constructor of XSDataResCutoffResult", total_isig, "XSDataFloat")
		self.__total_isig = total_isig
	def getRes(self): return self.__res
	def setRes(self, res):
		checkType("XSDataResCutoffResult", "setRes", res, "XSDataFloat")
		self.__res = res
	def delRes(self): self.__res = None
	# Properties
	res = property(getRes, setRes, delRes, "Property for res")
	def getBins(self): return self.__bins
	def setBins(self, bins):
		checkType("XSDataResCutoffResult", "setBins", bins, "list")
		self.__bins = bins
	def delBins(self): self.__bins = None
	# Properties
	bins = property(getBins, setBins, delBins, "Property for bins")
	def addBins(self, value):
		checkType("XSDataResCutoffResult", "setBins", value, "XSDataFloat")
		self.__bins.append(value)
	def insertBins(self, index, value):
		checkType("XSDataResCutoffResult", "setBins", value, "XSDataFloat")
		self.__bins[index] = value
	def getTotal_complete(self): return self.__total_complete
	def setTotal_complete(self, total_complete):
		checkType("XSDataResCutoffResult", "setTotal_complete", total_complete, "XSDataFloat")
		self.__total_complete = total_complete
	def delTotal_complete(self): self.__total_complete = None
	# Properties
	total_complete = property(getTotal_complete, setTotal_complete, delTotal_complete, "Property for total_complete")
	def getTotal_rfactor(self): return self.__total_rfactor
	def setTotal_rfactor(self, total_rfactor):
		checkType("XSDataResCutoffResult", "setTotal_rfactor", total_rfactor, "XSDataFloat")
		self.__total_rfactor = total_rfactor
	def delTotal_rfactor(self): self.__total_rfactor = None
	# Properties
	total_rfactor = property(getTotal_rfactor, setTotal_rfactor, delTotal_rfactor, "Property for total_rfactor")
	def getTotal_isig(self): return self.__total_isig
	def setTotal_isig(self, total_isig):
		checkType("XSDataResCutoffResult", "setTotal_isig", total_isig, "XSDataFloat")
		self.__total_isig = total_isig
	def delTotal_isig(self): self.__total_isig = None
	# Properties
	total_isig = property(getTotal_isig, setTotal_isig, delTotal_isig, "Property for total_isig")
	def export(self, outfile, level, name_='XSDataResCutoffResult'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResCutoffResult'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		if self.__res is not None:
			self.res.export(outfile, level, name_='res')
		else:
			warnEmptyAttribute("res", "XSDataFloat")
		for bins_ in self.getBins():
			bins_.export(outfile, level, name_='bins')
		if self.getBins() == []:
			warnEmptyAttribute("bins", "XSDataFloat")
		if self.__total_complete is not None:
			self.total_complete.export(outfile, level, name_='total_complete')
		else:
			warnEmptyAttribute("total_complete", "XSDataFloat")
		if self.__total_rfactor is not None:
			self.total_rfactor.export(outfile, level, name_='total_rfactor')
		else:
			warnEmptyAttribute("total_rfactor", "XSDataFloat")
		if self.__total_isig is not None:
			self.total_isig.export(outfile, level, name_='total_isig')
		else:
			warnEmptyAttribute("total_isig", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'res':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRes(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'bins':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.bins.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'total_complete':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setTotal_complete(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'total_rfactor':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setTotal_rfactor(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'total_isig':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setTotal_isig(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResCutoffResult" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResCutoffResult' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResCutoffResult is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResCutoffResult.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResCutoffResult()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResCutoffResult" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResCutoffResult()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResCutoffResult

class XSDataXdsOutput(XSDataResult):
	def __init__(self, status=None, sg_number=None, unit_cell_constants=None, cell_gamma=None, cell_beta=None, cell_alpha=None, cell_c=None, cell_b=None, cell_a=None, coordinates_of_unit_cell_c_axis=None, coordinates_of_unit_cell_b_axis=None, coordinates_of_unit_cell_a_axis=None, crystal_to_detector_distance=None, detector_origin=None, direct_beam_detector_coordinates=None, direct_beam_coordinates=None, crystal_mosaicity=None, total_completeness=None, completeness_entries=None):
		XSDataResult.__init__(self, status)
		if completeness_entries is None:
			self.__completeness_entries = []
		else:
			checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", completeness_entries, "list")
			self.__completeness_entries = completeness_entries
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", total_completeness, "XSDataXdsCompletenessEntry")
		self.__total_completeness = total_completeness
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", crystal_mosaicity, "XSDataFloat")
		self.__crystal_mosaicity = crystal_mosaicity
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", direct_beam_coordinates, "XSDataVectorDouble")
		self.__direct_beam_coordinates = direct_beam_coordinates
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", direct_beam_detector_coordinates, "XSData2DCoordinates")
		self.__direct_beam_detector_coordinates = direct_beam_detector_coordinates
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", detector_origin, "XSData2DCoordinates")
		self.__detector_origin = detector_origin
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", crystal_to_detector_distance, "XSDataFloat")
		self.__crystal_to_detector_distance = crystal_to_detector_distance
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", coordinates_of_unit_cell_a_axis, "XSDataVectorDouble")
		self.__coordinates_of_unit_cell_a_axis = coordinates_of_unit_cell_a_axis
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", coordinates_of_unit_cell_b_axis, "XSDataVectorDouble")
		self.__coordinates_of_unit_cell_b_axis = coordinates_of_unit_cell_b_axis
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", coordinates_of_unit_cell_c_axis, "XSDataVectorDouble")
		self.__coordinates_of_unit_cell_c_axis = coordinates_of_unit_cell_c_axis
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_a, "XSDataFloat")
		self.__cell_a = cell_a
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_b, "XSDataFloat")
		self.__cell_b = cell_b
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_c, "XSDataFloat")
		self.__cell_c = cell_c
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_alpha, "XSDataFloat")
		self.__cell_alpha = cell_alpha
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_beta, "XSDataFloat")
		self.__cell_beta = cell_beta
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", cell_gamma, "XSDataFloat")
		self.__cell_gamma = cell_gamma
		if unit_cell_constants is None:
			self.__unit_cell_constants = []
		else:
			checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", unit_cell_constants, "list")
			self.__unit_cell_constants = unit_cell_constants
		checkType("XSDataXdsOutput", "Constructor of XSDataXdsOutput", sg_number, "XSDataInteger")
		self.__sg_number = sg_number
	def getCompleteness_entries(self): return self.__completeness_entries
	def setCompleteness_entries(self, completeness_entries):
		checkType("XSDataXdsOutput", "setCompleteness_entries", completeness_entries, "list")
		self.__completeness_entries = completeness_entries
	def delCompleteness_entries(self): self.__completeness_entries = None
	# Properties
	completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
	def addCompleteness_entries(self, value):
		checkType("XSDataXdsOutput", "setCompleteness_entries", value, "XSDataXdsCompletenessEntry")
		self.__completeness_entries.append(value)
	def insertCompleteness_entries(self, index, value):
		checkType("XSDataXdsOutput", "setCompleteness_entries", value, "XSDataXdsCompletenessEntry")
		self.__completeness_entries[index] = value
	def getTotal_completeness(self): return self.__total_completeness
	def setTotal_completeness(self, total_completeness):
		checkType("XSDataXdsOutput", "setTotal_completeness", total_completeness, "XSDataXdsCompletenessEntry")
		self.__total_completeness = total_completeness
	def delTotal_completeness(self): self.__total_completeness = None
	# Properties
	total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
	def getCrystal_mosaicity(self): return self.__crystal_mosaicity
	def setCrystal_mosaicity(self, crystal_mosaicity):
		checkType("XSDataXdsOutput", "setCrystal_mosaicity", crystal_mosaicity, "XSDataFloat")
		self.__crystal_mosaicity = crystal_mosaicity
	def delCrystal_mosaicity(self): self.__crystal_mosaicity = None
	# Properties
	crystal_mosaicity = property(getCrystal_mosaicity, setCrystal_mosaicity, delCrystal_mosaicity, "Property for crystal_mosaicity")
	def getDirect_beam_coordinates(self): return self.__direct_beam_coordinates
	def setDirect_beam_coordinates(self, direct_beam_coordinates):
		checkType("XSDataXdsOutput", "setDirect_beam_coordinates", direct_beam_coordinates, "XSDataVectorDouble")
		self.__direct_beam_coordinates = direct_beam_coordinates
	def delDirect_beam_coordinates(self): self.__direct_beam_coordinates = None
	# Properties
	direct_beam_coordinates = property(getDirect_beam_coordinates, setDirect_beam_coordinates, delDirect_beam_coordinates, "Property for direct_beam_coordinates")
	def getDirect_beam_detector_coordinates(self): return self.__direct_beam_detector_coordinates
	def setDirect_beam_detector_coordinates(self, direct_beam_detector_coordinates):
		checkType("XSDataXdsOutput", "setDirect_beam_detector_coordinates", direct_beam_detector_coordinates, "XSData2DCoordinates")
		self.__direct_beam_detector_coordinates = direct_beam_detector_coordinates
	def delDirect_beam_detector_coordinates(self): self.__direct_beam_detector_coordinates = None
	# Properties
	direct_beam_detector_coordinates = property(getDirect_beam_detector_coordinates, setDirect_beam_detector_coordinates, delDirect_beam_detector_coordinates, "Property for direct_beam_detector_coordinates")
	def getDetector_origin(self): return self.__detector_origin
	def setDetector_origin(self, detector_origin):
		checkType("XSDataXdsOutput", "setDetector_origin", detector_origin, "XSData2DCoordinates")
		self.__detector_origin = detector_origin
	def delDetector_origin(self): self.__detector_origin = None
	# Properties
	detector_origin = property(getDetector_origin, setDetector_origin, delDetector_origin, "Property for detector_origin")
	def getCrystal_to_detector_distance(self): return self.__crystal_to_detector_distance
	def setCrystal_to_detector_distance(self, crystal_to_detector_distance):
		checkType("XSDataXdsOutput", "setCrystal_to_detector_distance", crystal_to_detector_distance, "XSDataFloat")
		self.__crystal_to_detector_distance = crystal_to_detector_distance
	def delCrystal_to_detector_distance(self): self.__crystal_to_detector_distance = None
	# Properties
	crystal_to_detector_distance = property(getCrystal_to_detector_distance, setCrystal_to_detector_distance, delCrystal_to_detector_distance, "Property for crystal_to_detector_distance")
	def getCoordinates_of_unit_cell_a_axis(self): return self.__coordinates_of_unit_cell_a_axis
	def setCoordinates_of_unit_cell_a_axis(self, coordinates_of_unit_cell_a_axis):
		checkType("XSDataXdsOutput", "setCoordinates_of_unit_cell_a_axis", coordinates_of_unit_cell_a_axis, "XSDataVectorDouble")
		self.__coordinates_of_unit_cell_a_axis = coordinates_of_unit_cell_a_axis
	def delCoordinates_of_unit_cell_a_axis(self): self.__coordinates_of_unit_cell_a_axis = None
	# Properties
	coordinates_of_unit_cell_a_axis = property(getCoordinates_of_unit_cell_a_axis, setCoordinates_of_unit_cell_a_axis, delCoordinates_of_unit_cell_a_axis, "Property for coordinates_of_unit_cell_a_axis")
	def getCoordinates_of_unit_cell_b_axis(self): return self.__coordinates_of_unit_cell_b_axis
	def setCoordinates_of_unit_cell_b_axis(self, coordinates_of_unit_cell_b_axis):
		checkType("XSDataXdsOutput", "setCoordinates_of_unit_cell_b_axis", coordinates_of_unit_cell_b_axis, "XSDataVectorDouble")
		self.__coordinates_of_unit_cell_b_axis = coordinates_of_unit_cell_b_axis
	def delCoordinates_of_unit_cell_b_axis(self): self.__coordinates_of_unit_cell_b_axis = None
	# Properties
	coordinates_of_unit_cell_b_axis = property(getCoordinates_of_unit_cell_b_axis, setCoordinates_of_unit_cell_b_axis, delCoordinates_of_unit_cell_b_axis, "Property for coordinates_of_unit_cell_b_axis")
	def getCoordinates_of_unit_cell_c_axis(self): return self.__coordinates_of_unit_cell_c_axis
	def setCoordinates_of_unit_cell_c_axis(self, coordinates_of_unit_cell_c_axis):
		checkType("XSDataXdsOutput", "setCoordinates_of_unit_cell_c_axis", coordinates_of_unit_cell_c_axis, "XSDataVectorDouble")
		self.__coordinates_of_unit_cell_c_axis = coordinates_of_unit_cell_c_axis
	def delCoordinates_of_unit_cell_c_axis(self): self.__coordinates_of_unit_cell_c_axis = None
	# Properties
	coordinates_of_unit_cell_c_axis = property(getCoordinates_of_unit_cell_c_axis, setCoordinates_of_unit_cell_c_axis, delCoordinates_of_unit_cell_c_axis, "Property for coordinates_of_unit_cell_c_axis")
	def getCell_a(self): return self.__cell_a
	def setCell_a(self, cell_a):
		checkType("XSDataXdsOutput", "setCell_a", cell_a, "XSDataFloat")
		self.__cell_a = cell_a
	def delCell_a(self): self.__cell_a = None
	# Properties
	cell_a = property(getCell_a, setCell_a, delCell_a, "Property for cell_a")
	def getCell_b(self): return self.__cell_b
	def setCell_b(self, cell_b):
		checkType("XSDataXdsOutput", "setCell_b", cell_b, "XSDataFloat")
		self.__cell_b = cell_b
	def delCell_b(self): self.__cell_b = None
	# Properties
	cell_b = property(getCell_b, setCell_b, delCell_b, "Property for cell_b")
	def getCell_c(self): return self.__cell_c
	def setCell_c(self, cell_c):
		checkType("XSDataXdsOutput", "setCell_c", cell_c, "XSDataFloat")
		self.__cell_c = cell_c
	def delCell_c(self): self.__cell_c = None
	# Properties
	cell_c = property(getCell_c, setCell_c, delCell_c, "Property for cell_c")
	def getCell_alpha(self): return self.__cell_alpha
	def setCell_alpha(self, cell_alpha):
		checkType("XSDataXdsOutput", "setCell_alpha", cell_alpha, "XSDataFloat")
		self.__cell_alpha = cell_alpha
	def delCell_alpha(self): self.__cell_alpha = None
	# Properties
	cell_alpha = property(getCell_alpha, setCell_alpha, delCell_alpha, "Property for cell_alpha")
	def getCell_beta(self): return self.__cell_beta
	def setCell_beta(self, cell_beta):
		checkType("XSDataXdsOutput", "setCell_beta", cell_beta, "XSDataFloat")
		self.__cell_beta = cell_beta
	def delCell_beta(self): self.__cell_beta = None
	# Properties
	cell_beta = property(getCell_beta, setCell_beta, delCell_beta, "Property for cell_beta")
	def getCell_gamma(self): return self.__cell_gamma
	def setCell_gamma(self, cell_gamma):
		checkType("XSDataXdsOutput", "setCell_gamma", cell_gamma, "XSDataFloat")
		self.__cell_gamma = cell_gamma
	def delCell_gamma(self): self.__cell_gamma = None
	# Properties
	cell_gamma = property(getCell_gamma, setCell_gamma, delCell_gamma, "Property for cell_gamma")
	def getUnit_cell_constants(self): return self.__unit_cell_constants
	def setUnit_cell_constants(self, unit_cell_constants):
		checkType("XSDataXdsOutput", "setUnit_cell_constants", unit_cell_constants, "list")
		self.__unit_cell_constants = unit_cell_constants
	def delUnit_cell_constants(self): self.__unit_cell_constants = None
	# Properties
	unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
	def addUnit_cell_constants(self, value):
		checkType("XSDataXdsOutput", "setUnit_cell_constants", value, "XSDataFloat")
		self.__unit_cell_constants.append(value)
	def insertUnit_cell_constants(self, index, value):
		checkType("XSDataXdsOutput", "setUnit_cell_constants", value, "XSDataFloat")
		self.__unit_cell_constants[index] = value
	def getSg_number(self): return self.__sg_number
	def setSg_number(self, sg_number):
		checkType("XSDataXdsOutput", "setSg_number", sg_number, "XSDataInteger")
		self.__sg_number = sg_number
	def delSg_number(self): self.__sg_number = None
	# Properties
	sg_number = property(getSg_number, setSg_number, delSg_number, "Property for sg_number")
	def export(self, outfile, level, name_='XSDataXdsOutput'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXdsOutput'):
		XSDataResult.exportChildren(self, outfile, level, name_)
		for completeness_entries_ in self.getCompleteness_entries():
			completeness_entries_.export(outfile, level, name_='completeness_entries')
		if self.getCompleteness_entries() == []:
			warnEmptyAttribute("completeness_entries", "XSDataXdsCompletenessEntry")
		if self.__total_completeness is not None:
			self.total_completeness.export(outfile, level, name_='total_completeness')
		else:
			warnEmptyAttribute("total_completeness", "XSDataXdsCompletenessEntry")
		if self.__crystal_mosaicity is not None:
			self.crystal_mosaicity.export(outfile, level, name_='crystal_mosaicity')
		else:
			warnEmptyAttribute("crystal_mosaicity", "XSDataFloat")
		if self.__direct_beam_coordinates is not None:
			self.direct_beam_coordinates.export(outfile, level, name_='direct_beam_coordinates')
		else:
			warnEmptyAttribute("direct_beam_coordinates", "XSDataVectorDouble")
		if self.__direct_beam_detector_coordinates is not None:
			self.direct_beam_detector_coordinates.export(outfile, level, name_='direct_beam_detector_coordinates')
		else:
			warnEmptyAttribute("direct_beam_detector_coordinates", "XSData2DCoordinates")
		if self.__detector_origin is not None:
			self.detector_origin.export(outfile, level, name_='detector_origin')
		else:
			warnEmptyAttribute("detector_origin", "XSData2DCoordinates")
		if self.__crystal_to_detector_distance is not None:
			self.crystal_to_detector_distance.export(outfile, level, name_='crystal_to_detector_distance')
		else:
			warnEmptyAttribute("crystal_to_detector_distance", "XSDataFloat")
		if self.__coordinates_of_unit_cell_a_axis is not None:
			self.coordinates_of_unit_cell_a_axis.export(outfile, level, name_='coordinates_of_unit_cell_a_axis')
		else:
			warnEmptyAttribute("coordinates_of_unit_cell_a_axis", "XSDataVectorDouble")
		if self.__coordinates_of_unit_cell_b_axis is not None:
			self.coordinates_of_unit_cell_b_axis.export(outfile, level, name_='coordinates_of_unit_cell_b_axis')
		else:
			warnEmptyAttribute("coordinates_of_unit_cell_b_axis", "XSDataVectorDouble")
		if self.__coordinates_of_unit_cell_c_axis is not None:
			self.coordinates_of_unit_cell_c_axis.export(outfile, level, name_='coordinates_of_unit_cell_c_axis')
		else:
			warnEmptyAttribute("coordinates_of_unit_cell_c_axis", "XSDataVectorDouble")
		if self.__cell_a is not None:
			self.cell_a.export(outfile, level, name_='cell_a')
		else:
			warnEmptyAttribute("cell_a", "XSDataFloat")
		if self.__cell_b is not None:
			self.cell_b.export(outfile, level, name_='cell_b')
		else:
			warnEmptyAttribute("cell_b", "XSDataFloat")
		if self.__cell_c is not None:
			self.cell_c.export(outfile, level, name_='cell_c')
		else:
			warnEmptyAttribute("cell_c", "XSDataFloat")
		if self.__cell_alpha is not None:
			self.cell_alpha.export(outfile, level, name_='cell_alpha')
		else:
			warnEmptyAttribute("cell_alpha", "XSDataFloat")
		if self.__cell_beta is not None:
			self.cell_beta.export(outfile, level, name_='cell_beta')
		else:
			warnEmptyAttribute("cell_beta", "XSDataFloat")
		if self.__cell_gamma is not None:
			self.cell_gamma.export(outfile, level, name_='cell_gamma')
		else:
			warnEmptyAttribute("cell_gamma", "XSDataFloat")
		for unit_cell_constants_ in self.getUnit_cell_constants():
			unit_cell_constants_.export(outfile, level, name_='unit_cell_constants')
		if self.__sg_number is not None:
			self.sg_number.export(outfile, level, name_='sg_number')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness_entries':
			obj_ = XSDataXdsCompletenessEntry()
			obj_.build(child_)
			self.completeness_entries.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'total_completeness':
			obj_ = XSDataXdsCompletenessEntry()
			obj_.build(child_)
			self.setTotal_completeness(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystal_mosaicity':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCrystal_mosaicity(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'direct_beam_coordinates':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setDirect_beam_coordinates(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'direct_beam_detector_coordinates':
			obj_ = XSData2DCoordinates()
			obj_.build(child_)
			self.setDirect_beam_detector_coordinates(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'detector_origin':
			obj_ = XSData2DCoordinates()
			obj_.build(child_)
			self.setDetector_origin(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'crystal_to_detector_distance':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCrystal_to_detector_distance(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'coordinates_of_unit_cell_a_axis':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setCoordinates_of_unit_cell_a_axis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'coordinates_of_unit_cell_b_axis':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setCoordinates_of_unit_cell_b_axis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'coordinates_of_unit_cell_c_axis':
			obj_ = XSDataVectorDouble()
			obj_.build(child_)
			self.setCoordinates_of_unit_cell_c_axis(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_a':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCell_a(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_b':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCell_b(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_c':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCell_c(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_alpha':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCell_alpha(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_beta':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCell_beta(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'cell_gamma':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCell_gamma(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'unit_cell_constants':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.unit_cell_constants.append(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'sg_number':
			obj_ = XSDataInteger()
			obj_.build(child_)
			self.setSg_number(obj_)
		XSDataResult.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXdsOutput" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXdsOutput' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXdsOutput is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXdsOutput.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXdsOutput()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXdsOutput" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXdsOutput()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXdsOutput

class XSDataXdsOutputFile(XSDataInput):
	def __init__(self, configuration=None, rover=None, compl=None, gxparm=None, correct_lp=None):
		XSDataInput.__init__(self, configuration)
		checkType("XSDataXdsOutputFile", "Constructor of XSDataXdsOutputFile", correct_lp, "XSDataFile")
		self.__correct_lp = correct_lp
		checkType("XSDataXdsOutputFile", "Constructor of XSDataXdsOutputFile", gxparm, "XSDataFile")
		self.__gxparm = gxparm
		checkType("XSDataXdsOutputFile", "Constructor of XSDataXdsOutputFile", compl, "XSDataBoolean")
		self.__compl = compl
		checkType("XSDataXdsOutputFile", "Constructor of XSDataXdsOutputFile", rover, "XSDataFloat")
		self.__rover = rover
	def getCorrect_lp(self): return self.__correct_lp
	def setCorrect_lp(self, correct_lp):
		checkType("XSDataXdsOutputFile", "setCorrect_lp", correct_lp, "XSDataFile")
		self.__correct_lp = correct_lp
	def delCorrect_lp(self): self.__correct_lp = None
	# Properties
	correct_lp = property(getCorrect_lp, setCorrect_lp, delCorrect_lp, "Property for correct_lp")
	def getGxparm(self): return self.__gxparm
	def setGxparm(self, gxparm):
		checkType("XSDataXdsOutputFile", "setGxparm", gxparm, "XSDataFile")
		self.__gxparm = gxparm
	def delGxparm(self): self.__gxparm = None
	# Properties
	gxparm = property(getGxparm, setGxparm, delGxparm, "Property for gxparm")
	def getCompl(self): return self.__compl
	def setCompl(self, compl):
		checkType("XSDataXdsOutputFile", "setCompl", compl, "XSDataBoolean")
		self.__compl = compl
	def delCompl(self): self.__compl = None
	# Properties
	compl = property(getCompl, setCompl, delCompl, "Property for compl")
	def getRover(self): return self.__rover
	def setRover(self, rover):
		checkType("XSDataXdsOutputFile", "setRover", rover, "XSDataFloat")
		self.__rover = rover
	def delRover(self): self.__rover = None
	# Properties
	rover = property(getRover, setRover, delRover, "Property for rover")
	def export(self, outfile, level, name_='XSDataXdsOutputFile'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataXdsOutputFile'):
		XSDataInput.exportChildren(self, outfile, level, name_)
		if self.__correct_lp is not None:
			self.correct_lp.export(outfile, level, name_='correct_lp')
		else:
			warnEmptyAttribute("correct_lp", "XSDataFile")
		if self.__gxparm is not None:
			self.gxparm.export(outfile, level, name_='gxparm')
		if self.__compl is not None:
			self.compl.export(outfile, level, name_='compl')
		else:
			warnEmptyAttribute("compl", "XSDataBoolean")
		if self.__rover is not None:
			self.rover.export(outfile, level, name_='rover')
		else:
			warnEmptyAttribute("rover", "XSDataFloat")
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'correct_lp':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setCorrect_lp(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'gxparm':
			obj_ = XSDataFile()
			obj_.build(child_)
			self.setGxparm(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'compl':
			obj_ = XSDataBoolean()
			obj_.build(child_)
			self.setCompl(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'rover':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRover(obj_)
		XSDataInput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataXdsOutputFile" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataXdsOutputFile' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataXdsOutputFile is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataXdsOutputFile.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataXdsOutputFile()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataXdsOutputFile" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataXdsOutputFile()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataXdsOutputFile

class XSDataResCutoff(XSDataXdsOutput):
	def __init__(self, status=None, sg_number=None, unit_cell_constants=None, cell_gamma=None, cell_beta=None, cell_alpha=None, cell_c=None, cell_b=None, cell_a=None, coordinates_of_unit_cell_c_axis=None, coordinates_of_unit_cell_b_axis=None, coordinates_of_unit_cell_a_axis=None, crystal_to_detector_distance=None, detector_origin=None, direct_beam_detector_coordinates=None, direct_beam_coordinates=None, crystal_mosaicity=None, total_completeness=None, completeness_entries=None, isig_cutoff=None, res_override=None, completeness_cutoff=None):
		XSDataXdsOutput.__init__(self, status, sg_number, unit_cell_constants, cell_gamma, cell_beta, cell_alpha, cell_c, cell_b, cell_a, coordinates_of_unit_cell_c_axis, coordinates_of_unit_cell_b_axis, coordinates_of_unit_cell_a_axis, crystal_to_detector_distance, detector_origin, direct_beam_detector_coordinates, direct_beam_coordinates, crystal_mosaicity, total_completeness, completeness_entries)
		checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", completeness_cutoff, "XSDataFloat")
		self.__completeness_cutoff = completeness_cutoff
		checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", res_override, "XSDataFloat")
		self.__res_override = res_override
		checkType("XSDataResCutoff", "Constructor of XSDataResCutoff", isig_cutoff, "XSDataFloat")
		self.__isig_cutoff = isig_cutoff
	def getCompleteness_cutoff(self): return self.__completeness_cutoff
	def setCompleteness_cutoff(self, completeness_cutoff):
		checkType("XSDataResCutoff", "setCompleteness_cutoff", completeness_cutoff, "XSDataFloat")
		self.__completeness_cutoff = completeness_cutoff
	def delCompleteness_cutoff(self): self.__completeness_cutoff = None
	# Properties
	completeness_cutoff = property(getCompleteness_cutoff, setCompleteness_cutoff, delCompleteness_cutoff, "Property for completeness_cutoff")
	def getRes_override(self): return self.__res_override
	def setRes_override(self, res_override):
		checkType("XSDataResCutoff", "setRes_override", res_override, "XSDataFloat")
		self.__res_override = res_override
	def delRes_override(self): self.__res_override = None
	# Properties
	res_override = property(getRes_override, setRes_override, delRes_override, "Property for res_override")
	def getIsig_cutoff(self): return self.__isig_cutoff
	def setIsig_cutoff(self, isig_cutoff):
		checkType("XSDataResCutoff", "setIsig_cutoff", isig_cutoff, "XSDataFloat")
		self.__isig_cutoff = isig_cutoff
	def delIsig_cutoff(self): self.__isig_cutoff = None
	# Properties
	isig_cutoff = property(getIsig_cutoff, setIsig_cutoff, delIsig_cutoff, "Property for isig_cutoff")
	def export(self, outfile, level, name_='XSDataResCutoff'):
		showIndent(outfile, level)
		outfile.write(unicode('<%s>\n' % name_))
		self.exportChildren(outfile, level + 1, name_)
		showIndent(outfile, level)
		outfile.write(unicode('</%s>\n' % name_))
	def exportChildren(self, outfile, level, name_='XSDataResCutoff'):
		XSDataXdsOutput.exportChildren(self, outfile, level, name_)
		if self.__completeness_cutoff is not None:
			self.completeness_cutoff.export(outfile, level, name_='completeness_cutoff')
		if self.__res_override is not None:
			self.res_override.export(outfile, level, name_='res_override')
		if self.__isig_cutoff is not None:
			self.isig_cutoff.export(outfile, level, name_='isig_cutoff')
	def build(self, node_):
		for child_ in node_.childNodes:
			nodeName_ = child_.nodeName.split(':')[-1]
			self.buildChildren(child_, nodeName_)
	def buildChildren(self, child_, nodeName_):
		if child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'completeness_cutoff':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setCompleteness_cutoff(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'res_override':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setRes_override(obj_)
		elif child_.nodeType == Node.ELEMENT_NODE and \
			nodeName_ == 'isig_cutoff':
			obj_ = XSDataFloat()
			obj_.build(child_)
			self.setIsig_cutoff(obj_)
		XSDataXdsOutput.buildChildren(self, child_, nodeName_)
	#Method for marshalling an object
	def marshal( self ):
		oStreamString = StringIO()
		oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
		self.export( oStreamString, 0, name_="XSDataResCutoff" )
		oStringXML = oStreamString.getvalue()
		oStreamString.close()
		return oStringXML
	#Only to export the entire XML tree to a file stream on disk
	def exportToFile( self, _outfileName ):
		outfile = open( _outfileName, "w" )
		outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
		self.export( outfile, 0, name_='XSDataResCutoff' )
		outfile.close()
	#Deprecated method, replaced by exportToFile
	def outputFile( self, _outfileName ):
		print("WARNING: Method outputFile in class XSDataResCutoff is deprecated, please use instead exportToFile!")
		self.exportToFile(_outfileName)
	#Method for making a copy in a new instance
	def copy( self ):
		return XSDataResCutoff.parseString(self.marshal())
	#Static method for parsing a string
	def parseString( _inString ):
		doc = minidom.parseString(_inString)
		rootNode = doc.documentElement
		rootObj = XSDataResCutoff()
		rootObj.build(rootNode)
		# Check that all minOccurs are obeyed by marshalling the created object
		oStreamString = StringIO()
		rootObj.export( oStreamString, 0, name_="XSDataResCutoff" )
		oStreamString.close()
		return rootObj
	parseString = staticmethod( parseString )
	#Static method for parsing a file
	def parseFile( _inFilePath ):
		doc = minidom.parse(_inFilePath)
		rootNode = doc.documentElement
		rootObj = XSDataResCutoff()
		rootObj.build(rootNode)
		return rootObj
	parseFile = staticmethod( parseFile )
# end class XSDataResCutoff



# End of data representation classes.


