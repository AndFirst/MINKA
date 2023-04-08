from users import User, Users
from users import (
    EmptyNameError,
    RepeatedIdError,
    UserAlreadyOnList,
    UserNotOnList,
    EmptySurnameError
    )
import pytest


def test_user_creat():
    user = User('Jacek', 'Kowalski', 1, 'password')
    assert user.name() == 'Jacek'
    assert user.surname() == 'Kowalski'
    assert user.score() == 0
    assert user.id() == 1
    assert user.password() == 'password'


def test_user_creat_with_score():
    user = User('Jacek', 'Kowalski', 1, 'password', 10)
    assert user.name() == 'Jacek'
    assert user.surname() == 'Kowalski'
    assert user.score() == 10
    assert user.id() == 1
    assert user.password() == 'password'


def test_user_name_not_capitalized():
    user = User('jacek', 'Kowalski', 1, 'password')
    assert user.name() == 'Jacek'
    user.set_name('aDaM')
    assert user.name() == 'Adam'


def test_user_empty_name():
    with pytest.raises(EmptyNameError):
        User('', 'Kowalski', 3, 'password')


def test_user_empty_surname():
    with pytest.raises(EmptySurnameError):
        User('Jacek', '', 3, 'password')


def test_user_add_point():
    user = User('Jacek', 'Kowalski', 1, 'password')
    assert user.score() == 0
    user.add_point()
    assert user.score() == 1


def test_user_reset_score():
    user = User('Jacek', 'Kowalski', 1, 'password')
    user.add_point()
    assert user.score() == 1
    user.reset_score()
    assert user.score() == 0


def test_user_str():
    user = User('Jacek', 'Kowalski', 1, 'password')
    assert str(user) == "Jacek Kowalski\nid: 1\npunkty: 0"


def test_users_creat():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    user2 = User('Adam', 'Gruszka', 2, 'password')
    users = Users([user1, user2])
    assert users.users() == [user1, user2]


def test_users_creat_repeated_id():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    user2 = User('Adam', 'Gruszka', 1, 'password')
    with pytest.raises(RepeatedIdError):
        Users([user1, user2])


def test_users_add_user():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    users = Users([user1])
    assert users.users() == [user1]
    user2 = User('Adam', 'Gruszka', 2, 'password')
    users.add_user(user2)
    assert users.users() == [user1, user2]


def test_users_add_player_on_list():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    users = Users([user1])
    with pytest.raises(UserAlreadyOnList):
        users.add_user(user1)


def test_users_remove_user():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    user2 = User('Adam', 'Gruszka', 2, 'password')
    users = Users([user1, user2])
    assert users.users() == [user1, user2]
    users.remove_user(user1)
    assert users.users() == [user2]


def test_users_remove_user_not_on_list():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    user2 = User('Adam', 'Gruszka', 2, 'password')
    users = Users([user1])
    assert users.users() == [user1]
    with pytest.raises(UserNotOnList):
        users.remove_user(user2)


def test_users_split_by_score():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    user2 = User('Adam', 'Gruszka', 2, 'password')
    user3 = User('Kasia', 'Gruszka', 3, 'password')
    users = Users([user1, user2, user3])
    user3.add_point()
    user3.add_point()
    user1.add_point()
    assert users.split_by_score()[0] == [user2]
    assert users.split_by_score()[1] == [user1]
    assert users.split_by_score()[2] == [user3]


def test_users_split_by_score_the_same_score():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    user2 = User('Adam', 'Gruszka', 2, 'password')
    user3 = User('Kasia', 'Gruszka', 3, 'password')
    users = Users([user1, user2, user3])
    user3.add_point()
    assert user1.score() == 0
    assert user2.score() == 0
    assert user3.score() == 1
    assert users.split_by_score()[1] == [user3]
    assert users.split_by_score()[0] == [user1, user2]


def test_users_ranking():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    user2 = User('Adam', 'Gruszka', 2, 'password')
    user3 = User('Kasia', 'Gruszka', 3, 'password')
    users = Users([user1, user2, user3])
    user3.add_point()
    ranking = users.ranking()
    ranking = ranking.split('\n')
    assert ranking[0] == "Ranking"
    assert ranking[1] == "1.|1p.| Kasia Gruszka"
    assert ranking[2] == "2.|0p.| Jacek Kowalski"
    assert ranking[3] == "            Adam Gruszka"


def test_users_max_id():
    user1 = User('Jacek', 'Kowalski', 1, 'password')
    user2 = User('Adam', 'Gruszka', 2, 'password')
    user3 = User('Kasia', 'Gruszka', 3, 'password')
    users = Users([user1, user2, user3])
    assert users.max_id() == 3
