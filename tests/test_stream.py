from cisco_config.stream import replayable


def test_replayable():
    stream = replayable(range(10))
    record = stream.record()

    assert list(stream) == list(range(10))

    stream.record()
    stream.replay(record)

    assert list(stream) == list(range(10))

    stream.cut()
