"""Backward-compatible facade over data.py.

`info` is consumed by the chatbot (name/pronoun) and the contact form (email).
All real content now lives in data.py — edit there, not here.
"""

from data import PROFILE, ABOUT

info = {
    "Pronoun": "his",
    "Name": "Hamid",
    "Full_Name": PROFILE["name"],
    "Title": PROFILE["title"],
    "Intro": PROFILE["title"],
    "Tagline": PROFILE["tagline"],
    "About": ABOUT,
    "City": PROFILE["location"],
    "Email": PROFILE["email"],
    "LinkedIn": PROFILE["links"]["LinkedIn"],
    "GitHub": PROFILE["links"]["GitHub"],
    "Portfolio": PROFILE["links"]["Portfolio"],
}
