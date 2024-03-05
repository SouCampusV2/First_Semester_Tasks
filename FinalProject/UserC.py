import sqlite3

class User:
    # Метод инициализации тех данных которые нам нужны
    def __init__(self, login, password, role, budget):
        self.login = login
        self.password = password
        self.role = role
        self.budget = budget

    def logining(self):
        try:
            # Подключаемся к базе данных
            con = sqlite3.connect("test.db")
            cursor = con.cursor()

            # Ищем пользователя в базе данных по логину и паролю, запрашиваем их с помощью запроса
            # Извлекает одну строку результата. Типо по одному юзеру - ид, логин, парол и тд
            cursor.execute("SELECT * FROM account WHERE login=? AND pass=?", (self.login, self.password))
            user_data = cursor.fetchone()

            if user_data:
                self.role = user_data[3]
                self.budget = user_data[4]
                message = ["Login successful", self.role, self.budget]
            else:
                message = ["Invalid login or password", self.role, self.budget]
        except Exception as e:
            # Если ошибка я отлавливаю ее и обрабатываю сам, но для пользователя одно и то же будет.
            message = [f"Error with login: {e}. Try again.", self.role, self.budget]
            print(message)
        finally:
            if con:
                con.close()
            return(message)
            
    def update_budget(self, new_budget):
        # Подключаемся к базе данных
        con = sqlite3.connect("test.db")
        cursor = con.cursor()
        # Обновление бюджета в базе данных
        cursor.execute('UPDATE account SET budget = ? WHERE login = ?', (new_budget, self.login))

        # Подтверждение изменений и закрытие соединения
        con.commit()
        con.close()

        # Обновление бюджета в объекте пользователя
        self.budget = new_budget

    def reg(self):
        try:
            # Конектимсяя к бд через скллайт3, спешал в пайтоне для нас вот придумали
            con = sqlite3.connect("test.db")
            # Интерфейс для выполнения SQL-запросов и извлечения данных из базы данных. 
            # Курсор позволяет приложению взаимодействовать с базой данных, отправлять запросы и получать результаты.
            cursor = con.cursor()
            # Запрос для доб. информации/регистрации
            cursor.execute("INSERT INTO account (id, login, pass, role, budget) VALUES (NULL, ?, ?, ?, ?)", (self.login, self.password, self.role, self.budget))

            # Для себя вывожу в консоли чтобы отлавливать ошибки.
            message = "You are registered"
            print(message)
            # После выполнения операций, ты просто юзаешь это чтобы обновиться и сохраниться, типо как с гитом только с бд
            con.commit()
        except Exception as e:
            # Если ошибка я отлавливаю ее и обрабатываю сам, но для пользователя одно и то же будет.
            message = f"Error with registration: {e}. Try again."
            print(message)
            message = ("Such login already exists")
        finally:
        # Важно закрывать соединение в блоке finally, чтобы гарантировать его закрытие,
        # даже если произошла ошибка.
            if con:
                con.close()
            return(message)