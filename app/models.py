from pydantic import BaseModel
from typing import Optional, List, Union

class Trademark(BaseModel):
    productName: Optional[str]
    productNameEng: Optional[str]
    applicationNumber: str
    applicationDate: Optional[str]
    registerStatus: Optional[str]
    publicationNumber: Optional[str]
    publicationDate: Optional[str]
    registrationNumber: Optional[Union[str, List[Optional[str]]]]
    registrationDate: Optional[Union[str, List[Optional[str]]]]
    internationalRegNumbers: Optional[str]
    internationalRegDate: Optional[str]
    priorityClaimNumList: Optional[List[str]]
    priorityClaimDateList: Optional[List[str]]
    asignProductMainCodeList: Optional[List[str]]
    asignProductSubCodeList: Optional[List[str]]
    viennaCodeList: Optional[List[str]]