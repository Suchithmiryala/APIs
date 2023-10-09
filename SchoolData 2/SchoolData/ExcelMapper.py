# excel_reader.py
import openpyxl

def evaluate_formula(cell):
    try:
        # Evaluate the formula and return the result
        return cell.value

    except Exception:
        # Return the formula itself if evaluation fails
        return f"Formula: {cell.formula}"

def read_excel_sheet(sheet_name, sheet_location):
    try:
        # Load the Excel workbook
        workbook = openpyxl.load_workbook(sheet_location, data_only=True)

        # Get the specified sheet
        sheet = workbook[sheet_name]

        # Get header row
        headers = [cell.value for cell in sheet[1]]

        # Initialize a list to store rows as dictionaries
        rows = []

        # Iterate through rows, starting from the second row (index 2)
        for row in sheet.iter_rows(min_row=2, values_only=False):
            row_dict = {headers[i]: evaluate_formula(cell) for i, cell in enumerate(row)}
            # Convert NaN-like values to None
            row_dict = {k: None if v == "nan" else v for k, v in row_dict.items()}
            rows.append(row_dict)

        # Convert list of rows to JSON
        json_data = rows

        return json_data

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
