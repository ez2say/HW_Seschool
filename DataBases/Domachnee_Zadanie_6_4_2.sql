USE `seschool_06`;

/*1. Найти всех игроков, у которых больше опыта, чем у игрока с именем "Марк".*/

SELECT `player_name` FROM `Игроки`
	WHERE `experience_points` > 
	(SELECT `experience_points` FROM `Игроки` 
		WHERE `player_name` = 'Марк');

/*2. Выбрать всех игроков, у которых есть хотя бы один предмет типа "броня".*/

SELECT `player_name` FROM `Игроки`
	WHERE `player_id` IN 
	(SELECT `player_id` FROM `предметы` 
		WHERE `item_type` = 'броня');

/*3. Найти названия всех предметов, принадлежащих игрокам из гильдии с наибольшим уровнем.*/

SELECT `item_name` FROM `предметы`
	WHERE `player_id` IN 
	(SELECT `player_id` FROM `Игроки`
   	WHERE `guild_id` = 
		(SELECT `guild_id` FROM `гильдии`
      	ORDER BY `guild_level` DESC
      	LIMIT 1));

/*4. Выбрать всех игроков, у которых хотя бы один предмет редкий (rarity = 'редкий').*/

SELECT `player_name` FROM `Игроки`
	WHERE `player_id` IN 
	(SELECT `player_id` FROM `предметы` 
		WHERE `rarity` = 'редкий');

/*5. Найти всех игроков, у которых больше предметов, чем у игрока с именем "Екатерина".*/

SELECT `player_name` FROM `Игроки`
	WHERE 
	(SELECT COUNT(*) FROM `предметы` 
		WHERE `предметы`.`player_id` = `Игроки`.`player_id`) 
		> 
	(SELECT COUNT(*) FROM `предметы`
   	WHERE `предметы`.`player_id` = 
		(SELECT `player_id` FROM `Игроки` 
			WHERE `player_name` = 'Екатерина'));

/*6. Выбрать названия всех гильдий, в которых состоит хотя бы один игрок с уровнем выше 20.*/

SELECT `guild_name` FROM `гильдии`
	WHERE `guild_id` IN 
	(SELECT `guild_id` FROM `Игроки`
   	WHERE `level` > 20);

/*7. Найти всех игроков, у которых есть предметы типа "оружие", но нет предметов типа "зелье".*/

SELECT `player_name` FROM `Игроки`
	WHERE `player_id` IN 
	(SELECT `player_id` FROM `предметы` 
		WHERE `item_type` = 'оружие')
	AND `player_id` NOT IN 
	(SELECT `player_id` FROM `предметы` 
		WHERE `item_type` = 'зелье');

/*8. Выбрать названия предметов, которые принадлежат игрокам, состоящим в гильдии с названием "Стражи Севера".*/

SELECT `item_name` FROM `предметы`
	WHERE `player_id` IN 
	(SELECT `player_id` FROM `Игроки`
   	WHERE `guild_id` = 
		(SELECT `guild_id` FROM `гильдии` 
			WHERE `guild_name` = 'Стражи Севера'));

/*9. Найти всех игроков, у которых есть более одного предмета, и при этом хотя бы один из этих предметов — эпический.*/

SELECT `player_name` FROM `Игроки`
	WHERE 
	(SELECT COUNT(*) FROM `предметы`
		WHERE `предметы`.`player_id` = `Игроки`.`player_id`) > 1
	AND `player_id` IN 
	(SELECT `player_id` FROM `предметы` 
		WHERE `rarity` = 'эпический');

/*10. Выбрать всех игроков, у которых больше опыта, чем у среднего значения опыта всех игроков.*/

SELECT `player_name` FROM `Игроки`
	WHERE `experience_points` > 
	(SELECT AVG(`experience_points`) FROM `Игроки`);

/*11. Найти названия всех предметов, которые принадлежат игрокам из гильдий с уровнем выше среднего уровня всех гильдий.*/

SELECT `item_name` FROM `предметы`
	WHERE `player_id` IN 
	(SELECT `player_id` FROM `Игроки`
   	WHERE `guild_id` IN 
		(SELECT `guild_id` FROM `гильдии`
        WHERE `guild_level` > (SELECT AVG(`guild_level`) FROM `гильдии`)));

