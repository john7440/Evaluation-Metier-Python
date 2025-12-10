from goncourt.daos.book_dao import BookDao
from goncourt.daos.selection_dao import SelectionDao
from goncourt.daos.vote_dao import VoteDao
from goncourt.menu import Menu

def main():
    menu = Menu(
        book_dao=BookDao(),
        selection_dao=SelectionDao(),
        vote_dao=VoteDao()
    )
    menu.run()

if __name__ == "__main__":
    main()