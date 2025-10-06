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


-- Procedimiento almacenados

-- Para cliente: 

-- Select
DELIMITER $$
CREATE PROCEDURE proc_select_clientes()
BEGIN
    SELECT 
        id_cliente,
        nombre,
        documento,
        telefono,
        correo,
        direccion
    FROM Cliente;
END$$
DELIMITER ;

--------
-- PROCEDIMIENTOS PARA CLIENTE

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
CREATE PROCEDURE proc_update_clientes(
    IN p_id_cliente INT,
    IN p_nombre VARCHAR(100),
    IN p_documento VARCHAR(20),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100),
    IN p_direccion VARCHAR(100)
)
BEGIN
    UPDATE cliente
    SET nombre = p_nombre,
        documento = p_documento,
        telefono = p_telefono,
        correo = p_correo,
        direccion = p_direccion
    WHERE id_cliente = p_id_cliente;
END$$


-- Eliminar
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
