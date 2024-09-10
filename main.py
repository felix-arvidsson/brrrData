from file_selection import single_file_selector, multi_file_selector
from data_processing.duplicate_handling import remove_duplicate_rows_in_excel, save_duplicate_rows_only, list_duplicates_in_excel
from data_processing.comparison import compare_columns_in_files_and_save
from data_processing.sorting import sort_excel_rows
from data_processing.modification import modify_column_in_excel
import inquirer

def select_menu():
    choices = [
        'Ta bort dubblett-rader', 
        'Behåll endast dubletter', 
        'Jämför kolumner mellan två filer', 
        'Lista dubletter i en fil', 
        "Sortera rader", 
        "Modifiera värden i column"
    ]
    questions = [
        inquirer.List('operation', message="Vilken operation vill du utföra?", choices=choices)
    ]
    answers = inquirer.prompt(questions)
    
    if answers:
        if answers['operation'] == choices[0]:
            remove_duplicate_rows_in_excel()
        elif answers['operation'] == choices[1]:
            save_duplicate_rows_only()
        elif answers['operation'] == choices[2]:
            compare_columns_in_files_and_save()
        elif answers['operation'] == choices[3]:
            list_duplicates_in_excel()
        elif answers['operation'] == choices[4]:
            sort_excel_rows()
        elif answers['operation'] == choices[5]:
            modify_column_in_excel()
    else:
        print("Ingen operation vald.")

if __name__ == "__main__":
    select_menu()
