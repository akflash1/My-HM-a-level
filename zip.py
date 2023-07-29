def my_zip(*args):
    iterators = [iter(iterable) for iterable in args]
    while True:
        try:
            yield tuple(next(itr) for itr in iterators)
        except StopIteration:
            if any(itr is not None for itr in iterators):
                continue
            return

Numbers = [7, 10, 19, 9]
Team = ['Real Madrid', 'Manchester City', 'Arsenal', 'Milan']
Players = ['CR7', 'Erling Haaland', 'Oleksandr Zinchenko', 'Zlatan Ibrahimović']
zipped = my_zip(Numbers, Team, Players)