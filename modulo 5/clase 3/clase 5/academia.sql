create database if not exists academia;
use academia;


--tabla de alumnos 
create table alumnos(
    id int auto_increment primary key,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    telefono varchar(20) not null,
    email varchar(50) unique not null, 
);

--tabla profesores
create table profesores(
    id int auto_increment primary key,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    telefono varchar(20) not null,
    email varchar(50) unique not null, 
    especialidad varchar(50) not null
);

--tabla cursos
create table cursos(
    id int auto_increment primary key,
    nombre varchar(50) not null,
    descripcion text not null,
    duracion_horas int not null,
    fecha_fin int,
    profesor_id int not null,
    foreign key (profesor_id) references profesores(id)
        on delete set null on update cascade
);

--tabla inscripciones(relaciones alumnos y cursos)
--un alumno puede estar inscrito en varios cursos y un curso puede tener varios alumnos
create table inscripciones(
    id int auto_increment primary key,
    alumno_id int not null,
    curso_id int not null,
    fecha_inscripcion date not null,
    foreign key (alumno_id) references alumnos(id)
        on delete cascade on update cascade,
    foreign key (curso_id) references cursos(id)
        on delete cascade on update cascade
);

--tabla horarios (relacion cursos y horarios)
--un curso puede tener varios horarios y un horario puede pertenecer a varios cursos
create table horarios(
    id int auto_increment primary key,
    curso_id int not null,
    dia_semana varchar(50) not null,
    hora_inicio time not null,
    hora_fin time not null,
    foreign key (curso_id) references cursos(id)
        on delete cascade on update cascade
);

-- insertar datos en la base de datos:
-- Insertar datos en la tabla alumnos
insert into alumnos (nombre, apellido, telefono, email)
values 
('Juan', 'Pérez', '123456789', 'juan.perez@example.com'),
('María', 'Gómez', '987654321', 'maria.gomez@example.com'),
('Pedro', 'López', '456789123', 'pedro.lopez@example.com');

-- Insertar datos en la tabla profesores
insert into profesores (nombre, apellido, telefono, email, especialidad)
values 
('Carlos', 'Martínez', '111222333', 'carlos.martinez@example.com', 'Matemáticas'),
('Ana', 'Fernández', '444555666', 'ana.fernandez@example.com', 'Historia'),
('Luis', 'García', '777888999', 'luis.garcia@example.com', 'Ciencias');

-- Insertar datos en la tabla cursos
insert into cursos (nombre, descripcion, duracion_horas, profesor_id)
values 
('Álgebra', 'Curso de álgebra básica', 40, 1),
('Historia Universal', 'Curso de historia universal', 30, 2),
('Física', 'Curso de física básica', 50, 3);

-- Insertar datos en la tabla inscripciones
insert into inscripciones (alumno_id, curso_id, fecha_inscripcion)
values 
(1, 1, '2025-04-01'),
(2, 2, '2025-04-02'),
(3, 3, '2025-04-03'),
(1, 3, '2025-04-04');

-- Insertar datos en la tabla horarios
insert into horarios (curso_id, dia_semana, hora_inicio, hora_fin)
values 
(1, 'Lunes', '08:00:00', '10:00:00'),
(1, 'Miércoles', '08:00:00', '10:00:00'),
(2, 'Martes', '10:00:00', '12:00:00'),
(3, 'Jueves', '14:00:00', '16:00:00');

-- mostrar los datos de las tablas
select * from alumnos;
select * from profesores; 
select * from cursos;
select * from inscripciones;
select * from horarios;
