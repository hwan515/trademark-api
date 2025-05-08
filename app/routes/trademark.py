from fastapi import APIRouter, Query
from typing import Optional, List
from app.database import get_trademarks
from app.models import Trademark

router = APIRouter()

@router.get("/search", response_model=List[Trademark])
def search_trademark(
    product_name: Optional[str] = None,
    product_name_eng: Optional[str] = None,
    register_status: Optional[str] = None,
    main_code: Optional[str] = None,
    application_from: Optional[str] = None,
    application_to: Optional[str] = None
):
    results = get_trademarks()

    if product_name:
        results = [
            r for r in results
            if r.get("productName") and product_name.lower() in r["productName"].lower()
        ]
    if product_name_eng:
        results = [
            r for r in results
            if r.get("productNameEng") and product_name_eng.lower() in r["productNameEng"].lower()
        ]
    if register_status:
        results = [
            r for r in results
            if r.get("registerStatus") == register_status
        ]
    if main_code:
        results = [
            r for r in results
            if main_code in (r.get("asignProductMainCodeList") or [])
        ]
    if application_from:
        results = [
            r for r in results
            if r.get("applicationDate") and r["applicationDate"] >= application_from
        ]
    if application_to:
        results = [
            r for r in results
            if r.get("applicationDate") and r["applicationDate"] <= application_to
        ]

    return [Trademark(**r) for r in results]
