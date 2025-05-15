class ComputerBook:
    def __init__(self, name=""):
        self.name = name

    def show(self):
        print("ComputerBook.show()")


class ProgramBook(ComputerBook):
    def show(self):
        print("ProgramBook.show()")

    def executeProgram(self):
        print("ProgramBook.executeProgram()")


class DatabaseBook(ComputerBook):
    def show(self):
        print("DatabaseBook.show()")

    def executeDB(self):
        print("DatabaseBook.executeDB()")


class PythonDBBook(ProgramBook, DatabaseBook):
    def execute(self):
        super().executeDB()


def main():
    pythonMongo = PythonDBBook()
    # 會呼叫第一順位父類別的方法
    pythonMongo.show()
    pythonMongo.execute()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
