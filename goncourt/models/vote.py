from dataclasses import dataclass
from typing import Optional

"""Class représentant les votes"""
@dataclass
class Vote:
    id_vote: Optional[int]= None

    id_jury_member: Optional["JuryMember"] = None  # type: ignore
    id_book: Optional["Book"] = None  # type: ignore

    def __str__(self):
        jm = f"{self.id_jury_member}" if self.id_jury_member else "Unknown Member"
        bk = f"{self.id_book}" if self.id_book else "Unknown Book"
        return f"Vote: {bk} par {jm}"