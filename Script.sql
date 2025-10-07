CREATE DATABASE IF NOT EXISTS db_parqueadero2;
USE db_parqueadero2;

-- =====================================================
-- 1. CLIENTE
-- =====================================================
CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    documento VARCHAR(20) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    correo VARCHAR(100),
    direccion VARCHAR(150)
);

ALTER TABLE Cliente
ADD CONSTRAINT uq_documento UNIQUE (documento);

-- =====================================================
-- 2. TIPO VEHICULO
-- =====================================================
CREATE TABLE TipoVehiculo (
    id_tipo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,          -- Carro, moto, bicicleta, camión
    descripcion VARCHAR(100)
);

-- =====================================================
-- 3. VEHICULO
-- =====================================================
CREATE TABLE Vehiculo (
    id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10) NOT NULL UNIQUE,
    marca VARCHAR(50),
    color VARCHAR(30),
    id_tipo INT NOT NULL,
    id_cliente INT,
    FOREIGN KEY (id_tipo) REFERENCES TipoVehiculo(id_tipo),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- =====================================================
-- 4. ROL EMPLEADO
-- =====================================================
CREATE TABLE RolEmpleado (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,      -- Ej: Administrador, Cajero, Valet Parking
    descripcion VARCHAR(100)
);

ALTER TABLE RolEmpleado
ADD CONSTRAINT uq_nombre UNIQUE (nombre);
-- =====================================================
-- 5. EMPLEADO
-- =====================================================
CREATE TABLE Empleado (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    documento VARCHAR(20) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    correo VARCHAR(100),
    id_rol INT NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES RolEmpleado(id_rol)
);

-- =====================================================
-- 6. TARIFA
-- =====================================================
CREATE TABLE Tarifa (
    id_tarifa INT AUTO_INCREMENT PRIMARY KEY,
    id_tipo INT NOT NULL,
    tipo_tarifa ENUM('Hora','Dia','Mes') NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_tipo) REFERENCES TipoVehiculo(id_tipo)
);

