"""

STRUCTURE OF THIS SCRIPT:

1. load packages
2. define needed functions
3. execute main function that makes use of the previously defined functions

"""


# load needed packages 
import pandas as pd
import tkinter as tk
from tkinter import ttk
from ctypes import windll
from tkinter.messagebox import showinfo
from tkinter import * 
from PIL import ImageTk, Image
import sys
windll.shcore.SetProcessDpiAwareness(1)



def create_survey():
    """ 
    This function creates the survey that the traveller must fill in
    - creates 2 radio buttons (type of vacation, holiday season) and 5 comboboxes (priorities when travelling)
    - a submit button makes the window disappear when being clicked
    - the command at the end, root.mainloop(), keeps the window displaying

    Returns:
        7 inputs by the future traveller (radio buttons and comboboxes)
    """

    root = tk.Tk()
    root.title("Travel Planner")
    root.geometry('1500x1200+50+50')
    root.attributes('-topmost', 1)

    # Place a label on the root window
    message = tk.Label(root, text="This is your travel planner!") #This creates a widget
    message.pack() #This unpacks the widget to the main window

    # Create the first option

    selected_type = tk.StringVar()
    types = (('Sightseeing', 'Sightseeing'),
            ('Outdoor', 'Outdoor'),
            ('Beach', 'Beach'),
            ('Party', 'Party'))

    label_type = ttk.Label(text="What's your favourite type of holiday?")
    label_type.pack(fill='x', padx=5, pady=5)

    for type in types:
        t = ttk.Radiobutton(
            root,
            text=type[0],
            value=type[1],
            variable=selected_type
        )
        t.pack(fill='x', padx=5, pady=5)

    separator_1 = ttk.Separator(root, orient='horizontal')
    separator_1.pack(fill='x')

    # Create the second option

    selected_season = tk.StringVar()
    seasons = (('Winter', 'winter'),
            ('Spring', 'spring'),
            ('Summer', 'summer'),
            ('Autumn', 'autumn'))

    label_season = ttk.Label(text="In which season do you want to travel?")
    label_season.pack(fill='x', padx=5, pady=5)

    for season in seasons:
        s = ttk.Radiobutton(
            root,
            text=season[0],
            value=season[1],
            variable=selected_season
        )
        s.pack(fill='x', padx=5, pady=5)

    separator_1 = ttk.Separator(root, orient='horizontal')
    separator_1.pack(fill='x')

    # Create the ranking in Python

    message_2 = tk.Label(root, text="Please select the priorities for your travel planner") #This creates a widget
    message_2.pack() #This unpacks the widget to the main window

    # Label 1
    label_ranking = ttk.Label(text="Please select your first priority:")
    label_ranking.pack(fill=tk.X, padx=5, pady=5)


    selected_priority_1 = tk.StringVar()
    selected_priority_2 = tk.StringVar()
    selected_priority_3 = tk.StringVar()
    selected_priority_4 = tk.StringVar()
    selected_priority_5 = tk.StringVar()

    # Create Combobox
    priorities = ('Budget',
                    'Flight time',
                    'CO2',
                    'Temperature',
                    'Rain probability'
                )

    rankings_1 = ttk.Combobox(textvariable = selected_priority_1,
                            state = "readonly",
                            values = priorities)

    rankings_1.current(0) 
    rankings_1.pack()

    # Label 2
    label_ranking = ttk.Label(text="Please select your second priority:")
    label_ranking.pack(fill=tk.X, padx=5, pady=5)

    rankings_2 = ttk.Combobox(textvariable = selected_priority_2,
                            state = "readonly",
                            values = priorities)

    rankings_2.current(0) 
    rankings_2.pack()

    # Label 3
    label_ranking = ttk.Label(text="Please select your third priority:")
    label_ranking.pack(fill=tk.X, padx=5, pady=5)

    rankings_3 = ttk.Combobox(textvariable = selected_priority_3,
                            state = "readonly",
                            values = priorities)

    rankings_3.current(0) 
    rankings_3.pack()

    # Label 4
    label_ranking = ttk.Label(text="Please select your fourth priority:")
    label_ranking.pack(fill=tk.X, padx=5, pady=5)

    rankings_4 = ttk.Combobox(textvariable = selected_priority_4,
                            state = "readonly",
                            values = priorities)

    rankings_4.current(0) 
    rankings_4.pack()

    # Label 5
    label_ranking = ttk.Label(text="Please select your fifth priority:")
    label_ranking.pack(fill=tk.X, padx=5, pady=5)

    rankings_5 = ttk.Combobox(textvariable = selected_priority_5,
                            state = "readonly",
                            values = priorities)

    rankings_5.current(0) 
    rankings_5.pack()

    # submit button

    submit_button = ttk.Button(root, text="Submit", command=root.destroy)
    submit_button.pack(ipadx=5,
        ipady=5,
        expand=True
    )

    # keep the window displaying

    root.mainloop()

    user_activity = selected_type.get()
    user_season = selected_season.get()
    user_prio1 = selected_priority_1.get()
    user_prio2 = selected_priority_2.get()
    user_prio3 = selected_priority_3.get()
    user_prio4 = selected_priority_4.get()
    user_prio5 = selected_priority_5.get()
    
    return user_activity, user_season, user_prio1, user_prio2, user_prio3, user_prio4, user_prio5



