
import sqlite3 as sq

with sq.connect('db_9.db') as con:
    cur = con.cursor()
    print()
    print('Решения заданий классной работы (запустите код в python и получите ответы):')
    print('1. Выведите список студентов физико-математического факультета.')
    cur.execute('''SELECT Student.FIO
                   FROM Student
                   JOIN G ON Student."Group" = G."Group"
                   JOIN Kafedra ON G.Kafedra = Kafedra.Kafedra
                   WHERE Kafedra.Decanat = 'Физико-математический'
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('2. Студенты какой кафедры и факультета сдавали социологию.')
    cur.execute('''SELECT Kafedra, Decanat
                   FROM Kafedra
                   WHERE Kafedra IN (
                           SELECT Kafedra
                           FROM G
                           WHERE "GROUP" IN (
                               SELECT "GROUP"
                               FROM Student
                               WHERE ID_St IN (
                                   SELECT id_St
                                   FROM Exzamen
                                   WHERE Predmet = 'Социология'
                              ))) 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('3. Выведите кафедры, список студентов, список студентов в алфавитном порядке.')
    cur.execute('''SELECT Student.FIO, G.Kafedra
                   FROM Student JOIN G ON Student."Group" = G."Group"
                   GROUP BY 1
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('4. Вывести номера зачеток только студентов физико-технического факультета.')
    cur.execute('''SELECT Zachetki.N_Z, Kafedra.Decanat
                   FROM Zachetki
                   JOIN Student ON Zachetki.id_Studenta = Student.ID_St 
                   JOIN G ON G."Group" = Student."Group" 
                   JOIN Kafedra ON G.Kafedra = Kafedra.Kafedra
                   WHERE Kafedra.Decanat = 'Физико-технический'
                   GROUP BY 1
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('5. Выведите студентов физико-технического факультета сдавших иностранный язык на 5.')
    cur.execute('''SELECT Student.FIO, Kafedra.Decanat, Exzamen.Predmet, Exzamen.Ball
                   FROM Student
                   JOIN G ON G."Group" = Student."Group"  
                   JOIN Kafedra ON G.Kafedra = Kafedra.Kafedra
                   JOIN Exzamen ON Exzamen.id_St = Student.ID_St
                   WHERE Exzamen.Predmet = 'Иностр. язык' AND Exzamen.Ball = 5
                   GROUP BY 1 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('6. Подсчитать сколько различных предметов сдавалось в сессию.')
    cur.execute('''SELECT COUNT(DISTINCT Predmet) RAZNYX_PREDMETOV
                   FROM Exzamen
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('7. Напишите запрос, который выводит средний балл по экзаменам Васильевой.')
    cur.execute('''SELECT Student.FIO, Round(AVG(Exzamen.Ball), 2) SREDNIY_BALL
                   FROM Exzamen
                   JOIN Student ON Student.ID_St = Exzamen.id_St
                   AND Student.FIO LIKE 'Васильева%'
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('8. Определите сколько человек учится на каждой специальности.')
    cur.execute('''SELECT Special, COUNT(FIO) STUDENTOV
                   FROM Student 
                   GROUP BY 1 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('9. Напишите запрос, который покажет все группы физико-технического факультета.')
    cur.execute('''SELECT "Group"
                   FROM G
                   JOIN Kafedra ON Kafedra.Kafedra = G.Kafedra 
                   AND Kafedra.Decanat = 'Физико-технический' 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('10. Вывести список фамилий студентов получивших 5 баллов по дифференциальным уравнениям.')
    cur.execute('''SELECT Student.FIO, Kafedra.Decanat, Exzamen.Predmet, Exzamen.Ball
                   FROM Student
                   JOIN G ON G."Group" = Student."Group"  
                   JOIN Kafedra ON G.Kafedra = Kafedra.Kafedra
                   JOIN Exzamen ON Exzamen.id_St = Student.ID_St
                   WHERE Exzamen.Predmet = 'Дифференциальные уравнения' AND Exzamen.Ball = 5
                   GROUP BY 1 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('11. Напишите запрос, который покажет,  сколько экзаменов  сдавал Шутов.')
    cur.execute('''SELECT Student.FIO, COUNT(Predmet) KOLI4_EXZAMENOV_
                   FROM Exzamen
                   JOIN Student ON Student.ID_St = Exzamen.Id_St AND Student.FIO = 'Шутов Анатолий Александрович' 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('12. Выведите название кафедры студентов, не сдавших хотя бы один экзамен.')
    cur.execute('''SELECT G.Kafedra KAFEDRY_S_NESDANNYM_EXAMENOM
                   FROM G
                   JOIN Student ON Student."Group" = G."Group"
                   JOIN Exzamen ON Exzamen.id_St = Student.ID_St
                   AND Exzamen.Ball IS NULL 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('13. Подсчитать количество кафедр на каждом факультете.')
    cur.execute('''SELECT Decanat, COUNT(Kafedra)
                   FROM Kafedra
                   GROUP BY 1
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('14. Подсчитать количество пятерок на физико-математическом факультете.')
    cur.execute('''SELECT Kafedra.Decanat, COUNT(Exzamen.Ball) PYATYOROK
                   FROM Exzamen
                   JOIN Student ON Exzamen.Id_St = Student.ID_St
                   JOIN G ON Student."Group" = G."Group"
                   JOIN Kafedra ON G.Kafedra = Kafedra.Kafedra
                   WHERE Exzamen.Ball = 5 AND Kafedra.Decanat = 'Физико-математический' 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('15. Определите номера зачетных книжек группы ФТ151.')
    cur.execute('''SELECT Student."Group", Zachetki.N_Z
                   FROM Zachetki
                   JOIN Student ON Zachetki.Id_Studenta = Student.ID_St
                   AND Student."Group" = 'ФТ151'
                   GROUP BY 1 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

    print('16. Выведите перечень специальностей физико-математического факультета.')
    cur.execute('''SELECT Student.Special, Kafedra.Decanat
                   FROM Student
                   JOIN Kafedra ON Kafedra.Kafedra = G.Kafedra
                   JOIN G ON G."Group" = Student."Group" 
                   AND Kafedra.Decanat = 'Физико-математический'
                   GROUP BY 1 
                ''')
    cur_list = list(cur.fetchall())
    print(cur_list)
    print()

