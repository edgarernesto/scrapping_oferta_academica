CREATE TABLE carrera(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL
);

CREATE TABLE materia(
  clave VARCHAR(5) PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  creditos INT NOT NULL
);

CREATE TABLE carrera_materia(
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_carrera INT NOT NULL,
  clave_materia VARCHAR(5) NOT NULL,
  FOREIGN KEY (id_carrera) REFERENCES carrera(id),
  FOREIGN KEY (clave_materia) REFERENCES materia(clave)
);

CREATE TABLE profesor(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL
);

CREATE TABLE periodo(
  id INT PRIMARY KEY AUTO_INCREMENT,
  periodo VARCHAR(50) NOT NULL
);

CREATE TABLE seccion(
  nrc INT PRIMARY KEY,
  seccion VARCHAR(4) NOT NULL,
  cupos INT NOT NULL,
  disponibles INT NOT NULL,
  id_periodo INT NOT NULL,
  clave_materia VARCHAR(5) NOT NULL,
  id_profesor INT NOT NULL,
  FOREIGN KEY (id_periodo) REFERENCES periodo(id),
  FOREIGN KEY (clave_materia) REFERENCES materia(clave),
  FOREIGN KEY (id_profesor) REFERENCES profesor(id)
);

CREATE TABLE horario(
  id INT PRIMARY KEY AUTO_INCREMENT,
  sesion INT NOT NULL,
  hora VARCHAR(10) NOT NULL,
  dias VARCHAR(12) NOT NULL,
  edificio VARCHAR(10) NOT NULL,
  aula VARCHAR(10) NOT NULL,
  nrc_seccion INT NOT NULL,
  FOREIGN KEY (nrc_seccion) REFERENCES seccion(nrc)
);
