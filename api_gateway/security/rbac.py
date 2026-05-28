from enum import Enum
from typing import List

class Role(str, Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    FINANCE_EXECUTIVE = "FINANCE_EXECUTIVE"
    OPS_MANAGER = "OPS_MANAGER"

class RBAC:
    """
    Defines which roles can access which endpoints/agents.
    """
    PERMISSIONS = {
        "Agent-1": [Role.SUPER_ADMIN, Role.FINANCE_EXECUTIVE],
        "Agent-2": [Role.SUPER_ADMIN, Role.OPS_MANAGER],
        "Agent-3": [Role.SUPER_ADMIN],
        "Simulation": [Role.SUPER_ADMIN]
    }

    @staticmethod
    def has_access(user_role: str, target_resource: str) -> bool:
        if user_role == Role.SUPER_ADMIN:
            return True
        allowed_roles = RBAC.PERMISSIONS.get(target_resource, [])
        return user_role in allowed_roles
