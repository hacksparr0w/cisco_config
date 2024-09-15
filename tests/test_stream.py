from cisco_config.stream import replayable


def test_replayable():
    stream = replayable(range(10))
    record = stream.start_recording()

    assert list(stream) == list(range(10))

    stream.stop_recording()
    stream.replay(record)

    assert list(stream) == list(range(10))