-- =====================================================
-- 7. ENTRADA / SALIDA
-- =====================================================
CREATE TABLE EntradaSalida (
    id_registro INT AUTO_INCREMENT PRIMARY KEY,
    id_vehiculo INT NOT NULL,
    id_empleado INT NOT NULL,
    fecha_entrada DATETIME NOT NULL,
    fecha_salida DATETIME,
    espacio VARCHAR(10),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculo(id_vehiculo),
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

-- =====================================================
-- 8. METODO DE PAGO
-- =====================================================
CREATE TABLE MetodoPago (
    id_metodo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,      -- Efectivo, tarjeta, app móvil, QR, etc.
    descripcion VARCHAR(100)
);
ALTER TABLE MetodoPago ADD CONSTRAINT uq_metodo_pago_nombre UNIQUE (nombre);

-- =====================================================
-- 9. PAGO
-- =====================================================
CREATE TABLE Pago (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_registro INT NOT NULL,
    id_metodo INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATETIME NOT NULL,
    id_empleado INT NOT NULL,
    FOREIGN KEY (id_registro) REFERENCES EntradaSalida(id_registro),
    FOREIGN KEY (id_metodo) REFERENCES MetodoPago(id_metodo),
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

-- =====================================================
-- 10. FACTURA
-- =====================================================
CREATE TABLE Factura (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_pago INT NOT NULL,
    numero_factura VARCHAR(20) NOT NULL UNIQUE,
    fecha_emision DATETIME NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pago) REFERENCES Pago(id_pago)
);

-- =====================================================
-- 11. MEMBRESIA
-- =====================================================
CREATE TABLE Membresia (
    id_membresia INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    tipo ENUM('Mensual','Trimestral','Anual') NOT NULL,
    descuento DECIMAL(5,2),
    estado ENUM('Activa','Vencida') DEFAULT 'Activa',
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- =====================================================
-- 12. INCIDENTE
-- =====================================================
CREATE TABLE Incidente (
    id_incidente INT AUTO_INCREMENT PRIMARY KEY,
    id_registro INT NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    fecha DATETIME NOT NULL,
    id_empleado INT,
    FOREIGN KEY (id_registro) REFERENCES EntradaSalida(id_registro),
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

-- =====================================================
-- 13. PROMOCION
-- =====================================================
CREATE TABLE Promocion (
    id_promocion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200),
    descuento DECIMAL(5,2) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL
);

-- =====================================================
-- 14. MULTA
-- =====================================================
CREATE TABLE Multa (
    id_multa INT AUTO_INCREMENT PRIMARY KEY,
    id_registro INT NOT NULL,
    motivo VARCHAR(150) NOT NULL,      -- Ej: pérdida de tiquete, exceso de tiempo
    valor DECIMAL(10,2) NOT NULL,
    fecha DATETIME NOT NULL,
    FOREIGN KEY (id_registro) REFERENCES EntradaSalida(id_registro)
);

-- =====================================================
-- 15. GASTO
-- =====================================================
CREATE TABLE Gasto (
    id_gasto INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(150) NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha DATE NOT NULL,
    id_empleado INT,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);


INSERT INTO cliente (nombre, documento, telefono, correo, direccion)
VALUES 
('Laura Gómez', '1003456789', '3124567890', 'laura.gomez@gmail.com', 'Cra 45 #12-34'),
('Carlos Pérez', '1009876543', '3109876543', 'carlos.perez@hotmail.com', 'Calle 10 #25-67');


-- PROCEDIMIENTOS ALMACENADOS

-- =====================================================
-- PROCEDIMIENTOS ALMACENADOS: CLIENTE
-- =====================================================

--  Insertar

DELIMITER $$
CREATE PROCEDURE proc_insert_clientes(
    IN p_nombre VARCHAR(100),
    IN p_documento VARCHAR(20),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100),
    IN p_direccion VARCHAR(100)
)
BEGIN
    INSERT INTO cliente (nombre, documento, telefono, correo, direccion)
    VALUES (p_nombre, p_documento, p_telefono, p_correo, p_direccion);
END$$


-- Actualizar

DELIMITER $$
CREATE PROCEDURE `proc_update_cliente_por_id`(
    IN p_id_cliente INT,
    IN p_nombre VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100),
    IN p_direccion VARCHAR(200)
)
BEGIN
    UPDATE cliente
    SET nombre = p_nombre,
        telefono = p_telefono,
        correo = p_correo,
        direccion = p_direccion
    WHERE id_cliente = p_id_cliente;
END$$

-- Eliminar
DELIMITER ;
CREATE PROCEDURE proc_delete_clientes(
    IN p_id_cliente INT
)
BEGIN
    DELETE FROM cliente WHERE id_cliente = p_id_cliente;
END$$


-- Consultar
CREATE PROCEDURE proc_select_clientes()
BEGIN
    SELECT id_cliente, nombre, documento, telefono, correo, direccion
    FROM cliente;
END$$

DELIMITER ;

-- =====================================================
-- PROCEDIMIENTOS ALMACENADOS: TIPO VECHIULO
-- =====================================================

-- Insertar
DELIMITER $$
CREATE PROCEDURE proc_insert_tipovehiculo(
    IN p_nombre VARCHAR(50),
    IN p_descripcion VARCHAR(100)
)
BEGIN
    INSERT INTO TipoVehiculo (nombre, descripcion)
    VALUES (p_nombre, p_descripcion);
END$$

-- Actualizar 
DELIMITER $$
CREATE PROCEDURE proc_update_tipovehiculo_por_id(
    IN p_id_tipo INT,
    IN p_nombre VARCHAR(50),
    IN p_descripcion VARCHAR(100)
)
BEGIN
    UPDATE TipoVehiculo
    SET nombre = p_nombre,
        descripcion = p_descripcion
    WHERE id_tipo = p_id_tipo;
END$$

-- Eliminar
DELIMITER $$
CREATE PROCEDURE proc_delete_tipovehiculo(
    IN p_id_tipo INT
)
BEGIN
    DELETE FROM TipoVehiculo WHERE id_tipo = p_id_tipo;
END$$

