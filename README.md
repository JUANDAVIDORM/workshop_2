# Workshop 2: Machine Learning & Deep Learning Aplicado

**Universidad EAFIT - Introducción a la Inteligencia Artificial (2026-01)**

## Descripción del Proyecto

Este proyecto completo aborda **dos problemas de aprendizaje supervisado** usando técnicas  de Machine Learning y Deep Learning:

### 1️⃣ Clasificación: Detección de Fatiga Muscular en Ciclismo

**Objetivo:** Detectar si un ciclista está en condición normal o tiene desgaste muscular usando señales EMG

**Dataset:** Muscle Fatigue Cycling (HuggingFace)
- 8 señales de electromiografía a 1000 Hz
- 2 clases: Normal (0) vs Fatiga (1)

**Técnica:** 
- Feature Engineering: Ventanas de 1 segundo con características de tiempo y frecuencia
- Modelos: kNN, Decision Tree, Random Forest, Gradient Boosting, DNN
- Métrica principal: Accuracy, Precision, Recall, F1-Score

📁 **Archivo:** `clasificacion/clasificacion.ipynb`

---

### 2️⃣ Regresión: Estimación de Edad desde Imágenes Faciales  

**Objetivo:** Predecir la edad exacta de una persona analizando su fotografía

**Dataset:** Faces Age Detection (Kaggle)
- Imágenes de caras de 128x128 píxeles
- Target: Edad (valor continuo entre 18-80 años)

**Técnica:**
- Modelo: CNN (Red Neuronal Convolucional)
- Arquitectura: 3 bloques convolucionales + capas densas + regularización
- Métrica principal: MAE, RMSE, R²

📁 **Archivo:** `regresion/regresion.ipynb`

---

## 📊 Estructura del Repositorio

```
workshop_2/
├── README.md                    ← Este archivo
├── clasificacion/
│   └── clasificacion.ipynb      ← Problema de CLASIFICACIÓN
├── regresion/
│   └── regresion.ipynb          ← Problema de REGRESIÓN
└── datasets/                    ← (Opcional) Datos descargados
```

---

## 🚀 Cómo Usar Este Proyecto

### Opción 1: En Google Colab (Recomendado - Sin instalación local)

1. Sube los notebooks a Google Colab
2. Instala las librerías necesarias (Colab ya trae la mayoría)
3. Ejecuta celda por celda

### Opción 2: Localmente en tu computadora

**Requisitos previos:**
- Python 3.8+
- Jupyter Notebook
- pip (gestor de paquetes)

**Instalación:**

```bash
# 1. Clonar o descargar el repositorio
git clone https://github.com/tuusuario/workshop_2
cd workshop_2

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

**Ejecutar los notebooks:**

```bash
jupyter notebook
```

Luego abre cualquiera de los archivos `.ipynb` en tu navegador.

---

## 📚 Conceptos Clave Aprendidos

### En Clasificación:
- ✅ Feature Engineering desde señales
- ✅ Análisis de balance de clases
- ✅ Comparación sistemática de modelos
- ✅ Detección de Overfitting/Underfitting
- ✅ Redes Neuronales Profundas para clasificación

### En Regresión:
- ✅ Problemas de regresión vs clasificación
- ✅ CNN para análisis de imágenes
- ✅ Data Augmentation
- ✅ Métricas de regresión (MAE, RMSE, R²)
- ✅ Validación en problemas continuos

---

## 📊 Resultados Esperados

Después de ejecutar los notebooks verás:

**Clasificación:**
- Tabla comparativa de 5 modelos
- Matrices de confusión
- Curvas de aprendizaje
- Análisis de características importantes
- Pruebas con datos artificiales

**Regresión:**
- Curvas de pérdida del entrenamiento
- Gráficos de predicciones vs reales
- Análisis de residuales
- Predicciones en imágenes de test

---

## 🔧 Tecnologías Utilizadas

- **Python 3**: Lenguaje principal
- **NumPy & Pandas**: Manipulación de datos
- **Matplotlib & Seaborn**: Visualizaciones
- **Scikit-Learn**: Modelos de ML clásicos
- **TensorFlow/Keras**: Deep Learning
- **OpenCV**: Procesamiento de imágenes

---

## 💡 Conclusiones y Aprendizajes

1. **La ingeniería de características es clave** en problemas con datos no estructurados
2. **No siempre el modelo más complejo es el mejor** (comparar siempre)
3. **El análisis exploratorio previo es fundamental** para entender nuestros datos
4. **La validación adecuada previene overfitting** (train/val/test)
5. **Las CNNs dominan en problemas de visión** (imágenes)

---

## 👥 Autores

Equipo de Workshop 2 - EAFIT 2026

---

## 📝 Notas Importantes  

- **Datos sintéticos en demostración**: Los notebooks usan datos simplic ados para correr rápido. En la solución final, reemplaza con datos reales de Kaggle y HuggingFace.
- **Requisitos computacionales**: La CNN puede entrenar en CPU pero es mucho más rápida con GPU
- **Tiempo de ejecución**: 5-15 minutos en promedio por notebook

---

**¡Éxito con tu sustentación! 🎓**