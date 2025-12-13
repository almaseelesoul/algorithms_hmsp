import numpy as np
import matplotlib.pyplot as plt
import numpy as np

class Grafica:
    def __init__(self):
        self.n_tareas_list=[50,100,200,400]
        self.inicializar_variablesMakespan()
        self.inicializar_variablesTemporales()
        self.fig, self.ax = plt.subplots(2)
        
    def inicializar_variablesMakespan(self):
        self.makespan={}
        self.makespan["GOROBI"]={}
        self.makespan["GREEDY1"]={}
        self.makespan["GREEDY2"]={}

        self.medias_gurobi=[]
        self.medias_greedy1=[]
        self.medias_greedy2=[]

        self.y_err_greedy1 = []
        self.y_err_greedy2 = []

    def procesar_informacion_makespan(self,makespan_gurobi,makespan_greedy1,makespan_greedy2,n_tareas_list=[50,100,200,400]):
        self.n_tareas_list=n_tareas_list
        for i,n_tareas in enumerate(self.n_tareas_list):
            self.makespan["GOROBI"][n_tareas]=makespan_gurobi[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS 
            self.makespan["GREEDY1"][n_tareas]=makespan_greedy1[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS
            self.makespan["GREEDY2"][n_tareas]=makespan_greedy2[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS

            #NORMALIZACIÓN

            self.makespan["GREEDY1"][n_tareas]=np.array(self.makespan["GREEDY1"][n_tareas])/np.array(self.makespan["GOROBI"][n_tareas]) 
            self.makespan["GREEDY2"][n_tareas]=np.array(self.makespan["GREEDY2"][n_tareas])/np.array(self.makespan["GOROBI"][n_tareas])
            self.makespan["GOROBI"][n_tareas]=np.array(self.makespan["GOROBI"][n_tareas])/np.array(self.makespan["GOROBI"][n_tareas]) 
            #GENERACION DE PUNTOS EN LA RECTA

            self.medias_gurobi.append(np.array(self.makespan["GOROBI"][n_tareas]).mean())
            self.medias_greedy1.append(np.array(self.makespan["GREEDY1"][n_tareas]).mean())
            self.medias_greedy2.append(np.array(self.makespan["GREEDY2"][n_tareas]).mean())
            self.y_err_greedy1.append(1.96*np.array(self.makespan["GREEDY1"][n_tareas]).std())
            self.y_err_greedy2.append(1.96*np.array(self.makespan["GREEDY2"][n_tareas]).std())
        self.graficar_makespans()
    
    #self.medias_gurobi=[1,1,1,1]
    #self.medias_greedy1=[1.2,1.3,1.1,1.4]
    #self.medias_greedy2=[1.6,1.4,1.8,1.7]

    #y_err_greedy1 = [0.03,0.06,0.04,0.07]
    #y_err_greedy2 = [0.05,0.03,0.02,0.03]

    def graficar_makespans(self):
        self.ax[0].set_title("Makespans")
        self.ax[0].plot(self.n_tareas_list,self.medias_gurobi,'b-',linewidth=2)
        self.ax[0].plot(self.n_tareas_list,self.medias_greedy1,'r-',linewidth=2)
        self.ax[0].plot(self.n_tareas_list,self.medias_greedy2,'g-',linewidth=2)
        self.ax[0].plot(self.n_tareas_list,4*[1.5],'c--')
        self.ax[0].plot(self.n_tareas_list,4*[2],'y--')
        self.ax[0].errorbar(self.n_tareas_list,self.medias_greedy1,self.y_err_greedy1,fmt='r-o',capsize=3)
        self.ax[0].errorbar(self.n_tareas_list,self.medias_greedy2,self.y_err_greedy2,fmt='g-o',capsize=3)
        self.ax[0].set_xlabel("Cantidad de tareas")
        self.ax[0].set_ylabel("Makespans(ms)")
        self.ax[0].legend(["Gurobi","List Scheduling","Longest Time Processing First"])

    def inicializar_variablesTemporales(self):
        self.tiempos={}
        self.tiempos["GOROBI"]={}
        self.tiempos["GREEDY1"]={}
        self.tiempos["GREEDY2"]={}

        self.medias_tiempos_gurobi=[]
        self.medias_tiempos_greedy1=[]
        self.medias_tiempos_greedy2=[]

        self.y_err_tiempos_greedy1 = []
        self.y_err_tiempos_greedy2 = []

    def procesar_informacion_tiempos(self,tiempos_gurobi,tiempos_greedy1,tiempos_greedy2,n_tareas_list=[50,100,200,400]):
        self.n_tareas_list=n_tareas_list
        for i,n_tareas in enumerate(self.n_tareas_list):
            self.tiempos["GOROBI"][n_tareas]=tiempos_gurobi[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS 
            self.tiempos["GREEDY1"][n_tareas]=tiempos_greedy1[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS
            self.tiempos["GREEDY2"][n_tareas]=tiempos_greedy2[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS

            #NORMALIZACIÓN
            #self.tiempos["GOROBI"][n_tareas]=np.array(self.tiempos["GOROBI"][n_tareas])/np.array(self.tiempos["GOROBI"][n_tareas]) 
            #self.tiempos["GREEDY1"][n_tareas]=np.array(self.tiempos["GREEDY1"][n_tareas])/np.array(self.tiempos["GOROBI"][n_tareas]) 
            #self.tiempos["GREEDY2"][n_tareas]=np.array(self.tiempos["GREEDY2"][n_tareas])/np.array(self.tiempos["GOROBI"][n_tareas])

            #GENERACION DE PUNTOS EN LA RECTA

            self.medias_tiempos_gurobi.append(np.array(self.tiempos["GOROBI"][n_tareas]).mean())
            self.medias_tiempos_greedy1.append(np.array(self.tiempos["GREEDY1"][n_tareas]).mean())
            self.medias_tiempos_greedy2.append(np.array(self.tiempos["GREEDY2"][n_tareas]).mean())
            self.y_err_tiempos_greedy1.append(1.96*np.array(self.tiempos["GREEDY1"][n_tareas]).std())
            self.y_err_tiempos_greedy2.append(1.96*np.array(self.tiempos["GREEDY2"][n_tareas]).std())
        self.graficar_tiempos()

    #self.medias_gurobi=[1,1,1,1]
    #self.medias_greedy1=[1.2,1.3,1.1,1.4]
    #self.medias_greedy2=[1.6,1.4,1.8,1.7]

    #y_err_greedy1 = [0.03,0.06,0.04,0.07]
    #y_err_greedy2 = [0.05,0.03,0.02,0.03]

    def graficar_tiempos(self):
        self.ax[1].set_title("Tiempos de ejecución")
        self.ax[1].plot(self.n_tareas_list,self.medias_tiempos_gurobi,'b-o',linewidth=2)
        self.ax[1].plot(self.n_tareas_list,self.medias_tiempos_greedy1,'r-o',linewidth=2)
        self.ax[1].plot(self.n_tareas_list,self.medias_tiempos_greedy2,'g-o',linewidth=2)
        self.ax[1].legend(["Gurobi","List Scheduling","Longest Time Processing First"])
        self.ax[1].set_xlabel("Cantidad de tareas")
        self.ax[1].set_ylabel("Tiempo de procesamiento(ms)")
        self.fig.tight_layout(rect=[0, 0, 1, 0.95])
        self.fig.set_size_inches(8, 6)
        self.fig.suptitle("Metricas metricosas XD\n", fontsize=24,fontfamily="serif",)
        plt.show()
    def guardar_grafica(self,nombre_figura):
        self.fig.savefig(nombre_figura)