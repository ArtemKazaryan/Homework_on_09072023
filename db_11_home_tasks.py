
# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ  !!!!!!


# Домашняя работа на 09.07.2023.
print('''Таблица Prodaves:
ID_Pr - уникальный номер продовца (первичный ключ)
Name_Pr - имя продавца
City_Pr - город в котором проживает продавец
Procent - комисcионные

Таблица Klient:
ID_KL - уникальный номер клиента (первичный ключ)
ID_Pr - уникальный номер продавца
Name_KL - имя клиента
City_KL – город, в котором живет клиент
Obl_KL – страна, в которой проживает клиент
Discoun - скидки

Таблица Zakaz:
ID_Z - уникальный номер заказа (первичный ключ)
ID_Pr – уникальный номер продавца
ID_KL - уникальный номер клиента
SUMMA - сумма заказа
Kol – количество единиц товара
DATA - дата заказа
CITY_Z – город, в который доставляется заказ
Cena_Dostavki - цена доставки заказа''')

import sqlite3 as sq
with sq.connect('db_11.db') as con:
    cur = con.cursor()
    print()
    print('Решения заданий домашней работы (запустите код в python и получите ответы):')
    print('1. С помощью объединения вывести данные о каждом заказчике, для которого определен продавец.')
    cur.execute('''SELECT * 
                   FROM Klient 
                   WHERE ID_Pr IN (SELECT ID_Pr
                                   FROM Prodaves
                                   WHERE Prodaves.ID_Pr = Klient.ID_Pr)
                   GROUP BY Klient.ID_Pr
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('2. Вывести имя заказчика и данные о средней цене доставки для него.'
          'Если цена доставки больше средней по таблице написать - lot, меньше – few')
    cur.execute('''SELECT Klient.Name_KL,
                          AVG(Zakaz.Cena_Dostavki) Сруд_цена_дост_для_заказчика,
                          CASE WHEN Zakaz.Cena_Dostavki > (
                                                              SELECT AVG(Cena_Dostavki) 
                                                                FROM Zakaz
                                                          )
                          THEN 'lot' ELSE 'few' END AS Статус_доставки
                     FROM Klient,
                          Zakaz
                    WHERE Klient.ID_KL = Zakaz.ID_KL
                    GROUP BY 1; 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('3. Соедините вместе все таблицы с помощью внешнего объединения.')
    cur.execute('''SELECT *
                   FROM Klient JOIN Prodaves 
                   ON Klient.ID_Pr = Prodaves.ID_Pr
                   JOIN Zakaz
                   ON Zakaz.ID_Pr = Prodaves.ID_Pr
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('4. С помощью объединения вывести данные о скидках клиента для каждого продавца.')
    cur.execute('''SELECT Klient.Name_KL, Prodaves.Name_Pr, Klient.Discoun
                   FROM Klient
                   JOIN Zakaz 
                   ON Klient.ID_KL = Zakaz.ID_KL
                   JOIN Prodaves
                   ON Zakaz.ID_Pr = Prodaves.ID_Pr
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('5. Напишите запрос, который выведет все города, в которых живут продавцы и заказчики.')
    cur.execute('''SELECT Prodaves.City_Pr, Klient.City_KL
                   FROM Prodaves
                   JOIN Klient 
                   ON Klient.ID_KL = Zakaz.ID_KL
                   JOIN Zakaz
                   ON Zakaz.ID_Pr = Prodaves.ID_Pr
                   AND Klient.City_KL = Prodaves.City_Pr
                   GROUP BY 1
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('6. С помощью объединения вывести все данные о заказчиках и заказах,'
          ' даже если заказчик не сделал ни одного заказа за указанный период.')
    cur.execute('''SELECT *
                   FROM Klient
                   JOIN Zakaz
                   ON Klient.ID_KL = Zakaz.ID_KL
                   AND Zakaz.DATA BETWEEN '1996-10-04 00:00:00' AND '1996-10-06 00:00:00'
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('7. Составьте запроса для вывода имен и кодов всех продавцов,'
          ' в чьих городах есть покупатели, которых они не обслуживают.'
          ' С помощью оператора в подзапросе.')
    cur.execute('''SELECT Name_Pr,
                          ID_Pr
                     FROM Prodaves
                    WHERE City_Pr IN (
                              SELECT City_KL
                                FROM Klient
                               WHERE ID_KL NOT IN (
                                         SELECT ID_KL
                                           FROM Zakaz
                                          WHERE Prodaves.ID_Pr != Klient.ID_Pr
                                     )
                          );
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('8. Напишите запрос, который выведет все города и имена продавцов и заказчиков,'
          ' которые живут в Лондоне.')
    cur.execute('''SELECT Zakaz.ID_Z,
       Klient.Name_KL,
       Klient.City_KL,
       Prodaves.Name_Pr,
       Prodaves.City_Pr
  FROM Klient,
       Prodaves,
       Zakaz
 WHERE Klient.City_KL = 'London' AND 
       Klient.City_KL = Prodaves.City_Pr AND 
       Klient.ID_Pr = Prodaves.ID_Pr AND 
       Klient.ID_KL = Zakaz.ID_KL
 ORDER BY 1
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)

