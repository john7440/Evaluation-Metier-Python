from dataclasses import dataclass
from datetime import date
from typing import Optional

"""Class représentant les votes"""
@dataclass
class Vote:
    id_vote: Optional[int]= None
    vote_date: Optional[date]= None

    id_jury_member: Optional["JuryMember"] = None  # type: ignore
    id_book: Optional["Book"] = None  # type: ignore
    id_selection: Optional["Selection"] = None  # type: ignore

    def __str__(self):
        jm = f"{self.id_jury_member}" if self.id_jury_member else "Unknown Member"
        bk = f"{self.id_book}" if self.id_book else "Unknown Book"
        sel = f"Sélection {self.id_selection}" if self.id_selection else "Unknown Selection"
        vote_val = f"(note: {self.value})" if self.value is not None else ""
        return f"Vote: {bk} par {jm} - {sel} {vote_val}"