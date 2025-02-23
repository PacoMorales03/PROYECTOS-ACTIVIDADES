insert into CLUB(NUMERO,NOMBRE,CIUDAD,FUNDACION) values(1,"POSEIDON","UTRERA","2000-12-23");
insert into CLUB values
(null,"ADOL","SEVILLA","1995-10-15"),
(null,"MONTELLANO", "MONTELLANO","1999-07-20"),
(null,"COMA","MALAGA","1957-11-23"),
(null,"COHU","HUELVA","1959-12-15"),
(null,"FUNDIO","CÁDIZ","1995-10-15"),
(null,"GALILEO", "DOS HERMANAS","1999-07-20"),
(null,"VELETA","GRANADA","1957-11-23"),
(null,"ORCA","PALENCIA","1959-12-15"),
(null,"SURCO","ALMERIA","1995-10-15");

insert into CORREDOR (NUM_LICENCIA,NUM_PINZA,CATEGORIA,EDAD,GENERO,NOMBRE,PUNTUACION,NUM_CLUB) values(1,123456,"M-16",15, null, "Juan Fernandez", 15, 1);
insert into CORREDOR (NUM_LICENCIA,NUM_PINZA,CATEGORIA,EDAD,NOMBRE,PUNTUACION,NUM_CLUB) values(null,123457,"F-16",15, "Maria Fernandez", 15, 1);
insert into CORREDOR values
(null,123451,"F-21", 21, 1, "Natalia Giraldez", 400, 2),
(null,123452,"M-21", 22, 1, "Paco Morales", 350, 1),
(null,123453,"F-50", 55, 1, "Chelo Ruiz", 40, 1),
(null,123454,"M-50", 55, 1, "Pedro Morales", 50, 1),
(null,123455,"F-21", 21, 1, "Juana de Arcos", 0, 6),
(null,123458,"M-21", 22, 1, "Pepe Botella", 15, 10),
(null,123459,"M-45", 45, 1, "Jack Sparrow", 400, 9),
(null,123450,"F-45", 47 , 1, "Michele Obama", 350, 7);


insert into MARCA values
(1,"Nike",1000, "Zapatos y ropa"),
(null,"Adidas", 1000, "Zapatos y ropa"),
(null,"Kellops",2000, null),
(null,"Tenth", 1000, "Zapatos y ropa"),
(null,"Abibas",10000, "Zapatos y ropa"),
(null,"Adidas", 1000, "Zapatos y ropa"),
(null,"Facebook",2000, null),
(null,"Kalenji", 1000, "Zapatos, ropa y relojes"),
(null,"Agerul",2000, null),
(null,"Gussi", 10000, "Zapatos y ropa");

insert into COMPETICION values
(1, 'Campeonato Provincial de Primavera', 'Madrid', 'Provincial', '2025-03-15'),
(null, 'Torneo Regional del Norte', 'Santander', 'Regional', '2025-04-10'),
(null, 'Copa Nacional de Verano', 'Barcelona', 'Nacional', '2025-06-20'),
(null, 'Campeonato Internacional de Montaña', 'Andorra', 'Internacional', '2025-07-05'),
(null, 'Campeonato Provincial de Otoño', 'Sevilla', 'Provincial', '2025-09-12'),
(null, 'Torneo Regional del Sur', 'Granada', 'Regional', '2025-10-08'),
(null, 'Copa Nacional de Invierno', 'Bilbao', 'Nacional', '2025-12-01'),
(null, 'Campeonato Internacional de Velocidad', 'Lisboa', 'Internacional', '2026-01-15'),
(null, 'Campeonato Provincial de Invierno', 'Valencia', 'Provincial', '2026-02-10'),
(null, 'Torneo Regional del Este', 'Zaragoza', 'Regional', '2026-03-25');

