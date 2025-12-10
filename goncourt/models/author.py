from dataclasses import dataclass
from typing import Optional

from goncourt.models.person import Person

@dataclass
class Author(Person):
    """
    Classe représentant un auteur, héritée de Person

    Attributs :
    : id_author: (Optional[int]) : identifiant unique de l'auteur (optionnel)
    : biography: (Optional[str]) : texte biographique de l'auteur (optionnel)
    """
    id_author: Optional[int] = None
    biography: Optional[str] = None

    def get_role(self) -> str:
        """ Retourne le role associé à cette classe """
        return 'Author'