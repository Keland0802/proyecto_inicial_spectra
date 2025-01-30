-- Ver tipo de activdades
WITH main AS (
    SELECT *
    FROM tipo_actividades
)

SELECT *
FROM main
LIMIT 1;

SELECT * FROM usuarios WHERE cedula = '1113066428';

SELECT r.*, p.*
FROM registro_actividades r
JOIN planeacion_actividades p ON r.cedula_usu = p.cedula_usu
WHERE r.cedula_usu = '1113066428';

SELECT * FROM registro_actividades WHERE fecha BETWEEN '2025-01-01' AND '2025-01-30';

SELECT * FROM planeacion_actividades WHERE fecha BETWEEN '2025-01-01' AND '2025-01-30';

SELECT r.*, ta.nombre_tipo_actividad FROM registro_actividades r JOIN tipo_actividades ta ON r.actividad=ta.id_tipo_actividad;

SELECT 
    r.id_registro,
    r.cedula_usu,
    ta.nombre_tipo_actividad AS actividad,
    r.descripcion_act,
    r.num_proyecto,
    r.horas,
    r.fecha,
    r.comentario
    
FROM 
    registro_actividades r
LEFT JOIN 
    tipo_actividades ta 
ON 
    r.actividad = ta.id_tipo_actividad;


SELECT * FROM planeacion_actividades;


SELECT 
    p.id_planeacion,
    p.cedula_usu,
    ta.nombre_tipo_actividad AS actividad,
    p.descripcion_act,
    p.num_proyecto,
    p.horas,
    p.fecha,
    p.comentario
    
FROM 
    planeacion_actividades p
LEFT JOIN 
    tipo_actividades ta 
ON 
    p.actividad = ta.id_tipo_actividad;



SELECT COUNT(*) FROM planeacion_actividades;


SELECT 
    p.id_planeacion,
    p.cedula_usu,
    ta.nombre_tipo_actividad AS actividad,
    p.descripcion_act,
    p.num_proyecto,
    p.horas,
    p.fecha,
    p.comentario
    
FROM 
    planeacion_actividades p
LEFT JOIN 
    tipo_actividades ta 
ON 
    p.actividad = ta.id_tipo_actividad
WHERE p.cedula_usu=1113066428;



SELECT 
    r.id_registro,
    r.cedula_usu,
    ta.nombre_tipo_actividad AS actividad,
    r.descripcion_act,
    r.num_proyecto,
    r.horas,
    r.fecha,
    r.comentario
    
FROM 
    registro_actividades r
LEFT JOIN 
    tipo_actividades ta 
ON 
    r.actividad = ta.id_tipo_actividad
WHERE r.cedula_usu=1113066428;



SELECT * FROM registro_actividades WHERE fecha BETWEEN %s AND %s;



SELECT 
    p.id_planeacion,
    p.cedula_usu,
    ta.nombre_tipo_actividad AS actividad,
    p.descripcion_act,
    p.num_proyecto,
    p.horas,
    p.fecha,
    p.comentario
    
FROM 
    planeacion_actividades p
LEFT JOIN 
    tipo_actividades ta 
ON 
    p.actividad = ta.id_tipo_actividad
WHERE p.fecha BETWEEN '2025-01-01' AND '2025-01-25';



SELECT 
    r.id_registro,
    r.cedula_usu,
    ta.nombre_tipo_actividad AS actividad,
    r.descripcion_act,
    r.num_proyecto,
    r.horas,
    r.fecha,
    r.comentario
    
FROM 
    registro_actividades r
LEFT JOIN 
    tipo_actividades ta 
ON 
    r.actividad = ta.id_tipo_actividad
WHERE r.fecha BETWEEN '2025-01-01' AND '2025-01-30';