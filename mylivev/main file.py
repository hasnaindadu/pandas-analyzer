import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Datasetload:# i created saparate class to load data
    def __init__(self):#constructor
        self.data = None#BY DEFAULT WE HAVE TO WRITE NONE REFRENCE FROM YOUTUBE
    def load_dataset(self, file_path):#FILE PATH ARGUMENT TO LOAD FILE
        try:
            print(f"Loading dataset from: {file_path}")
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully.\n")
            print(self.data.head())  # Display first 5 rows
        except FileNotFoundError:#PLEASE NOT HERE EXEPTION HANDLING IS REFRENCE FROM CHAT GPT
            print(f"Error: File '{file_path}' not found.check  path.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except pd.errors.ParserError:
            print("Error: There is an issue with parsing the CSV file. Check for formatting issues.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_data(self):
        return self.data#returns data set


class SalesDataAnalyzer:
    
    def __init__(self, dataset_loader):
        self.dataset_loader = dataset_loader  # Reference to Datasetload instance
        self.data = None

    def update_data(self):

        self.data = self.dataset_loader.get_data()#takes data from loader

    def explore_data(self):#explore data method

        self.update_data()
        if self.data is None:
            print("No dataset loaded.")#if data set not found
            return

        print("\nSelect exploration option:")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            print(self.data.head())#basic functions of pandas
        elif choice == '2':
            print(self.data.tail())
        elif choice == '3':
            print(self.data.columns)
        elif choice == '4':
            print(self.data.dtypes)
        elif choice == '5':
            print(self.data.info())
        else:
            print("Invalid choice.")

    def perform_dataset_operations(self):

        self.update_data()
        if self.data is None:
            print("No dataset loaded.")
            return

        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if numeric_cols.empty:
            print("No numeric columns available for operations.")
            return

        print("\nSelect mathematical operation:")
        print("1. Calculate mean of a column")
        print("2. Calculate sum of a column")
        print("3. Multiply column values by a scalar")

        choice = input("Enter choice: ").strip()
        column = input("Enter column name for operation: ").strip()

        if column not in numeric_cols:
            print("Invalid column name.")
            return

        np_array = self.data[column].to_numpy()

        if choice == '1':
            print(f"Mean of {column}: {np.mean(np_array)}")
        elif choice == '2':
            print(f"Sum of {column}: {np.sum(np_array)}")
        elif choice == '3':
            scalar = float(input("Enter scalar value: "))
            print(f"Result after multiplication:\n{np_array * scalar}")
        else:
            print("Invalid choice.")

    def handle_missing_data(self):

        self.update_data()
        if self.data is None:
            print("No dataset loaded.")
            return

        print("\nSelect missing data handling option:")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            print(self.data[self.data.isnull().any(axis=1)])
        elif choice == '2':
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Missing values filled with mean.")
        elif choice == '3':
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped.")
        elif choice == '4':
            column = input("Enter column name to replace missing values: ").strip()
            if column in self.data.columns:
                value = input("Enter the value to replace missing values with: ")
                self.data[column].fillna(value, inplace=True)
                print(f"Missing values in {column} replaced with {value}.")
            else:
                print("Invalid column name.")
        else:
            print("Invalid choice.")

    def generate_statistics(self):#simply use .describe
        self.update_data()
        if self.data is None:
            print("No dataset loaded.")
        else:
            print(self.data.describe())#simple method of pandas

    def visualize_data(self):
        self.update_data()
        if self.data is None:
            print("No dataset loaded.")
            return

        print("\nSelect visualization type:")
        print("1. histogram")
        print("2. Bar Chart")
        print("3. Line Chart")
        print("4. scatter Plot")
        print("5. box Plot")
        print("6. Pie Chart")

        choice = input("Enter choice: ").strip()
        column = input("Enter column name for visualization: ").strip()

        if column not in self.data.columns:
            print("Invalid column name.")
            return

        plt.figure(figsize=(10, 6))

        if choice == '1':
            self.data[column].hist()
        elif choice == '2':
            self.data[column].value_counts().plot(kind='bar')
        elif choice == '3':
            self.data[column].plot(kind='line')
        elif choice == '4':
            x_col = input("Enter X-axis column: ").strip()
            if x_col in self.data.columns:
                self.data.plot(kind='scatter', x=x_col, y=column)
            else:
                print("Invalid X-axis column.")
                return
        elif choice == '5':
            self.data[column].plot(kind='box')
        elif choice == '6':
            self.data[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
        else:
            print("Invalid choice.")
            return

        plt.title(f"{column} Visualization")
        plt.show()

    def main_menu(self):
        while True:
            print("\nPANDAS ANALYZER AND VISUALIZER")
            print("1. LOAD DATASET")
            print("2. EXPLORE DATA")
            print("3. PERFORM DATASET OPERATIONS")
            print("4. HANDLE MISSING DATA")
            print("5. GENERATE STATISTICS")
            print("6. VISUALIZE DATA")
            print("7. EXIT")

            choice = input("Please select an option: ").strip()

            if choice == '1':
                file_path = input("Enter file path: ").strip()
                self.dataset_loader.load_dataset(file_path)
            elif choice == '2':
                self.explore_data()
            elif choice == '3':
                self.perform_dataset_operations()
            elif choice == '4':
                self.handle_missing_data()
            elif choice == '5':
                self.generate_statistics()
            elif choice == '6':
                self.visualize_data()
            elif choice == '7':
                print("Exiting program...")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    loader = Datasetload()  # Create dataset loader instance
    analyzer = SalesDataAnalyzer(loader)  # Pass it to the analyzer
    analyzer.main_menu()
