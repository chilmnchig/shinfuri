from shinfuri.function import process_file, average


def main():

    file = "shinfuri/point_zero.csv"
    process_file(file)

    print(average())
    print(average(engineer=True))


if __name__ == '__main__':
    main()
