import openpyxl

class ImportCSV:
    def read_excel_file(self, file_obj):
        try:
            workbook = openpyxl.load_workbook(file_obj, read_only=True)
            sheet = workbook.active
            print(sheet)
            rows = []
            for row in sheet.iter_rows(values_only=True):
                row_dict = {
                    header.value: cell_value for header, cell_value in zip(sheet[1], row)
                }
                rows.append(row_dict)
            return rows
        except Exception as e:
            # Handle exceptions or log the error as needed
            print(f"Error loading Excel file: {e}")
            return []
