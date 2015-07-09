# Script to create blog post table
import sqlite3

with sqlite3.connect("blog.db") as connection:
    # Get DB cursor
    c = connection.cursor()
    # Create posts table
    c.execute("""CREATE table posts (title TEXT, post TEXT)""")
    # Insert entries
    c.execute('INSERT into posts VALUES("Good", "I\'m good")')
    c.execute('INSERT into posts VALUES("Well", "I\'m well")')
    c.execute('INSERT into posts VALUES("Excellent", "I\'m excellent")')
    c.execute('INSERT into posts VALUES("Okay", "I\'m okay")')
