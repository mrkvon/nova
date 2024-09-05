# Nova

Monitor the upcoming outburst of the recurrent nova **T Coronae Borealis** by scraping its [magnitude data from theskylive.com](https://theskylive.com/sky/stars/hr-5958-star).

The script prints:
- The last recorded magnitude of the nova.
- The time elapsed in hours and minutes (H:mm) since the last measurement reported on the website.
- A little star indicator (✦) during the duration of the outburst event.

## Magnitude

Lower magnitude means brighter star. T CrB will change from magnitude ~10 to ~2 during the event.

## Requirements

- Python 3.7 or higher.

## Installation and Running the Script

1. **Clone the repository**:

    ```bash
    git clone https://github.com/mrkvon/nova.git
    cd nova
    ```

2. **Set up and activate the virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Use venv\Scripts\activate on Windows
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the script**:

    ```bash
    python main.py
    ```

5. **Deactivate the virtual environment** when done:

    ```bash
    deactivate
    ```

## Notes

- Ensure that you have a stable internet connection as the script fetches data from theskylive.com.
- If you encounter any issues with dependencies, make sure you are using the correct Python version and that all required packages are installed.
