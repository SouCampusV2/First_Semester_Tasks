from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QDialog, QLineEdit, QComboBox, QMessageBox, QWidget, QInputDialog, QListWidget, QHBoxLayout
from UserC import User # Мой класс где я выполняю функции связанные с БД
from Products import Product # Класс для продуктов и действиями над ними - хочу вынести весь код связанный с продуктами в него(не успел этог сделать), плюс добавить функционала по типу сортировки продуктов, картинки и поработать над дизайном.
import sqlite3

class RegistrationDialog(QDialog): # Класс для окна с регистрацией - в ней происходит ввод всех данных
    def __init__(self):
        super().__init__() # Просто конструктор родительского класса

        # Некие параметры окна
        self.setWindowTitle('Registration')
        self.resize(640, 480)

        # Создаю все кнопочки поля и тд
        self.init_ui()

    def init_ui(self):
        # Просто контейнер в котром все мои кнопочки будут вертикально - для удобного размещения
        layout = QVBoxLayout()

        # Далее все одинаково - создаем поле редактируемое, с серым текстом так сказать после чего добавляем  в лист layout
        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText('Enter your login')
        layout.addWidget(self.login_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Enter your password')
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.role_input = QComboBox(self)
        self.role_input.addItems(['Seller', 'Customer'])
        layout.addWidget(self.role_input)

        self.register_button = QPushButton('Register', self)
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    # Функция для получения информацию из полей и вызов метода класса(временно) Тест.пу и соотвественно вывод о состоянии
    def register(self):
        login = self.login_input.text()
        password = self.password_input.text()
        role = self.role_input.currentText()
        budget = 0

        # Экземпляр класса
        user = User(login, password, role, budget)
        # Метод регистрации
        result = user.reg()

        # Рег ретурнит нам текст и просто выводим по нему результат.
        if(result == "You are registered"):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Registration")
            msg.setText(result)
            msg.exec_()
        else:
            # Если мы регаемся и выдаст ошибку о которой я не знаю, будет тот же текст, но в консоли я увижу нужную ошибку и обработую
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Registration")
            msg.setText(result)
            msg.exec_()

        self.accept()

class LoginDialog(QDialog): # Класс для окна с логином, после открывается конркетное окно и программа под пользователя "Продавца" или же "Покупателя"
    def __init__(self):
        super().__init__()

        # Некие параметры окна
        self.setWindowTitle('Logining')
        self.resize(640, 480)

        # Создаю все кнопочки поля и тд
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText('Enter your login')
        layout.addWidget(self.login_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Enter your password')
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        # Получаем пароль и логин с полей
        login = self.login_input.text()
        password = self.password_input.text()

        # Создаем объект пользователя для проверки логина и пароля
        user = User(login, password, '', '') 
        # В экземпляре проверяем есть ли такой пользователь и кто он
        result = user.logining()  
        if result[0] == "Login successful":
            print(result[0])
            print(result[1])
            # Присваиваю эти все перемены так как они мне понадобятся в будущем для входов и проверок - 
            self.user = user
            self.user.role = result[1]
            self.user.budget = result[2]
            # Закрыть окно входа после успешного входа
            self.accept()  
        else:
            print(result)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Logining")
            msg.setText(result[0])
            msg.exec_()

class SellerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Seller Window')
        self.resize(1080,680)

        self.selected_products = []  # Выбранные продукты

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Виджет для отображения списка продуктов
        self.product_list_widget = QListWidget(self)
        layout.addWidget(self.product_list_widget)

        label = QLabel(f'Welcome to LidlXXX', self)
        layout.addWidget(label)
        self.load_products()
        add_product_button = QPushButton('Add Product', self)
        add_product_button.clicked.connect(self.add_product)
        layout.addWidget(add_product_button)

        self.setLayout(layout)

    def load_products(self): # Метод для загрузки всех продуктов и данных
        try:
            con = sqlite3.connect("products.db")
            cursor = con.cursor()

            # Получаем все продукты из базы данных
            cursor.execute("SELECT * FROM Product")
            products = cursor.fetchall()

            # Отображаем продукты в списке
            self.product_list_widget.clear()
            for product in products:
                name, price, count = product[1], product[2], product[3]
                self.product_list_widget.addItem(f"{name} - Price: ${price} - Available: {count}")

        except Exception as e:
            print(f"Error loading products: {e}")
        finally:
            if con:
                con.close()

    def add_product(self): # Добавление продуктов
        # Открываем диалоговое окно для ввода информации о продукте
        name, ok = QInputDialog.getText(self, 'Add Product', 'Enter product name:')
        print(name)
        if not ok:
            return
        
        price, ok = QInputDialog.getDouble(self, 'Add Product', 'Enter product price:')
        if not ok:
            return

        count, ok = QInputDialog.getInt(self, 'Add Product', 'Enter product count:')
        if not ok:
            return

        # Создаем экземпляр класса Product и используем его метод add
        product = Product(name, float(price), float(count))
        result = product.add()
        self.load_products()

        QMessageBox.information(self, 'Product Added', result)
     
class CustomerWindow(QWidget):
    def __init__(self, login, password, role, budget):
        super().__init__()

        self.user = User(login, password, role, budget)
        self.setWindowTitle('Customer Window')
        self.resize(1080,680)

        self.selected_products = []  # Выбранные продукты

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Виджет для отображения списка продуктов
        self.product_list_widget = QListWidget(self)
        layout.addWidget(self.product_list_widget)

        self.label1 = QLabel(f'Your budget: {self.user.budget}', self)
        layout.addWidget(self.label1)

        add_budget_button = QPushButton('Add Budget', self)
        add_budget_button.clicked.connect(lambda: self.add_budget())
        layout.addWidget(add_budget_button)

        # Виджет для выбора продукта и количества
        selection_layout = QHBoxLayout()

        self.product_combobox = QComboBox(self)
        self.product_combobox.addItem("Select Product")

        self.load_products()

        self.quantity_label = QLabel('Quantity:', self)
        self.quantity_input = QInputDialog(self)
        self.quantity_input.setLabelText("Enter quantity:")
        self.quantity_input.setIntRange(1, 100)  # Ограничение на количество

        self.add_button = QPushButton('Add to Cart', self)
        self.add_button.clicked.connect(lambda: self.add_to_cart())

        selection_layout.addWidget(self.product_combobox)
        selection_layout.addWidget(self.quantity_label)
        selection_layout.addWidget(self.quantity_input)
        selection_layout.addWidget(self.add_button)

        layout.addLayout(selection_layout)

        # Виджет для отображения выбранных продуктов и общей стоимости
        self.cart_label = QLabel('Shopping Cart:', self)
        layout.addWidget(self.cart_label)

        self.cart_list_widget = QListWidget(self)
        layout.addWidget(self.cart_list_widget)

        self.setLayout(layout)
        
    def load_products(self): # Все тот же метод чтобы подгружать продукты, в будущем вынесу его в класс продукты
        try:
            con = sqlite3.connect("products.db")
            cursor = con.cursor()

            # Получаем все продукты из базы данных
            cursor.execute("SELECT * FROM Product")
            products = cursor.fetchall()

            # Отображаем продукты в списке
            self.product_list_widget.clear()
            self.product_combobox.clear()
            self.product_combobox.addItem("Select product: ")

            for product in products:
                name, price, count = product[1], product[2], product[3]
                self.product_combobox.addItem(name)
                self.product_list_widget.addItem(f"{name} - Price: ${price} - Available: {count}")

        except Exception as e:
            print(f"Error loading products: {e}")
        finally:
            if con:
                con.close()
    
    def add_to_cart(self,): # Добавление в корзину
        try:
            selected_product = self.product_combobox.currentText()

            # Проверка выбран ли продукт
            if not selected_product:
                QMessageBox.warning(self, 'Invalid Selection', 'Please select a valid product.')
                return

            # Получите количество
            quantity, ok = QInputDialog.getInt(self, 'Add to Cart', f'Enter quantity for {selected_product}:'   )

            # Проверка ввел ли я количество
            if not ok or quantity <= 0:
                QMessageBox.warning(self, 'Invalid Quantity', 'Please enter a valid quantity.')
                return
        
            # Проверка достаточно ли количества товара
            available_quantity = self.get_product_quantity(selected_product)
            if quantity > available_quantity:
                QMessageBox.warning(self, 'Not Enough Stock', f'There is not enough stock for {selected_product}. Available: {available_quantity}.')
                return
        
            # Проверка хватает ли бюджета для покупки
            price = self.get_product_price(selected_product)
            if self.user.budget > price * quantity:
                self.user.budget -= price * quantity
                self.label1.setText(f"Your budget: {self.user.budget}")
                self.user.update_budget(self.user.budget)
       
            total_cost = price * quantity
        
            # Проверка хватает ли денюжек
            if total_cost > self.user.budget: 
                QMessageBox.warning(self, 'Insufficient Funds', 'You do not have enough budget for this purchase.')
                return

            self.selected_products.append((selected_product, quantity, total_cost))
        except Exception as e:
            message = f"Error with something: {e}. Try again."
            print(message)
        finally: 
            # Обновляю отображение корзины и общей стоимости
            self.update_cart_display()
    
    def get_product_quantity(self, product_name):
        try:
            con = sqlite3.connect("products.db")
            cursor = con.cursor()

            # Получаем количество продукта из базы данных
            cursor.execute("SELECT count FROM Product WHERE name=?", (product_name,))
            quantity = cursor.fetchone()

            if quantity:
                return quantity[0]

        except Exception as e:
            print(f"Error getting product quantity: {e}")
        finally:
            if con:
                con.close()

        return 0
    
    def update_product_quantity(self, product_name, purchased_quantity):
        try:
            con = sqlite3.connect("products.db")
            cursor = con.cursor()

            # Получите текущее количество продукта из базы данных
            cursor.execute("SELECT count FROM Product WHERE name=?", (product_name,))
            current_quantity = cursor.fetchone()

            if current_quantity:
                new_quantity = current_quantity[0] - purchased_quantity

                # Обновите количество продукта в базе данных
                cursor.execute("UPDATE Product SET count=? WHERE name=?", (new_quantity, product_name))
                con.commit()
                self.load_products()

        except Exception as e:
            print(f"Error updating product quantity: {e}")
        finally:
            if con:
                con.close()

    def update_cart_display(self): # Добавляем продукты в коризну и обн. виджеты
        pn = self.selected_products[0][0]
        pq = self.selected_products[0][1]
        pp = self.selected_products[0][2]
        self.selected_products.clear()

        for index in range(self.product_combobox.count()):
            product_name = self.product_combobox.itemText(index)
        
            if product_name == pn:
                # Обновляем отображение корзины и общей стоимости
                self.update_product_quantity(pn, pq)
                self.update_cart_list_widget(pn, pq, pp)

        # Очищаем поля ввода
        self.product_combobox.setCurrentIndex(0)

    def update_cart_list_widget(self, product_name, quantity, total_cost): 
        self.cart_list_widget.addItem(f"{product_name} - Quantity: {quantity} - Cost: ${total_cost}")

    def get_product_price(self, product_name):
        try:
            con = sqlite3.connect("products.db")
            cursor = con.cursor()

            # Получаем цену продукта из базы данных
            cursor.execute("SELECT price FROM Product WHERE name=?", (product_name,))
            price = cursor.fetchone()

            if price:
                print(price[0])
                return price[0]

        except Exception as e:
            print(f"Error getting product price: {e}")
        finally:
            if con:
                con.close()

        return 0
    
    def add_budget(self): # Добавление денюжек
        print(self.user.budget)
        budget, ok = QInputDialog.getInt(self, 'Add Budget', 'Enter budget:')
        if ok:
            self.user.budget += budget
            self.user.update_budget(self.user.budget)
            QMessageBox.information(self, 'Budget Added', f'Your budget is now {self.user.budget}.')
        self.label1.setText(f'Your budget: {self.user.budget}') 

class MainWindow(QMainWindow): # Класс для логина и регистрация - просто мейн окно которое открывается первым и от него все идет далее
    def __init__(self, parent=None):
        super().__init__(parent) # Все тот же конструктор

        #Все те же некие параметры окна
        self.setWindowTitle("Store Super LidlXXX")
        self.resize(1080, 680)

        # Все те же кнопочки и тд
        self.setup_ui()

    def setup_ui(self):
        # Кнопочка и ее позиция, 3 строка это стили из CSS, работают немного криво но работают остальные кнопки и тд не успел покрасить, но в будущем исправлю
        self.btn = QLabel('Login', self)
        self.btn.setGeometry(340, 340, 200, 45)
        self.btn.setStyleSheet('''
            QLabel {
                text-decoration: none;
                display: inline-block;
                width: 140px;
                height: 45px;
                line-height: 45px;
                border-radius: 45px;
                margin: 10px 20px;
                font-size: 11px;
                text-transform: uppercase;
                text-align: center;
                letter-spacing: 3px;
                font-weight: 600;
                color: #524f4e;
                background: white;
                border: 2px solid #524f4e;
                box-shadow: 0 8px 15px rgba(0, 0, 0, .1);
                transition: .3s;
            }

            QLabel:hover {
                background: #2EE59D;
                box-shadow: 0 15px 20px rgba(46, 229, 157, .4);
                color: white;
                transform: translateY(-7px);
            }
        ''')

        #Тоже самое
        self.btn2 = QLabel('Register', self)
        self.btn2.setGeometry(540, 340, 200, 45)
        self.btn2.setStyleSheet('''
            QLabel {
                text-decoration: none;
                display: inline-block;
                width: 140px;
                height: 45px;
                line-height: 45px;
                border-radius: 45px;
                margin: 10px 20px;
                font-size: 11px;
                text-transform: uppercase;
                text-align: center;
                letter-spacing: 3px;
                font-weight: 600;
                color: #524f4e;
                background: white;
                border: 2px solid #524f4e;
                box-shadow: 0 8px 15px rgba(0, 0, 0, .1);
                transition: .3s;
            }

            QLabel:hover {
                background: #2EE59D;
                box-shadow: 0 15px 20px rgba(46, 229, 157, .4);
                color: white;
                transform: translateY(-7px);
            }
        ''')

        # По нажатию на кнопочку вызываем регистрацию, почему лямбда не знаю, так интернет сказал.
        self.btn.mousePressEvent = lambda event: self.show_logining_window()
        self.btn2.mousePressEvent = lambda event: self.show_register_window()

    def show_logining_window(self):
        logining_dialog = LoginDialog()

        result = logining_dialog.exec_()
        print(logining_dialog.user.login)
        print(logining_dialog.user.role)
        if result == QDialog.Accepted:
            print("Logining successful!")
            if logining_dialog.user.role == "Seller":
                # Создайем окно для продавца
                self.seller_window = SellerWindow()
                self.seller_window.show()
                print("Cool")
            elif logining_dialog.user.role == "Customer":
                # Создаем окно для покупателя
                self.customer_window = CustomerWindow(logining_dialog.user.login, logining_dialog.user.password, logining_dialog.user.role, logining_dialog.user.budget)
                self.customer_window.show()
            else:
                print("Invalid role")
        else:
            print("Logining canceled.") 

    def show_register_window(self):
        # Создаем экземпляр обьекта класса регистрации
        register_dialog = RegistrationDialog()
        # Просто достаем резульат из всего окна что по итогу, получилось или нет, именно у экзепляра, а не из метода/функции, так как там все работает внутри класса
        result = register_dialog.exec_()
        # Для отлавливания ошибок, для себя просматриваю в консоли
        if result == QDialog.Accepted:
            print("Registration successful!")
        else:
            print("Registration canceled.")

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()