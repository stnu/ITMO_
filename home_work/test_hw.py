def test_hw():
    assert ('home', 'work') == ('home', 'work')


def test_qa():
    assert 'QA' != 'QC'


def test_list():
    x = (1, 1, 2, 3, 5)
    y = (2, 3, 5)
    assert not x == y
