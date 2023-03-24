class Stats(object):
    def __init__(self, list_):
        list_.sort()
        self.list_ = list_

    def __str__(self):
        return str(self.list_)

    def mean(self):
        return sum(self.list_) / len(self.list_)

    def median(self):
        if len(self.list_) % 2 == 0:
            return (self.list_[len(self.list_)//2] + self.list_[len(self.list_)//2 - 1]) / 2
        else:
            return self.list_[len(self.list_)//2]

    def mode(self):
        sum_ = 1
        max_sum = 1
        index = 0
        temp = self.list_[0]
        for i in range(1, len(self.list_)):
            if self.list_[i] == temp:
                sum_ += 1
            else:
                temp = self.list_[i]
                if sum_ > max_sum:
                    max_sum = sum_
                    index = i - 1
                sum_ = 1
        if sum_ > max_sum:
            index = len(self.list_) - 1
        return self.list_[index]


def main():
    list_num = input("Enter number:")
    list_ = []
    for i in list_num.split():
        list_.append(int(i))
    stats = Stats(list_)
    print("Mean:", stats.mean())
    print("Median:", stats.median())
    print("Mode:", stats.mode())


if __name__ == '__main__':
    main()