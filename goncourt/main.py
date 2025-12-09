from goncourt.daos.author_dao import AuthorDao
from goncourt.daos.book_dao import BookDao
from goncourt.daos.jury_member_dao import JuryMemberDao
from goncourt.daos.publisher_dao import PublisherDao
from goncourt.daos.selection_dao import SelectionDao


def main():
    dao = SelectionDao()
    authors = dao.read_all()
    for author in authors:
        print(author)

if __name__ == "__main__":
    main()