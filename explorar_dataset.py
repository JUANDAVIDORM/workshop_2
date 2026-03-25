from datasets import load_dataset
import numpy as np

print("Cargando dataset...")
dataset = load_dataset('YominE/Muscle_Fatigue_Cycling')
train_data = dataset['train']

print("\n" + "="*70)
print("INFORMACIÓN DEL DATASET")
print("="*70)
print(f"Total de muestras: {len(train_data)}")
print(f"\nNombres de columnas: {train_data.column_names}")

print("\n" + "="*70)
print("TIPOS DE DATOS")
print("="*70)
print(train_data.features)

print("\n" + "="*70)
print("PRIMERAS 3 MUESTRAS")
print("="*70)
for i in range(min(3, len(train_data))):
    muestra = train_data[i]
    print(f"\n--- Muestra {i} ---")
    for col, val in muestra.items():
        if isinstance(val, list):
            print(f"{col}: {val[:10]}... (lista de {len(val)} elementos)")
        else:
            print(f"{col}: {val}")

print("\n" + "="*70)
print("ANÁLISIS DE COLUMNAS IMPORTANTES")
print("="*70)
for col in train_data.column_names:
    col_lower = col.lower()
    if any(x in col_lower for x in ['label', 'target', 'class', 'estado', 'condition', 'fatigue']):
        # Obtener valores únicos
        valores = [train_data[i][col] for i in range(min(100, len(train_data)))]
        unique_vals = set(valores)
        print(f"\n{col}:")
        print(f"  Valores únicos: {sorted(unique_vals)}")
        print(f"  Rango: {min(valores)} a {max(valores)}")
