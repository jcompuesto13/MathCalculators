def main():
    volume1 = float(input("Enter initial volume of cement slurry (L): "))
    concentration1 = float(input("Enter initial concentration value (g/L): "))
    concentration2 = float(input("Enter desired concentration value (g/L): "))
    volume2 = concentration1 * volume1 / concentration2

    print(f"So, you need {volume2:,.2f} L of the original slurry.")

if __name__ == "__main__":
    main()