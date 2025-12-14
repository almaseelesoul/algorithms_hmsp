import heapq
import time

class GreedyQueues:

    @staticmethod
    def schedule_tasks_on_processors(tasks, num_processors, flag):
        """
        Asigna tareas a procesadores homogéneos usando un min-heap.
        Cada procesador se representa como (carga_actual, id_procesador).

        Parámetros:
        - task : tareas a procesar
        - num_processors = número de procesadores
        - flag : Bandera para indicar si se ordenan (True) o no (False) las tareas.
    
        Retorna:
        - asignaciones: lista de listas; asignaciones[i] contiene las tareas asignadas al procesador i
        - cargas: lista con la carga final de cada procesador
        - tiempo : duración de la ejecución del algoritmo en ms

        """
        # ------ Inicia el conteo de tiempo ------
        start_time = time.perf_counter()

        # Define si las tareas van ordenadas (LPT) o no (LS)
        if flag:
            # Ordenar tareas de mayor a menor duración para solución greedy 2 - LPT (Longest Processing Time)
            tasks_sorted = sorted(tasks, reverse=True)
        else:
            # Se deja las tareas como se generaron - List Scheduling 
            tasks_sorted=tasks
        
        #Este print se puso sólo para ver si quedaban ordenadas las tareas :P
        #print(">>>>> Tareas a procesar: ", tasks_sorted)
        

        ## >>>>>>>>>>>>>>>>>>>>>>>>>>> Inicialización de la Cola de Prioridades <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        # La cola almacenará tuplas: (carga_actual, indice_procesador)
        # Al inicio, todos los procesadores tienen carga 0.
        # El heap se ordena automáticamente por el primer elemento de la tupla (carga_actual).
        heap = [(0, id_proc) for id_proc in range(num_processors)]
        heapq.heapify(heap) # >>>>>>>>>>>>> Transforma una lista a min-heap


        # Estructura para guardar qué tareas se asignaron a qué procesador (para visualización)
        # Es una lista de listas.
        # Para almacenar qué tareas le tocan a cada procesador
        asignaciones = [[] for _ in range(num_processors)]


        for tarea in tasks_sorted:
            # Sacar el procesador menos cargado
            carga_actual, id_proc = heapq.heappop(heap) #>>>>>>>>>>>>> Devuelve el elemento más pequeño del heap
            # Asignar la tarea al procesador
            asignaciones[id_proc].append(tarea)
            nueva_carga = carga_actual + tarea

            # Volver a insertar el procesador con su carga actualizada
            heapq.heappush(heap, (nueva_carga, id_proc))

        # Al final, las cargas quedan en el heap
        cargas_finales = [0] * num_processors
        for carga_actual, id_proc in heap:
            cargas_finales[id_proc] = carga_actual


        # -------------- MAKESPAN -----------------------------
        max_makespan = max(cargas_finales)
        

        # ---- Fin: medir tiempo ----
        finish_time = time.perf_counter()
        tiempo_ejecucion = (finish_time - start_time)

        return asignaciones, cargas_finales, max_makespan, tiempo_ejecucion
