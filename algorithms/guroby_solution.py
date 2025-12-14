import gurobipy as gp
import time
from gurobipy import GRB


class GurobiSolution:

    @staticmethod
    def resolver_exacto_gurobi(num_procesadores, duraciones, tiempo_limite):
        """ Retorna (makespan, tiempo_ejecucion) """
        start_time = time.perf_counter()
        num_tareas = len(duraciones)
        
        modelo = gp.Model("P_Cmax")
        modelo.setParam('OutputFlag', 0) # Silenciar output para no llenar la consola
        modelo.setParam('TimeLimit', tiempo_limite)
        modelo.setParam('MIPGap', 0.0)

        x = modelo.addVars(num_procesadores, range(num_tareas), vtype=GRB.BINARY)
        Cmax = modelo.addVar(vtype=GRB.CONTINUOUS)
        modelo.setObjective(Cmax, GRB.MINIMIZE)

        # Restricciones
        for j in range(num_tareas):
            modelo.addConstr(gp.quicksum(x[i, j] for i in range(num_procesadores)) == 1)
        for i in range(num_procesadores):
            modelo.addConstr(gp.quicksum(duraciones[j] * x[i, j] for j in range(num_tareas)) <= Cmax)

        modelo.optimize()
        
        # Si no encuentra solución (por tiempo muy corto), retornamos infinito para evitar error
        if modelo.SolCount == 0:
            return float('inf'), time.perf_counter() - start_time
            
        return modelo.ObjVal, time.perf_counter() - start_time