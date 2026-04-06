from fastapi import Header, HTTPException, Depends
from typing import List


def require_role(allowed_roles: List[str]):
    def role_checker(role: str = Header(...)):
        if role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Access forbidden: insufficient permissions"
            )
        return role
    return role_checker