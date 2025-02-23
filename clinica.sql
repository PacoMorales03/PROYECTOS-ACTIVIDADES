DROP DATABASE IF EXISTS clinica;
CREATE DATABASE IF NOT EXISTS clinica;
USE clinica;

CREATE TABLE pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    genero ENUM('M', 'F', 'Otro') NOT NULL,
    telefono VARCHAR(15),
    direccion TEXT,
    correo VARCHAR(100) UNIQUE
);

CREATE TABLE especialidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE doctores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    correo VARCHAR(100) UNIQUE,
    especialidad_id INT,
    FOREIGN KEY (especialidad_id) REFERENCES especialidades(id)
);


CREATE TABLE medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    Precio DECIMAL NOT NULL DEFAULT(12.5),
    descripcion TEXT
);

CREATE TABLE consultas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    doctor_id INT NOT NULL,
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    diagnostico TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

CREATE TABLE recetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    consulta_id INT NOT NULL,
    fecha_emision DATE NOT NULL DEFAULT (CURRENT_DATE),
    indicaciones TEXT,
    FOREIGN KEY (consulta_id) REFERENCES consultas(id)
);

CREATE TABLE detalle_receta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    receta_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    dosis VARCHAR(255) NOT NULL,
    FOREIGN KEY (receta_id) REFERENCES recetas(id),
    FOREIGN KEY (medicamento_id) REFERENCES medicamentos(id)
);



INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, genero, telefono, direccion, correo) VALUES 
('Juan', 'Pérez', '1985-06-15', 'M', '5551234567', 'Calle 1, Barcelona', 'juan.perez@gmail.com'),
('María', 'López', '1990-03-22', 'F', '5552345678', 'Calle 2, Sevilla', 'maria.lopez@gmail.com'),
('Carlos', 'Gómez', '1978-09-10', 'M', NULL, 'Calle 3, Madrid ', 'carlos.gomez@example.com'),
('Ana', 'Martínez', '1982-07-30', 'F', '5554567890', 'Calle 4, Madrid ', NULL),
('Luis', 'Hernández', '1995-12-05', 'M', NULL, 'Calle 5, Madrid ', 'luis.hernandez@gmail.es'),
('Elena', 'Ramírez', '1988-11-12', 'F', NULL, 'Calle 6, Madrid ', 'elena.ramirez@example.es'),
('Jorge', 'Sánchez', '1975-05-08', 'M', '5557890123', 'Calle 7, Barcelona', 'jorge.sanchez@example.com'),
('Patricia', 'Torres', '1993-04-18', 'F', '5558901234', 'Calle 8, Cuenca', NULL),
('Fernando', 'Díaz', '1980-08-21', 'M', NULL, 'Calle 9, Madrid ', NULL),
('Gabriela', 'Mendoza', '1998-01-17', 'F', '5550123456', 'Calle 10, Madrid ', 'gabriela.mendoza@gmail.es'),
('Ricardo', 'Vargas', '1984-06-25', 'M', '5552233445', 'Calle 11, Madrid ', 'ricardo.vargas@example.com'),
('Andrea', 'Reyes', '1992-03-14', 'F', '5553344556', 'Calle 12, Madrid ', 'andrea.reyes@gmail.com'),
('Manuel', 'Gutiérrez', '1976-10-09', 'M', '5554455667', 'Calle 13, Madrid ', NULL),
('Sofía', 'Rojas', '1997-07-19', 'F', '5555566778', 'Calle 14, Madrid ', 'sofia.rojas@example.com'),
('Hugo', 'Navarro', '1981-02-23', 'M', NULL, 'Calle 15, Huelva', 'hugo.navarro@example.com'),
('Isabel', 'Cabrera', '1986-09-05', 'F', '5557788990', 'Calle 16, Sevilla', 'isabel.cabrera@example.com'),
('Pablo', 'Castro', '1994-04-29', 'M', '5558899001', 'Calle 17, Tarragona', 'pablo.castro@gmail.com'),
('Natalia', 'Ortega', '1979-11-11', 'F', '5559900112', 'Calle 18, Barcelona', 'natalia.ortega@gmail.com'),
('Esteban', 'Silva', '1991-06-07', 'M', '5551011123', 'Calle 19, Sevilla', 'esteban.silva@gmail.es'),
('Luisa', 'Morales', '1987-12-15', 'F', '5552122233', 'Calle 20, Salamanca', 'luisa.morales@example.es'),
('Daniel', 'Peña', '1996-01-24', 'M', '5553233344', 'Calle 21, Madrid ', 'daniel.pena@example.com'),
('Carolina', 'Garrido', '1983-08-30', 'F', '5554344455', 'Calle 22, Madrid ', 'carolina.garrido@example.com'),
('Martín', 'Flores', '1974-03-28', 'M', NULL, 'Calle 23, Madrid ', 'martin.flores@example.com'),
('Valeria', 'Salinas', '1999-10-03', 'F', '5556566677', 'Calle 24, Tarragona', 'valeria.salinas@example.com'),
('Guillermo', 'Araya', '1989-07-22', 'M', NULL, 'Calle 25, Tarragona', NULL),
('Rosa', 'Fuentes', '1977-02-14', 'F', '5558788899', 'Calle 26, Madrid ', 'rosa.fuentes@example.com'),
('César', 'Escobar', '1993-09-16', 'M', '5559899000', 'Calle 27, Barcelona', NULL),
('Beatriz', 'Godoy', '1985-05-31', 'F', '5550900111', 'Calle 28, Sevilla', 'beatriz.godoy@example.com'),
('Tomás', 'Vega', '1990-12-08', 'M', '5551111222', 'Calle 29, Madrid CC', 'tomas.vega@example.com'),
('Monica', 'Espinoza', '1982-06-21', 'F', '5552222333', 'Calle 30, Tarragona', NULL),
('Rodrigo', 'Muñoz', '1979-04-05', 'M', '5553333444', 'Calle 31, Madrid ', 'rodrigo.munoz@example.com'),
('Angela', 'Pizarro', '1998-08-19', 'F', '5554444555', 'Calle 32, Madrid ', 'angela.pizarro@example.com'),
('Sebastián', 'Lara', '1986-03-15', 'M', '5555555666', 'Calle 33, Barcelona', 'sebastian.lara@example.com'),
('Camila', 'Soto', '1995-09-26', 'F', '5556666777', 'Calle 34, Madrid ', NULL),
('Ignacio', 'Ojeda', '1975-11-07', 'M', '5557777888', 'Calle 35, Madrid ', 'ignacio.ojeda@example.com'),
('Paula', 'Rivera', '1984-07-13', 'F', '5558888999', 'Calle 36, Madrid ', NULL),
('Alejandro', 'Saavedra', '1992-05-09', 'M', '5559999000', 'Calle 37, Madrid ', 'alejandro.saavedra@example.com'),
('Francisca', 'Moya', '1981-10-18', 'F', '5550000111', 'Calle 38, Madrid ', NULL),
('Emilio', 'Zamora', '1978-06-03', 'M', '5551111222', 'Calle 39, Madrid ', NULL),
('Catalina', 'Álvarez', '1997-01-29', 'F', '5552222333', 'Calle 40, Madrid ', 'catalina.alvarez@example.com');

