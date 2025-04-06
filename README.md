# BUSCADOR DE TELEFONOS MOVILES

---

## Caracteristicas principales

---
- **Filtrado multicriterio** por 10+ parámetros técnicos
- **Validación automática** de rangos técnicos
- **Interfaz intuitiva** con menú interactivo

## Columnas Disponibles
---

| Parámetro                | Tipo       | Filtrable | Validación                     | Ejemplo Válido |
| ------------------------ | ---------- | --------- | ------------------------------ | -------------- |
| **Brand**                | Categórico | ✅ Sí     | Valores únicos del dataset     | Samsung, Apple |
| **Price (USD)**          | Numérico   | ✅ Sí     | > 0                            | 300-800        |
| **Model**                | Texto      | ❌ No     | -                              | iPhone 13 Pro  |
| **Selling Platform**     | Categórico | ✅ Sí     | [Amazon, eBay, Official Store] | Amazon         |
| **Rating**               | Numérico   | ✅ Sí     | 0 ≤ x ≤ 5                      | 4.2            |
| **Refresh Rate (Hz)**    | Numérico   | ✅ Sí     | 90 ≤ x ≤ 164                   | 120            |
| **Screen Size (inches)** | Numérico   | ✅ Sí     | 4.0 ≤ x ≤ 7.5                  | 6.4            |
| **RAM (GB)**             | Numérico   | ✅ Sí     | 1 ≤ x ≤ 24                     | 8              |
| **Storage (GB)**         | Numérico   | ✅ Sí     | 32 ≤ x ≤ 1024                  | 256            |
| **Processor**            | Categórico | ✅ Sí     | Valores únicos del dataset     | Snapdragon 888 |
| **Camera Setup**         | Categórico | ✅ Sí     | Valores únicos del dataset     | Triple 64MP    |

## install

---
`nix`: Sigue las instrucciones de [`devenv`](https://devenv.sh/getting-started/)
`otros`: Instala `panda` y una version
relativamente nueva de `python`

## Uso Basico
---

```python
python main.py
```