-- Consultar
DELIMITER $$
CREATE PROCEDURE proc_select_tipovehiculo()
BEGIN
    SELECT id_tipo, nombre, descripcion
    FROM TipoVehiculo;
END$$
DELIMITER ;



-- =====================================================
-- PROCEDIMIENTOS ALMACENADOS: VEHICULO
-- =====================================================

-- Insertar

DELIMITER $$

CREATE PROCEDURE proc_insert_vehiculo(
    IN p_placa VARCHAR(10),
    IN p_marca VARCHAR(50),
    IN p_color VARCHAR(30),
    IN p_id_tipo INT,
    IN p_id_cliente INT
)
BEGIN
    INSERT INTO Vehiculo (placa, marca, color, id_tipo, id_cliente)
    VALUES (p_placa, p_marca, p_color, p_id_tipo, p_id_cliente);
END$$

--DROP PROCEDURE IF EXISTS proc_update_vehiculo_por_id;

-- Actualizar
DELIMITER $$
CREATE PROCEDURE proc_update_vehiculo_por_id(
    IN p_id_vehiculo INT,
    IN p_placa VARCHAR(10),
    IN p_marca VARCHAR(50),
    IN p_color VARCHAR(30),
    IN p_id_tipo INT,
    IN p_id_cliente INT
)
BEGIN
    UPDATE Vehiculo
    SET placa = p_placa,
        marca = p_marca,
        color = p_color,
        id_tipo = p_id_tipo,
        id_cliente = p_id_cliente
    WHERE id_vehiculo = p_id_vehiculo;
END$$


-- Eliminar
DELIMITER $$
CREATE PROCEDURE proc_delete_vehiculo(
    IN p_id_vehiculo INT
)
BEGIN
    DELETE FROM Vehiculo WHERE id_vehiculo = p_id_vehiculo;
END$$


-- Consultar
DELIMITER $$
CREATE PROCEDURE proc_select_vehiculos()
BEGIN
    SELECT 
        v.id_vehiculo, 
        v.placa, 
        v.marca, 
        v.color, 
        v.id_tipo, 
        v.id_cliente
    FROM Vehiculo v;
END$$

-- ============================================
-- PROCEDIMIENTOS ALMACENADOS: EntradaSalida
-- ============================================

-- Insertar

DELIMITER $$

CREATE PROCEDURE proc_insert_registro(
    IN p_id_vehiculo INT,
    IN p_id_empleado INT,
    IN p_fecha_entrada DATETIME,
    IN p_espacio VARCHAR(20)
)
BEGIN
    INSERT INTO EntradaSalida (id_vehiculo, id_empleado, fecha_entrada, espacio)
    VALUES (p_id_vehiculo, p_id_empleado, p_fecha_entrada, p_espacio);
END$$

-- Actualizar

-- Eliminar procedimiento anterior si existe
DROP PROCEDURE IF EXISTS proc_update_salida;
DELIMITER $$

-- Actualizar fecha de salida
CREATE PROCEDURE proc_update_salida(
    IN p_id_registro INT,
    IN p_fecha_salida DATETIME
)
BEGIN
    UPDATE EntradaSalida
    SET fecha_salida = p_fecha_salida
    WHERE id_registro = p_id_registro;
END$$


DELIMITER $$
CREATE PROCEDURE proc_update_registro_por_id(
    IN p_id_registro INT,
    IN p_id_vehiculo INT,
    IN p_id_empleado INT,
    IN p_fecha_entrada DATETIME,
    IN p_fecha_salida DATETIME,
    IN p_espacio VARCHAR(20)
)
BEGIN
    UPDATE EntradaSalida
    SET id_vehiculo = p_id_vehiculo,
        id_empleado = p_id_empleado,
        fecha_entrada = p_fecha_entrada,
        fecha_salida = p_fecha_salida,
        espacio = p_espacio
    WHERE id_registro = p_id_registro;
END$$

-- Eliminar
DELIMITER $$
CREATE PROCEDURE proc_delete_registro(
    IN p_id_registro INT
)
BEGIN
    DELETE FROM EntradaSalida WHERE id_registro = p_id_registro;
END$$

