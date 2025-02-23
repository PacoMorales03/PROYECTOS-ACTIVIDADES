drop database if exists ORIENTEERING_RESULTS;
create database ORIENTEERING_RESULTS;
use ORIENTEERING_RESULTS;

-- Creación de las tablas: --
create table CLUB(
NUMERO int primary key auto_increment,
NOMBRE varchar(50) not null,
CIUDAD varchar(50) not null
);
create table CORREDOR(
NUM_LICENCIA int primary key auto_increment,
NUM_PINZA int unique not null,
CATEGORIA varchar(20) not null,
EDAD int check(EDAD>0 and EDAD<100) not null,
GENERO enum('M','F'),
NOMBRE varchar(50) not null,
PUNTUACION int not null default(0),
NUM_CLUB int,
foreign key(NUM_CLUB) references CLUB(NUMERO) on delete set null
);

create table MARCA(
ID int primary key auto_increment,
NOMBRE varchar(50) not null,
PRESUPUESTO int not null,
MATERIAL varchar(100)
);

create table COMPETICION(
ID int primary key auto_increment,
NOMBRE varchar(100),
UBICACION varchar(50),
TIPO varchar(50),
FECHA date
);

create table CARRERA(
ID int primary key auto_increment,
TIPO varchar(50),
DISTANCIA float,
MAPA varchar(50),
ID_COMPETICION int,
foreign key(ID_COMPETICION) references COMPETICION(ID) on delete set null
);

create table BALIZA(
ID int primary key auto_increment,
NUMERO int not null, 
ORDEN varchar(100) not null, 
CATEGORIA enum('M-12','F-12','M-14','F-14', 'M-16','F-16','M-20','F-20', 'M-21','F-21','M-21B','F-21B','M-35','F-35','M-45','F-45','M-50','F-50','M-55','F-55','M-65','F-65') not null,
ID_CARRERA int,
foreign key(ID_CARRERA) references CARRERA(ID) on delete set null
);


create table CORREDOR_PARTICIPA_COMPETICION(
ID int primary key auto_increment,
NUM_LICENCIA int,
foreign key(NUM_LICENCIA) references CORREDOR(NUM_LICENCIA) on delete set null,
ID_COMPETICION int,
foreign key(ID_COMPETICION) references COMPETICION(ID) on delete set null
);

create table CORREDOR_CLASIFICA_COMPETICION(
ID int primary key auto_increment,
NUM_LICENCIA int,
foreign key(NUM_LICENCIA) references CORREDOR(NUM_LICENCIA) on delete set null,
ID_COMPETICION int,
foreign key(ID_COMPETICION) references COMPETICION(ID) on delete set null,
PUESTO int
);

create table CLUB_ORGANIZA_COMPETICION(
ID int primary key auto_increment,
NUM_CLUB int,
foreign key(NUM_CLUB) references CLUB(NUMERO) on delete set null,
ID_COMPETICION int,
foreign key(ID_COMPETICION) references COMPETICION(ID) on delete set null
);

create table CLUB_COLABORA_MARCA(
ID int primary key auto_increment,
ID_MARCA int,
foreign key(ID_MARCA) references MARCA(ID) on delete set null,
NUM_CLUB int,
foreign key(NUM_CLUB) references CLUB(NUMERO) on delete set null
);

-- Creación de indices --
create index I_CLUB on CLUB(NOMBRE,CIUDAD);
create index I_CORREDOR on CORREDOR(NUM_PINZA,CATEGORIA,NOMBRE);
create index I_MARCA on MARCA(NOMBRE,MATERIAL);
create index I_COMPETICION on COMPETICION(UBICACION, TIPO, NOMBRE);
create index I_CARRERA on CARRERA(TIPO, MAPA);
create index I_BALIZA on BALIZA(NUMERO, CATEGORIA);
create index PUESTO on CORREDOR_CLASIFICA_COMPETICION(PUESTO);
-- Del resto de tablas no creo índices ya que sólo contienen primary key y foreign key --

-- Creación de vistas --
create view V_CLUB as select NUMERO, NOMBRE, CIUDAD from CLUB;
create view V_CORREDOR as select NUM_LICENCIA as LICENCIA, NUM_PINZA as PINZA, NOMBRE, CATEGORIA, PUNTUACION as PUNTOS from CORREDOR;
create view V_MARCA as select NOMBRE, MATERIAL from MARCA;
create view V_COMPETICION as select NOMBRE, TIPO, UBICACION from COMPETICION;
create view V_CARRERA as select MAPA, TIPO, DISTANCIA from CARRERA;
create view V_BALIZA as select NUMERO, CATEGORIA, ORDEN from BALIZA;
-- El resto de tablas son relacionales --

-- Creación de los roles de usuario y asignación de sus permisos --
drop role if exists ADMINISTRACION;
create role ADMINISTRACION;
grant all privileges on ORIENTEERING_RESULTS.* to ADMINISTRACION;
drop role if exists USUARIO;
create role USUARIO;
grant select on ORIENTEERING_RESULTS.* to USUARIO;
drop role if exists TRABAJADOR;
create role TRABAJADOR;
grant create, drop, delete, insert, select on ORIENTEERING_RESULTS.* to TRABAJADOR;

-- Creación de 6 usuarios --
drop user if exists Pepe;
create user Pepe identified by '1234';
drop user if exists Juan;
create user Juan identified by '1234';
drop user if exists Natalia;
create user Natalia identified by '1234';
drop user if exists Paco;
create user Paco identified by '1234';
drop user if exists Maria;
create user Maria identified by '1234';
drop user if exists Marta;
create user Marta identified by '1234';

-- Asignación de los roles creados --
grant ADMINISTRACION to Natalia, Paco;
set default role ADMINISTRACION to Natalia, Paco;
grant TRABAJADOR to Pepe, Maria;
set default role TRABAJADOR to Pepe, Maria;
grant USUARIO to Juan, Marta;
set default role USUARIO to Juan, Marta;

-- MODIFICACIONES --
alter table CORREDOR modify GENERO boolean;
alter table CLUB add column FUNDACION date;
alter table CARRERA change ID_COMPETICION COMPETICION int;