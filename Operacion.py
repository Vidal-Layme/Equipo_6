print("=== Operacion ===")
a = 12
b = 8
suma = a + b
print(f"La suma de {a} + {b} = {suma}")

integrantes = [
    {"nombre": "Mayra Fabiola Gutierrez Herrera", "CI": 13789973,},
    {"nombre": "Jhesica Laura Colque Huchani", "CI": 12768305,},
    {"nombre": "Vidal Layme Gonza", "CI": 13184148,},
    {"nombre": "Nils Reiner Aguilar Machicado", "CI": 13648810,},
]
print("=== Integrantes del Grupo ===")
for integrante in integrantes:
    print(f"Nombre: {integrante['nombre']}, CI: {integrante['CI']}")
