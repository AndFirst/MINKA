from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow
from PySide2.QtWidgets import QListWidgetItem
import sys

from trash_bin import TrashBin
from users import User

from ui_aplication import Ui_MainWindow
from ui_add_user import Ui_Dialog
from ui_full_trash import Ui_Message
from ui_add_bin import Ui_BinDialog

from firebase_main import (
    set_user_data,
    list_of_users,
    check_user_particular_data,
    update_user_particular_data,
    user_instance_by_id
)
from firebase_main import (
    find_trash_bin_by_key,
    check_trash_bin_data,
    set_trash_bin_data,
    list_of_trash_bins,
    update_trash_bin_particular_data
)


class BinFullWindow(QDialog):
    """
    Class BinFullWindow (alert window about full trash bins)
    :param full: list of full trash bins
    :type full: list
    """
    def __init__(self, bin_list, parent=None):
        """
        Creats instance of BinFullWindow
        """
        super().__init__(parent)
        self.ui = Ui_Message()
        self.ui.setupUi(self)
        self.full = bin_list
        self.text()

    def text(self):
        """
        Displays alert informing how many trash bins
        are full
        """
        bins = self.full
        self.ui.message.clear()
        bins_num = len(bins)
        info = f'Alert!\nLiczba pełnych koszy: {bins_num}.\n'
        info += 'Przejdź do zakładki wyrzuć śmieci.'
        self.ui.message.setText(info)


class BinAddDialog(QDialog):
    """
    Class BinAddDialog (dialog window to add trash bin)
    """
    def __init__(self, parent=None):
        """
        Creats instance of BinAddDialog
        """
        super().__init__(parent)
        self.ui = Ui_BinDialog()
        self.ui.setupUi(self)

    def id(self):
        """
        Gets id written by user.
        """
        id = self.ui.id.text()
        return id

    def apartment(self):
        """
        Gets apartment written by user.
        """
        apartment = self.ui.apartment.text()
        return apartment

    def trash_bin(self):
        """
        Creats instance of TrashBin with given
        data
        """
        id = int(self.id())
        apartment = self.apartment()
        bin = TrashBin(id, apartment)
        return bin

    def empty_id(self):
        """
        Check if id is empty or contains letters
        If error occures, displays information about it
        """
        id = self.id()
        if not id:
            self.ui.empty_id_error.setText('Id nie może być puste')
            self.ui.empty_id_error.setStyleSheet('color: red')
            return True
        try:
            int(id)
        except ValueError:
            self.ui.empty_id_error.setText(
                'Id nie może zawierać liter, jedynie cyfry.')
            self.ui.empty_id_error.setStyleSheet('color: red')
        else:
            self.ui.empty_id_error.clear()
            return False

    def empty_apartment(self):
        """
        Check if apartment is empty
        If error occures, displays information about it
        """
        apartment = self.apartment()
        if not apartment:
            self.ui.empty_apartment_error.setText(
                'Numer mieszkanie nie może być pusty')
            self.ui.empty_apartment_error.setStyleSheet('color: red')
            return True
        else:
            self.ui.empty_apartment_error.clear()
            return False

    def accept(self):
        """
        Checks if given data is correct and close window if
        it is
        If data isn't correct displays error
        """
        id_check = self.empty_id()
        apartment_check = self.empty_apartment()
        if id_check or apartment_check:
            return
        return super().accept()


class UserAddDialog(QDialog):
    """
    Class UserAddDialog (dialog window to add user)
    """
    def __init__(self, parent=None):
        """
        Creats instance of UserAddDialog
        """
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def name(self):
        """
        Gets name written by user.
        """
        name = self.ui.name.text()
        return name

    def surname(self):
        """
        Gets surname written by user.
        """
        surname = self.ui.surname.text()
        return surname

    def password(self):
        """
        Gets password written by user.
        """
        password = self.ui.password.text()
        return password

    def id(self):
        """
        Assigns id to user
        """
        users = list_of_users()
        if not users.users():
            return 1
        max_id = users.max_id()
        return max_id + 1

    def user(self):
        """
        Creats instance of User with given
        data
        """
        name = self.name()
        surname = self.surname()
        password = self.password()
        id = self.id()
        user = User(name, surname, id, password)
        return user

    def empty_name(self):
        """
        Check if name is empty
        If error occures, displays information about it
        """
        name = self.name()
        if not name:
            self.ui.empty_name_error.setText('Imie nie może być puste')
            self.ui.empty_name_error.setStyleSheet('color: red')
            return True
        else:
            self.ui.empty_name_error.clear()
            return False

    def empty_surname(self):
        """
        Check if surname is empty
        If error occures, displays information about it
        """
        surname = self.surname()
        if not surname:
            self.ui.empty_surname_error.setText('Nazwisko nie może być puste')
            self.ui.empty_surname_error.setStyleSheet('color: red')
            return True
        else:
            self.ui.empty_surname_error.clear()
            return False

    def empty_password(self):
        """
        Check if password is empty
        If error occures, displays information about it
        """
        password = self.password()
        if not password:
            self.ui.empty_password_error.setText('Hasło nie może być puste')
            self.ui.empty_password_error.setStyleSheet('color: red')
            return True
        else:
            self.ui.empty_password_error.clear()
            return False

    def accept(self):
        """
        Checks if given data is correct and close window if
        it is
        If data isn't correct displays error
        """
        name_check = self.empty_name()
        surname_check = self.empty_surname()
        password_check = self.empty_password()
        if name_check or surname_check or password_check:
            return
        return super().accept()


