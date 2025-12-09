from dataclasses import dataclass
from enum import Enum
from typing import Optional

from goncourt.models.person import Person

class JuryRole(Enum):
    PRESIDENT = "Président"
    MEMBER = "Membre"

@dataclass
class JuryMember(Person):
    role: JuryRole
    id_jury: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None

    def get_role(self) -> str:
        return self.role.value