-- Consultar todos
DELIMITER $$
CREATE PROCEDURE proc_select_registros()
BEGIN
    SELECT 
        r.id_registro,
        r.id_vehiculo,
        r.id_empleado,
        r.fecha_entrada,
        r.fecha_salida,
        r.espacio
    FROM EntradaSalida r;
END$$

-- Consultar registros activos (sin salida)
DELIMITER $$
CREATE PROCEDURE proc_select_registros_activos()
BEGIN
    SELECT 
        r.id_registro,
        r.id_vehiculo,
        r.fecha_entrada,
        r.espacio
    FROM EntradaSalida r
    WHERE r.fecha_salida IS NULL;
END$$


-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: ROL EMPLEADO
-- =============================================
-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_rol_empleado;
DROP PROCEDURE IF EXISTS proc_update_rol_empleado;
DROP PROCEDURE IF EXISTS proc_delete_rol_empleado;
DROP PROCEDURE IF EXISTS proc_select_rol_empleados;
DELIMITER $$

-- Insertar
CREATE PROCEDURE proc_insert_rol_empleado(
    IN p_nombre VARCHAR(50),
    IN p_descripcion VARCHAR(100)
)
BEGIN
    INSERT INTO RolEmpleado (nombre, descripcion)
    VALUES (p_nombre, p_descripcion);
END$$


-- Actualizar
CREATE PROCEDURE proc_update_rol_empleado(
    IN p_id_rol INT,
    IN p_nombre VARCHAR(50),
    IN p_descripcion VARCHAR(100)
)
BEGIN
    UPDATE RolEmpleado
    SET nombre = p_nombre,
        descripcion = p_descripcion
    WHERE id_rol = p_id_rol;
END$$


-- Eliminar
CREATE PROCEDURE proc_delete_rol_empleado(
    IN p_id_rol INT
)
BEGIN
    DELETE FROM RolEmpleado
    WHERE id_rol = p_id_rol;
END$$


-- Consultar
CREATE PROCEDURE proc_select_rol_empleados()
BEGIN
    SELECT 
        r.id_rol,
        r.nombre,
        r.descripcion
    FROM RolEmpleado r;
END$$

DELIMITER ;


-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: EMPLEADO
-- =============================================

-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_empleado;
DROP PROCEDURE IF EXISTS proc_update_empleado_por_id;
DROP PROCEDURE IF EXISTS proc_delete_empleado;
DROP PROCEDURE IF EXISTS proc_select_empleados;
DELIMITER $$

-- Insertar
CREATE PROCEDURE proc_insert_empleado(
    IN p_nombre VARCHAR(100),
    IN p_documento VARCHAR(20),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100),
    IN p_id_rol INT
)
BEGIN
    -- Verificar si el documento ya existe
    IF EXISTS (SELECT 1 FROM Empleado WHERE documento = p_documento) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El documento ya está registrado.';
    ELSE
        INSERT INTO Empleado (nombre, documento, telefono, correo, id_rol)
        VALUES (p_nombre, p_documento, p_telefono, p_correo, p_id_rol);
    END IF;
END$$


-- Actualizar
CREATE PROCEDURE proc_update_empleado_por_id(
    IN p_id_empleado INT,
    IN p_nombre VARCHAR(100),
    IN p_documento VARCHAR(20),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100),
    IN p_id_rol INT
)
BEGIN
    -- Verificar que exista el empleado
    IF NOT EXISTS (SELECT 1 FROM Empleado WHERE id_empleado = p_id_empleado) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El empleado no existe.';
    END IF;

    -- Verificar si el documento pertenece a otro empleado
    IF EXISTS (SELECT 1 FROM Empleado WHERE documento = p_documento AND id_empleado <> p_id_empleado) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El documento pertenece a otro empleado.';
    END IF;

    -- Actualizar datos
    UPDATE Empleado
    SET nombre = p_nombre,
        documento = p_documento,
        telefono = p_telefono,
        correo = p_correo,
        id_rol = p_id_rol
    WHERE id_empleado = p_id_empleado;
END$$


-- Eliminar
CREATE PROCEDURE proc_delete_empleado(
    IN p_id_empleado INT
)
BEGIN
    DELETE FROM Empleado
    WHERE id_empleado = p_id_empleado;
