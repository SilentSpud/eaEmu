##################################################
# file: StorageServer_server.py
#
# skeleton generated by "ZSI.generate.wsdl2dispatch.ServiceModuleWriter"
#      /usr/bin/wsdl2py -wb StorageServer.wsdl
#
##################################################

from ZSI.schema import GED, GTD
from ZSI.TCcompound import ComplexType, Struct
from StorageServer_types import *
from ZSI.twisted.WSresource import WSResource

# Messages
CreateRecordSoapIn = GED("http://gamespy.net/sake", "CreateRecord").pyclass

CreateRecordSoapOut = GED("http://gamespy.net/sake", "CreateRecordResponse").pyclass

UpdateRecordSoapIn = GED("http://gamespy.net/sake", "UpdateRecord").pyclass

UpdateRecordSoapOut = GED("http://gamespy.net/sake", "UpdateRecordResponse").pyclass

DeleteRecordSoapIn = GED("http://gamespy.net/sake", "DeleteRecord").pyclass

DeleteRecordSoapOut = GED("http://gamespy.net/sake", "DeleteRecordResponse").pyclass

SearchForRecordsSoapIn = GED("http://gamespy.net/sake", "SearchForRecords").pyclass

SearchForRecordsSoapOut = GED("http://gamespy.net/sake", "SearchForRecordsResponse").pyclass

GetMyRecordsSoapIn = GED("http://gamespy.net/sake", "GetMyRecords").pyclass

GetMyRecordsSoapOut = GED("http://gamespy.net/sake", "GetMyRecordsResponse").pyclass

GetSpecificRecordsSoapIn = GED("http://gamespy.net/sake", "GetSpecificRecords").pyclass

GetSpecificRecordsSoapOut = GED("http://gamespy.net/sake", "GetSpecificRecordsResponse").pyclass

GetRandomRecordsSoapIn = GED("http://gamespy.net/sake", "GetRandomRecords").pyclass

GetRandomRecordsSoapOut = GED("http://gamespy.net/sake", "GetRandomRecordsResponse").pyclass

GetRecordCountSoapIn = GED("http://gamespy.net/sake", "GetRecordCount").pyclass

GetRecordCountSoapOut = GED("http://gamespy.net/sake", "GetRecordCountResponse").pyclass

RateRecordSoapIn = GED("http://gamespy.net/sake", "RateRecord").pyclass

RateRecordSoapOut = GED("http://gamespy.net/sake", "RateRecordResponse").pyclass

GetRecordLimitSoapIn = GED("http://gamespy.net/sake", "GetRecordLimit").pyclass

GetRecordLimitSoapOut = GED("http://gamespy.net/sake", "GetRecordLimitResponse").pyclass

GetMyImagesSoapIn = GED("http://gamespy.net/sake", "GetMyImages").pyclass

GetMyImagesSoapOut = GED("http://gamespy.net/sake", "GetMyImagesResponse").pyclass

DeleteImageSoapIn = GED("http://gamespy.net/sake", "DeleteImage").pyclass

DeleteImageSoapOut = GED("http://gamespy.net/sake", "DeleteImageResponse").pyclass


