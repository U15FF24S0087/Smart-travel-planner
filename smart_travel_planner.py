# ============================================================
#  Smart Travel Planner
#  A beginner-friendly console program to plan and estimate
#  the total cost of a trip.
# ============================================================

# ------------------------------------------------------------
# INPUT HELPERS  (with validation)
# ------------------------------------------------------------

def get_string_input(prompt):
    """Ask the user for a non-empty text value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] This field cannot be empty. Please try again.")


def get_positive_int(prompt):
    """Ask the user for a whole number that is greater than zero."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value > 0:
                return value
            print("  [!] The value must be greater than 0. Please try again.")
        except ValueError:
            print("  [!] Please enter a valid whole number (e.g. 3).")


def get_non_negative_float(prompt):
    """Ask the user for a decimal number that is zero or greater."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value >= 0:
                return value
            print("  [!] Cost cannot be negative. Please try again.")
        except ValueError:
            print("  [!] Please enter a valid number (e.g. 150 or 99.99).")


# ------------------------------------------------------------
# CALCULATION FUNCTIONS
# ------------------------------------------------------------

def calculate_transport_cost(cost_per_traveler, num_travelers):
    """
    Total transportation cost = cost per traveler × number of travelers.
    Returns a float.
    """
    return cost_per_traveler * num_travelers


def calculate_hotel_cost(cost_per_day, num_days):
    """
    Total hotel cost = cost per day × number of days.
    Returns a float.
    """
    return cost_per_day * num_days


def calculate_food_cost(num_travelers, num_days, daily_food_per_person=50.0):
    """
    Food cost is estimated at a fixed daily rate per person.
    Total food cost = daily rate × number of travelers × number of days.
    The default daily food budget per person is $50.
    Returns a float.
    """
    return daily_food_per_person * num_travelers * num_days


def calculate_activity_cost(cost_per_traveler, num_travelers):
    """
    Total activity cost = cost per traveler × number of travelers.
    Returns a float.
    """
    return cost_per_traveler * num_travelers


def calculate_overall_cost(transport, hotel, food, activities):
    """
    Overall trip cost = sum of all cost components.
    Returns a float.
    """
    return transport + hotel + food + activities


def calculate_cost_per_traveler(overall_cost, num_travelers):
    """
    Cost per traveler = overall cost / number of travelers.
    Returns a float.
    """
    return overall_cost / num_travelers


def calculate_average_daily_cost(overall_cost, num_days):
    """
    Average daily cost = overall cost / number of days.
    Returns a float.
    """
    return overall_cost / num_days


# ------------------------------------------------------------
# DISPLAY FUNCTION
# ------------------------------------------------------------

def display_summary(trip_info, cost_breakdown):
    """
    Print a clean, formatted travel summary.

    Parameters:
        trip_info      (dict)  – traveler and trip details
        cost_breakdown (tuple) – (transport, hotel, food, activities,
                                   overall, per_traveler, avg_daily)
    """
    # Unpack the cost tuple
    (transport_total, hotel_total, food_total, activity_total,
     overall_total, per_traveler, avg_daily) = cost_breakdown

    border = "=" * 54

    print("\n")
    print(border)
    print("          ✈  SMART TRAVEL PLANNER SUMMARY  ✈")
    print(border)

    # Trip details section
    print("\n  TRIP DETAILS")
    print("  " + "-" * 50)
    print(f"  Traveler Name   : {trip_info['traveler_name']}")
    print(f"  Destination     : {trip_info['destination']}")
    print(f"  No. of Travelers: {trip_info['num_travelers']}")
    print(f"  No. of Days     : {trip_info['num_days']}")

    # Cost breakdown section
    print("\n  COST BREAKDOWN")
    print("  " + "-" * 50)
    print(f"  Transportation  : ${transport_total:>10,.2f}")
    print(f"  Hotel           : ${hotel_total:>10,.2f}")
    print(f"  Food (est.)     : ${food_total:>10,.2f}")
    print(f"  Activities      : ${activity_total:>10,.2f}")
    print("  " + "-" * 50)
    print(f"  OVERALL COST    : ${overall_total:>10,.2f}")

    # Summary statistics section
    print("\n  SUMMARY STATISTICS")
    print("  " + "-" * 50)
    print(f"  Cost per Traveler     : ${per_traveler:>10,.2f}")
    print(f"  Average Daily Cost    : ${avg_daily:>10,.2f}")

    print("\n" + border)
    print("       Have a wonderful trip! Bon Voyage! 🌍")
    print(border + "\n")


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():
    border = "=" * 54

    print(border)
    print("       WELCOME TO THE SMART TRAVEL PLANNER")
    print("  Plan your trip and estimate your total budget!")
    print(border)
    print("\nPlease fill in the details below.\n")

    # ── Collect traveler information ──────────────────────────
    traveler_name  = get_string_input("  Enter your name               : ")
    destination    = get_string_input("  Enter destination             : ")
    num_travelers  = get_positive_int("  Number of travelers           : ")
    num_days       = get_positive_int("  Number of travel days         : ")

    print()  # blank line for readability

    # ── Collect cost information ──────────────────────────────
    transport_per_traveler = get_non_negative_float(
        "  Transportation cost/traveler  : $"
    )
    hotel_per_day = get_non_negative_float(
        "  Hotel cost per day            : $"
    )
    activity_per_traveler = get_non_negative_float(
        "  Activity cost per traveler    : $"
    )

    # ── Store trip info in a dictionary (data structure) ─────
    trip_info = {
        "traveler_name" : traveler_name,   # str
        "destination"   : destination,     # str
        "num_travelers" : num_travelers,   # int
        "num_days"      : num_days,        # int
    }

    # ── Run all calculations ──────────────────────────────────
    transport_total = calculate_transport_cost(transport_per_traveler, num_travelers)
    hotel_total     = calculate_hotel_cost(hotel_per_day, num_days)
    food_total      = calculate_food_cost(num_travelers, num_days)          # uses default $50/person/day
    activity_total  = calculate_activity_cost(activity_per_traveler, num_travelers)

    overall_total   = calculate_overall_cost(transport_total, hotel_total,
                                             food_total, activity_total)
    per_traveler    = calculate_cost_per_traveler(overall_total, num_travelers)
    avg_daily       = calculate_average_daily_cost(overall_total, num_days)

    # ── Pack results into a tuple (data structure) ────────────
    cost_breakdown = (
        transport_total,   # float
        hotel_total,       # float
        food_total,        # float
        activity_total,    # float
        overall_total,     # float
        per_traveler,      # float
        avg_daily,         # float
    )

    # ── Show the formatted summary ────────────────────────────
    display_summary(trip_info, cost_breakdown)


# Run the program
if __name__ == "__main__":
    main()