END$$


-- Consultar
CREATE PROCEDURE proc_select_empleados()
BEGIN
    SELECT 
        e.id_empleado,
        e.nombre,
        e.documento,
        e.telefono,
        e.correo,
        r.nombre AS rol
    FROM Empleado e
    INNER JOIN RolEmpleado r ON e.id_rol = r.id_rol;
END$$

DELIMITER ;



-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: METODO PAGO
-- =============================================
-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_metodo_pago;
DROP PROCEDURE IF EXISTS proc_update_metodo_pago;
DROP PROCEDURE IF EXISTS proc_delete_metodo_pago;
DROP PROCEDURE IF EXISTS proc_select_metodo_pagos;
DELIMITER $$

-- Insertar
CREATE PROCEDURE proc_insert_metodo_pago(
    IN p_nombre VARCHAR(50),
    IN p_descripcion VARCHAR(100)
)
BEGIN
    INSERT INTO MetodoPago (nombre, descripcion)
    VALUES (p_nombre, p_descripcion);
END$$


-- Actualizar
CREATE PROCEDURE proc_update_metodo_pago(
    IN p_id_metodo INT,
    IN p_nombre VARCHAR(50),
    IN p_descripcion VARCHAR(100)
)
BEGIN
    UPDATE MetodoPago
    SET nombre = p_nombre,
        descripcion = p_descripcion
    WHERE id_metodo = p_id_metodo;
END$$


-- Eliminar
CREATE PROCEDURE proc_delete_metodo_pago(
    IN p_id_metodo INT
)
BEGIN
    DELETE FROM MetodoPago
    WHERE id_metodo = p_id_metodo;
END$$


-- Consultar
CREATE PROCEDURE proc_select_metodo_pagos()
BEGIN
    SELECT 
        id_metodo,
        nombre,
        descripcion
    FROM MetodoPago;
END$$

DELIMITER ;

-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: PAGO
-- =============================================


-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_pago;
DROP PROCEDURE IF EXISTS proc_update_pago;
DROP PROCEDURE IF EXISTS proc_delete_pago;
DROP PROCEDURE IF EXISTS proc_select_pagos;
DELIMITER $$

-- Insertar
CREATE PROCEDURE proc_insert_pago(
    IN p_id_registro INT,
    IN p_id_metodo INT,
    IN p_monto DECIMAL(10,2),
    IN p_fecha_pago DATETIME,
    IN p_id_empleado INT
)
BEGIN
    INSERT INTO Pago (id_registro, id_metodo, monto, fecha_pago, id_empleado)
    VALUES (p_id_registro, p_id_metodo, p_monto, p_fecha_pago, p_id_empleado);
END$$


-- Actualizar
CREATE PROCEDURE proc_update_pago(
    IN p_id_pago INT,
    IN p_id_registro INT,
    IN p_id_metodo INT,
    IN p_monto DECIMAL(10,2),
    IN p_fecha_pago DATETIME,
    IN p_id_empleado INT
)
BEGIN
    UPDATE Pago
    SET id_registro = p_id_registro,
        id_metodo = p_id_metodo,
        monto = p_monto,
        fecha_pago = p_fecha_pago,
        id_empleado = p_id_empleado
    WHERE id_pago = p_id_pago;
END$$


-- Eliminar
CREATE PROCEDURE proc_delete_pago(
    IN p_id_pago INT
)
BEGIN
    DELETE FROM Pago
    WHERE id_pago = p_id_pago;
END$$


-- Consultar
CREATE PROCEDURE proc_select_pagos()
BEGIN
    SELECT 
        p.id_pago,
        p.id_registro,
        p.id_metodo,
        p.monto,
        p.fecha_pago,
        p.id_empleado
    FROM Pago p;
END$$

DELIMITER ;


-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: TIPO
-- =============================================


-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_tarifa;
DROP PROCEDURE IF EXISTS proc_update_tarifa;
DROP PROCEDURE IF EXISTS proc_delete_tarifa;
DROP PROCEDURE IF EXISTS proc_select_tarifas;

DELIMITER $$

