import tkinter as Tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [{"suit": suit, "rank": rank} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


if __name__ == "__main__":
    deck = create_deck()
    print(f"Created a shuffled deck with {len(deck)} cards.")
    
