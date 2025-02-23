DROP DATABASE IF EXISTS islamagica;
CREATE DATABASE islamagica;
use islamagica;

CREATE TABLE ATRACCIONES(
ID INT auto_increment primary KEY,
NOMBRE VARCHAR(50),
TIPO ENUM ('Montaña Rusa', 'Acuática', 'Infantil', 'Simulador') NOT NULL,
CAPACIDAD INT NOT NULL CONSTRAINT capacidad_minima check(capacidad >0),
estado enum('Operativa', 'Mantenimiento', 'Cerrada') default('Operativa'),
duracion_promedio time not null,
coste_mantenimiento decimal(10,2) not null constraint coste_mantenimiento_check check(coste_mantenimiento>0));

CREATE TABLE EMPLEADOS (
ID int primary key auto_increment,
Nombre varchar(50) not null,
apellido varchar(50) not null,
puesto enum('Operador', 'Supervisor', 'Administrador') not null,
fecha_contratacion  timestamp default current_timestamp(),
salario decimal (8, 2) constraint jefe_explotador check(salario>0),
id_atraccion int,
constraint fk_atraccion_empleados foreign key (id_atraccion) references ATRACCIONES(ID));

CREATE TABLE CLIENTES (
ID int auto_increment primary key,
nombre varchar(50) not null,
DNI varchar(9) NOT NULL unique,
EMAIL varchar(100),
FECHA_N DATE NOT NULL,
FECHA_REGISTRO  DATE default(current_date()),
VIP boolean default(FALSE)
);

CREATE TABLE TIENDA (
ID INT auto_increment primary KEY,
NOMBRE VARCHAR(50) NOT NULL,
TIPO ENUM ('Comida', 'Souvenirs', 'Ropa' , 'Accesorios') NOT NULL,
UBICACION VARCHAR(100) NOT NULL,
ingresos_anuales decimal(10, 2) not null constraint sueldito_anual check(ingresos_anuales>0),
numero_empleados int default 1
);

CREATE TABLE TRANSACCIONES(
ID INT primary KEY auto_increment,
ID_CLIENTE INT,
ID_TIENDA INT,
FECHA timestamp NOT NULL default(current_timestamp()),
TOTAL DECIMAL(8,2) NOT NULL constraint TRANSACCION_NEGATIVA check (TOTAL>0),
metodo_pago ENUM ('Efectivo', 'Tarjeta' , 'Online') NOT NULL,
foreign key (ID_CLIENTE) references CLIENTES(ID),
foreign key (ID_TIENDA) references TIENDA(ID)
);

CREATE INDEX INDEX_ATRACCIONES ON ATRACCIONES(estado);
CREATE INDEX EMPLEADO_PUESTO ON EMPLEADOS (PUESTO);
CREATE INDEX CLIENTE_VIP ON CLIENTES (VIP);
CREATE VIEW SUPERVISOR_ATRACCIONES AS 
SELECT NOMBRE, estado, coste_mantenimiento FROM ATRACCIONES WHERE ESTADO != 'Operativa';
create view administrador_view as select Nombre, apellido,puesto,id_atraccion from EMPLEADOS
where puesto != 'Administrador';
create view privacidad_clientes as select nombre,EMAIL,VIP from CLIENTES;
create view tienda_suvenir as 
select NOMBRE,UBICACION,ingresos_anuales from TIENDA where tipo = 'Souvenirs';

ALTER TABLE EMPLEADOS ADD COLUMN TURNO ENUM('Mañana', 'Tarde' , 'Noche') default('Mañana');
ALTER TABLE CLIENTES ADD COLUMN TELEFONO INT;
ALTER TABLE CLIENTES DROP column DNI;
ALTER TABLE ATRACCIONES ADD constraint CAPACIDAD_NUEVA CHECK (CAPACIDAD>10);
ALTER TABLE ATRACCIONES DROP constraint coste_mantenimiento_check;
ALTER TABLE ATRACCIONES CHANGE coste_mantenimiento coste_operativo decimal(10,2) not null constraint coste_operativo_check check(coste_operativo>0);
ALTER TABLE TIENDA modify ingresos_anuales INT not null;