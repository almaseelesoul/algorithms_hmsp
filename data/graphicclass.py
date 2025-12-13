import matplotlib.pyplot as plt
import numpy as np

class Graphics:

    @staticmethod
    def graficar_resultados(x_vals, m_g, m_ls, m_lpt, t_g, t_lg, t_lpt):

        
        
        # --- GRÁFICA 1: CALIDAD DE LA SOLUCIÓN (NORMALIZADA) ---
        plt.figure(figsize=(10, 6))
        
        # Linea base óptima (y=1)
        plt.axhline(y=1.0, color='black', linestyle='--', label='Solución Exacta (Óptimo)')
        
        # Curvas Greedy
        plt.plot(x_vals, r_g1, marker='o', label='Greedy 1: List Scheduling (Sin Orden)', color='red')
        plt.plot(x_vals, r_g2, marker='s', label='Greedy 2: LPT (Ordenado)', color='green')
        
        plt.title("Calidad de la Solución (Normalizada respecto al Óptimo)")
        plt.xlabel("Número de Tareas")
        plt.ylabel("Ratio de Aproximación (Greedy / Óptimo)")
        plt.legend()
        plt.grid(True)
        plt.ylim(0.9, 2.1) # Ajustar límites para ver bien el rango 1 a 2
        plt.savefig("grafica_calidad_01.png")
        plt.show()

        # --- GRÁFICA 2: TIEMPO DE EJECUCIÓN ---
        plt.figure(figsize=(10, 6))
        
        plt.plot(x_vals, t_ex, marker='o', label='Exacto (Gurobi - MILP)', color='blue')
        plt.plot(x_vals, t_g1, marker='^', label='Greedy 1', color='red')
        plt.plot(x_vals, t_g2, marker='v', label='Greedy 2', color='green')
        
        plt.title("Comparativa de Tiempo de Ejecución")
        plt.xlabel("Número de Tareas")
        plt.ylabel("Tiempo Promedio (segundos)")
        plt.yscale('log') # <--- IMPORTANTE: Escala logarítmica porque Gurobi es muy lento comparado a Greedy
        plt.legend()
        plt.grid(True, which="both", ls="-")
        plt.savefig("grafica_tiempos_01.png")
        plt.show()
    

    '''def promedios():
        if obj_exact > 0:
                sum_ratio_g1 += (obj_g1 / obj_exact)
                sum_ratio_g2 += (obj_g2 / obj_exact)
            else:
                sum_ratio_g1 += 1
                sum_ratio_g2 += 1
                
            sum_time_exact += t_exact
            sum_time_g1 += t_g1
            sum_time_g2 += t_g2

        # Guardar promedios de este tamaño n
        avg_ratios_g1.append(sum_ratio_g1 / REPETICIONES)
        avg_ratios_g2.append(sum_ratio_g2 / REPETICIONES)
        
        avg_times_exact.append(sum_time_exact / REPETICIONES)
        avg_times_g1.append(sum_time_g1 / REPETICIONES)
        avg_times_g2.append(sum_time_g2 / REPETICIONES)'''