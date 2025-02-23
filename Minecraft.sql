drop database if exists MINECRAFT;
create database MINECRAFT;
use MINECRAFT;

create table JUGADORES(
ID int auto_increment primary key,
USUARIO varchar(50) not null unique,
EMAIL varchar(100) not null unique,
REGISTRO timestamp default (current_timestamp),
NIVEL int check(NIVEL < 0 and NIVEL > 100),
EXPERIENCIA int default (0),
RANGO enum('BEBE', 'NOVATO', 'DAMISELA', 'BESTIA', 'MAESTRO', 'GOD') default ('BEBE')
);

create table CLAN(
NOMBRE varchar(50),
CREACION timestamp default (current_timestamp()),
FUNDADOR int,
foreign key (FUNDADOR) references JUGADORES(ID),
MIEMBRO1 int,
foreign key (MIEMBRO1) references JUGADORES(ID),
MIEMBRO2 int,
foreign key (MIEMBRO2) references JUGADORES(ID),
MIEMBRO3 int,
foreign key (MIEMBRO3) references JUGADORES(ID),
MIEMBRO4 int,
foreign key (MIEMBRO4) references JUGADORES(ID)
);

create table OBJETO(
ID int primary key,
NOMBRE varchar(50) not null unique,
RAREZA enum('COMÚN', 'RARO', 'ÉPICO', 'LÉGENDARIO'),
DESCRIPCION text
);

create table LOGRO(
ID int auto_increment primary key,
NOMBRE varchar(50),
DESCRIPCION text,
EXPERIENCIA int,
ITEM int,
foreign key (ITEM) references OBJETO(ID)
);

create table MOB(
ID int auto_increment primary key,
NOMBRE varchar(50) not null unique,
NATURALEZA enum('HOSTIL', 'PASIVO', 'NEUTRAL'),
VIDA int check (VIDA>1),
DAÑO int default (0)
);

create table ALDEANO(
ID int auto_increment primary key,
NOMBRE varchar(50),
PROFESION enum('AGRICULTOR', 'HERRERO', 'BIBLIOTECARIO', 'CLERIGO', 'PESCADOR', 'PASTOR', 'PARADO') default('PARADO'),
NIVEL_COMERCIO enum('NOVATO', 'APRENDIZ', 'OFICIAL', 'EXPERTO', 'MAESTRO') default('NOVATO'),
ESTADO enum('FELIZ', 'NORMAL', 'ENFADADO', 'ASUSTADO', 'ROMANTICO') default ('NORMAL')
);

create table COMERCIO(
ID int auto_increment primary key,
ITEM int,
foreign key (ITEM) references OBJETO(ID),
ALDEANO int,
foreign key (ALDEANO) references ALDEANO(ID),
CANTIDAD int not null,
VALOR int,
foreign key (VALOR) references OBJETO(ID),
CANTIDAD_VALOR int not null
);

-- MODIFICACIONES --
alter table ALDEANO add column MOB int;
alter table ALDEANO add foreign key (MOB) references MOB(ID);
alter table JUGADORES add column ULT_CONEXION timestamp not null;
alter table CLAN drop constraint CLAN_ibfk_1;
alter table CLAN add foreign key (FUNDADOR) references JUGADORES(ID) on delete cascade;
alter table MOB drop constraint MOB_chk_1;
alter table MOB change VIDA PUNTOS_VIDA int check (PUNTOS_VIDA>1);
alter table OBJETO add column COMERCIABLE boolean;
alter table OBJETO drop column DESCRIPCION;
alter table CLAN add primary key(NOMBRE, FUNDADOR);

-- VISTA --
create view V_JUGADORES as select USUARIO, NIVEL, RANGO from JUGADORES;
create view V_MOBS as select NOMBRE, PUNTOS_VIDA as VIDA, DAÑO from MOB;
create view V_ALDEANO as select NOMBRE, NIVEL_COMERCIO, ESTADO from ALDEANO;
create view V_CLAN as select NOMBRE, FUNDADOR from CLAN;
create view V_COMERCIO as select ITEM, CANTIDAD, VALOR, CANTIDAD_VALOR from COMERCIO;
create view V_OBJETO as select NOMBRE, RAREZA from OBJETO where (COMERCIABLE = TRUE);

-- INDICES --
create index ULT_INICIO on JUGADORES(ULT_CONEXION);
create index ALD_PROFESION on ALDEANO(PROFESION);
create index MOB_NATURALEZA on MOB(NATURALEZA);
create index OBJ_RAREZA on OBJETO(RAREZA);

-- ROLES --
drop role if exists JUGADOR_BASICO;
create role JUGADOR_BASICO;
grant select on V_ALDEANO to JUGADOR_BASICO;
grant select on V_CLAN to JUGADOR_BASICO;
grant select on V_COMERCIO to JUGADOR_BASICO;
grant select on V_JUGADORES to JUGADOR_BASICO;
grant select on V_MOBS to JUGADOR_BASICO;
grant select on V_OBJETO to JUGADOR_BASICO;

drop role if exists JUGADOR_VIP;
create role JUGADOR_VIP;
grant JUGADOR_BASICO to JUGADOR_VIP;
grant insert, delete on MINECRAFT.CLAN to JUGADOR_VIP;
grant select on MINECRAFT.LOGRO to JUGADOR_VIP;

drop role if exists ADMINISTRADOR;
create role ADMINISTRADOR;
grant all privileges on MINECRAFT.* to ADMINISTRADOR;
revoke drop, create on *.* from ADMINISTRADOR;
revoke grant option on *.* from ADMINISTRADOR;


-- USUARIOS --
drop user if exists USUARIO1, USUARIO2, USUARIO3, USUARIO4, USUARIO5, USUARIO6;
create user USUARIO1, USUARIO2, USUARIO3, USUARIO4, USUARIO5, USUARIO6 identified by '1234';
grant JUGADOR_BASICO to USUARIO1, USUARIO2;
grant JUGADOR_VIP to USUARIO3, USUARIO4;
grant ADMINISTRADOR to USUARIO5, USUARIO6;

set default role JUGADOR_BASICO to USUARIO1, USUARIO2;
set default role JUGADOR_VIP to USUARIO3, USUARIO4;
set default role ADMINISTRADOR to USUARIO5, USUARIO6;