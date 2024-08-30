# ------------------------------------------------- #
# Title: Assignment08
# # Description: Application for managing employee ratings
# ChangeLog: (Who, When, What)
# JWidner,21aug2024, Created Script, Moved classes into separate modules
# JWidner,26aug2024, adjusted for removed employee_type arguments
# ------------------------------------------------- #

try:
    if __name__ == "__main__":
        import processing_classes as proc
        import presentation_classes as pres
        from data_classes import Employee, FILE_NAME, employees, MENU
        import json
        from datetime import date
    else:
        raise Exception("This file starts the application and should not be imported.")
except Exception as e:
    print(e.__str__())

# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                            employee_data=employees,
                                                            employee_type=Employee)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees: object = pres.IO.input_employee_data(employee_data=employees, employee_type=Employee)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
