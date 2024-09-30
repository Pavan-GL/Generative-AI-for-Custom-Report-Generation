from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils import ReportGenerator

report_router = APIRouter()

@report_router.post("/generate-report/")
async def create_report(file: UploadFile = File(...)):
    try:
        # Read the file content
        content = await file.read()
        
        # Initialize the ReportGenerator with the file content
        report_generator = ReportGenerator(content)
        
        # Generate the report
        report = report_generator.generate_report()
        
        return {"report": report}
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    
    except RuntimeError as re:
        raise HTTPException(status_code=500, detail=str(re))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
