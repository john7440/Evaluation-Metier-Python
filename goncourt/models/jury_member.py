from dataclasses import dataclass
from enum import Enum
from typing import Optional

from goncourt.models.person import Person

class JuryRole(Enum):
    """
    Enumération des rôles possibles pour un membre du jury :
    PRESIDENT : rôle de président du jury
    MEMBER : rôle de membre simple du jury
    """
    PRESIDENT = "Président"
    MEMBER = "Membre"

@dataclass
class JuryMember(Person):
    """
    Classe représentant un membre du jury, héritée de Person

    - role: (JuryRole) : rôle du membre (Président ou Membre).
    - id_jury: (Optional[int]) : identifiant unique du membre du jury.
    - login: (Optional[str]) : identifiant de connexion du membre.
    - password: (Optional[str]) : mot de passe associé au login.
    """
    role: JuryRole
    id_jury: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None

    def get_role(self) -> str:
        return self.role.value
