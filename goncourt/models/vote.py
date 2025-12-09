from dataclasses import dataclass
from typing import Optional

"""Class représentant les votes"""
@dataclass
class Vote:
    number_vote: int

    jury_member: Optional["JuryMember"] = None  # type: ignore
    book: Optional["Book"] = None  # type: ignore

    def __str__(self):
        jm = f"{self.jury_member}" if self.jury_member else "Unknown JuryMember"
        bk = f"{self.book}" if self.book else "Unknown Book"
        return f"Vote: {self.number_vote} voix pour {bk} par {jm}"