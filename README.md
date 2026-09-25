# Smart Travel Planner

A beginner-friendly Python console program that collects trip details, validates user input, calculates all major travel costs, and displays a clean formatted summary — using only Python's built-in features.

---

## How to Run

```bash
python smart_travel_planner.py
```

No external libraries, no database, no files, no APIs required. Just Python 3.

---

## What the Program Does

The program walks you through a series of prompts, collects your trip details, and produces a full cost breakdown at the end.

### Information Collected

| Input | Type | Validation |
|---|---|---|
| Traveler name | Text | Cannot be empty |
| Destination | Text | Cannot be empty |
| Number of travelers | Whole number | Must be > 0 |
| Number of travel days | Whole number | Must be > 0 |
| Transportation cost per traveler | Decimal number | Cannot be negative |
| Hotel cost per day | Decimal number | Cannot be negative |
| Activity cost per traveler | Decimal number | Cannot be negative |

### Costs Calculated

| Calculation | Formula |
|---|---|
| Total transportation cost | cost per traveler × number of travelers |
| Total hotel cost | cost per day × number of days |
| Total food cost | $50 per person per day × travelers × days |
| Total activity cost | cost per traveler × number of travelers |
| Overall trip cost | transport + hotel + food + activities |
| Cost per traveler | overall cost ÷ number of travelers |
| Average daily cost | overall cost ÷ number of days |

> Food cost uses a built-in estimate of **$50 per person per day** since it is difficult to know in advance.

---

## Sample Run

```
======================================================
       WELCOME TO THE SMART TRAVEL PLANNER
  Plan your trip and estimate your total budget!
======================================================

Please fill in the details below.

  Enter your name               : Alice
  Enter destination             : Paris
  Number of travelers           : 2
  Number of travel days         : 5
  Transportation cost/traveler  : $300
  Hotel cost per day            : $120
  Activity cost per traveler    : $80


======================================================
          ✈  SMART TRAVEL PLANNER SUMMARY  ✈
======================================================

  TRIP DETAILS
  --------------------------------------------------
  Traveler Name   : Alice
  Destination     : Paris
  No. of Travelers: 2
  No. of Days     : 5

  COST BREAKDOWN
  --------------------------------------------------
  Transportation  : $    600.00
  Hotel           : $    600.00
  Food (est.)     : $    500.00
  Activities      : $    160.00
  --------------------------------------------------
  OVERALL COST    : $  1,860.00

  SUMMARY STATISTICS
  --------------------------------------------------
  Cost per Traveler     : $    930.00
  Average Daily Cost    : $    372.00

======================================================
       Have a wonderful trip! Bon Voyage! 🌍
======================================================
```

---

## Program Structure

```
smart_travel_planner.py
│
├── Input Helpers
│   ├── get_string_input()        – collects non-empty text
│   ├── get_positive_int()        – collects whole numbers > 0
│   └── get_non_negative_float()  – collects decimal numbers >= 0
│
├── Calculation Functions
│   ├── calculate_transport_cost()     – returns total transport cost
│   ├── calculate_hotel_cost()         – returns total hotel cost
│   ├── calculate_food_cost()          – returns estimated food cost
│   ├── calculate_activity_cost()      – returns total activity cost
│   ├── calculate_overall_cost()       – returns sum of all costs
│   ├── calculate_cost_per_traveler()  – returns cost split per person
│   └── calculate_average_daily_cost() – returns daily spend average
│
├── Display Function
│   └── display_summary()  – prints the formatted trip summary
│
└── main()  – drives the program: collects input, runs calculations,
              stores data, calls display
```

---

## Python Concepts Demonstrated

| Concept | Where Used |
|---|---|
| **Variables** | Storing name, destination, costs, totals |
| **Data types** | `str`, `int`, `float`, `bool` (implicitly in conditions) |
| **Type conversion** | `int(raw)`, `float(raw)` inside input helpers |
| **Input / output** | `input()` for collection, `print()` for display |
| **Data structures – dict** | `trip_info` stores traveler name, destination, counts |
| **Data structures – tuple** | `cost_breakdown` packs all 7 calculated values |
| **Functions** | Separate function for every major operation |
| **Parameters & return values** | Every calculation function takes arguments and returns a result |
| **Arithmetic operations** | `*`, `/`, `+` across all cost formulas |
| **Input validation** | Loops with `try / except` and range checks |
| **Formatted output** | f-strings with `,.2f` for currency formatting |

---

## Project Files

```
Smart-travel-planner/
├── smart_travel_planner.py   ← main program
└── README.md                 ← this file
```