INSERT INTO especialidades (nombre) VALUES 
('Cardiología'),
('Dermatología'),
('Gastroenterología'),
('Endocrinología'),
('Neurología'),
('Oftalmología'),
('Oncología'),
('Pediatría'),
('Psiquiatría'),
('Traumatología'),
('Urología'),
('Ginecología'),
('Otorrinolaringología'),
('Neumología'),
('Nefrología'),
('Reumatología'),
('Medicina Interna'),
('Cirugía General'),
('Radiología'),
('Anestesiología'),
('Medicina Familiar'),
('Hematología'),
('Inmunología'),
('Cirugía Plástica'),
('Dermatopatología'),
('Medicina del Deporte'),
('Genética Médica'),
('Medicina Física y Rehabilitación'),
('Patología'),
('Toxicología Clínica'),
('Medicina Preventiva'),
('Geriatría'),
('Neurocirugía'),
('Cirugía Cardiovascular'),
('Cirugía Pediátrica'),
('Medicina de Emergencia'),
('Medicina del Trabajo'),
('Medicina Estética'),
('Foniatría'),
('Alergología');

INSERT INTO doctores (nombre, apellido, telefono, correo, especialidad_id) VALUES 
('Roberto', 'Fernández', '5551230001', 'roberto.fernandez@example.com', 1), -- Cardiología
('Laura', 'Gómez', NULL, 'laura.gomez@example.com', 2), -- Dermatología
('Alejandro', 'Martínez', '5551230003', 'alejandro.martinez@example.com', 3), -- Gastroenterología
('Sofía', 'López', '5551230004', 'sofia.lopez@example.com', 4), -- Endocrinología
('Javier', 'Hernández', '5551230005', 'javier.hernandez@example.com', 5), -- Neurología
('Gabriela', 'Ramírez', '5551230006', 'gabriela.ramirez@example.com', 6), -- Oftalmología
('Fernando', 'Sánchez', '5551230007', 'fernando.sanchez@example.com', 7), -- Oncología
('Patricia', 'Torres', '5551230008', 'patricia.torres@example.com', 8), -- Pediatría
('Luis', 'Díaz', '5551230009', 'luis.diaz@example.com', 9), -- Psiquiatría
('Elena', 'Mendoza', '5551230010', 'elena.mendoza@example.com', 10), -- Traumatología
('Carlos', 'Vargas', NULL, 'carlos.vargas@example.com', 11), -- Urología
('Ana', 'Reyes', NULL, 'ana.reyes@example.com', 12), -- Ginecología
('Jorge', 'Gutiérrez', NULL, 'jorge.gutierrez@example.com', 13), -- Otorrinolaringología
('Beatriz', 'Rojas', NULL, 'beatriz.rojas@example.com', 14), -- Neumología
('Hugo', 'Navarro', '5551230015', 'hugo.navarro@example.com', 15), -- Nefrología
('Isabel', 'Cabrera', '5551230016', 'isabel.cabrera@example.com', 16), -- Reumatología
('Pablo', 'Castro', '5551230017', 'pablo.castro@example.com', 17), -- Medicina Interna
('Natalia', 'Ortega', '5551230018', 'natalia.ortega@example.com', 18), -- Cirugía General
('Esteban', 'Silva', '5551230019', 'esteban.silva@example.com', 19), -- Radiología
('Luisa', 'Morales', NULL, 'luisa.morales@example.com', 20), -- Anestesiología
('Daniel', 'Peña', '5551230021', 'daniel.pena@example.com', 21), -- Medicina Familiar
('Carolina', 'Garrido', '5551230022', 'carolina.garrido@example.com', 22), -- Hematología
('Martín', 'Flores', '5551230023', 'martin.flores@example.com', 23), -- Inmunología
('Valeria', 'Salinas', '5551230024', 'valeria.salinas@example.com', 24), -- Cirugía Plástica
('Guillermo', 'Araya', NULL, 'guillermo.araya@example.com', 25), -- Dermatopatología
('Rosa', 'Fuentes', '5551230026', 'rosa.fuentes@example.com', 26), -- Medicina del Deporte
('César', 'Escobar', '5551230027', 'cesar.escobar@example.com', 27), -- Genética Médica
('Beatriz', 'Godoy', '5551230028', 'beatriz.godoy@example.com', 28), -- Medicina Física y Rehabilitación
('Tomás', 'Vega', '5551230029', 'tomas.vega@example.com', 29), -- Patología
('Monica', 'Espinoza', '5551230030', 'monica.espinoza@example.com', 30), -- Toxicología Clínica
('Rodrigo', 'Muñoz', '5551230031', 'rodrigo.munoz@example.com', 31), -- Medicina Preventiva
('Angela', 'Pizarro', '5551230032', 'angela.pizarro@example.com', 32), -- Geriatría
('Sebastián', 'Lara', '5551230033', 'sebastian.lara@example.com', 33), -- Neurocirugía
('Camila', 'Soto', NULL, 'camila.soto@example.com', 34), -- Cirugía Cardiovascular
('Ignacio', 'Ojeda', '5551230035', 'ignacio.ojeda@example.com', 35), -- Cirugía Pediátrica
('Paula', 'Rivera', NULL, 'paula.rivera@example.com', 36), -- Medicina de Emergencia
('Alejandro', 'Saavedra', '5551230037', 'alejandro.saavedra@example.com', 37), -- Medicina del Trabajo
('Francisca', 'Moya', NULL, 'francisca.moya@example.com', 38), -- Medicina Estética
('Emilio', 'Zamora', '5551230039', 'emilio.zamora@example.com', 39), -- Foniatría
('Catalina', 'Álvarez', '5551230040', 'catalina.alvarez@example.com', 40); -- Alergología

