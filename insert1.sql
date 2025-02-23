
insert into empleado(codigo_empleado,nombre,apellido1,apellido2,extension,email,codigo_oficina,codigo_jefe,puesto) 
values(32, 'Paco', 'Morales', 'Ruiz', '2445', 'pmorales@jardineria.es', 'MAD-ES', 7, 'Representante Ventas'); 
insert into empleado values(33, 'Raul', 'Adriano', 'Gomez', '2445', 'rgomez@jardineria.es', 'MAD-ES', 7, 'Representante Ventas');
insert into oficina values('SEV-ES', 'Sevilla', 'España', 'Andalucía', '41001', '+34 955 123456', 'Avenida de la Constitución, 23', null);
insert into empleado(nombre,apellido1,extension,email,codigo_oficina,puesto) 
values('Juan', 'Perez', '41001', 'jperez@jardineria.es', 'SEV-ES', 'Director General');
insert into empleado(nombre,apellido1,extension,email,codigo_oficina,codigo_jefe) 
values('Roberto', 'Salva', '41001', 'correo@jardineria.es', 'SEV-ES', 34);
insert into empleado(nombre,apellido1,extension,email,codigo_oficina,codigo_jefe, puesto) 
values('Jorge', 'Salvador', '41001', 'correo@jardineria.es', 'SEV-ES', 34, default);
insert into empleado(nombre,apellido1,apellido2,extension,email,codigo_oficina,codigo_jefe, puesto) 
values
('si', 'si',null, '41001', 'correo@jardineria.es', 'SEV-ES', 34, 'Subdirector Marketing'),
('si', 'si',null, '41001','correo@jardineria.es', 'SEV-ES', 34, 'Subdirector Ventas'),
('si', 'si',null, '41001','correo@jardineria.es', 'SEV-ES', 34, 'Secretaria'),
('si', 'si',null, '41001','correo@jardineria.es', 'SEV-ES', 34, 'Representante Ventas'),
('si', 'si','si', '41001','correo@jardineria.es', 'SEV-ES', 34, 'Director Oficina'),
('si', 'si',null, '41001','correo@jardineria.es', 'SEV-ES', 34, 'Becario');


select * from empleado;