import types


def empty_in():
    yield from ()


def given_in(data):
    assert type(data) is bytes

    yield data


def empty_out():
    yield


def ignore_out():
    while True:
        yield


def collect_out(data_list):
    assert data_list == []

    while True:
        data_list.append((yield))


def concat(gen_1, gen_2):
    assert type(gen_1) is types.GeneratorType
    assert type(gen_2) is types.GeneratorType

    yield from gen_1
    yield from gen_2