-- Insertar
CREATE PROCEDURE proc_insert_tarifa(
    IN p_id_tipo INT,
    IN p_tipo_tarifa ENUM('Hora','Dia','Mes'),
    IN p_valor DECIMAL(10,2)
)
BEGIN
    INSERT INTO Tarifa (id_tipo, tipo_tarifa, valor)
    VALUES (p_id_tipo, p_tipo_tarifa, p_valor);
END$$

-- Actualizar
CREATE PROCEDURE proc_update_tarifa(
    IN p_id_tarifa INT,
    IN p_id_tipo INT,
    IN p_tipo_tarifa ENUM('Hora','Dia','Mes'),
    IN p_valor DECIMAL(10,2)
)
BEGIN
    UPDATE Tarifa
    SET id_tipo = p_id_tipo,
        tipo_tarifa = p_tipo_tarifa,
        valor = p_valor
    WHERE id_tarifa = p_id_tarifa;
END$$

-- Eliminar
CREATE PROCEDURE proc_delete_tarifa(
    IN p_id_tarifa INT
)
BEGIN
    DELETE FROM Tarifa
    WHERE id_tarifa = p_id_tarifa;
END$$

-- Consultar todas las tarifas
CREATE PROCEDURE proc_select_tarifas()
BEGIN
    SELECT 
        t.id_tarifa,
        t.id_tipo,
        t.tipo_tarifa,
        t.valor
    FROM Tarifa t;
END$$

DELIMITER ;

-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: INCIDENTE
-- =============================================

-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_incidente;
DROP PROCEDURE IF EXISTS proc_update_incidente;
DROP PROCEDURE IF EXISTS proc_delete_incidente;
DROP PROCEDURE IF EXISTS proc_select_incidentes;
DELIMITER $$

-- Insertar
CREATE PROCEDURE proc_insert_incidente(
    IN p_id_registro INT,
    IN p_descripcion VARCHAR(200),
    IN p_fecha DATETIME,
    IN p_id_empleado INT
)
BEGIN
    INSERT INTO Incidente (id_registro, descripcion, fecha, id_empleado)
    VALUES (p_id_registro, p_descripcion, p_fecha, p_id_empleado);
END$$

-- Actualizar
CREATE PROCEDURE proc_update_incidente(
    IN p_id_incidente INT,
    IN p_id_registro INT,
    IN p_descripcion VARCHAR(200),
    IN p_fecha DATETIME,
    IN p_id_empleado INT
)
BEGIN
    UPDATE Incidente
    SET id_registro = p_id_registro,
        descripcion = p_descripcion,
        fecha = p_fecha,
        id_empleado = p_id_empleado
    WHERE id_incidente = p_id_incidente;
END$$

-- Eliminar
CREATE PROCEDURE proc_delete_incidente(
    IN p_id_incidente INT
)
BEGIN
    DELETE FROM Incidente
    WHERE id_incidente = p_id_incidente;
END$$

-- Consultar
CREATE PROCEDURE proc_select_incidentes()
BEGIN
    SELECT 
        i.id_incidente,
        i.id_registro,
        i.descripcion,
        i.fecha,
        i.id_empleado
    FROM Incidente i;
END$$

DELIMITER ;

-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: PROMOCIONES
-- =============================================

-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_promocion;
DROP PROCEDURE IF EXISTS proc_update_promocion;
DROP PROCEDURE IF EXISTS proc_delete_promocion;
DROP PROCEDURE IF EXISTS proc_select_promociones;

DELIMITER $$

-- Insertar promoción
CREATE PROCEDURE proc_insert_promocion(
    IN p_nombre VARCHAR(100),
    IN p_descripcion VARCHAR(200),
    IN p_descuento DECIMAL(5,2),
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE
)
BEGIN
    INSERT INTO Promocion (nombre, descripcion, descuento, fecha_inicio, fecha_fin)
    VALUES (p_nombre, p_descripcion, p_descuento, p_fecha_inicio, p_fecha_fin);
END$$

