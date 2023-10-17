"""
[Author]: Montana R. Briggs.

[Updated]: 17 October 2023.
[Version]: 1.0.0.

[LICENSE]

MIT License

Copyright © 2023, Montana R. Briggs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import csv
import random

class DataGenerator:
    def __init__(self):
        """
        Initialize an instance of the DataGenerator class.

        Attributes:
        - current_data (list): A list to hold the generated data.
        """

        self.current_data = None

    def generate_data(self, x_min: int, x_max: int, y_min: int, y_max: int, data_points: int):
        """
        Generates random data points for X (independent variable) and Y (dependent variable).

        Arguments:
        - x_min (int): Minimum value for X.
        - x_max (int): Maximum value for X.
        - y_min (int): Minimum value for Y.
        - y_max (int): Maximum value for Y.
        - data_points (int): Total number of data points to generate.
        """

        x_data = [random.randint(x_min, x_max) for _ in range(data_points)]
        y_data = [random.randint(y_min, y_max) for _ in range(data_points)]
        
        self.current_data = [(x, y) for x, y in zip(x_data, y_data)]
    
    def print_data(self, mapped_x_values: dict = None, mapped_y_values: dict = None, verbose: bool = False):
        """
        Prints the generated data set to the terminal with mapped labels (optional).

        Arguments:
        - mapped_x_values (dict) (opt): A dictionary to map X values to labels.
        - mapped_y_values (dict) (opt): A dictionary to map Y values to labels.
        - verbose (bool): Print warnings for data points missing labels.
        """

        if self.current_data == None:
            print("[ERROR]: There is no data, please use generate_data()."); return
        
        if mapped_x_values == None:
            print("[WARN]: No mapped (X) values provided; you are viewing raw computational data for (X)!")
        
        if mapped_y_values == None:
            print("[WARN]: No mapped (Y) values provided; you are viewing raw computational data for (Y)!")

        formatted_data = []

        for x, y in self.current_data:
            if mapped_x_values and x in mapped_x_values:
                x_label = mapped_x_values[x]
            else:
                if verbose:
                    print(f"[WARN]: X-Value {x} does not have a mapped value!")

                x_label = x

            if mapped_y_values and y in mapped_y_values:
                y_label = mapped_y_values[y]
            else:
                if verbose:
                    print(f"[WARN]: Y-Value {y} does not have a mapped value!")
                
                y_label = y
            
            formatted_data.append(f'({x_label}, {y_label})')
        
        print('[' + ', '.join(formatted_data) + ']')
    
    def save_data(self, file_name: str, mapped_x_values: dict = None, mapped_y_values: dict = None, verbose: bool = False):
        """
        Saves the generated data to a CSV file with mapped labels (optional).

        This function WILL overwrite CSV files with the same name as file_name.

        Arguments:
        - file_name (str): The name of the CSV file to save to (without .csv).
        - mapped_x_values (dict) (opt): A dictionary to map X values to labels.
        - mapped_y_values (dict) (opt): A dictionary to map Y values to labels.
        - verbose (bool): Print warnings for data points missing labels.

        Exceptions:
        - PermissionError: raised if the program lacks permissions to create, or write to, the file.
        """
        
        if self.current_data == None:
            print("[ERROR]: There is no data, please use generate_data()."); return
        
        if mapped_x_values == None:
            print("[WARN]: No mapped (X) values provided; you are saving raw computational data for (X)!")
        
        if mapped_y_values == None:
            print("[WARN]: No mapped (Y) values provided; you are saving raw computational data for (Y)!")
        
        try:
            with open(file_name, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                for x, y in self.current_data:
                    if mapped_x_values and x in mapped_x_values:
                        x_label = mapped_x_values[x]
                    else:
                        if verbose:
                            print(f"[WARN]: X-Value {x} does not have a mapped value!")

                        x_label = x

                    if mapped_y_values and y in mapped_y_values:
                        y_label = mapped_y_values[y]
                    else:
                        if verbose:
                            print(f"[WARN]: Y-Value {y} does not have a mapped value!")

                        y_label = y
                    
                    csv_writer.writerow([x_label, y_label])
        except PermissionError:
            print("[ERROR]: DATA HAS NOT BEEN SAVED! The program lacks permissions to create, or write to, the file.")