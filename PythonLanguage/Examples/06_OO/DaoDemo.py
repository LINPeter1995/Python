from abc import abstractmethod, ABC


class Dao(ABC):
    @abstractmethod
    def add(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def delete(self): pass

    @abstractmethod
    def find(self): pass


class DaoMySql(Dao):
    def add(self):
        print("MySQL add()")

    def update(self):
        print("MySQL update()")

    def delete(self):
        print("MySQL delete()")

    def find(self):
        print("MySQL find()")


class DaoMongoDB(Dao):
    def add(self):
        print("MongoDB add()")

    def update(self):
        print("MongoDB update()")

    def delete(self):
        print("MongoDB delete()")

    def find(self):
        print("MongoDB find()")


def main():
    dao: Dao
    dao = DaoMySql()
    # dao = DaoMongoDB()
    dao.add()
    dao.update()
    dao.delete()
    dao.find()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
