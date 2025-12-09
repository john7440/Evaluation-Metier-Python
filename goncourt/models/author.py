from dataclasses import dataclass
from typing import Optional

from goncourt.models.person import Person

@dataclass
class Author(Person):
    id_author: Optional[int] = None
    biography: Optional[str] = None

    def get_role(self) -> str:
        return 'Author'