class AplicationWindow(QMainWindow):
    """
    Class AplicationWindow (main window of aplication)
    """
    def __init__(self, parent=None):
        """
        Creats instance of AplicationWindow
        """
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._show_logo()
        self.ui.stack.setCurrentIndex(0)
        self.show_news()

        self.ui.users.triggered.connect(self.go_to_users)
        self.ui.ranking.triggered.connect(self.go_to_ranking)
        self.ui.throw_trash.triggered.connect(self.go_to_throw_trash)
        self.ui.main.triggered.connect(self.go_to_main)
        self.ui.confirm_throwing.triggered.connect(self.go_to_confirm_throwing)

        self.ui.add_user.clicked.connect(self.add_user)
        self.ui.add_bin.clicked.connect(self.add_bin)
        self.ui.volunteer_to_throw.clicked.connect(self.volunteer)
        self.ui.confirm.clicked.connect(self.confirm_declaration)
        self.ui.cancel.clicked.connect(self.cancel_declaration)
        self.ui.confirm_throwed.clicked.connect(self.confirm_throwing_trash)

    # Menu bar

    def go_to_main(self):
        """
        Changes current page to main page
        """
        self.ui.stack.setCurrentIndex(0)
        self.show_news()

    def go_to_users(self):
        """
        Changes current page to page with list of users
        """
        self.ui.stack.setCurrentIndex(1)
        self.ui.users_list.clear()
        self.setup_users_list()

    def go_to_ranking(self):
        """
        Changes current page to page with ranking
        """
        self.ui.stack.setCurrentIndex(2)
        self.ranking()

    def go_to_throw_trash(self):
        """
        Changes current page to page with volunteering to throw trash
        """
        self.ui.stack.setCurrentIndex(3)
        self.ui.stack_volunteer.setCurrentIndex(0)
        self.ui.volunteer_to_throw.setEnabled(False)
        self.setup_full_trash_list()

    def go_to_confirm_throwing(self):
        """
        Changes current page to page with confirming throwing trash
        """
        self.ui.stack.setCurrentIndex(4)
        self.ui.stack_confirm_throwing.setCurrentIndex(0)
        self.setup_bins_declared_list()

    # Main window

    def _show_logo(self):
        """
        Displays logo
        """
        pic = QPixmap('logo.png')
        self.ui.image.setPixmap(pic)

    def show_news(self):
        """
        Displays information about which trash bins are full
        or if there aren't any full trash bins informs about it
        """
        full_bins = find_trash_bin_by_key('full', True)
        if not full_bins:
            info = 'Informacje\n\nBrak śmieci do wyrzucenia\n'
            self.ui.news.setText(info)
            return
        else:
            news = 'Informacje\n\n'
            for key in full_bins:
                bin = check_trash_bin_data(key)
                apartment = bin['apartment']
                news += f'Kosz {key} z mieszkania {apartment} jest pełny\n'
            self.ui.news.setText(news)

    def add_user(self):
        """
        Displays dialog window to add user
        """
        dialog = UserAddDialog()
        if dialog.exec_():
            user = dialog.user()
            set_user_data(user)

    def add_bin(self):
        """
        Displays dialog window to add trash bin
        """
        dialog = BinAddDialog()
        if dialog.exec_():
            bin = dialog.trash_bin()
            set_trash_bin_data(bin)

    # Users

    def setup_users_list(self):
        """
        Adds each user from database to list widget
        and displays it
        """
        users = list_of_users()
        for user in users.users():
            description = f'{user.name()} {user.surname()}'
            item = QListWidgetItem(description)
            item.user = user
            self.ui.users_list.addItem(item)
        self.ui.users_list.itemClicked.connect(self.select_user)

    def select_user(self, item):
        """
        If user from listwidget is selected displays user's information
        """
        self.ui.user_info.clear()
        self.ui.user_info.setText(str(item.user))

    # Ranking

    def ranking(self):
        """
        Displays users' ranking
        """
        users = list_of_users()
        ranking = users.ranking()
        self.ui.ranking_list.setText(ranking)

    # Volunteer to throw trash

    def setup_full_trash_list(self):
        """
        Adds each full trash bin from database to list widget
        and displays it
        """
        self.ui.full_trash_list.clear()
        bins = list_of_trash_bins()
        for bin in bins.bins():
            if bin.full() and bin.user_throwing() == '':
                item = QListWidgetItem(f'Mieszkanie {bin.apartment()}')
                item.bin = bin
                self.ui.full_trash_list.addItem(item)
        self.ui.full_trash_list.itemClicked.connect(self.select_full_bin)

    def select_full_bin(self, item):
        """
        If trash bin from listwidget is selected
        displays users list
        """
        self.selected_bin = item.bin
        self.ui.stack_volunteer.setCurrentIndex(1)
        self.setup_users_list_throw()

    def setup_users_list_throw(self):
        """
        Displays list of users
        """
        self.ui.users_list_throw.clear()
        users = list_of_users()
        for user in users.users():
            description = f'{user.name()} {user.surname()}'
            item = QListWidgetItem(description)
            item.user = user
            self.ui.users_list_throw.addItem(item)
        self.ui.users_list_throw.itemClicked.connect(self.select_volunteer)

    def select_volunteer(self, item):
        """
        If user from list is selected enables buttom to
        volunteer to throw trash
        """
        self.user_volunteer = item.user
        self.ui.volunteer_to_throw.setEnabled(True)

    def volunteer(self):
        """
        Displays information about user who volunteered to throw
        trash and asks for password
        """
        self.ui.stack_volunteer.setCurrentIndex(2)
        self.ui.error_confirmation.clear()
        self.ui.password.clear()
        text = f'{self.user_volunteer.name()} {self.user_volunteer.surname()}'
        text += '\nWpisz swoje hasło'
        self.ui.volunteer_info.setText(text)

    def confirm_declaration(self):
        """
        Confirms declaration by checking user's password
        If incorrect password is given displays information about error
        """
        user = self.user_volunteer
        password_correct = check_user_particular_data(user.id(), 'password')
        given_password = self.ui.password.text()
        if password_correct == given_password:
            update_trash_bin_particular_data(
                self.selected_bin.id(), 'user_throwing', user.id())
            self.ui.stack_volunteer.setCurrentIndex(3)
            self.setup_full_trash_list()
            return
        else:
            self.ui.error_confirmation.setText('Nieprawidłowe hasło')

    def cancel_declaration(self):
        """
        Cancels declaration and goes back to list of users
        """
        self.ui.stack_volunteer.setCurrentIndex(1)
        self.ui.volunteer_to_throw.setEnabled(False)
        self.ui.users_list_throw.clearSelection()

    # Confirm throwing trash

    def setup_bins_declared_list(self):
        """
        Adds each trash bin, which has been volunteered to be throw
        from database to list widget and displays it
        """
        self.ui.bins_volunteered_list.clear()
        bins = list_of_trash_bins()
        for bin in bins.bins():
            if bin.user_throwing() != '':
                item = QListWidgetItem(f'Mieszkanie {bin.apartment()}')
                item.bin = bin
                self.ui.bins_volunteered_list.addItem(item)
        self.ui.bins_volunteered_list.itemClicked.connect(self.select_bin)

    def select_bin(self, item):
        """
        If trash bin is selected displays information who
        volunteered to throw trash from it
        """
        self.ui.stack_confirm_throwing.setCurrentIndex(1)
        self.ui.bin_info.clear()
        self.ui.message.clear()
        self.bin_confirm = item.bin
        user_id = self.bin_confirm.user_throwing()
        user = user_instance_by_id(user_id)
        self.user_confirm = user
        text = f"Zgłoszony użytkownik {user.name()} {user.surname()}\n"
        text += "Aby potwierdzić wyrzucenie śmieci kliknij przycisk"
        self.ui.bin_info.setText(text)
        self.ui.confirm_throwed.setEnabled(True)

    def confirm_throwing_trash(self):
        """
        Confirms that trash has been thrown from selected bin, by
        checking its status
        If trash bin is empty adds one point to user
        If trash bin is still full display information about it
        (user doesn't get any point)
        """
        bin = self.bin_confirm
        user = self.user_confirm
        if bin.full() is False:
            user.add_point()
            self.ui.message.setText("Potwierdzono wyrzucenie śmieci")
            update_trash_bin_particular_data(bin.id(), 'user_throwing', '')
            update_user_particular_data(user.id(), 'score', user.score())
            self.setup_bins_declared_list()
            self.ui.confirm_throwed.setEnabled(False)
        else:
            text = "Śmieci z tego kosza nie zostały jeszcze wyrzucone\n"
            text += "Wyrzuć śmieci i dopiero wtedy potwierdź ich wyrzucenie"
            self.ui.message.setText(text)


def guiMain(args):
    app = QApplication(args)
    window = AplicationWindow()
    window.show()

    full_bins = find_trash_bin_by_key('full', True)
    if full_bins:
        pop_app = QApplication
        pop_window = BinFullWindow(full_bins)
        pop_window.show()
        return pop_app.exec_()

    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
