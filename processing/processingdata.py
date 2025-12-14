import logging
import random
from data.datagenerator import GeneradorTareas
from algorithms.greedy_priority_queues import GreedyQueues
from algorithms.guroby_solution import GurobiSolution


class ProcesaDatos:
    
    #Esto lo vamos a usar para graficar
    def __init__(self):
        # Aquí se define la "memoria" del objeto.
        # Creamos una lista vacía que pertenecerá a la instancia.
        self.resultados_guardados = []


    def Procesamiento(self, repeticiones, tamanio_tareas, num_processors, distribution):

        master_makespan_gurobi = []
        master_makespan_ls = []
        master_makespan_lpt = []
        
        master_tiempo_gurobi = []
        master_tiempo_ls = []
        master_tiempo_lpt = []

        #Aquí va el for de las 10 instancias
        for i in range(len(tamanio_tareas)):

            # Genera las instancias:
            gen = GeneradorTareas()
            media_duracion=10

            sub_makespans_ls=[]
            sub_makespans_lpt=[]
            sub_makespans_gurobi=[]
            sub_times_ls=[]
            sub_times_lpt=[]
            sub_times_gurobi=[]

            for r in range(repeticiones):

                print(">>>>>>>>>>>>>>>> Repetición: ",r)
                
                tasks = gen.generar_instancia( tamanio_tareas[i], media_duracion, random.random(), distribution)

                #logging.info(f">>>>>>>>>>>>>  Instancia a procesar: {tasks}")

                # >>>>>>>>>>>>>>> LIST SCHEDULING
                asignaciones_ls, cargas_ls, makespan_ls, tiempo_ls = GreedyQueues.schedule_tasks_on_processors(tasks, num_processors, flag=False)
                logging.info(f"\n >>> List Scheduling para instancia de {tamanio_tareas[i]} tareas | Repetición {r} <<<")
                
                logging.info(f">>> LS Makespan: {makespan_ls}")
                
                logging.info(f">>> LS Tiempo de ejecución: {tiempo_ls:.5f} s")


                # >>>>>>>>>>>>>>>>< LONGEST PROCESSING TIME FIRST
                asignaciones_lpt, cargas_lpt, makespan_lpt, tiempo_lpt = GreedyQueues.schedule_tasks_on_processors(tasks, num_processors, flag=True)
                logging.info(f"\n >>> Longest Processing Time First para instancia de {tamanio_tareas[i]} tareas  | Repetición {r} <<<")
                
                logging.info(f">>> LPT Makespan: {makespan_lpt}")
                
                logging.info(f">>> LPT Tiempo de ejecución: {tiempo_lpt:.5f} s")
        

                # >>>>>>>>>>>>>>>>< GUROBI EXACTA
                tiempo_limite=40
                makespan_gurobi, tiempo_gurobi = GurobiSolution.resolver_exacto_gurobi(num_processors, tasks, tiempo_limite)
                logging.info(f"\n >>> Gurobi para instancia de {tamanio_tareas[i]} tareas  | Repetición {r} <<<")
                logging.info(f">>> Gurobi Makespan: {makespan_gurobi:.5f}")
                logging.info(f">>> Gurobi Times: {tiempo_gurobi:.5f} s")

                sub_makespans_ls.append(makespan_ls)
                sub_makespans_lpt.append(makespan_lpt)
                sub_makespans_gurobi.append(makespan_gurobi)
                sub_times_ls.append(tiempo_ls)
                sub_times_lpt.append(tiempo_lpt)
                sub_times_gurobi.append(tiempo_gurobi)

            logging.info(f"sub_makespans_ls para {tamanio_tareas[i]} tareas en la repetición {r}: {sub_makespans_ls}")
            logging.info(f"sub_makespans_lpt para {tamanio_tareas[i]} tareas en la repetición {r}: {sub_makespans_lpt}")
            logging.info(f"sub_makespans_gurobi para {tamanio_tareas[i]} tareas en la repetición {r}: {sub_makespans_gurobi}")
            logging.info(f"sub_times_ls para {tamanio_tareas[i]} tareas en la repetición {r}: {sub_times_ls}")
            logging.info(f"sub_times_lpt para {tamanio_tareas[i]} tareas en la repetición {r}: {sub_times_lpt}")
            logging.info(f"sub_times_gurobi para {tamanio_tareas[i]} tareas en la repetición {r}: {sub_times_gurobi}")   
            
            
            master_makespan_gurobi.append(sub_makespans_gurobi)
            master_makespan_ls.append(sub_makespans_ls)
            master_makespan_lpt.append(sub_makespans_lpt)
            
            master_tiempo_gurobi.append(sub_times_gurobi)
            master_tiempo_ls.append(sub_times_ls)
            master_tiempo_lpt.append(sub_times_lpt)

        
        return master_makespan_gurobi, master_makespan_ls, master_makespan_lpt, master_tiempo_gurobi, master_tiempo_ls, master_tiempo_lpt

    def graficar():
        pass