# Service Skeletons
class StorageServer(WSResource):
    soapAction = {}
    root = {}

    def __init__(self, post="/SakeStorageServer/StorageServer.asmx", **kw):
        WSResource.__init__(self)

    def soap_CreateRecord(self, ps, **kw):
        request = ps.Parse(CreateRecordSoapIn.typecode)
        return request, CreateRecordSoapOut()

    soapAction["http://gamespy.net/sake/CreateRecord"] = "soap_CreateRecord"
    root[(CreateRecordSoapIn.typecode.nspname, CreateRecordSoapIn.typecode.pname)] = "soap_CreateRecord"

    def soap_UpdateRecord(self, ps, **kw):
        request = ps.Parse(UpdateRecordSoapIn.typecode)
        return request, UpdateRecordSoapOut()

    soapAction["http://gamespy.net/sake/UpdateRecord"] = "soap_UpdateRecord"
    root[(UpdateRecordSoapIn.typecode.nspname, UpdateRecordSoapIn.typecode.pname)] = "soap_UpdateRecord"

    def soap_DeleteRecord(self, ps, **kw):
        request = ps.Parse(DeleteRecordSoapIn.typecode)
        return request, DeleteRecordSoapOut()

    soapAction["http://gamespy.net/sake/DeleteRecord"] = "soap_DeleteRecord"
    root[(DeleteRecordSoapIn.typecode.nspname, DeleteRecordSoapIn.typecode.pname)] = "soap_DeleteRecord"

    def soap_SearchForRecords(self, ps, **kw):
        request = ps.Parse(SearchForRecordsSoapIn.typecode)
        return request, SearchForRecordsSoapOut()

    soapAction["http://gamespy.net/sake/SearchForRecords"] = "soap_SearchForRecords"
    root[(SearchForRecordsSoapIn.typecode.nspname, SearchForRecordsSoapIn.typecode.pname)] = "soap_SearchForRecords"

    def soap_GetMyRecords(self, ps, **kw):
        request = ps.Parse(GetMyRecordsSoapIn.typecode)
        return request, GetMyRecordsSoapOut()

    soapAction["http://gamespy.net/sake/GetMyRecords"] = "soap_GetMyRecords"
    root[(GetMyRecordsSoapIn.typecode.nspname, GetMyRecordsSoapIn.typecode.pname)] = "soap_GetMyRecords"

    def soap_GetSpecificRecords(self, ps, **kw):
        request = ps.Parse(GetSpecificRecordsSoapIn.typecode)
        return request, GetSpecificRecordsSoapOut()

    soapAction["http://gamespy.net/sake/GetSpecificRecords"] = "soap_GetSpecificRecords"
    root[(GetSpecificRecordsSoapIn.typecode.nspname, GetSpecificRecordsSoapIn.typecode.pname)] = "soap_GetSpecificRecords"

    def soap_GetRandomRecords(self, ps, **kw):
        request = ps.Parse(GetRandomRecordsSoapIn.typecode)
        return request, GetRandomRecordsSoapOut()

    soapAction["http://gamespy.net/sake/GetRandomRecords"] = "soap_GetRandomRecords"
    root[(GetRandomRecordsSoapIn.typecode.nspname, GetRandomRecordsSoapIn.typecode.pname)] = "soap_GetRandomRecords"

    def soap_GetRecordCount(self, ps, **kw):
        request = ps.Parse(GetRecordCountSoapIn.typecode)
        return request, GetRecordCountSoapOut()

    soapAction["http://gamespy.net/sake/GetRecordCount"] = "soap_GetRecordCount"
    root[(GetRecordCountSoapIn.typecode.nspname, GetRecordCountSoapIn.typecode.pname)] = "soap_GetRecordCount"

    def soap_RateRecord(self, ps, **kw):
        request = ps.Parse(RateRecordSoapIn.typecode)
        return request, RateRecordSoapOut()

    soapAction["http://gamespy.net/sake/RateRecord"] = "soap_RateRecord"
    root[(RateRecordSoapIn.typecode.nspname, RateRecordSoapIn.typecode.pname)] = "soap_RateRecord"

    def soap_GetRecordLimit(self, ps, **kw):
        request = ps.Parse(GetRecordLimitSoapIn.typecode)
        return request, GetRecordLimitSoapOut()

    soapAction["http://gamespy.net/sake/GetRecordLimit"] = "soap_GetRecordLimit"
    root[(GetRecordLimitSoapIn.typecode.nspname, GetRecordLimitSoapIn.typecode.pname)] = "soap_GetRecordLimit"

    def soap_GetMyImages(self, ps, **kw):
        request = ps.Parse(GetMyImagesSoapIn.typecode)
        return request, GetMyImagesSoapOut()

    soapAction["http://gamespy.net/sake/GetMyImages"] = "soap_GetMyImages"
    root[(GetMyImagesSoapIn.typecode.nspname, GetMyImagesSoapIn.typecode.pname)] = "soap_GetMyImages"

    def soap_DeleteImage(self, ps, **kw):
        request = ps.Parse(DeleteImageSoapIn.typecode)
        return request, DeleteImageSoapOut()

    soapAction["http://gamespy.net/sake/DeleteImage"] = "soap_DeleteImage"
    root[(DeleteImageSoapIn.typecode.nspname, DeleteImageSoapIn.typecode.pname)] = "soap_DeleteImage"