-- Actualizar promoción
CREATE PROCEDURE proc_update_promocion(
    IN p_id_promocion INT,
    IN p_nombre VARCHAR(100),
    IN p_descripcion VARCHAR(200),
    IN p_descuento DECIMAL(5,2),
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE
)
BEGIN
    UPDATE Promocion
    SET nombre = p_nombre,
        descripcion = p_descripcion,
        descuento = p_descuento,
        fecha_inicio = p_fecha_inicio,
        fecha_fin = p_fecha_fin
    WHERE id_promocion = p_id_promocion;
END$$

-- Eliminar promoción
CREATE PROCEDURE proc_delete_promocion(
    IN p_id_promocion INT
)
BEGIN
    DELETE FROM Promocion
    WHERE id_promocion = p_id_promocion;
END$$

-- Consultar promociones
CREATE PROCEDURE proc_select_promociones()
BEGIN
    SELECT 
        id_promocion,
        nombre,
        descripcion,
        descuento,
        fecha_inicio,
        fecha_fin
    FROM Promocion;
END$$

DELIMITER ;


-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: MEMBRESIA
-- =============================================

-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_membresia;
DROP PROCEDURE IF EXISTS proc_update_membresia;
DROP PROCEDURE IF EXISTS proc_delete_membresia;
DROP PROCEDURE IF EXISTS proc_select_membresias;

DELIMITER $$

-- Insertar Membresía
CREATE PROCEDURE proc_insert_membresia(
    IN p_id_cliente INT,
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_tipo ENUM('Mensual','Trimestral','Anual'),
    IN p_descuento DECIMAL(5,2),
    IN p_estado ENUM('Activa','Vencida')
)
BEGIN
    INSERT INTO Membresia (id_cliente, fecha_inicio, fecha_fin, tipo, descuento, estado)
    VALUES (p_id_cliente, p_fecha_inicio, p_fecha_fin, p_tipo, p_descuento, p_estado);
END$$

-- Actualizar Membresía
CREATE PROCEDURE proc_update_membresia(
    IN p_id_membresia INT,
    IN p_id_cliente INT,
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_tipo ENUM('Mensual','Trimestral','Anual'),
    IN p_descuento DECIMAL(5,2),
    IN p_estado ENUM('Activa','Vencida')
)
BEGIN
    UPDATE Membresia
    SET id_cliente = p_id_cliente,
        fecha_inicio = p_fecha_inicio,
        fecha_fin = p_fecha_fin,
        tipo = p_tipo,
        descuento = p_descuento,
        estado = p_estado
    WHERE id_membresia = p_id_membresia;
END$$

-- Eliminar Membresía
CREATE PROCEDURE proc_delete_membresia(
    IN p_id_membresia INT
)
BEGIN
    DELETE FROM Membresia
    WHERE id_membresia = p_id_membresia;
END$$

-- Consultar todas las Membresías
CREATE PROCEDURE proc_select_membresias()
BEGIN
    SELECT 
        m.id_membresia,
        m.id_cliente,
        m.fecha_inicio,
        m.fecha_fin,
        m.tipo,
        m.descuento,
        m.estado
    FROM Membresia m;
END$$

DELIMITER ;

-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: MULTA
-- =============================================

-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_multa;
DROP PROCEDURE IF EXISTS proc_update_multa;
DROP PROCEDURE IF EXISTS proc_delete_multa;
DROP PROCEDURE IF EXISTS proc_select_multas;
DELIMITER $$

-- Insertar
CREATE PROCEDURE proc_insert_multa(
    IN p_id_registro INT,
    IN p_motivo VARCHAR(150),
    IN p_valor DECIMAL(10,2),
    IN p_fecha DATETIME
)
BEGIN
    INSERT INTO Multa (id_registro, motivo, valor, fecha)
    VALUES (p_id_registro, p_motivo, p_valor, p_fecha);
END$$

-- Actualizar
CREATE PROCEDURE proc_update_multa(
    IN p_id_multa INT,
    IN p_id_registro INT,
    IN p_motivo VARCHAR(150),
    IN p_valor DECIMAL(10,2),
    IN p_fecha DATETIME
)
BEGIN
    UPDATE Multa
    SET id_registro = p_id_registro,
        motivo = p_motivo,
        valor = p_valor,
        fecha = p_fecha
    WHERE id_multa = p_id_multa;
