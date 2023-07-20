import csv  # A tuple


def read_rides_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dictionary(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = {
                "route": row[0],
                "date": row[1],
                "daytype": row[2],
                "rides": int(row[3]),
            }
            records.append(record)
    return records


def read_rides_as_class(filename):
    class Row:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_class_with_slots(filename):
    class Row:
        __slots__ = ["route", "date", "daytype", "rides"]

        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_namedtuples(filename):
    from collections import namedtuple

    Row = namedtuple("Row", ["route", "date", "daytype", "rides"])
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_dataclass(filename):
    from dataclasses import dataclass

    @dataclass
    class Row:
        route: str
        date: str
        daytype: str
        rides: int

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


if __name__ == "__main__":
    import tracemalloc

    for func in [
        read_rides_as_tuples,
        read_rides_as_dictionary,
        read_rides_as_class,
        read_rides_as_class_with_slots,
        read_rides_as_namedtuples,
        read_rides_as_dataclass,
    ]:
        tracemalloc.start()
        rows = func("Data/ctabus.csv")

        print(func.__name__)
        print(
            f"Current memory usage is {tracemalloc.get_traced_memory()[1] / 10 ** 6} MB"
        )
        print(f"Peak was {tracemalloc.get_traced_memory()[1] / 10 ** 6} MB")
        tracemalloc.stop()
