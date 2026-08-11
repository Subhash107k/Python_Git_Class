"""
main.py

The main entry point for the Nepal District Weather Fetcher CLI application.
Connects the UI, the weather API, and the district data.
"""
from districts import DISTRICTS
from utils import clear_screen, print_header, get_user_choice, display_weather
from weather_api import fetch_weather

def get_all_districts_flat():
    """Returns a flat dictionary of all districts."""
    flat_districts = {}
    for province, province_districts in DISTRICTS.items():
        for district, coords in province_districts.items():
            flat_districts[district] = {
                "province": province,
                "coords": coords
            }
    return flat_districts

def fetch_and_show_weather(district_name, province_name, coords):
    """
    Wrapper function to fetch weather, handle errors, and display it.
    """
    print(f"\nFetching weather for {district_name}...")
    try:
        # Call the API module
        weather_data = fetch_weather(coords["latitude"], coords["longitude"])
        
        # Display the result
        display_weather(district_name, province_name, weather_data)
        
    except Exception as e:
        print("\nERROR:")
        print("-" * 40)
        print(e)
        print("-" * 40)
    
    input("\nPress Enter to return to the main menu...")

def browse_by_province():
    """Allows user to select a province, then a district."""
    clear_screen()
    print_header("SELECT PROVINCE")
    
    provinces = list(DISTRICTS.keys())
    for i, province in enumerate(provinces, 1):
        print(f"{i}. {province}")
    print(f"{len(provinces) + 1}. Back")
    print()
    
    valid_choices = [str(i) for i in range(1, len(provinces) + 2)]
    choice = get_user_choice("Enter choice: ", valid_choices)
    
    if choice == str(len(provinces) + 1):
        return # Go back
        
    selected_province = provinces[int(choice) - 1]
    
    # Select district within province
    clear_screen()
    print_header(f"{selected_province.upper()}")
    
    province_districts = DISTRICTS[selected_province]
    district_names = list(province_districts.keys())
    district_names.sort()
    
    for i, district in enumerate(district_names, 1):
        print(f"{i}. {district}")
    print(f"{len(district_names) + 1}. Back")
    print()
    
    valid_choices = [str(i) for i in range(1, len(district_names) + 2)]
    d_choice = get_user_choice("Enter choice: ", valid_choices)
    
    if d_choice == str(len(district_names) + 1):
        return # Go back
        
    selected_district = district_names[int(d_choice) - 1]
    coords = province_districts[selected_district]
    
    fetch_and_show_weather(selected_district, selected_province, coords)

def browse_by_district():
    """Allows user to select from an alphabetical list of all districts."""
    clear_screen()
    print_header("ALL DISTRICTS")
    
    flat_districts = get_all_districts_flat()
    district_names = list(flat_districts.keys())
    district_names.sort()
    
    for i, district in enumerate(district_names, 1):
        # Format output in multiple columns could be done, but keeping it simple for educational purposes
        print(f"{i}. {district}")
    
    print(f"{len(district_names) + 1}. Back")
    print()
    
    valid_choices = [str(i) for i in range(1, len(district_names) + 2)]
    choice = get_user_choice("Enter choice: ", valid_choices)
    
    if choice == str(len(district_names) + 1):
        return
        
    selected_district = district_names[int(choice) - 1]
    data = flat_districts[selected_district]
    
    fetch_and_show_weather(selected_district, data["province"], data["coords"])

def search_district():
    """Allows user to type a district name."""
    clear_screen()
    print_header("SEARCH DISTRICT")
    
    flat_districts = get_all_districts_flat()
    # Create lowercase keys for case-insensitive search
    search_dict = {name.lower(): (name, data) for name, data in flat_districts.items()}
    
    while True:
        query = input("Enter district name (or 'back' to cancel): ").strip().lower()
        
        if query == 'back':
            return
            
        if not query:
            continue
            
        if query in search_dict:
            actual_name, data = search_dict[query]
            fetch_and_show_weather(actual_name, data["province"], data["coords"])
            return
        else:
            # Simple substring matching
            matches = [name for name in search_dict.keys() if query in name]
            if matches:
                print(f"\nDid you mean:")
                for match in matches:
                    print(f"- {search_dict[match][0]}")
                print()
            else:
                print("\nDistrict not found. Please try again.\n")

def main_menu():
    """Main application loop."""
    while True:
        clear_screen()
        print_header("NEPAL WEATHER FETCHER")
        print("1. Weather by Province")
        print("2. Weather by District")
        print("3. Search District")
        print("4. List Nepal Districts")
        print("5. Exit")
        print()
        
        choice = get_user_choice("Enter your choice: ", ["1", "2", "3", "4", "5"])
        
        if choice == "1":
            browse_by_province()
        elif choice == "2":
            browse_by_district()
        elif choice == "3":
            search_district()
        elif choice == "4":
            browse_by_district() # Using the same function as it lists them
        elif choice == "5":
            print("\nExiting... Goodbye!\n")
            break

if __name__ == "__main__":
    main_menu()