END$$

-- Eliminar
CREATE PROCEDURE proc_delete_multa(
    IN p_id_multa INT
)
BEGIN
    DELETE FROM Multa
    WHERE id_multa = p_id_multa;
END$$

-- Consultar
CREATE PROCEDURE proc_select_multas()
BEGIN
    SELECT 
        m.id_multa,
        m.id_registro,
        m.motivo,
        m.valor,
        m.fecha
    FROM Multa m;
END$$

DELIMITER ;


-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: FACTURA
-- =============================================

-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_factura;
DROP PROCEDURE IF EXISTS proc_update_factura;
DROP PROCEDURE IF EXISTS proc_delete_factura;
DROP PROCEDURE IF EXISTS proc_select_facturas;

DELIMITER $$

-- Insertar Factura
CREATE PROCEDURE proc_insert_factura(
    IN p_id_pago INT,
    IN p_numero_factura VARCHAR(20),
    IN p_fecha_emision DATETIME,
    IN p_total DECIMAL(10,2)
)
BEGIN
    INSERT INTO Factura (id_pago, numero_factura, fecha_emision, total)
    VALUES (p_id_pago, p_numero_factura, p_fecha_emision, p_total);
END$$

-- Actualizar Factura
CREATE PROCEDURE proc_update_factura(
    IN p_id_factura INT,
    IN p_id_pago INT,
    IN p_numero_factura VARCHAR(20),
    IN p_fecha_emision DATETIME,
    IN p_total DECIMAL(10,2)
)
BEGIN
    UPDATE Factura
    SET id_pago = p_id_pago,
        numero_factura = p_numero_factura,
        fecha_emision = p_fecha_emision,
        total = p_total
    WHERE id_factura = p_id_factura;
END$$

-- Eliminar Factura
CREATE PROCEDURE proc_delete_factura(
    IN p_id_factura INT
)
BEGIN
    DELETE FROM Factura
    WHERE id_factura = p_id_factura;
END$$

-- Consultar Facturas
CREATE PROCEDURE proc_select_facturas()
BEGIN
    SELECT 
        f.id_factura,
        f.id_pago,
        f.numero_factura,
        f.fecha_emision,
        f.total
    FROM Factura f;
END$$

DELIMITER ;

-- =============================================
-- PROCEDIMIENTOS ALMACENADOS: GASTO
-- =============================================

-- Eliminar procedimientos anteriores si existen
DROP PROCEDURE IF EXISTS proc_insert_gasto;
DROP PROCEDURE IF EXISTS proc_update_gasto;
DROP PROCEDURE IF EXISTS proc_delete_gasto;
DROP PROCEDURE IF EXISTS proc_select_gastos;

DELIMITER $$

-- Insertar
CREATE PROCEDURE proc_insert_gasto(
    IN p_descripcion VARCHAR(150),
    IN p_monto DECIMAL(10,2),
    IN p_fecha DATE,
    IN p_id_empleado INT
)
BEGIN
    INSERT INTO Gasto (descripcion, monto, fecha, id_empleado)
    VALUES (p_descripcion, p_monto, p_fecha, p_id_empleado);
END$$

-- Actualizar
CREATE PROCEDURE proc_update_gasto(
    IN p_id_gasto INT,
    IN p_descripcion VARCHAR(150),
    IN p_monto DECIMAL(10,2),
    IN p_fecha DATE,
    IN p_id_empleado INT
)
BEGIN
    UPDATE Gasto
    SET descripcion = p_descripcion,
        monto = p_monto,
        fecha = p_fecha,
        id_empleado = p_id_empleado
    WHERE id_gasto = p_id_gasto;
END$$

-- Eliminar
CREATE PROCEDURE proc_delete_gasto(
    IN p_id_gasto INT
)
BEGIN
    DELETE FROM Gasto
    WHERE id_gasto = p_id_gasto;
END$$

-- Consultar
CREATE PROCEDURE proc_select_gastos()
BEGIN
    SELECT id_gasto, descripcion, monto, fecha, id_empleado
    FROM Gasto;
END$$

DELIMITER ;
