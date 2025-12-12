from goncourt.daos.jury_member_dao import JuryMemberDao
from goncourt.daos.book_dao import BookDao
from goncourt.daos.selection_dao import SelectionDao
from goncourt.daos.vote_dao import VoteDao
from goncourt.menu import Menu

def main():
    """
    Initialise les DAO nécessaires (BookDao, SelectionDao, VoteDao),
    crée une instance du menu et lance l'application
    """
    menu = Menu(
        book_dao=BookDao(),
        selection_dao=SelectionDao(),
        vote_dao=VoteDao(),
        jury_dao= JuryMemberDao()
    )
    menu.run()


if __name__ == "__main__":
    """ Démarre l'application """
    main()
