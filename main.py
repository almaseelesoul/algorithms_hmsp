import logging
import time
import datetime
from processing.processingdata import ProcesaDatos
from data.graphics import Grafica
from data.graphicclass import Graphics

def main():
    

    start_time = time.time()

    ########################################################################################
    #                        V A R I A B L E S 
    ########################################################################################

    #Número de repeticiones: 10
    repeticiones=5

    # Número de procesadores fijo = 10
    num_processors = 5

    # Número de tareas por instancia
    tamanio_tareas = [10, 20, 30, 40]
    #tamanio_tareas = [10, 20, 30, 40, 50, 60, 70]

    #Tipo de distribución de tareas que va a generar
    #distribucion="exponencial" 
    #distribucion="pareto"
    #distribucion="uniforme"
    distribucion="log-normal" 


    ########################################################################################
    
    marca_de_tiempo = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Declaración de logs
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s', # Para agregar fecha y hora automática: %(asctime)s 
        handlers=[
            logging.FileHandler("hmsp_"+distribucion+"_"+marca_de_tiempo+".log"),
            logging.StreamHandler()
        ]
    )

    logging.info(">>>> Propuestas de solución para 'Homogeneous Multiprocessor Scheduling Problem'<<<<")
    

    

    processing = ProcesaDatos()


    #Aquí se devielven los makespans finales y tiempos totales apra cada algoritmo
    # con su respectiva cantidad de tareas y para el número de repeticiones definido
    # mksps_g, t_g -> makespans y tiempos de Gurobi
    # mksps_ls, t_ls -> makespans y tiempos de List Scheduling (LS)
    # mksps_lpt, t_lpt -> makespan y tiempos de Longest Time Processing First (LTP)
    mksps_g, mksps_ls, mksps_lpt, t_g,  t_ls,  t_lpt = processing.Procesamiento(repeticiones, tamanio_tareas, num_processors, distribucion)

    
    logging.info("makespans_totales_gurobi")
    for fila_mg in mksps_g:
        logging.info(fila_mg)

    logging.info("makespans_totales_ls")
    for fila_mls in mksps_ls:
        logging.info(fila_mls)
    
    logging.info("makespans_totales_lpt")
    for fila_lpt in mksps_lpt:
        logging.info(fila_lpt)
    
    logging.info("tiempos_totales_gurobi")
    for fila_tg in t_g:
        logging.info(fila_tg)

    logging.info("tiempos_totales_ls")
    for fila_tls in t_ls:
        logging.info(fila_tls)

    logging.info("tiempos_totales_lpt")
    for fila_tlpt in t_lpt:
        logging.info(fila_tlpt)




    #Aquí se agrega la línea para graficar

    graficas=Grafica()
    graficas.procesar_informacion_makespan(mksps_g, mksps_ls, mksps_lpt, tamanio_tareas)
    graficas.procesar_informacion_tiempos(t_g,  t_ls,  t_lpt, tamanio_tareas)
    graficas.guardar_grafica(distribucion+"_"+marca_de_tiempo+".jpg")
        
    logging.info(">>>> FIN DE LA EJECUCIÓN <<<<")
    tf=time.time() - start_time
    logging.info(f"Tiempo total: {tf}")


if __name__ == "__main__":
    main()