def check_valid_input(user_activity, user_season, user_prio1, user_prio2, user_prio3, user_prio4, user_prio5):
    """
    Checks if the the user's input are correct
    - if not, an error message is displayed clarifying the mistake
    - the execution of the program stops, if the user input is not correct
    - if the input is correct, nothing happens
    """
    
    chosen_prios = [user_prio1, user_prio2, user_prio3, user_prio4, user_prio5]
    chosen_prios_unique = set(chosen_prios)
    chosen_prios_number = len(chosen_prios_unique)

    if (chosen_prios_number != 5) or (user_season == "") or (user_activity == ""):
        error_window = tk.Tk()
        error_window.title("Error")
        error_window.geometry('1500x800+50+50')
        error_window.attributes('-topmost', 1)

        # Place a label on the root window
        if (user_activity == ""):
            error_message = "Error: Please select a type of holiday!"
        elif (user_season == ""):
            error_message = "Error: Please select a season!"
        else: 
            error_message = "Error: Please select every preference only once!"
            
        message = tk.Label(error_window, text=error_message, fg='red', font=( 'Lucida', 16, 'bold' )) #This creates a widget
        message.pack() #This unpacks the widget to the main window
        
        exit_button = ttk.Button(error_window, text="Understood!", command=error_window.destroy)
        exit_button.pack(ipadx=5,
            ipady=5,
            expand=True
        )
        
        error_window.mainloop()

        sys.exit()



def get_season_data(test_set, user_season):
    """
    Removes all months which are not in the selected season

    Returns:
        data set with the relevant months of the selected season
    """
    
    # dictionary containing all months of a season
    season_dict = {
        'winter': ["Dec", "Jan", "Feb"],
        'spring': ["Mar", "Apr", "May"],
        'summer': ["Jun", "Jul", "Aug"],
        'autumn': ["Sep", "Oct", "Nov"]
    }

    user_months = season_dict[user_season]

    test_set = test_set[test_set["Month"].isin(user_months)]
    
    return test_set



def get_category_data(test_set, user_activity):
    """
    Removes all months which are not in the selected season

    Returns:
        data frame with the relevant months of the selected season
    """
    
    test_set_clean = test_set.groupby(["City", "Country", "Category", "Category 2", "Budget"]).mean()
    test_set_clean = test_set_clean.reset_index()

    # filter for user category in both category columns
    # watch out, user has to pass 'user_category' first!
    test_set_clean = test_set_clean[ (test_set_clean["Category"] == user_activity) | (test_set_clean["Category 2"] == user_activity) ]
    test_set_clean = test_set_clean.reset_index()
    
    return test_set_clean



def rank_locations(test_set_clean, user_prio1, user_prio2, user_prio3, user_prio4, user_prio5):
    """
    Rank the remaining locations for the selected season according to the 5 priorities (comboboxes)
    
    Returns:
        data frame with the locations sorted according to the ranking
    """

    preferences_dict = {
        user_prio1: {"weight": 30},
        user_prio2: {"weight": 25},
        user_prio3: {"weight": 20},
        user_prio4: {"weight": 15},
        user_prio5: {"weight": 10}
    }

    df_scores = test_set_clean.copy()

    for x in ["CO2", "Flight time (min)", "Rain probability"]:
        for i in range(0, len(df_scores)):
            if test_set_clean.loc[i, x] <= test_set_clean[x].median():
                df_scores.loc[i, x] = 1
            else: 
                df_scores.loc[i, x] = 0

    for y in ["Average Temp", "Sun hours per day"]:
        for j in range(0, len(df_scores)):
            if test_set_clean.loc[j, y] >= test_set_clean[y].median():
                df_scores.loc[j, y] = 1
            else: 
                df_scores.loc[j, y] = 0

    replace_dic = {"Low": "1", "Medium": 0.5, "High": 0}
    df_scores["Budget"].replace(replace_dic, inplace = True)

    score_budget = preferences_dict["Budget"]["weight"] * df_scores["Budget"]
    score_flight_time = preferences_dict["Flight time"]["weight"] * df_scores["Flight time (min)"]
    score_co2 = preferences_dict["CO2"]["weight"] * df_scores["CO2"]
    score_temp = preferences_dict["Temperature"]["weight"] * df_scores["Average Temp"]
    score_rain = preferences_dict["Rain probability"]["weight"] * df_scores["Rain probability"]

    df_scores["Score"] = pd.concat([score_budget, score_flight_time, score_co2, score_temp, score_rain], axis=1).sum(axis=1)

    # sort according to Score
    df_scores.sort_values(by=['Score'], ascending = False, inplace = True)
    df_scores["index"] = df_scores.reset_index().index
    df_scores["index"] += 1
    df_scores.rename({"index": "Rank"}, axis=1, inplace=True)
    df_scores = df_scores.set_index("Rank")
    
    return df_scores
 
 
 
