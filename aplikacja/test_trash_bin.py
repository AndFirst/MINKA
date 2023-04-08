from trash_bin import TrashBin, TrashBins
from users import RepeatedIdError
import pytest


def test_trash_bin_creat():
    bin = TrashBin(1, 12, False, 2)
    assert bin.id() == 1
    assert bin.full() is False
    assert bin.apartment() == 12
    assert bin.user_throwing() == 2


def test_trash_bin_creat_full_default():
    bin = TrashBin(1, 12)
    assert bin.id() == 1
    assert bin.apartment() == 12
    assert bin.full() is False


def test_trash_bin_creat_user_throwing_default():
    bin = TrashBin(1, 12)
    assert bin.id() == 1
    assert bin.apartment() == 12
    assert bin.user_throwing() == ''


def test_trash_bin_set_full():
    bin = TrashBin(1, 12)
    assert bin.full() is False
    bin.set_full(True)
    assert bin.full() is True


def test_trash_bin_set_user_throwing():
    bin = TrashBin(1, 12)
    assert bin.user_throwing() == ''
    bin.set_user_throwing(3)
    assert bin.user_throwing() == 3


def test_trash_bins_creat():
    bin1 = TrashBin(1, 12)
    bin2 = TrashBin(2, 12, True)
    bins = TrashBins([bin1, bin2])
    assert bins.bins() == [bin1, bin2]


def test_trash_bins_repeated_id():
    bin1 = TrashBin(1, 12)
    bin2 = TrashBin(1, 12, True)
    with pytest.raises(RepeatedIdError):
        TrashBins([bin1, bin2])
