USE `seschool_06`;

/* 1. Выбрать всех игроков и их уровень.*/

SELECT `player_name`, `level` FROM `Игроки`;

/* 2. Выбрать всех игроков, которые состоят в гильдии с ID = 3. */

SELECT `player_name` FROM `Игроки`
	WHERE `guild_id` = 3;

/* 3. Вывести имена и уровень игроков, которые достигли уровня 10 и выше.*/

SELECT `player_name`, `level` FROM `Игроки`
	WHERE `level` >= 10;

/* 4. Выбрать названия всех предметов, принадлежащих игроку с именем "Алекс". */

SELECT `item_name` FROM `предметы`
	JOIN `Игроки` ON `предметы`.`player_id` = `Игроки`.`player_id`
	WHERE `Игроки`.`player_name` = 'Алекс';

/* 5. Выбрать все редкие предметы (rarity = 'редкий').*/

SELECT `item_name` FROM `предметы`
	WHERE `rarity` = 'редкий';

/* 6. Найти все предметы типа "оружие" и вывести их названия.*/

SELECT `item_name` FROM `предметы`
	WHERE `item_type` = 'оружие';

/* 7. Вывести названия всех гильдий и количество игроков в каждой гильдии.*/

SELECT `гильдии`.`guild_name`, COUNT(`Игроки`.`player_id`) AS `количество_игроков` FROM `гильдии`
	LEFT JOIN `Игроки` ON `гильдии`.`guild_id` = `Игроки`.`guild_id`
	GROUP BY `гильдии`.`guild_id`;

/* 8. Найти имена всех игроков, у которых есть предмет типа "броня".*/

SELECT `Игроки`.`player_name` FROM `Игроки`
	JOIN `предметы` ON `Игроки`.`player_id` = `предметы`.`player_id`
	WHERE `предметы`.`item_type` = 'броня';

/* 9. Выбрать игроков, у которых уровень больше 5 и которые принадлежат к гильдии с уровнем 2 и выше.*/

SELECT `Игроки`.`player_name` FROM `Игроки`
	JOIN `гильдии` ON `Игроки`.`guild_id` = `гильдии`.`guild_id`
	WHERE `Игроки`.`level` > 5 AND `гильдии`.`guild_level` >= 2;

/* 10. Найти всех игроков, у которых есть эпические предметы (rarity = 'эпический').*/

SELECT DISTINCT `Игроки`.`player_name` FROM `Игроки`
	JOIN `предметы` ON `Игроки`.`player_id` = `предметы`.`player_id`
	WHERE `предметы`.`rarity` = 'эпический';

/* 11. Вывести названия всех предметов, принадлежащих игрокам с уровнем выше 15.*/

SELECT `предметы`.`item_name` FROM `предметы`
	JOIN `Игроки` ON `предметы`.`player_id` = `Игроки`.`player_id`
	WHERE `Игроки`.`level` > 15;

/* 12. Найти все предметы, которые принадлежат игрокам из гильдии с названием "Клан Дракона".*/

SELECT `предметы`.`item_name` FROM `предметы`
	JOIN `Игроки` ON `предметы`.`player_id` = `Игроки`.`player_id`
	JOIN `гильдии` ON `Игроки`.`guild_id` = `гильдии`.`guild_id`
	WHERE `гильдии`.`guild_name` = 'Клан Дракона';

/* 13. Выбрать игроков, у которых нет предметов.*/

SELECT `Игроки`.`player_name` FROM `Игроки`
	LEFT JOIN `предметы` ON `Игроки`.`player_id` = `предметы`.`player_id`
	WHERE `предметы`.`item_id` IS NULL;

/* 14. Найти всех игроков, у которых есть предметы типа "зелье" и уровень выше 8.*/

SELECT DISTINCT `Игроки`.`player_name` FROM `Игроки`
	JOIN `предметы` ON `Игроки`.`player_id` = `предметы`.`player_id`
	WHERE `предметы`.`item_type` = 'зелье' AND `Игроки`.`level` > 8;

/* 15. Вывести названия всех предметов, которые принадлежат игрокам из гильдии с уровнем больше 3.*/

SELECT `предметы`.`item_name` FROM `предметы`
	JOIN `Игроки` ON `предметы`.`player_id` = `Игроки`.`player_id`
	JOIN `гильдии` ON `Игроки`.`guild_id` = `гильдии`.`guild_id`
	WHERE `гильдии`.`guild_level` > 3;

/* 16. Найти игроков, у которых больше 500 опыта и которые имеют хотя бы один предмет типа "оружие".*/

SELECT DISTINCT `Игроки`.`player_name` FROM `Игроки`
	JOIN `предметы` ON `Игроки`.`player_id` = `предметы`.`player_id`
	WHERE `Игроки`.`experience_points` > 500 AND `предметы`.`item_type` = 'оружие';

/* 17. Вывести названия всех гильдий, в которых нет игроков.*/

SELECT `гильдии`.`guild_name` FROM `гильдии`
	LEFT JOIN `Игроки` ON `гильдии`.`guild_id` = `Игроки`.`guild_id`
	WHERE `Игроки`.`player_id` IS NULL;

/* 18. Найти игроков, у которых есть редкие предметы, и вывести их имена и названия этих предметов.*/

SELECT `Игроки`.`player_name`, `предметы`.`item_name` FROM `Игроки`
	JOIN `предметы` ON `Игроки`.`player_id` = `предметы`.`player_id`
	WHERE `предметы`.`rarity` = 'редкий';

/* 19. Вывести игроков, у которых нет предметов типа "зелье".*/

SELECT `Игроки`.`player_name` FROM `Игроки`
	LEFT JOIN `предметы` ON `Игроки`.`player_id` = `предметы`.`player_id` AND `предметы`.`item_type` = 'зелье'
	WHERE `предметы`.`item_id` IS NULL;

/* 20. Найти всех игроков, которые находятся на уровне 20 и имеют хотя бы один эпический предмет.*/

SELECT DISTINCT `Игроки`.`player_name` FROM `Игроки`
	JOIN `предметы` ON `Игроки`.`player_id` = `предметы`.`player_id`
	WHERE `Игроки`.`level` = 20 AND `предметы`.`rarity` = 'эпический';