def show_results(df_scores):
    """
    Shows the results of the survey
    - recommends top 3 locations (sorted) with their scores
    - the flag of the top location is shown
    - "holiday greetings" are written in the language of the top recommended location
    """
    
    # create a table
    class Table:
        def __init__(self, result_window): 
            # Create Table
            for i in range(4):
                for j in range(3):
                    
                    self.e = Entry(result_window, width=20, fg='black')
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, final_output[i][j])

    # Data
    final_output = [("Rank","City","Match"),
        (1,df_scores.loc[1,"City"], str(df_scores.loc[1,"Score"]) + "%"),
        (2,df_scores.loc[2,"City"], str(df_scores.loc[2,"Score"])  + "%"),
        (3,df_scores.loc[3,"City"], str(df_scores.loc[3,"Score"])  + "%") ]

    #Create Popup
    result_window = Tk()
    result_window.title("Your suggested travel destinations")
    result_window.geometry('1500x1000+50+50')
    result_window.attributes('-topmost', 1)
    result_window.columnconfigure(0, weight=20)
    result_window.columnconfigure(1, weight=20)
    result_window.columnconfigure(2, weight=20)
    result_window.columnconfigure(3, weight=20)

    tk.Label(result_window, text="These are your top 3 results",font=("Lucida",15,"bold")).grid(row=0, column=0)
    tk.Label(result_window, text="Rank",font=("Lucida",12,"bold")).grid(row=1, column=0)
    tk.Label(result_window, text="1",fg="gold",font=("Lucida",10,"bold")).grid(row=2, column=0)
    tk.Label(result_window, text="2").grid(row=3, column=0)
    tk.Label(result_window, text="3").grid(row=4, column=0)
    tk.Label(result_window, text="City",font=("Lucida",12,"bold")).grid(row=1, column=1)
    tk.Label(result_window, text=str(df_scores.loc[1,"City"]),fg="gold",font=("Lucida",10,"bold")).grid(row=2, column=1)
    tk.Label(result_window, text=str(df_scores.loc[2,"City"])).grid(row=3, column=1)
    tk.Label(result_window, text=str(df_scores.loc[3,"City"])).grid(row=4, column=1)
    tk.Label(result_window, text="Match",font=("Lucida",12,"bold")).grid(row=1, column=2)
    tk.Label(result_window, text=str(df_scores.loc[2,"Score"])+ "%",fg="gold",font=("Lucida",10,"bold")).grid(row=2, column=2)
    tk.Label(result_window, text=str(df_scores.loc[2,"Score"])+ "%").grid(row=3, column=2)
    tk.Label(result_window, text=str(df_scores.loc[2,"Score"])+ "%").grid(row=4, column=2)
    tk.Label(result_window, text="").grid(row=5, column=2)
    tk.Label(result_window, text="").grid(row=6, column=2)
    tk.Label(result_window, text="").grid(row=7, column=2)
    tk.Label(result_window, text="").grid(row=8, column=2)
    tk.Label(result_window, text="").grid(row=9, column=2)

    best_country = df_scores.loc[1,"Country"]
    image_path = "../images/monster_" + best_country + ".png"

    #Creates a Tkinter-compatible photo image
    img = ImageTk.PhotoImage(Image.open(image_path))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    tk.Label(result_window, image = img).grid(row=50, column=1)
    
    result_window.mainloop()



def main():
    """
    main function:
    - read data
    - get survey information from user
    - work on the data frame using the user's preferences
    - show the best travel locations
    """
    
    # load csv containing our travel location data
    test_set = pd.read_csv("../data/destinations_v5.csv", sep=";")
    
    # create a survey, ask the user for their preferences and save them as variables
    user_activity, user_season, user_prio1, user_prio2, user_prio3, user_prio4, user_prio5 = create_survey()

    # check if the user's input are valid
    check_valid_input(user_activity, user_season, user_prio1, user_prio2, user_prio3, user_prio4, user_prio5)
    
    # only keep data of the chosen season 
    test_set = get_season_data(test_set, user_season)
    
    # only keep locations for the chosen activity category
    test_set_clean = get_category_data(test_set, user_activity)
    
    # sort and rank the remaining locations accorind to the other preferences
    df_scores = rank_locations(test_set_clean, user_prio1, user_prio2, user_prio3, user_prio4, user_prio5)
    
    # display the best travel locations
    show_results(df_scores)
    
    

if __name__ == "__main__":

    # execute main function
    main()