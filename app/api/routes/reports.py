from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from datetime import date
from app.services.report_service import ReportService
from app.api.dependencies import get_report_service

router = APIRouter()

@router.get("/report")
def generate_report(
    report_date: date,
    format: str = "csv",
    report_service: ReportService = Depends(get_report_service)
):
    if format == "csv":
        csv_file = report_service.generate_csv_report(report_date)
        return StreamingResponse(
            csv_file,
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=library_report_{report_date}.csv"}
        )
    elif format == "xlsx":
        excel_file = report_service.generate_excel_report(report_date)
        return StreamingResponse(
            excel_file,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename=library_report_{report_date}.xlsx"}
        )
    else:
        raise HTTPException(status_code=400, detail="Unsupported format. Use 'csv' or 'xlsx'.")