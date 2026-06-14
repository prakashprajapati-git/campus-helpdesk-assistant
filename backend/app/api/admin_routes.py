from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.schemas import APIResponse, AuditLogResponse, EscalationResponse, TicketResponse, TicketUpdate
from app.services.audit_service import AuditService
from app.services.database_services import DBService
from typing import List

router = APIRouter()

@router.get("/audit-logs", response_model=APIResponse[List[AuditLogResponse]])
def view_system_audit_trail(db: Session = Depends(get_db)):
    """
    Retrieve system execution records tracking agent selections and confidence scores.
    """
    logs = AuditService.get_all_logs(db)
    return APIResponse(
        success=True,
        message="System audit telemetry retrieved successfully.",
        data=logs
    )

@router.get("/escalations", response_model=APIResponse[List[EscalationResponse]])
def view_escalated_student_queries(db: Session = Depends(get_db)):
    """
    Retrieve a list of student queries that the RAG model could not confidently resolve.
    """
    escalations = AuditService.get_all_escalations(db)
    return APIResponse(
        success=True,
        message="Active low-confidence escalations retrieved successfully.",
        data=escalations
    )

@router.put("/tickets/{ticket_id}", response_model=APIResponse[TicketResponse])
def administrative_modify_ticket(ticket_id: str, update_data: TicketUpdate, db: Session = Depends(get_db)):
    """
    Administrative control endpoint to change a student grievance ticket's tracking status flag.
    """
    updated_ticket = DBService.update_ticket_status(db, ticket_id=ticket_id, current_status=update_data.status)
    
    if not updated_ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Target grievance record tracking key '{ticket_id}' could not be located in database records."
        )
        
    return APIResponse(
        success=True,
        message=f"Grievance record '{ticket_id}' successfully shifted to status state: {update_data.status}.",
        data=updated_ticket
    )