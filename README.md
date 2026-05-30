# P10 - Gestor de Pedidos

## Problemas detectados
1. Lógica de descuento duplicada en `ver_pedidos()` y `calcular_total_desde_menu()`
2. `cambiar_estado_pedido()` es código muerto, definida pero nunca se llama
3. `nuevo_pedido()` mezcla validación, input y lógica de negocio en una sola función

## Refactorizaciones realizadas
| Problema | Refactorización | Archivo | Commit |
|---|---|---|---|
| Variable `l` poco clara | Renombrada a `linea` | pedidos.py | Mejora nombres de variables |
| While manual con contador | Sustituido por `for` con `enumerate()` | clientes.py | Simplifica listar_clientes: while manual -> enumerate |
| Diccionarios sin estructura | Refactorizado a clases (`Cliente`, `Pedido`, `LineaPedido`) | clientes.py, pedidos.py | Refactoriza a clases para pasar los tests del ejercicio 7 |
| Descuentos con if/elif fijo | Extraído a tabla de tramos configurable | pedidos.py | Refactoriza lógica de descuentos |

## Pruebas creadas
| Test | Qué comprueba |
|---|---|
| test_cliente_valido | Que un cliente con datos correctos es válido |
| test_cliente_con_email_invalido | Que un email sin @ se rechaza |
| test_validar_nombre_rechaza_vacio | Que un nombre vacío devuelve False |
| test_validar_email_correcto | Que un email con formato válido devuelve True |
| test_calcula_subtotal_linea | Que precio × cantidad da el subtotal correcto |
| test_calcula_total_lineas | Que suma correctamente varias líneas |
| test_aplica_descuento_del_10_por_ciento | Que aplica 10% a subtotales >= 100 |
| test_aplica_descuento_del_15_por_ciento | Que aplica 15% a subtotales >= 200 |
| test_total_final_pedido_con_descuento | Que el total del pedido aplica el descuento correctamente |
| test_no_permite_cantidad_cero | Que lanza ValueError si la cantidad es 0 |

## Analizador de código
Analizador usado: Ruff

Opciones configuradas:
1. `line-length = 100` — máximo de caracteres por línea
2. `select = ["E", "F", "W", "I"]` — errores, imports, warnings y orden de imports
3. `exclude = [".venv", "__pycache__"]` — ignora carpetas que no son código del proyecto

## Trabajo con Git y ramas
Rama creada: `refactor-descuentos`

Commits principales:
- Inicializa el proyecto base
- Mejora nombres de variables
- Simplifica listar_clientes: while manual -> enumerate
- Refactoriza a clases para pasar los tests del ejercicio 7
- Documenta clases y funciones principales
- Configura analizador de código y corrige errores Ruff
- Refactoriza lógica de descuentos
- Configura integración continua

Fusión realizada: `refactor-descuentos` → `main`

## Integración continua
Resultado del workflow: ✅ Pipeline en verde — ruff check y pytest pasan correctamente