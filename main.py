import tkinter
import generator
import random

top = tkinter.Tk()

with open("./tweets/tweets_realDonaldTrump_sanitized.txt") as f:
    real_tweets = f.readlines()

rng = random.Random()
showing_results = False
choice_1_text = tkinter.StringVar()
choice_2_text = tkinter.StringVar()
results_button_text = tkinter.StringVar()
results_button_text.set("Show results")
results_text = tkinter.StringVar()
real_tweet_pos = 0
num_correct = 0
num_done = 0

def generate_choices():
    global real_tweet_pos
    real_tweet = rng.choice(real_tweets)
    fake_tweet = generator.generate_tweet()
    if bool(rng.getrandbits(1)):
        real_tweet_pos = 2
        choice_1_text.set(fake_tweet)
        choice_2_text.set(real_tweet)
    else:
        real_tweet_pos = 1
        choice_1_text.set(real_tweet)
        choice_2_text.set(fake_tweet)

def on_choose_choice_1():
    global num_correct, num_done
    if real_tweet_pos == 1:
        num_correct = num_correct + 1
    num_done = num_done + 1
    generate_choices()
    show_results_button.config(state = tkinter.NORMAL)

def on_choose_choice_2():
    global num_correct, num_done
    if real_tweet_pos == 2:
        num_correct = num_correct + 1
    num_done = num_done + 1
    generate_choices()
    show_results_button.config(state = tkinter.NORMAL)

def on_show_results():
    global showing_results, num_done, num_correct
    showing_results = not showing_results
    if showing_results:
        choice_1.config(state = tkinter.DISABLED)
        choice_2.config(state = tkinter.DISABLED)
        results_button_text.set("Restart")
        results_text.set("You rated Donald Trump more human " + str(int(100 * (num_correct / num_done))) + "% of the time")
    else:
        choice_1.config(state = tkinter.NORMAL)
        choice_2.config(state = tkinter.NORMAL)
        results_button_text.set("Show results")
        results_text.set("")
        num_done = 0
        num_correct = 0
        show_results_button.config(state = tkinter.DISABLED)

choice_1 = tkinter.Button(top, textvariable = choice_1_text, command = on_choose_choice_1, justify = tkinter.LEFT, wraplength = 200)
choice_2 = tkinter.Button(top, textvariable = choice_2_text, command = on_choose_choice_2, justify = tkinter.LEFT, wraplength = 200)

generate_choices()

top.columnconfigure(0, minsize = 200, weight = 1)
top.columnconfigure(1, minsize = 200, weight = 1)
top.rowconfigure(0, minsize = 100, weight = 1)
top.rowconfigure(1, minsize = 100, weight = 1)

choice_1.grid(row = 0, column = 0, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W, padx = 5, pady = 5)
choice_2.grid(row = 0, column = 1, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W, padx = 5, pady = 5)

show_results_button = tkinter.Button(top, textvariable = results_button_text, command = on_show_results)

show_results_button.grid(row = 1, column = 0, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W, padx = 5, pady = 5)
show_results_button.config(state = tkinter.DISABLED)

results_label = tkinter.Label(top, textvariable = results_text, wraplength = 200)

results_label.grid(row = 1, column = 1, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W, padx = 5, pady = 5)

top.mainloop()