INSERT INTO medicamentos (nombre, precio, descripcion) VALUES 
('Paracetamol', DEFAULT , 'Analgésico y antipirético usado para tratar fiebre y dolor leve a moderado.'),
('Ibuprofeno', DEFAULT , 'Antiinflamatorio no esteroideo usado para tratar dolor e inflamación.'),
('Amoxicilina', 13.45 ,'Antibiótico de amplio espectro usado para tratar infecciones bacterianas.'),
('Omeprazol', DEFAULT ,'Inhibidor de la bomba de protones usado para tratar reflujo gástrico y úlceras.'),
('Loratadina', DEFAULT ,'Antihistamínico usado para tratar alergias y rinitis.'),
('Cetirizina', DEFAULT ,'Antihistamínico de segunda generación para alergias.'),
('Diclofenaco', 10.24 ,'Antiinflamatorio no esteroideo usado para dolor e inflamación.'),
('Metformina', DEFAULT ,'Medicamento para la diabetes tipo 2 que reduce la producción de glucosa en el hígado.'),
('Salbutamol', DEFAULT ,'Broncodilatador usado para el asma y EPOC.'),
('Prednisona', 2.34 ,'Corticosteroide usado para tratar inflamaciones y alergias severas.'),
('Aspirina', DEFAULT ,'Analgésico y antipirético que también previene coágulos sanguíneos.'),
('Diazepam', DEFAULT ,'Benzodiacepina usada para ansiedad, espasmos musculares y convulsiones.'),
('Sertralina', 23.22 ,'Antidepresivo del grupo ISRS usado para depresión y ansiedad.'),
('Losartán', 30.45 , 'Antihipertensivo que bloquea los receptores de angiotensina II.'),
('Atorvastatina', DEFAULT ,'Fármaco hipolipemiante usado para reducir el colesterol.'),
('Enalapril', DEFAULT , 'Inhibidor de la ECA usado para tratar la hipertensión.'),
('Furosemida', 3.54 , 'Diurético de asa usado para tratar edemas y presión arterial alta.'),
('Ranitidina', DEFAULT , 'Antihistamínico H2 usado para tratar úlceras y reflujo gástrico.'),
('Clonazepam', DEFAULT ,'Benzodiacepina usada para tratar crisis epilépticas y ansiedad.'),
('Tramadol', DEFAULT ,'Analgésico opioide usado para tratar el dolor moderado a severo.'),
('Levotiroxina', DEFAULT ,'Hormona tiroidea usada para tratar el hipotiroidismo.'),
('Insulina', DEFAULT ,'Hormona usada para el tratamiento de la diabetes mellitus.'),
('Carbamazepina',3.54 ,'Antiepiléptico usado para tratar convulsiones y trastornos bipolares.'),
('Morfina',46.7,'Opioide usado para tratar dolor severo.'),
('Azitromicina',3.54 ,'Antibiótico macrólido usado para tratar infecciones bacterianas.'),
('Ciprofloxacino', 34.65 , 'Antibiótico fluoroquinolona usado para tratar infecciones bacterianas.'),
('Ketorolaco', 5.55 ,'Antiinflamatorio no esteroideo usado para el dolor moderado a severo.'),
('Naproxeno', 52.35 , 'Antiinflamatorio no esteroideo usado para tratar dolor e inflamación.'),
('Dexametasona', 34.35 , 'Corticosteroide usado para inflamaciones severas y reacciones alérgicas.'),
('Betametasona', DEFAULT , 'Corticosteroide usado para enfermedades inflamatorias y autoinmunes.'),
('Fluconazol', 5.45 , 'Antifúngico usado para tratar infecciones por hongos.'),
('Albendazol', 52.35 , 'Antiparasitario usado para tratar infecciones por parásitos.'),
('Mebendazol', 4.35 , 'Antiparasitario usado para tratar infecciones por helmintos.'),
('Metronidazol', 3.35 , 'Antibiótico y antiparasitario usado para infecciones bacterianas y protozoarias.'),
('Hidroxicloroquina', 43.20 , 'Usado para tratar malaria, artritis reumatoide y lupus.'),
('Claritromicina', 88.55 , 'Antibiótico macrólido usado para infecciones respiratorias y cutáneas.'),
('Doxiciclina', 55.34 , 'Antibiótico tetraciclina usado para infecciones bacterianas.'),
('Vildagliptina', 66.44 , 'Medicamento para la diabetes tipo 2 que mejora la secreción de insulina.'),
('Rosuvastatina', DEFAULT , 'Estatina usada para reducir el colesterol y prevenir enfermedades cardiovasculares.');

