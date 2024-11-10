import random

# Definizione delle città e della matrice dei costi
cities = ['A', 'D', 'B', 'C', 'E']
cost = {
    ('A', 'B'): 3,  ('A', 'C'): 4,  ('A', 'D'): 2,  ('A', 'E'): 7,
    ('B', 'A'): 3,  ('B', 'C'): 4,  ('B', 'D'): 6,  ('B', 'E'): 3,
    ('C', 'A'): 4,  ('C', 'B'): 4,  ('C', 'D'): 5,  ('C', 'E'): 8,
    ('D', 'A'): 2,  ('D', 'B'): 6,  ('D', 'C'): 5,  ('D', 'E'): 6,
    ('E', 'A'): 7,  ('E', 'B'): 3,  ('E', 'C'): 8,  ('E', 'D'): 6
}

# Funzione per calcolare il costo totale di un percorso
def calculate_route_cost(route):
    # Ignora l'arco finale che è da 'A' a 'A'
    return sum(cost[i, j] for i, j in zip(route, route[1:]) if i != 'A' or j != 'A')

# Funzione per applicare il 2-opt
def two_opt(route):
    best_route = route[:]
    best_cost = calculate_route_cost(best_route)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):  # Inizia dal secondo elemento, ignora 'A' all'inizio
            for j in range(i + 1, len(route) - 1):  # Ignora l'ultimo elemento (ritorno su 'A')
                if j - i == 1: continue  # Evita di scambiare archi adiacenti
                # Scambia i segmenti tra i e j
                new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
                new_cost = calculate_route_cost(new_route)
                # Se il nuovo percorso è migliore, aggiornalo
                if new_cost < best_cost:
                    best_route = new_route
                    best_cost = new_cost
                    improved = True
                    route = best_route
    return best_route, best_cost

# Funzione per creare un percorso casuale
def generate_random_route(cities):
    # Crea un percorso casuale senza includere 'A' (che verrà aggiunta successivamente)
    route = random.sample([city for city in cities if city != 'A'], len(cities) - 1)
    route.insert(0, 'A')  # Inserisce 'A' come primo elemento
    route.append('A')     # Inserisce 'A' come ultimo elemento
    return route

# Inizializzazione del percorso casuale
initial_route = generate_random_route(cities)
print("Percorso iniziale:", initial_route)
initial_cost = calculate_route_cost(initial_route)
print(f"Costo iniziale: {initial_cost}")

# Ottimizzazione del percorso con 2-opt
optimized_route, optimized_cost = two_opt(initial_route)

# Risultati finali
print("\nPercorso ottimizzato (dopo 2-opt):", optimized_route)
print(f"Costo ottimizzato: {optimized_cost}")
