import pandas as pd

def main():
    # Constants
    G = 1.327E11  # Gravitational constant of Isaac Newton (km/s per Solar Mass)
    pi = 3.14159  # Value of pi

    # Get user input for CO orbital circumference
    CO = float(input("Enter the orbital circumference of your object (km): "))

    # Lists to store data
    PO_values = []
    MassHole_values = []

    # Loop over PO values from 10 to 1000 in steps of 10
    for PO in range(10, 1000, 10):
        # Calculate MassHole using the given formula
        MassHole = CO * CO * CO / (2 * pi * G * PO * PO)
        # Append data to lists
        PO_values.append(PO)
        MassHole_values.append(round(MassHole, 1))

    # Create a DataFrame
    data = {'One orbit around the object in (seconds)': PO_values,
            'Mass of the object in solar masses': MassHole_values}
    df = pd.DataFrame(data)

    # Display DataFrame
    print(df)

if __name__ == "__main__":
    main()