INSERT INTO consultas (paciente_id, doctor_id, fecha, diagnostico) VALUES 
(1, 5, '2024-01-10', 'Migraña crónica controlada con medicación.'),
(2, 12, '2024-01-12', 'Control prenatal, embarazo en buen estado.'),
(3, 7, '2024-01-15', 'Cáncer de mama en etapa inicial, se inicia tratamiento.'),
(4, 20, '2024-01-20', 'Evaluación preoperatoria para cirugía menor.'),
(5, 33, '2024-01-22', 'Paciente con antecedentes de traumatismo craneoencefálico leve.'),
(6, 8, '2024-01-25', 'Niño con infección respiratoria aguda, tratamiento sintomático.'),
(7, 16, '2024-01-27', 'Artritis reumatoide, ajuste de medicación.'),
(8, 21, '2024-02-01', 'Hipertensión arterial, control de tratamiento.'),
(9, 14, '2024-02-05', 'Paciente con insuficiencia renal en tratamiento de diálisis.'),
(10, 3, '2024-02-08', 'Gastritis crónica, se recomienda dieta y medicación.'),
(11, 5, '2024-02-10', 'Paciente con cefaleas tensionales recurrentes.'),
(12, 9, '2024-02-15', 'Trastorno de ansiedad generalizada, inicio de tratamiento psicológico.'),
(13, 35, '2024-02-18', 'Cirugía pediátrica programada para hernia umbilical.'),
(14, 6, '2024-02-20', 'Paciente con conjuntivitis alérgica, tratamiento con antihistamínicos.'),
(15, 1, '2024-02-25', 'Revisión cardiovascular, se mantiene estable.'),
(16, 28, '2024-03-01', 'Fractura de muñeca en proceso de recuperación.'),
(17, 32, '2024-03-05', 'Demencia senil avanzada, apoyo familiar recomendado.'),
(18, 18, '2024-03-07', 'Cirugía de apendicitis programada.'),
(19, 11, '2024-03-10', 'Infección urinaria recurrente, ajustes en tratamiento antibiótico.'),
(20, 10, '2024-03-12', 'Lesión deportiva en rodilla, tratamiento con fisioterapia.'),
(21, 4, '2024-03-15', 'Paciente con diabetes tipo 2, ajustes en dosis de metformina.'),
(22, 30, '2024-03-18', 'Paciente con intoxicación alimentaria, manejo sintomático.'),
(23, 2, '2024-03-20', 'Dermatitis atópica, se receta crema con corticoides.'),
(24, 13, '2024-03-22', 'Otitis media aguda, se indica antibiótico oral.'),
(25, 24, '2024-03-25', 'Paciente candidato a cirugía plástica reconstructiva.'),
(26, 17, '2024-03-27', 'Evaluación de paciente con lupus eritematoso sistémico.'),
(27, 15, '2024-03-30', 'Nefritis aguda, se recomienda seguimiento estrecho.'),
(28, 27, '2024-04-02', 'Paciente con diagnóstico de fibrosis quística, manejo multidisciplinario.'),
(29, 22, '2024-04-05', 'Paciente con leucemia en seguimiento oncológico.'),
(30, 26, '2024-04-08', 'Atleta con lesión muscular, rehabilitación recomendada.'),
(31, 30, '2024-04-10', 'Reacción alérgica grave, manejo con antihistamínicos y corticoides.'),
(32, 19, '2024-04-12', 'Paciente con fractura costal, manejo del dolor.'),
(33, 29, '2024-04-15', 'Paciente con insuficiencia hepática, tratamiento paliativo.'),
(34, 31, '2024-04-18', 'Paciente con problemas cardiovasculares, control médico mensual.'),
(35, 25, '2024-04-20', 'Paciente solicita cirugía estética, evaluación preoperatoria.'),
(36, 36, '2024-04-22', 'Paciente con quemaduras leves, manejo con cremas regenerativas.'),
(37, 38, '2024-04-25', 'Paciente con trastorno de la voz, terapia foniátrica recomendada.'),
(38, 23, '2024-04-27', 'Paciente con deficiencia inmunológica, se inicia terapia específica.'),
(39, 39, '2024-04-30', 'Paciente con problemas de articulación temporomandibular, tratamiento con fisioterapia.'),
(40, 34, '2024-05-02', 'Paciente con problemas cardiovasculares, evaluación para cirugía.'),
(5, 10, '2024-05-05', 'Esguince de tobillo leve, tratamiento con reposo y fisioterapia.'),
(8, 3, '2024-05-07', 'Revisión de gastritis, ajuste en tratamiento con omeprazol.'),
(2, 12, '2024-05-10', 'Seguimiento de embarazo, sin complicaciones.'),
(15, 21, '2024-05-12', 'Hipertensión controlada, sin cambios en medicación.'),
(9, 14, '2024-05-15', 'Insuficiencia renal crónica, ajuste en terapia de diálisis.'),
(20, 5, '2024-05-18', 'Paciente con cefalea tensional, recomendación de terapia física.'),
(11, 9, '2024-05-20', 'Trastorno de ansiedad en mejoría, seguimiento en tres meses.'),
(7, 16, '2024-05-22', 'Artritis reumatoide en control, sin nuevos síntomas.'),
(1, 5, '2024-05-25', 'Seguimiento de migrañas, sin cambios en medicación.'),
(4, 20, '2024-05-28', 'Paciente con esguince cervical, manejo con analgésicos.'),
(25, 7, '2024-06-01', 'Paciente con diagnóstico de melanoma en evaluación oncológica.'),
(3, 18, '2024-06-03', 'Postoperatorio de apendicectomía, sin complicaciones.'),
(32, 11, '2024-06-05', 'Infección urinaria recurrente, nuevo tratamiento antibiótico.'),
(19, 10, '2024-06-07', 'Fractura de muñeca en proceso de consolidación.'),
(22, 30, '2024-06-10', 'Gastroenteritis viral, manejo sintomático con hidratación.'),
(6, 8, '2024-06-12', 'Niño con bronquitis leve, prescripción de broncodilatador.'),
(10, 3, '2024-06-15', 'Gastritis con reflujo, tratamiento con antiácidos.'),
(12, 35, '2024-06-18', 'Hernia umbilical en evaluación quirúrgica.'),
(31, 32, '2024-06-20', 'Reacción alérgica cutánea, manejo con antihistamínicos.'),
(21, 4, '2024-06-22', 'Control de diabetes tipo 2, buen control glucémico.'),
(13, 27, '2024-06-25', 'Fibrosis quística en seguimiento, ajuste en medicación.'),
(24, 13, '2024-06-28', 'Otitis media con mejoría, seguimiento en una semana.'),
(9, 14, '2024-07-01', 'Seguimiento de insuficiencia renal, control en laboratorio.'),
(26, 17, '2024-07-03', 'Paciente con lupus eritematoso, seguimiento trimestral.'),
(30, 22, '2024-07-05', 'Paciente con leucemia, ajuste en tratamiento oncológico.'),
(35, 24, '2024-07-07', 'Evaluación preoperatoria para cirugía plástica.'),
(40, 31, '2024-07-10', 'Paciente con hipertensión en seguimiento cardiológico.'),
(33, 29, '2024-07-12', 'Insuficiencia hepática en fase avanzada, manejo paliativo.'),
(28, 6, '2024-07-15', 'Paciente con conjuntivitis bacteriana, prescripción de antibióticos.'),
(15, 21, '2024-07-18', 'Hipertensión estable, sin cambios en medicación.'),
(37, 38, '2024-07-20', 'Trastorno de la voz, sesión de terapia foniátrica.'),
(16, 28, '2024-07-22', 'Paciente con fractura de radio en seguimiento.'),
(18, 19, '2024-07-25', 'Paciente con dolor lumbar, manejo con fisioterapia.'),
(29, 32, '2024-07-28', 'Demencia senil en progresión, apoyo familiar recomendado.'),
(14, 26, '2024-08-01', 'Lesión muscular en atleta, terapia de rehabilitación.'),
(27, 39, '2024-08-03', 'Trastorno de articulación temporomandibular, fisioterapia indicada.'),
(34, 34, '2024-08-05', 'Evaluación cardiovascular preoperatoria, sin contraindicaciones.'),
(36, 25, '2024-08-07', 'Paciente con quemaduras en cicatrización, seguimiento en dos semanas.'),
(23, 23, '2024-08-10', 'Deficiencia inmunológica en tratamiento con inmunoglobulina.');

