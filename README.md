# Python Programming

A comprehensive collection of Python exercises and projects covering fundamental programming concepts, control structures, data manipulation, and file handling. All modules feature descriptive naming conventions and well-documented functions for easy learning and reference.

## Project Structure

### 🔄 Controlling Program Flow
Comprehensive exercises on control structures, loops, conditionals, and recursion:

#### String Operations
String manipulation and parsing functions:
- `first_vowel` - Find first vowel position in strings
- `first_vowel_with_default` - Vowel finder with -1 default return
- `email_name_extractor` - Extract names from email addresses (2 formats)
- `email_name_extractor_extended` - Extract names from email addresses (3 formats)
- `number_string_validator` - Validate comma-separated number format
- `pig_latin_converter` - Convert English words to Pig Latin
- `pig_latin_converter_duplicate` - Alternative Pig Latin implementation
- `time_converters` - Convert between 12-hour and 24-hour time formats

#### Precondition Testing
Validation and precondition enforcement:
- `time_validator` - Validate and convert 12-hour time format
- `european_float_validator` - Validate European float format (comma as decimal)
- `iso_time_validator` - Validate ISO 8601 time format

#### For Loop Functions
Iterative algorithms using for-loops:
- `count_and_average` - Count elements and calculate averages
- `clamp_and_unique` - Clamp values and count unique elements
- `factorial_and_range` - Factorial calculation and reversed ranges
- `skip_and_fixed_points` - Skip characters and find fixed points

#### While Loops
Iterative algorithms using while-loops:
- `input_counter.py` - Count user inputs interactively
- `coin_flip_and_partition.py` - Coin flip counter and string partitioner
- `skip_and_fixed_points_while.py` - While-loop versions of skip and fixed points
- `quasar.py` - Full text-based betting game

#### Recursion
Recursive function implementations:
- `factorial_recursive.py` - Recursive factorial calculation
- `fibonacci_recursive.py` - Recursive Fibonacci sequence
- `hanoi_and_lucas` - Tower of Hanoi and Lucas numbers

#### Final Project
Advanced capstone exercises:
- `substring_finder.py` - Find all positions of substring in text
- `caesar_cipher.py` - Caesar cipher encoder/decoder
- `blackjack_scorer.py` - Blackjack hand scoring with Ace handling

### 💱 Currency Converter
A complete currency conversion application with web service integration:
- `currency.py` - String parsing, JSON handling, and exchange rate calculations
- `exchangeit.py` - User interface for currency exchange
- `test_currency.py` - Comprehensive unit tests

### 📚 Mastering Data Structures
Deep dive into Python's core data structures with practical implementations:

#### Core Operations
- `list_operations.py` - Mutable and immutable list operations (clamp, remove, rotate)
- `dictionary_operations.py` - Dictionary operations (grades, filtering, weather reports)
- `nested_list_operations.py` - Nested list operations (row sums, crossout, place sums)
- `higher_order_functions.py` - Fold left and fold right implementations
- `keyword_expansion.py` - Circle area calculation using keyword arguments
- `tuple_expansion.py` - Average calculation using variable arguments

#### Specialized Modules
- `time_operations` - Time object addition (immutable and mutable versions)
- `string_methods` - Parentheses extraction and NetID validation
- `tuple_replacer` - Replace first occurrence in tuples

### 📊 Auditing Datasets
Working with different file formats and data processing:
- `csv_files.py` - CSV file handling and processing
- `json_files.py` - JSON data manipulation
- `text_files.py` - Text file operations (line counting, number writing)
- `datetime_ops.py` - DateTime operations and time parsing

## File Organization

All files follow a consistent naming convention:
- **Implementation files**: Named after their functionality (e.g., `caesar_cipher.py`, `email_name_extractor.py`)
- **Test files**: Prefixed with `test_` matching their implementation (e.g., `test_caesar_cipher.py`)
- **Folders**: Descriptively named to indicate content (e.g., `string_operations`, `recursion`)


## Requirements

- Python 3.x
- `introcs` module (for string operations)
- `datetime` and `dateutil` (for datetime operations)
- `pytz` (for timezone handling)

## Learning Path

1. **String Operations** - Master string manipulation and parsing
2. **Precondition Testing** - Learn input validation and error handling
3. **For Loop Functions** - Practice iterative algorithms
4. **While Loops** - Understand loop control and user interaction
5. **Recursion** - Explore recursive problem-solving
6. **Currency Converter** - Apply concepts in a practical project
7. **Mastering Data Structures** - Deep dive into Python's core data types
8. **Auditing Datasets** - Practice file handling and data processing

## Project Highlights

- 🎯 **70+ exercises** covering fundamental to advanced Python concepts
- 📝 **Comprehensive documentation** with examples for every function
- 🧪 **Full test coverage** with unit tests for all modules
- 🎓 **Progressive difficulty** from basic string operations to complex recursion
- 💼 **Real-world applications** including currency conversion and game development