insert into CARRERA VALUES
(1,'Media', 7.5, 'mapa_media1.jpg', 1),
(null,'Sprint', 3.5, 'mapa_sprint1.jpg', 2),
(null,'Larga', 15.1, 'mapa_larga1.jpg', 3),
(null,'Trail-O', 12.2, 'mapa_trailo1.jpg', 4),
(null,'Rogaine', 7.8, 'mapa_rogaine1.jpg', 5),
(null,'Sprint', 3.0, 'mapa_sprint2.jpg', 2),
(null,'Larga', 17.8, 'mapa_larga2.jpg', 6),
(null,'Media', 8.2, 'mapa_media2.jpg', 7),
(null,'Trail-O', 11.2, 'mapa_trailo2.jpg', 5),
(null,'Rogaine', 9.7, 'mapa_rogaine2.jpg', 8);

insert into BALIZA values
(1, 90,'Inicio - Punto 1', 'M-12', 1),
(null, 91,'Punto 1 - Punto 2', 'F-12', 1),
(null, 92,'Punto 2 - Punto 3', 'M-14', 2),
(null, 93,'Punto 3 - Punto 4', 'F-14', 2),
(null, 94,'Punto 4 - Meta', 'M-16', 3),
(null, 95,'Inicio - Punto 1', 'F-16', 3),
(null, 96,'Punto 1 - Punto 2', 'M-20', 4),
(null, 97,'Punto 2 - Meta', 'F-20', 4),
(null, 98,'Inicio - Meta', 'M-21', 5),
(null, 99,'Inicio - Punto 1', 'F-21', 5);

insert into CORREDOR_PARTICIPA_COMPETICION values
(1, 1, 1),
(null, 2, 1),
(null, 3, 2),
(null, 4, 2),
(null, 5, 3),
(null, 6, 3),
(null, 7, 4),
(null, 8, 4),
(null, 9, 5),
(null, 10, 5);

insert into CORREDOR_CLASIFICA_COMPETICION values
(1, 1, 1, 1),
(null, 1, 2, 2),
(null, 2, 1, 3),
(null, 2, 3, 4),
(null, 3, 2, 1),
(null, 3, 4, 2),
(null, 4, 1, 3),
(null, 4, 5, 4),
(null, 5, 3, 1),
(null, 5, 2, 2);

insert into CLUB_ORGANIZA_COMPETICION values
(1, 1, 1),
(null, 2, 2),
(null, 3, 3),
(null, 4, 4),
(null, 5, 5),
(null, 6, 6),
(null, 7, 7),
(null, 8, 8),
(null, 9, 9),
(null, 10, 10);

insert into CLUB_COLABORA_MARCA (ID, ID_MARCA, NUM_CLUB) values
(1, 1, 1),
(null, 2, 2),
(null, 3, 3),
(null, 4, 4),
(null, 5, 5),
(null, 6, 6),
(null, 7, 7),
(null, 8, 8),
(null, 9, 9),
(null, 10, 10);

delete from CARRERA where ID = 1;
delete from BALIZA where NUMERO = 92;
delete from MARCA where NOMBRE = "Abibas";
delete from CLUB where NOMBRE = "POSEIDON";
delete from CORREDOR_CLASIFICA_COMPETICION where ID_COMPETICION = 1;

update CORREDOR set NUM_CLUB = 2 where NUM_CLUB is null;
update CLUB set CIUDAD = "MADRID" where NUMERO = 3;
update COMPETICION set UBICACION = "Sevilla", TIPO = "SPRINT" where ID = 7;
set sql_safe_updates = 0;
update CORREDOR set CATEGORIA = "ELITE" where PUNTUACION >300;
set sql_safe_updates = 1;
set sql_safe_updates = 0;
update MARCA set MATERIAL = null where PRESUPUESTO < 2000;
set sql_safe_updates = 1;


start transaction;
insert into CLUB values(0,"NO-TIENE","NO-APLICA",null);
update CORREDOR set NUM_CLUB = 0 where NUM_CLUB is null;
delete from MARCA where NOMBRE = "Nike";
rollback;

start transaction;
insert into CLUB values(0,"NO-TIENE","NO-APLICA",null);
update CORREDOR set NUM_CLUB = 0 where NUM_CLUB is null;
delete from MARCA where NOMBRE = "Nike";
commit;