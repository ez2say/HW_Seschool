USE seschool_06;

CREATE TABLE students_table (
    `№` INT AUTO_INCREMENT PRIMARY KEY,
    Фамилия_пол VARCHAR(255) NOT NULL,
    Дата_рождения DATE NOT NULL,
    СНИЛС VARCHAR(11) UNIQUE NOT NULL,
    Курс INT DEFAULT 1 NOT NULL,
    Группа VARCHAR(255) NOT NULL,
    Средний_балл DECIMAL(5, 2) NOT NULL,
    Хобби VARCHAR(255)
);


INSERT INTO students_table (Фамилия_пол, Дата_рождения, СНИЛС, Курс, Группа, Средний_балл, Хобби) 
VALUES
	('Горбунова Е.А.', '1993-07-21', '128-389-457', 3, 'АУС-36', 86.3, 'Плавание'),
	('Ильин Л.И.', '1993-12-25', '279-237-417', 3, 'АУС-35', 98.1, 'Чтение'),
	('Борисенко С.Д.', '1994-11-01', '872-954-736', 2, 'АВМ-41', 92.4, 'Шахматы'),
	('Макаров С.С.', '1995-05-23', '864-278-354', 1, 'ЭОП-118', 82.0, 'Альпинизм'),
	('Курилин Д.В.', '1992-04-16', '711-257-696', 3, 'АУС-36', 63.7, 'Плавание'),
	('Иноземцева Д.Д.', '1993-08-12', '112-598-478', 3, 'АУС-36', 91.8, 'Дайвинг'),
	('Шипунов Р.Е.', '1995-03-04', '996-478-258', 1, 'ЭОП-238', 75.4, NULL),
	('Скородумов Д.Б.', '1994-01-14', '359-489-269', 1, 'ЭОП-118', 72.6, 'Бильярд'),
	('Пикулина С.А.', '1995-03-02', '234-217-598', 1, 'ЭОП-238', 86.4, 'Шахматы'),
	('Сафронова М.Д.', '1993-08-19', '887-555-124', 3, 'АУС-36', 90.1, 'Плавание'),
	('Ковшова Э.А.', '1995-09-26', '469-489-557', 1, 'ЭОП-238', 65.8, 'Бильярд'),
	('Зайцев К.С.', '1993-12-15', '689-565-487', 3, 'АУС-35', 72.6, 'Чтение'),
	('Антонова С.Д.', '1992-12-19', '773-557-986', 3, 'АУС-35', 99.6, NULL),
	('Кондрашова Е.В.', '1993-02-08', '669-476-123', 3, 'АУС-35', 97.7, 'Чтение'),
	('Кукушкина Е.В.', '1995-10-14', '369-568-559', 2, 'АВМ-41', 90.2, 'Шахматы');


DESCRIBE students_table;


SELECT * FROM students_table;


SELECT * FROM students_table WHERE Фамилия_пол LIKE '% ж';

SELECT * FROM students_table WHERE Курс = 3;

SELECT * FROM students_table WHERE Дата_рождения > '1994-02-03';

SELECT * FROM students_table WHERE Средний_балл >= 70 AND Средний_балл <= 85;

SELECT * FROM students_table WHERE Средний_балл BETWEEN 70 AND 85;

SELECT * FROM students_table WHERE Курс = 2 OR Курс = 3;

SELECT * FROM students_table WHERE Курс IN (2, 3);

SELECT * FROM students_table WHERE Фамилия_пол LIKE 'С%' OR Фамилия_пол LIKE 'К%';

SELECT * FROM students_table WHERE Фамилия_пол LIKE '% ж' AND Группа LIKE 'АУС%';

SELECT * FROM students_table WHERE Хобби IS NULL;

SELECT DISTINCT Курс FROM students_table;

SELECT * FROM students_table ORDER BY Средний_балл DESC LIMIT 5;

SELECT * FROM students_table ORDER BY Средний_балл ASC, Фамилия_пол ASC LIMIT 10;

SELECT
   COUNT(*) AS Число_всех_студентов,
   COUNT(CASE WHEN Хобби IS NULL THEN 1 END) AS Число_студентов_без_хобби,
   MAX(Средний_балл) AS Максимальный_балл,
   MIN(Средний_балл) AS Минимальный_балл,
   AVG(Средний_балл) AS Средний_балл_по_всем_студентам
	FROM students_table;

SELECT Курс, COUNT(*) AS Число_студентов
FROM students_table
GROUP BY Курс;

SELECT CASE WHEN Фамилия_пол LIKE '% ж' THEN 'Студентки' ELSE 'Студенты'
END AS Пол, AVG(Средний_балл) AS Средний_балл FROM students_table
	GROUP BY Пол;

SELECT MAX(Средний_балл) AS Максимальный_балл FROM students_table
	WHERE Курс = 3 AND Дата_рождения >= '1993-01-01';

SELECT Фамилия_пол, Средний_балл,
   CASE
        WHEN Средний_балл >= 90 THEN 'Отлично'
        WHEN Средний_балл >= 75 THEN 'Хорошо'
        WHEN Средний_балл >= 60 THEN 'Удовлетворительно'
        ELSE 'Неудовлетворительно'
   END AS Оценка
	FROM students_table;