/*12. Найти всех игроков, у которых хотя бы один предмет редкий, и больше опыта, чем у игрока с именем "Дмитрий".*/

SELECT `player_name` FROM `Игроки`
	WHERE `player_id` IN 
	(SELECT `player_id` FROM `предметы` 
		WHERE `rarity` = 'редкий')
	AND `experience_points` > 
	(SELECT `experience_points` FROM `Игроки` 
		WHERE `player_name` = 'Дмитрий');

/*13. Выбрать названия всех гильдий, в которых нет игроков, у которых есть хотя бы один предмет типа "броня".*/

SELECT `guild_name` FROM `гильдии`
	WHERE `guild_id` NOT IN 
	(SELECT `guild_id` FROM `Игроки`
   	WHERE `player_id` IN 
		(SELECT `player_id` FROM `предметы`
			WHERE `item_type` = 'броня'));

/*14. Найти игроков, которые состоят в гильдиях, имеющих больше опыта, чем гильдия с названием "Легион".*/

SELECT `player_name`	FROM `Игроки`
	WHERE `guild_id` IN 
	(SELECT `guild_id` FROM `гильдии`
   	WHERE 
		(SELECT SUM(`experience_points`) FROM `Игроки`
			WHERE `guild_id` = `гильдии`.`guild_id`) 
			> 
		(SELECT SUM(`experience_points`) FROM `Игроки`
      	WHERE `guild_id` = 
			(SELECT `guild_id` FROM `гильдии` 
				WHERE `guild_name` = 'Легион')));

/*15. Выбрать всех игроков, у которых количество предметов больше, чем у среднего игрока.*/

SELECT `player_name` FROM `Игроки`
	WHERE 
	(SELECT COUNT(*) FROM `предметы` 
		WHERE `предметы`.`player_id` = `Игроки`.`player_id`) 
		> 
	(SELECT AVG(item_count) FROM (SELECT COUNT(*) AS item_count FROM `предметы` GROUP BY `player_id`) AS item_counts);

/*16. Найти всех игроков, у которых больше опыта, чем у всех игроков в гильдии с названием "Темный Братство".*/

SELECT `player_name` FROM `Игроки`
	WHERE `experience_points` > ALL
	(SELECT `experience_points`FROM `Игроки`
   	WHERE `guild_id` = 
		(SELECT `guild_id` FROM `гильдии` 
			WHERE `guild_name` = 'Темный Братство'));

/*17. Выбрать названия всех предметов, которые принадлежат игрокам, у которых опыт выше, чем у всех игроков в гильдии с названием "Львы".*/

SELECT `item_name` FROM `предметы`
	WHERE `player_id` IN 
	(SELECT `player_id` FROM `Игроки`
   	WHERE `experience_points` > ALL
		(SELECT `experience_points` FROM `Игроки`
      	WHERE `guild_id` = 
			(SELECT `guild_id` FROM `гильдии` 
				WHERE `guild_name` = 'Львы')));

/*18. Найти всех игроков, у которых больше опыта, чем у среднего игрока из их гильдии.*/

SELECT `player_name` FROM `Игроки` AS p1
	WHERE `experience_points` > 
	(SELECT AVG(`experience_points`) FROM `Игроки` AS p2
   	WHERE p1.`guild_id` = p2.`guild_id`);

/*19. Найти игроков, у которых больше 1000 опыта и хотя бы один редкий предмет, но при этом они не состоят в гильдии.*/

SELECT `player_name` FROM `Игроки`
	WHERE `experience_points` > 1000
	AND `player_id` IN 
	(SELECT `player_id` FROM `предметы` 
		WHERE `rarity` = 'редкий') 
	AND `guild_id` IS NULL;

/*20. Найти игроков, у которых опыт больше, чем у игроков, у которых есть хотя бы один эпический предмет.*/

SELECT `player_name` FROM `Игроки`
	WHERE `experience_points` > 
	(SELECT MAX(`experience_points`) FROM `Игроки`
   	WHERE `player_id` IN 
		(SELECT `player_id` FROM `предметы` 
			WHERE `rarity` = 'эпический'));