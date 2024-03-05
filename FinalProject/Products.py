import sqlite3

class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def add(self):
        try:
            con = sqlite3.connect("products.db")
            cursor = con.cursor()

            # Проверяем, существует ли продукт с таким же именем
            cursor.execute("SELECT * FROM Product WHERE name=?", (self.name,))
            existing_product = cursor.fetchone()

            if existing_product:
                # Продукт существует, обновляем количество и цену
                updated_quantity = existing_product[3] + self.count
                updated_price = self.price if existing_product[2] != self.price else existing_product[2]

                # Обновляем информацию о продукте в базе данных
                cursor.execute("UPDATE Product SET count=?, price=? WHERE name=?", (updated_quantity, updated_price, self.name))
                message = "Product quantity and price updated!"
            else:
                # Продукта нет, добавляем новую запись
                cursor.execute("INSERT INTO Product (id, name, price, count) VALUES (NULL, ?, ?, ?)", (self.name, self.price, self.count))
                message = "Product added!"

            con.commit()
            print(message)
        except Exception as e:
            message = f"Error with something: {e}. Try again."
            print(message)
        finally:
            if con:
                con.close()
            return message