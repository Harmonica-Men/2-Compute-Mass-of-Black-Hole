# Compute Mass Of Black Hole
# Print Data for M vs C vs P Plot

# CO orbital circumference
# PO orbital, period, seconds
# G Gravitational constant km**3/s**2 per solar mass
def main():
    # Constants
    G = 1.327E11  # Gravitational constant of Isaac Newton (km/s per Solar Mass)
    pi = 3.14159  # Value of pi

    # Get user input for CO orbital circumference
    CO = float(input("Enter the orbital circumference of your object (km): "))

    # Loop over PO values from 10 to 1000 in steps of 10
    for PO in range(10, 1000, 10):
        # Calculate MassHole using the given formula
        MassHole = CO * CO * CO / (2 * pi * G * PO * PO)
        # Print PO and MassHole
        print("One orbit around the object in:", PO,
              "seconds.  Then the Mass of the object is: ", round(MassHole,1),
              "in solar masses")


if __name__ == "__main__":
    main()
