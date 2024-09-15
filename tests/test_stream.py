from cisco_config.stream import Replayable


def test_replayable():
    stream = Replayable(iter(range(10)))
    record = stream.start_recording()

    assert list(stream) == list(range(10))

    stream.stop_recording()
    stream.replay(record)

    assert list(stream) == list(range(10))

