# How to run

1. **Clone the repository if you haven't:**

   ```bash
   git clone https://github.com/snigdhat1/thoughtfulAI.git
   cd thoughtfulAI

2. **Make sure python is installed (I am using python 3.13.2):**
    ```bash
    python --version
    ```

3. **Run the script**
    ```bash
    python sort.py <width> <height> <length> <mass>
    ```
    or if you are using python3
    ```bash
    python3 sort.py <width> <height> <length> <mass>
    ```


I have test cases created in the test_sort.py file. To run:

1. **Install pytest**

   ```bash
   pip install pytest
   ```
   or if you are using python3
    ```bash
    python3 -m pip install pytest
    ```

2. **Make sure pytest is installed (I am using pytest 8.4.0):**
    ```bash
    pytest --version
    ```

3. **Run the script**
    ```bash
    pytest test_sort.py
    ```