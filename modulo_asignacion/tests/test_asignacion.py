import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from modulo_asignacion.asignacion import asignar_tarea

def test_asignar_tarea():
    tarea = asignar_tarea("Nick", "Implementar backend", 5, "2025-08-10", "Alta")
    assert tarea["usuario"] == "Nick"
    assert tarea["tiempo_estimado"] == 5
    assert tarea["prioridad"] == "Alta"
