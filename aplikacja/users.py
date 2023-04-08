class EmptyNameError(Exception):
    def __init__(self):
        super().__init__("User's name cannot be empty")


class EmptySurnameError(Exception):
    def __init__(self):
        super().__init__("User's surname cannot be empty")


class RepeatedIdError(Exception):
    def __init__(self):
        super().__init__("Id cannot be repeated")


class UserAlreadyOnList(Exception):
    def __init__(self):
        super().__init__("User is already on the list")


class UserNotOnList(Exception):
    def __init__(self):
        super().__init__("User is not on the list and cannot be removed")


class User:
    """
    Class User. Contains attributes:
    :param name: user's name
    :type name: str

    :param surname: user's surname
    :type surname: str

    :param id: user's identification number
    :type id: int

    :param score: user's score, defaults to 0
    :type score: int

    :param password: user's password
    :type password: str
    """
    def __init__(self, name: str, surname: str, id: int, password: str, score: int = 0):
        """
        Creats instance of User.
        """
        self.set_name(name)
        self.set_surname(surname)
        self._score = score
        self._id = id
        self._password = password

    def name(self):
        """
        Returns user's name
        """
        return self._name

    def set_name(self, name: str):
        """
        Sets user's name to given name in capitalized form
        (first letter upper case, rest lower case)

        Raises EmptyNameError if given name is empty
        """
        if not name:
            raise EmptyNameError
        self._name = str(name).capitalize()

    def surname(self):
        """
        Returns user's surname
        """
        return self._surname

    def set_surname(self, surname: str):
        """
        Sets user's surname to given surname in capitalized form
        (first letter upper case, rest lower case)

        Raises EmptySurnameError if given surname is empty
        """
        if not surname:
            raise EmptySurnameError
        self._surname = str(surname).capitalize()

    def id(self):
        """
        Returns user's identification number
        """
        return self._id

    def password(self):
        """
        Returns user's password
        """
        return self._password

    def score(self):
        """
        Returns user's score
        """
        return self._score

    def add_point(self):
        """
        Adds user one point to the score
        """
        self._score += 1

    def reset_score(self):
        """
        Resets user's score (sets it to 0)
        """
        self._score = 0

    def __str__(self):
        """
        Returns player's info
        """
        name_and_surname = f'{self.name()} {self.surname()}'
        return f'{name_and_surname}\nid: {self.id()}\npunkty: {self.score()}'


class Users:
    """
    Class Users. Contains attributes:
    :param users: list of users
    :type users: list
    """
    def __init__(self, users: list):
        """
        Creats instance of Users
        """
        self.set_users(users)

    def users(self):
        """
        Returns users' list
        """
        return self._users

    def set_users(self, users: list):
        """
        Sets users' list to given list

        Raises RepeatedIdError if user's id repeats in given list
        """
        users_id = [user.id() for user in users]
        if len(users_id) != len(set(users_id)):
            raise RepeatedIdError
        self._users = users
        self._users_id = users_id

    def add_user(self, user: 'User'):
        """
        Adds user to users' list

        Raises UserAlreadyOnList if given user is already on users' list
        """
        if user.id() in self._users_id:
            raise UserAlreadyOnList
        self.users().append(user)

    def remove_user(self, user: 'User'):
        """
        Removes user from users' list

        Raises UserNotOnList id given user is not on the users' list
        """
        if user.id() not in self._users_id:
            raise UserNotOnList
        self.users().remove(user)

    def split_by_score(self) -> dict:
        """
        Returns dictionary where key is score and values are lists of
        users with this score
        """
        users = self.users()
        users_dict = {}
        for user in users:
            score = user.score()
            if score in users_dict.keys():
                users_dict[score].append(user)
            else:
                users_dict[score] = [user]
        return users_dict

    def ranking(self) -> str:
        """
        Returns ranking of players
        """
        users = self.split_by_score()
        scores = list(users.keys())
        scores.sort(reverse=True)
        ranking = "Ranking\n"
        number = 1
        for score in scores:
            ranking += f'{str(number)}.|{score}p.| '
            number_len = len(f'{str(number)}.|{score}p.| ') + 4
            ranking += f'{users[score][0].name()} {users[score][0].surname()}'
            for user in users[score][1:]:
                ranking += '\n'
                ranking += ' ' * number_len
                ranking += f'{user.name()} {user.surname()}'
            ranking += '\n'
            number += 1
        return ranking

    def max_id(self):
        """
        Returns the biggest id from list of users
        """
        id_list = [user.id() for user in self.users()]
        return max(id_list)
