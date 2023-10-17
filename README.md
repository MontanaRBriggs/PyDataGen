# PyDataGen - [![Version](https://img.shields.io/badge/Version-1.0.0-blue)](https://github.com/MontanaRBriggs/PyDataGen)

Generate bivariate (X, Y) data sets for the assessment of machine learning algorithms.

## Usage

Import the DataGenerator class.

```py
from PyDataGen import DataGenerator
```

Create and instantiate DataGenerator object.

```py
data_generator = DataGenerator()
```

Generate a data set, print it to the console (optional), and save it.

```py
# Generate 10 points of random data where X can be (1-5) and Y (1-10).

data_generator.generate_data(x_min=1, x_max=5, y_min=1, y_max=10, data_points=10)

# Optionally print the data to the console using the default parameters.
# This is functionally equivalent to data_generator.print_data().

data_generator.print_data(mapped_x_values=None, mapped_y_values=None, verbose=False)

# Save the generated data to a .csv file using the default parameters.
# This is functionally equivalent to data_generator.save_data().

data_generator.save_data(file_name="Data", mapped_x_values=None, mapped_y_values=None, verbose=False)
```

Read the CSV file where necessary.

```py
import csv

def get_csv_data(csv_file_path: str) -> list:
    try:
        with open(csv_file_path, 'r', newline='') as csv_data:
            return list(csv.reader(csv_data))
    except FileExistsError: # Should the file not exist.
        pass # Handle the exception as needed.
    except PermissionError: # Should the file be inaccessible.
        pass # Handle the exception as needed.
    except OSError: # Should the previous two cases be insufficient.
        pass # Handle the exception as needed.

    return [] # Return an empty list if the .csv file was not read. 
```

## MIT License

Copyright © 2023, Montana R. Briggs

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.