INSERT INTO recetas (consulta_id, fecha_emision, indicaciones) VALUES 
(1, '2024-01-10', 'Tomar Paracetamol 500mg cada 8 horas por 5 días.'),
(2, '2024-01-12', 'Suplementación con ácido fólico y hierro, dieta equilibrada.'),
(3, '2024-01-15', 'Administrar terapia oncológica según protocolo.'),
(4, '2024-01-20', 'Ayuno previo a cirugía, no consumir alimentos por 12 horas.'),
(5, '2024-01-22', 'Descanso absoluto por una semana, uso de analgésicos.'),
(6, '2024-01-25', 'Administrar Salbutamol en nebulización cada 6 horas.'),
(7, '2024-01-27', 'Tomar Metotrexato 7.5 mg semanalmente para artritis.'),
(8, '2024-02-01', 'Tomar Losartán 50 mg diariamente para control de presión.'),
(9, '2024-02-05', 'Ajuste de diálisis, monitoreo de niveles de creatinina.'),
(10, '2024-02-08', 'Tomar Omeprazol 20 mg cada mañana en ayunas.'),
(11, '2024-02-10', 'Ejercicio físico regular y técnicas de relajación.'),
(12, '2024-02-15', 'Iniciar tratamiento con Sertralina 50 mg diarios.'),
(13, '2024-02-18', 'Preoperatorio con antibióticos profilácticos.'),
(14, '2024-02-20', 'Aplicar gotas oftálmicas antihistamínicas cada 8 horas.'),
(15, '2024-02-25', 'Continuar con aspirina 100 mg diarios.'),
(16, '2024-03-01', 'Inmovilización de muñeca con férula durante 3 semanas.'),
(17, '2024-03-05', 'Monitoreo cognitivo mensual, apoyo familiar.'),
(18, '2024-03-07', 'Ayuno previo y administración de antibióticos prequirúrgicos.'),
(19, '2024-03-10', 'Tomar Ciprofloxacino 500 mg cada 12 horas por 7 días.'),
(20, '2024-03-12', 'Fisioterapia para rehabilitación de rodilla.'),
(21, '2024-03-15', 'Ajustar dosis de Metformina según niveles de glucosa.'),
(22, '2024-03-18', 'Rehidratación oral con suero fisiológico y dieta blanda.'),
(23, '2024-03-20', 'Aplicar crema con corticoides en áreas afectadas.'),
(24, '2024-03-22', 'Tomar Amoxicilina 500 mg cada 8 horas por 10 días.'),
(25, '2024-03-25', 'Evaluación médica para determinar viabilidad quirúrgica.'),
(26, '2024-03-27', 'Tomar Prednisona 5 mg en días alternos.'),
(27, '2024-03-30', 'Monitoreo de función renal, dieta baja en sodio.'),
(28, '2024-04-02', 'Terapia multidisciplinaria para manejo de fibrosis quística.'),
(29, '2024-04-05', 'Ajuste en protocolo de quimioterapia.'),
(30, '2024-04-08', 'Reposo relativo y aplicación de compresas frías.'),
(31, '2024-04-10', 'Administrar antihistamínicos en caso de reacciones alérgicas.'),
(32, '2024-04-12', 'Uso de analgésicos y seguimiento en 5 días.'),
(33, '2024-04-15', 'Manejo con dieta baja en proteínas y medicamentos hepáticos.'),
(34, '2024-04-18', 'Control estricto de presión arterial con medicación.'),
(35, '2024-04-20', 'Evaluación psicológica previa a cirugía estética.'),
(36, '2024-04-22', 'Aplicar crema regenerativa dos veces al día.'),
(37, '2024-04-25', 'Terapia de rehabilitación para recuperación vocal.'),
(38, '2024-04-27', 'Administrar inmunoterapia específica según protocolo.'),
(39, '2024-04-30', 'Ejercicios de fisioterapia para articulación temporomandibular.'),
(40, '2024-05-02', 'Evaluación cardiovascular para cirugía, monitoreo de ECG.'),
(41, '2024-05-05', 'Reposo y aplicación de hielo en tobillo afectado.'),
(42, '2024-05-07', 'Tomar Omeprazol 20mg diariamente antes del desayuno.'),
(43, '2024-05-10', 'Continuar con ácido fólico y hierro hasta el tercer trimestre.'),
(44, '2024-05-12', 'Control de presión arterial con enalapril 10 mg diario.'),
(45, '2024-05-15', 'Ajuste de dosis en diálisis, seguimiento renal mensual.'),
(46, '2024-05-18', 'Ejercicios de relajación y terapia física para cefalea tensional.'),
(47, '2024-05-20', 'Terapia conductual para ansiedad, evaluación en 1 mes.'),
(48, '2024-05-22', 'Continuar con metotrexato 7.5 mg semanalmente.'),
(49, '2024-05-25', 'Control de migrañas, se sugiere terapia alternativa.'),
(50, '2024-05-28', 'Usar collarín cervical y evitar movimientos bruscos.'),
(51, '2024-06-01', 'Programación de cirugía para extracción de melanoma.'),
(52, '2024-06-03', 'Tomar analgésicos en caso de dolor postquirúrgico.'),
(53, '2024-06-05', 'Iniciar tratamiento con antibióticos por 10 días.'),
(54, '2024-06-07', 'Aplicar compresas frías y reposo de la muñeca.'),
(55, '2024-06-10', 'Hidratación oral y dieta blanda hasta mejoría.'),
(56, '2024-06-12', 'Nebulización con broncodilatador en caso de dificultad respiratoria.'),
(57, '2024-06-15', 'Tomar ranitidina 150 mg antes de dormir.'),
(58, '2024-06-18', 'Planificar cirugía de hernia en los próximos meses.'),
(59, '2024-06-20', 'Tomar loratadina 10 mg diariamente por 7 días.'),
(60, '2024-06-22', 'Monitoreo de glucosa en ayunas cada 2 semanas.'),
(61, '2024-06-25', 'Iniciar fisioterapia pulmonar para mejorar la respiración.'),
(62, '2024-06-28', 'Revisión en consulta para confirmar curación de otitis.'),
(63, '2024-07-01', 'Continuar con tratamiento de insuficiencia renal.'),
(64, '2024-07-03', 'Tomar hidroxicloroquina 200 mg diariamente para lupus.'),
(65, '2024-07-05', 'Continuar con terapia de quimioterapia según cronograma.'),
(66, '2024-07-07', 'Planificar cirugía plástica en las próximas semanas.'),
(67, '2024-07-10', 'Control de hipertensión, ajuste de dosis si es necesario.'),
(68, '2024-07-12', 'Dieta baja en sodio y reducción de proteínas.'),
(69, '2024-07-15', 'Aplicar colirio antibiótico cada 8 horas por 5 días.'),
(70, '2024-07-18', 'Control mensual de presión arterial.'),
(71, '2024-07-20', 'Ejercicios de vocalización y fisioterapia foniátrica.'),
(72, '2024-07-22', 'Uso de yeso por 4 semanas y seguimiento en consulta.'),
(73, '2024-07-25', 'Evitar levantamiento de objetos pesados, terapia de fortalecimiento.'),
(74, '2024-07-28', 'Monitoreo del deterioro cognitivo, apoyo familiar recomendado.'),
(75, '2024-08-01', 'Ejercicios de estiramiento y terapia física para recuperación muscular.'),
(76, '2024-08-03', 'Fisioterapia para mejorar la función mandibular.'),
(77, '2024-08-05', 'Evaluación preoperatoria para cirugía cardiovascular.'),
(78, '2024-08-07', 'Aplicar crema hidratante en quemaduras 3 veces al día.'),
(79, '2024-08-10', 'Aplicar inmunoglobulina según indicación médica.');
INSERT INTO detalle_receta (receta_id, medicamento_id, dosis) VALUES 
(1, 5, '500mg cada 8 horas por 5 días'),
(2, 12, '1 tableta diaria con el desayuno'),
(3, 30, 'Según protocolo oncológico'),
(4, 18, 'Ayuno 12 horas antes de cirugía'),
(5, 7, '1 tableta cada 12 horas por 7 días'),
(6, 22, 'Nebulización cada 6 horas'),
(7, 14, '7.5 mg semanalmente'),
(8, 3, '50 mg diario por la mañana'),
(9, 25, 'Ajuste en terapia de diálisis'),
(10, 11, '20 mg diario en ayunas'),
(11, 29, 'Ejercicios de respiración y relajación'),
(12, 32, '50 mg diarios antes de dormir'),
(13, 8, '1 tableta antes de cirugía'),
(14, 21, 'Aplicar 2 gotas en cada ojo cada 8 horas'),
(15, 35, '100 mg diarios para control de presión'),
(16, 24, 'Inmovilización con férula por 3 semanas'),
(17, 19, 'Monitoreo cognitivo mensual'),
(18, 6, 'Administración de antibióticos antes de cirugía'),
(19, 16, '500 mg cada 12 horas por 7 días'),
(20, 28, 'Fisioterapia para recuperación de rodilla'),
(21, 13, 'Ajustar dosis de metformina según glucosa'),
(22, 9, 'Rehidratación oral con suero fisiológico'),
(23, 34, 'Aplicar en zonas afectadas cada 12 horas'),
(24, 10, '500 mg cada 8 horas por 10 días'),
(25, 26, 'Evaluación para cirugía en la próxima consulta'),
(26, 20, '5 mg en días alternos'),
(27, 23, 'Monitoreo de función renal'),
(28, 33, 'Tratamiento multidisciplinario para fibrosis'),
(29, 15, 'Ajuste de quimioterapia según respuesta'),
(30, 2, 'Reposo y aplicación de compresas frías'),
(31, 1, 'Administrar antihistamínicos en caso de alergias'),
(32, 27, 'Analgésicos en caso de dolor intenso'),
(33, 4, 'Dieta baja en proteínas y sodio'),
(34, 17, 'Control estricto de presión arterial'),
(35, 31, 'Evaluación psicológica previa a cirugía'),
(36, 36, 'Aplicar crema regenerativa 2 veces al día'),
(37, 20, 'Terapia de rehabilitación para voz'),
(38, 39, 'Administrar inmunoterapia según indicación'),
(39, 37, 'Ejercicios de fisioterapia mandibular'),
(40, 38, 'Monitoreo cardíaco antes de cirugía'),
(41, 5, '500mg cada 8 horas por 5 días'),
(42, 12, '1 tableta diaria con el desayuno'),
(43, 30, 'Según protocolo oncológico'),
(44, 18, 'Ayuno 12 horas antes de cirugía'),
(45, 7, '1 tableta cada 12 horas por 7 días'),
(46, 22, 'Nebulización cada 6 horas'),
(47, 14, '7.5 mg semanalmente'),
(48, 3, '50 mg diario por la mañana'),
(49, 25, 'Ajuste en terapia de diálisis'),
(50, 11, '20 mg diario en ayunas'),
(51, 29, 'Ejercicios de respiración y relajación'),
(52, 32, '50 mg diarios antes de dormir'),
(53, 8, '1 tableta antes de cirugía'),
(54, 21, 'Aplicar 2 gotas en cada ojo cada 8 horas'),
(55, 35, '100 mg diarios para control de presión'),
(56, 24, 'Inmovilización con férula por 3 semanas'),
(57, 19, 'Monitoreo cognitivo mensual'),
(58, 6, 'Administración de antibióticos antes de cirugía'),
(59, 16, '500 mg cada 12 horas por 7 días'),
(60, 28, 'Fisioterapia para recuperación de rodilla'),
(61, 13, 'Ajustar dosis de metformina según glucosa'),
(62, 9, 'Rehidratación oral con suero fisiológico'),
(63, 34, 'Aplicar en zonas afectadas cada 12 horas'),
(64, 10, '500 mg cada 8 horas por 10 días'),
(65, 26, 'Evaluación para cirugía en la próxima consulta'),
(66, 20, '5 mg en días alternos'),
(67, 23, 'Monitoreo de función renal'),
(68, 33, 'Tratamiento multidisciplinario para fibrosis'),
(69, 15, 'Ajuste de quimioterapia según respuesta'),
(70, 2, 'Reposo y aplicación de compresas frías'),
(71, 1, 'Administrar antihistamínicos en caso de alergias'),
(72, 27, 'Analgésicos en caso de dolor intenso'),
(73, 4, 'Dieta baja en proteínas y sodio'),
(74, 17, 'Control estricto de presión arterial'),
(75, 31, 'Evaluación psicológica previa a cirugía'),
(76, 36, 'Aplicar crema regenerativa 2 veces al día'),
(78, 39, 'Administrar inmunoterapia según indicación'),
(79, 37, 'Ejercicios de fisioterapia mandibular');

