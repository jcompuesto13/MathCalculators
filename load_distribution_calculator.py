def main():
    u_load = float(input("Enter uniform load (N/m): "))
    length = float(input("Enter length (m): "))
    load = u_load * length

    print(f"So, the total load acting on the beam is {load:,.2f} N.")

if __name__ == "__main__":
    main()