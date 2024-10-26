import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from textblob import TextBlob

# Sample data for tourist spots and reviews
tourist_spots = [
    "Eiffel Tower",
    "Statue of Liberty",
    "Taj Mahal",
    "Great Wall of China",
    "Machu Picchu",
    "Golden Temple",
    "Jaipur's Amer Fort",
    "Kerala Backwaters",
    "Goa Beaches",
    "Hampi Ruins",
    "Gateway of India (Mumbai)",
    "Marine Drive (Mumbai)",
    "Elephanta Caves (Mumbai)",
    "Agra Fort",
    "Qutub Minar (Delhi)",
    "Red Fort (Delhi)",
    "Varanasi Ghats",
    "Rajasthan's City Palace",
    "Rann of Kutch",
    "Jaisalmer Fort",
    "Kolkata's Victoria Memorial",
    "Mysore Palace",
    "Kochi's Fort Kochi",
    "Jodhpur's Mehrangarh Fort",
    "Amritsar's Wagah Border",
    "Kashmir's Dal Lake",
    "Ajanta and Ellora Caves",
    "Ooty's Botanical Gardens",
    "Darjeeling's Tiger Hill",
    "Pondicherry's French Quarter",
]

# Initialize an empty dictionary to store reviews for each spot
reviews = {spot: [] for spot in tourist_spots}

# Function to get the colored emoji representation based on the sentiment score
def get_colored_emoji(sentiment_score):
    if sentiment_score >= 0.7:
        return "😄"  # Very positive
    elif sentiment_score >= 0.3:
        return "😊"  # Positive
    elif sentiment_score >= -0.3:
        return "😐"  # Neutral
    elif sentiment_score >= -0.7:
        return "😕"  # Negative
    else:
        return "😢"  # Very negative

# Function to update the progress bar and sentiment label
def update_sentiment(event=None):
    spot_name = combo_var.get()
    review = review_entry.get("1.0", "end").strip()

    if review == "":
        progress_bar["value"] = 0
        progress_label.config(text="Sentiment: 0.00%", foreground="black")
        sentiment_result.config(text="")
        return

    blob = TextBlob(review)
    sentiment_score = blob.sentiment.polarity # type: ignore
    reviews[spot_name].append((review, sentiment_score))

    progress = sum(score for _, score in reviews[spot_name]) / len(reviews[spot_name])
    progress_bar["value"] = (progress + 1) * 50

    colored_emoji = get_colored_emoji(sentiment_score)
    progress_label.config(text=f"Sentiment: {progress*100:.2f}% {colored_emoji}", foreground="black")

    sentiment_msg = "Good to go!" if sentiment_score >= 0 else "Consider other options."
    sentiment_result.config(text=sentiment_msg)

# Function to show the next tourist spot
def show_next_spot():
    spot_name = combo_var.get()
    next_index = (tourist_spots.index(spot_name) + 1) % len(tourist_spots)
    combo_var.set(tourist_spots[next_index])
    progress_bar["value"] = 0
    progress_label.config(text="Sentiment: 0.00%", foreground="black")
    sentiment_result.config(text="")
    review_entry.delete("1.0", "end")

# Function to show a message box when the user clicks the "Submit" button
def submit_response():
    messagebox.showinfo("Response Submitted", "Your response is successfully submitted!")
    review_entry.delete("1.0", "end")  # Clear the text entry after submission

# Function to display the results in a separate window
def show_results():
    results_window = tk.Toplevel(root)
    results_window.title("Results")
    results_window.geometry("400x500")

    results_text = tk.Text(results_window, width=60, height=20)
    results_text.pack(padx=20, pady=20)

    for spot_name, spot_reviews in reviews.items():
        sentiment_scores = [score for _, score in spot_reviews]
        if sentiment_scores:
            average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
            if average_sentiment >= 0:
                sentiment_result = "Positive review"
            else:
                sentiment_result = "Bad review"
            results_text.insert(tk.END, f"{spot_name}: {sentiment_result}\n")

    results_text.config(state="disabled")

# Calculate the width based on the maximum length of tourist spot names
max_spot_length = max(len(spot) for spot in tourist_spots)
combo_width = max_spot_length + 5  # Add some extra space for aesthetics

# GUI setup
root = tk.Tk()
root.title("Tourist Spot Sentiment Analysis")
root.geometry("400x500")

# Change the theme to 'clam' for a modern look
root.style = ttk.Style() # type: ignore
root.style.theme_use("clam") # type: ignore

# Create a frame to center-align contents
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

combo_var = tk.StringVar()
combo_var.set(tourist_spots[0])
combo = ttk.Combobox(frame, textvariable=combo_var, values=tourist_spots, width=combo_width)
combo.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

review_entry = tk.Text(frame, height=6, width=30)
review_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Customize button styles with an accent color
style = ttk.Style()
style.configure("Accent.TButton", background="#0078d4", foreground="white")
next_button = ttk.Button(frame, text="Next", command=show_next_spot, style="Accent.TButton")
submit_button = ttk.Button(frame, text="Submit", command=submit_response, style="Accent.TButton")
next_button.grid(row=2, column=1, padx=10, pady=10)
submit_button.grid(row=2, column=0, padx=10, pady=10)

# Customize progress bar color
style.configure("Green.Horizontal.TProgressbar", foreground="green", background="green")
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate", style="Green.Horizontal.TProgressbar")
progress_bar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Set a custom font for labels
custom_font = ("Helvetica", 12)
progress_label = ttk.Label(frame, text="Sentiment: 0.00%", font=custom_font, foreground="black")
sentiment_result = ttk.Label(frame, text="", font=custom_font, foreground="black")
progress_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
sentiment_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

results_button = ttk.Button(frame, text="Results", command=show_results, style="Accent.TButton")
results_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Bind the update_sentiment function to the KeyRelease event of the review_entry
review_entry.bind("<KeyRelease>", update_sentiment)

root.mainloop()