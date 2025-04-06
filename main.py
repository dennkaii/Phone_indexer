import pandas as pd


def get_numeric_filter(column_name):
    print(f"\nFiltrar por {column_name}:")

    # Límites por columna (personaliza según tus necesidades)
    limits = {
        "Refresh Rate (Hz)": (60, 165),
        "Rating": (0, 5),
        "RAM (GB)": (4, 16),
        "Screen Size (inches)": (5, 7.5),
    }

    # Obtener límites si existen
    min_limit, max_limit = limits.get(column_name, (float("0"), float("inf")))

    while True:
        try:
            min_val = input(f"Mínimo (dejar vacío para {min_limit}): ")
            max_val = input(f"Máximo (dejar vacío para {max_limit}): ")

            # Manejar valores por defecto
            min_val = float(min_val) if min_val else min_limit
            max_val = float(max_val) if max_val else max_limit

            # Validar rangos
            if min_val < min_limit or max_val > max_limit:
                print(
                    f"Error: El rango permitido para {column_name} es {min_limit}-{max_limit}"
                )
                continue

            if min_val > max_val:
                print("Error: El mínimo no puede ser mayor al máximo")
                continue

            return min_val, max_val

        except ValueError:
            print("Error: Ingresa un número válido")


def get_categorical_filter(column_name, unique_values):
    print(f"\nValores disponibles para {column_name}: {', '.join(unique_values)}")
    selected = input(
        "Ingrese valores separados por comas (dejar vacío para omitir): "
    ).strip()
    if not selected:
        return None
    return [v.strip() for v in selected.split(",")]


def main():
    print("Bienvenido al buscador avanzado de teléfonos móviles")
    df = pd.read_csv("./mobile_phones_2000.csv")

    # Columnas disponibles para filtrar (EXCLUYENDO 'Model')
    filterable_columns = {
        "Brand": "categorical",
        "Price (USD)": "numeric",
        "Selling Platform": "categorical",
        "Rating": "numeric",
        "Refresh Rate (Hz)": "numeric",
        "Screen Size (inches)": "numeric",
        "RAM (GB)": "numeric",
        "Storage (GB)": "numeric",
        "Processor": "categorical",
        "Camera Setup": "categorical",
    }

    filtered_df = df.copy()

    while True:
        print("\nOpciones de filtrado disponibles:")
        for i, (col, col_type) in enumerate(filterable_columns.items(), 1):
            print(f"{i}. {col}")

        print("\n0. Aplicar filtros y mostrar resultados")
        print("-1. Salir")

        choice = input("\nSeleccione una opción para filtrar: ")

        if choice == "0":
            break
        if choice == "-1":
            return
        if not choice.isdigit() or int(choice) not in range(
            1, len(filterable_columns) + 1
        ):
            print("Opción inválida")
            continue

        col_name = list(filterable_columns.keys())[int(choice) - 1]
        col_type = filterable_columns[col_name]

        if col_type == "numeric":
            min_val, max_val = get_numeric_filter(col_name)
            filtered_df = filtered_df[
                (filtered_df[col_name] >= min_val) & (filtered_df[col_name] <= max_val)
            ]
        else:
            unique_vals = filtered_df[col_name].dropna().unique().astype(str)
            selected_vals = get_categorical_filter(col_name, unique_vals)
            if selected_vals:
                filtered_df = filtered_df[
                    filtered_df[col_name].astype(str).isin(selected_vals)
                ]

        print(f"\nRegistros restantes: {len(filtered_df)}")
        if len(filtered_df) == 0:
            print("No hay resultados con estos filtros. Reiniciando...")
            filtered_df = df.copy()
            continue

    # Mostrar resultados
    print("\nResultados filtrados:")
    print(f"Total de teléfonos encontrados: {len(filtered_df)}")

    if len(filtered_df) > 0:
        print("\nMarcas disponibles en resultados:")
        print(", ".join(filtered_df["Brand"].unique()))

        # Mostrar modelos solo en los resultados (no como filtro)
        columns_to_show = input(
            "\nIngrese columnas a mostrar (separadas por comas, vacío para todas): "
        )
        if columns_to_show.strip():
            columns_to_show = [c.strip() for c in columns_to_show.split(",")]
            valid_columns = [c for c in columns_to_show if c in filtered_df.columns]
            if valid_columns:
                print(filtered_df[valid_columns].to_string(index=False))
            else:
                print("No hay columnas válidas, mostrando todas")
                print(filtered_df.to_string(index=False))
        else:
            print(filtered_df.to_string(index=False))


if __name__ == "__main__":

    main()
