import pytest

def test_screen_locate_is_open_gap():
    from src.deskrecorder import screen_locate
    with pytest.raises(NotImplementedError):
        screen_locate.process({"id": "x"})

def test_batch_is_open_gap():
    from src.deskrecorder import batch
    with pytest.raises(NotImplementedError):
        batch.process({"id": "x"})
