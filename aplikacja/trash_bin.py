from users import RepeatedIdError


class TrashBin:
    """
    Class TrashBin. Contains attributes:
    :param id: trash bin's identification number
    :type id: int

    :param apartment: apartment number in which trash bin is
    :type apartment: int

    :param full: if True trash bin is full, defaults to False
    :type full: bool (True or False)

    :param user_throwing: id of user who is throwing trash from this trash bin,
    defaults to empty string
    :type user_throwing: int
    """
    def __init__(self, id: int, apartment: int,
                 full=False, user_throwing=''):
        """
        Creats instance of TrashBin.
        """
        self._id = id
        self._full = full
        self._apartment = apartment
        self._user_throwing = user_throwing

    def id(self):
        """
        Returns trash bin's identification number.
        """
        return self._id

    def apartment(self):
        """
        Returns trash bin's apartment number.
        """
        return self._apartment

    def full(self):
        """
        Returns information whether trash bin is full(True) or not(Flase).
        """
        return self._full

    def set_full(self, full: bool):
        """
        Sets information about fullness of trash bin.
        """
        self._full = full

    def user_throwing(self):
        """
        Returns id of user who is throwing trash from this trash bin.
        """
        return self._user_throwing

    def set_user_throwing(self, user_id: int):
        """
        Sets id of user who is throwing trash from this trash bin.
        """
        self._user_throwing = user_id


class TrashBins:
    """
    Class TrashBins. Contains attributes:
    :param bins: list of trash bins
    :type bins: list
    """
    def __init__(self, bins: list):
        """
        Creats instance of TrashBins.
        """
        self.set_bins(bins)

    def bins(self):
        """
        Returns list of trash bins.
        """
        return self._bins

    def set_bins(self, bins: list):
        """
        Sets trash bins' list to given list.
        """
        bins_id = [bin.id() for bin in bins]
        if len(bins_id) != len(set(bins_id)):
            raise RepeatedIdError
        self._bins = bins
