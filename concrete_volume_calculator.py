def main():
    length = float(input("Enter length (m): "))
    width = float(input("Enter width (m): "))
    depth = float(input("Enter depth (m): "))
    volume = length * width * depth

    print(f"So, you need {volume:,.2f} cubic meters of concrete.")

if __name__ == "__main__":
    main()