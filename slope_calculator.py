def main():
    rise = float(input("Enter rise of the road (m): "))
    run = float(input("Enter run of the road (m): "))
    slope = rise / run * 100

    print(f"So, the slope of the road is {slope:,.2f}%.")

if __name__ == "__main__":
    main()