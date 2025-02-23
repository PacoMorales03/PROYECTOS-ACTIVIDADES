drop database if exists TFT;
create database TFT;
use TFT;

create table JUGADOR(
NICK varchar(50) primary key,
CORREO varchar(100) unique not null,
FECHA_REGISTRO date default (current_date),
NACIMIENTO year,
EDAD int check (EDAD > 16)
);

create table PARTIDA(
NOMBRE varchar(50),
TIPO enum ('Clasificatoria', 'Simple', 'VSbot', 'Especial'),
primary key (NOMBRE, TIPO),
CANTIDAD int check (CANTIDAD > 0 and CANTIDAD <= 8)
);

create table OBJETO(
NOMBRE varchar(50) primary key,
DESCRIPCION text,
AD int check (AD >= 0 and AD <= 150),
AP int check (AP >= 0 and AP <= 150),
SPEED int check (SPEED >= 0 and SPEED <= 150),
HP int check (HP >= 0 and HP <= 150),
TD int check (TD >= 0 and TD <= 150)
);

create table CAMPEONES(
NOMBRE varchar(50) primary key,
TIPO1 enum ('SOBRENATURAL', 'MAGO', 'HECHICERO', 'PIRO', 'LUCHADOR', 'CABALLERO', 'VANGUARDIA', 'DRUIDA') not null,
TIPO2 enum ('SOBRENATURAL', 'MAGO', 'HECHICERO', 'PIRO', 'LUCHADOR', 'CABALLERO', 'VANGUARDIA', 'DRUIDA'),
TIPO3 enum ('SOBRENATURAL', 'MAGO', 'HECHICERO', 'PIRO', 'LUCHADOR', 'CABALLERO', 'VANGUARDIA', 'DRUIDA'),
OBJETO1 varchar(50),
foreign key (OBJETO1) references OBJETO(NOMBRE),
OBJETO2 varchar(50),
foreign key (OBJETO2) references OBJETO(NOMBRE),
OBJETO3 varchar(50),
foreign key (OBJETO3) references OBJETO(NOMBRE),
OBJETO4 varchar(50),
foreign key (OBJETO4) references OBJETO(NOMBRE)
);

create table HISTORIAL(
ID int primary key auto_increment,
JUGADOR varchar(50),
foreign key (JUGADOR) references JUGADOR(NICK),
PARTIDA_NOMBRE varchar(50),
PARTIDA_TIPO enum ('Clasificatoria', 'Simple', 'VSbot', 'Especial'),
foreign key (PARTIDA_NOMBRE, PARTIDA_TIPO) references PARTIDA(NOMBRE, TIPO),
RESULTADO int check (RESULTADO >= 1 and RESULTADO <= 8),
FECHA timestamp default current_timestamp not null,
CAMPEON1 varchar(50),
foreign key (CAMPEON1) references CAMPEONES(NOMBRE),
CAMPEON2 varchar(50),
foreign key (CAMPEON2) references CAMPEONES(NOMBRE),
CAMPEON3 varchar(50),
foreign key (CAMPEON3) references CAMPEONES(NOMBRE),
CAMPEON4 varchar(50),
foreign key (CAMPEON4) references CAMPEONES(NOMBRE),
CAMPEON5 varchar(50),
foreign key (CAMPEON5) references CAMPEONES(NOMBRE)
);

alter table CAMPEONES add unique(NOMBRE, TIPO1, TIPO2, TIPO3);
alter table HISTORIAL add column PUNTOS int;
alter table CAMPEONES add constraint REST_CAMPEONES check (TIPO1 != TIPO2 and TIPO1 != TIPO3 and TIPO2 != TIPO3);
alter table JUGADOR drop column EDAD;