-- Actividades --
select * from pacientes;
select nombre,fecha_nacimiento from pacientes;
select nombre, especialidad_id from doctores;
select * from doctores;
select * from pacientes where genero = 'M';
select * from doctores where especialidad_id = 3;
select * from consultas where fecha > '2024-01-01';
select * from medicamentos where descripcion like "%dolor%";
select * from consultas where diagnostico like "%hipertensión%";
select * from medicamentos where precio >= 10 and precio <= 30;
select especialidad_id*2 from doctores;
select id-100 from consultas;
select Precio/2 from medicamentos;
select * from pacientes where genero = 'M' and direccion like "%Madrid%";
select * from medicamentos where nombre like "A%" and nombre not like "%ina";
select distinct year(fecha_emision) from recetas;
select concat(nombre,' ',apellido) as "Nombre completo" from pacientes;
select Precio as "Costo Unitario" from medicamentos;
select fecha_emision as "Fecha de Receta" from recetas;
select * from pacientes where nombre like "M%";
select * from doctores where apellido like "%ez";
select * from consultas where diagnostico like "%asma%";
select * from pacientes order by nombre;
select * from doctores order by apellido desc;
select * from medicamentos order by Precio;
select * from consultas order by fecha desc;
select * from doctores where especialidad_id != 5;
select * from consultas where fecha > '2024-03-01';
select * from medicamentos where Precio < 20;
select * from pacientes where fecha_nacimiento > '1995-10-02';
