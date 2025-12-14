import matplotlib.pyplot as plt
import numpy as np

class Graphics:

    @staticmethod
    def graficar_resultados(x_vals, r_g1, r_g2, t_ex, t_g1, t_g2):
    
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
        plt.savefig("grafica_calidad.png")
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
        plt.savefig("grafica_tiempos.png")
        plt.show()

