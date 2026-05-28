from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import jwt
import os

security = HTTPBearer()

JWT_SECRET = os.getenv("JWT_SECRET", "mir_super_secret_dev_key")
ALGORITHM = "HS256"

class TokenPayload(BaseModel):
    user_id: str
    tenant_id: str
    role: str

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenPayload:
    """
    Validates the JWT token, extracts tenant_id for isolation, and user role.
    """
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=[ALGORITHM])
        
        # Strict Tenant Isolation Check
        if "tenant_id" not in payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token missing tenant_id. Access denied for strict tenant isolation.",
            )
            
        return TokenPayload(**payload)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def require_role(target_resource: str):
    """
    Dependency generator for RBAC.
    """
    def role_checker(user: TokenPayload = Depends(get_current_user)):
        from api_gateway.security.rbac import RBAC
        if not RBAC.has_access(user.role, target_resource):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Role {user.role} does not have access to {target_resource}"
            )
        return user
    return role_checker
