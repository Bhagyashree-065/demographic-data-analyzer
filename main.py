# main.py
from src.demographic_data_analyzer import calculate_demographic_data
def main():
    # Run the demographic analysis and store results
    results = calculate_demographic_data(print_data=True)
    # Optionally, access specific values from the returned dictionary
    print("\n--- Summary ---")
    print(f"Country with highest % of >50K earners: {results['highest_earning_country']} ({results['highest_earning_country_percentage']}%)")
    print(f"Top occupation in India among >50K earners: {results['top_IN_occupation']}")

if __name__ == "__main__":
    main()