from dataclasses import dataclass
from typing import Optional

@dataclass
class Character:
    name: str

    book: Optional["Book"] = None  # type: ignore

    def __str__(self):
        bk = f"{self.book}" if self.book else "No Book"
        return f"Character: {self.name} (Book: {bk})"