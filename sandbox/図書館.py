import sys

class LibrarySys:
    def __init__(self, lines):
        self.data = {}
        self.reserve_data = {}
        self.opan_flag = 0
        self.borrowable_num = int(lines.pop(0))
        self.lines = lines
        self.tana = []
        self.borrow_all = []
        self.reserve_all = []

    def job(self):
        for i, v in enumerate(self.lines):
            cmd = v.split()
            operation = cmd.pop(0)

            if operation == "open":
                self.opan_flag = 1
                print("open")
            elif operation == "close":
                self.opan_flag = 0
                print("close")
            elif operation == "borrow" and self.opan_flag:
                self.borrow_book(cmd)
            elif operation == "return" and self.opan_flag:
                self.return_book(cmd)
            elif operation == "reserve" and self.opan_flag:
                self.reserve_book(cmd)



    def borrow_book(self, cmd):
        user_id = cmd.pop(0)
        book_list = sorted(cmd)

        user_data = []
        if user_id in self.data:
            user_data = self.data[user_id]

        reserve_user_data = []
        if user_id in self.reserve_data:
            reserve_user_data = self.reserve_data[user_id]

        reserve_book_list = []
        for r in reserve_user_data:
            if r in self.tana:
                self.tana.remove(r)
                reserve_book_list.append(r)

        booK_sum = len(user_data) + len(book_list) + len(reserve_book_list)

        if booK_sum <= self.borrowable_num:
            print("can")
            user_data.extend(book_list)
            user_data.extend(reserve_book_list)
            self.borrow_all.extend(book_list)
            self.borrow_all.extend(reserve_book_list)
        else:
            self.tana.extend(reserve_book_list)
            print("cannot {}".format(booK_sum - self.borrowable_num))


        self.data[user_id] = user_data

        return

    def return_book(self, cmd):
        book_list = sorted(cmd)

        for k, v in self.data.items():
            for user_book in v:
                if user_book in book_list:
                    self.data[k].remove(user_book)
                    self.borrow_all.remove(user_book)
                if user_book in self.reserve_all:
                    self.tana.append(user_book)

        print("return {}".format(" ".join(book_list)))

        return

    def reserve_book(self, cmd):
        user_id = cmd.pop(0)
        book_list = sorted(cmd)

        user_reserve_data = []
        if user_id in self.reserve_data:
            user_reserve_data = self.reserve_data[user_id]

        user_data = []
        if user_id in self.data:
            user_data = self.data[user_id]

        booK_sum = len(user_reserve_data) + len(book_list) + len(user_data)

        if booK_sum > self.borrowable_num:
            print("cannot1 {}".format(booK_sum - self.borrowable_num))
        else:
            cannot_lsit = []
            for book in book_list:
                if book in self.borrow_all:
                    cannot_lsit.append("b{}".format(book))
                elif book in self.reserve_all:
                    cannot_lsit.append("r{}".format(book))
                elif book in self.tana:
                    cannot_lsit.append("s{}".format(book))
                else:
                    pass

            if len(cannot_lsit) > 0:
                print("cannot {}".format(" ".join(cannot_lsit)))
            else:
                user_reserve_data.extend(book_list)
                self.reserve_all.extend(book_list)
                print("can")

        self.reserve_data[user_id] = user_reserve_data
        return

def main(lines):
    ls = LibrarySys(lines)
    ls.job()


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
