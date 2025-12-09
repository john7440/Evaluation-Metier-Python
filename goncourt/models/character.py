from dataclasses import dataclass
from typing import Optional

@dataclass
class Character:
    name: str
    id_character: Optional[int] = None

    id_book: Optional["Book"] = None  # type: ignore

    def __str__(self):
        bk = f"{self.id_book}" if self.id_book else "No Book"
        return f"Character: {self.name} (Book: {bk})"