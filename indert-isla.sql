use islamagica;
insert into ATRACCIONES values(null, "Rápidos del Amazonas","Acuática", 20,"Operativa","00:15:00", 250.50);
insert into ATRACCIONES values(null, "Montaña del Dragón","Montaña Rusa", 30,"Operativa","00:05:00", 500.00);
insert into ATRACCIONES values(null, "Cueva Encantada","Infantil", 15,"Mantenimiento","00:10:00", 300.00);
insert into ATRACCIONES values(null, "Viaje Espacial","Simulador", 25,"Operativa","00:20:00", 300.00);

insert into EMPLEADOS (Nombre,apellido,puesto,salario,id_atraccion) values 
("Ana","López","Operador",1800,1),
("Luis","Martínez","Supervisor",2500,2),
("María","García","Administrador",3200,null);

describe CLIENTES;
