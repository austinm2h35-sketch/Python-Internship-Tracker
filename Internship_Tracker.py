###Title: Internship Application Tracker
###Date: 16 October 2025
###Author: Austin Heitzman
###Notes: This app allows for easy tracking of applications sent out, as well as
###       interview details that come from them

#Import libraries
import pandas as pd

#Read files
df1 = pd.read_csv('Internship_Apps.csv')
df2 = pd.read_csv('Interview_Notes.csv')

#Get password
def get_password():
    print()
    print("#PasswordForApplications#")
    print()
    return

#Add to file
def add_to_file(df, file_code):
    print()
    #Application list
    if file_code == 1:
        company_name = input("Enter company name: ")
        date_applied = input("Enter date applied (mm/dd): ")
        job_found = input("Where did you find the job? ")
        position = input("Enter job type: ")
        app_notes = input("Enter notes: ")
        new_entry = {
            "Company": company_name,
            "Date Applied": date_applied,
            "Position Found On:": job_found,
            "Job Type": position,
            "Notes": app_notes
            }
        df.loc[len(df)] = new_entry
    #Interview list
    else:
        company_name = input("Enter company name: ")
        interview_date = input("Enter interview date (mm/dd): ")
        position_notes = input("Enter any position notes: ")
        new_entry = {
            "Company": company_name,
            "Interview date": interview_date,
            "Notes re: Position": position_notes
            }
        df.loc[len(df)] = new_entry
    print()
    return

#Update file; file_code specifies which file to edit
def update_file(df, file_code):
    print()
    company_name = input("Enter company which you want to update: ")
    matches = df[df["Company"] == company_name]
    if matches.empty:
        print("No entry found for ", company_name)
        return
    if file_code == 1:
        #application
        continue_editing = 'y'
        while continue_editing.lower() == 'y':
            print("Column options: ")
            print("Notes")
            print("Company Interested?")
            column_name = input("Which column would you like to edit? ")
            new_value = input("Enter edits: ")
            if column_name in df.columns:
                df.loc[df["Company"] == company_name, column_name] = new_value
            else:
                print("Invalid column name.")
            continue_editing = input("Continue editing? (y/n)")
    else:
        #interview
        continue_editing = 'y'
        while continue_editing.lower() == 'y':
            print("Column options: ")
            print("Called back?")
            print("Notes re: Interview")
            print("Follow-up")
            column_name = input("Which column would you like to edit? ")
            new_value = input("Enter edits: ")
            if column_name in df.columns:
                df.loc[df["Company"] == company_name, column_name] = new_value
            else:
                print("Invalid column name.")
            print()
            continue_editing = input("Continue editing? (y/n)")
    return

#Print entry
def print_entry(df):
    print()
    company_name = input("Enter company you want information from: ")
    matches = df[df["Company"] == company_name]
    if not matches.empty:
        print("Matching entries:\n")
        print(matches.to_string(index=False))
    else:
        print("No entry found for ", company_name)
    print()
    return

#Check number of applications
def number_of_apps(df):
    num_rows = len(df)
    print()
    print(f"You have {num_rows} applications sent out.")
    print()
    return

#Exit program
def save_and_exit(df, filename):
    df.to_csv(filename, index=False)
    return True

#Main menu
def main_menu():
    print()
    print("Select from the following:")
    print("1 - Internship menu")
    print("2 - Interview menu")
    print("9 - Exit application")
    option = input("Enter your selection: ")
    print()
    return option

#Internship menu
def internship_menu():
    print()
    print("Select from the following:")
    print("1 - Add entry")
    print("2 - Update entry")
    print("3 - Print/find entry")
    print("4 - Check total number of entries")
    print("5 - Get password")
    print("9 - Exit")
    option = input("Enter your selection: ")
    print()
    return option

#Internship menu handling
def internship_menu_handling():
    appOption = internship_menu()
    while appOption != '9':
        if appOption == '1':
            #Add entry
            add_to_file(df1, 1)
        elif appOption == '2':
            update_file(df1, 1)
            #Update entry
        elif appOption == '3':
            #print entry
            print_entry(df1)
        elif appOption == '4':
            #check number of entries
            number_of_apps(df1)
        elif appOption == '5':
            get_password()
        else:
            print("Invalid option; try again")
        appOption = internship_menu()
    return

#Interview menu
def interview_menu():
    print()
    print("Select from the following:")
    print("1 - Add interview")
    print("2 - Update entry")
    print("3 - Print entry")
    print("9 - Exit")
    option = input("Enter your selection: ")
    print()
    return option

#Interview menu handling
def interview_menu_handling():
    appOption = interview_menu()
    while appOption != '9':
        if appOption == '1':
            #add entry
            add_to_file(df2, 2)
        elif appOption == '2':
            #update entry
            update_file(df2, 2)
        elif appOption == '3':
            #print entry
            print_entry(df2)
        else:
            print()
            print("Invalid option; try again")
            print()
        appOption = interview_menu()
    return

def main():
    print("Welcome to your Internship Tracker!")
    run_again = 'y'
    while run_again.lower() == 'y':
        mainOption = main_menu()
        #Application data
        if mainOption == '1':
            internship_menu_handling()
        #Interview data
        elif mainOption == '2':
            interview_menu_handling()
        #Ensure a proper save before exiting
        elif mainOption == '9':
            save1 = save_and_exit(df1, "Internship_Apps.csv")
            save2 = save_and_exit(df2, "Interview_Notes.csv")
            if save1 == True and save2 == True:
                print()
                print("Changes saved successfully")
                print("Exiting program")
                print()
                break
            else:
                print("Warning: Changes not saved, try again")
                mainOption = main_menu()
        #Validation
        else:
            print()
            print("Invalid option; try again")
            print()
            mainOption = main_menu()
        print()
        run_again = input("Do you want to run again?")
        print()
    save1 = save_and_exit(df1, "Internship_Apps.csv")
    save2 = save_and_exit(df2, "Interview_Notes.csv")
    if save1 == True and save2 == True:
        print()
        print("Changes saved successfully")
        print("Exiting program")
        print()
    return


main()


