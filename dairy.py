#Программа-дневник
import csv
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import base64
import os

#Для начала соберём часть с БД (айди, ФИО студента, курс, год обучения (исчисляется из послдней цифры курса), предмет, оценка/Посещение(Н,НБ))

def init_db():
    con = sqlite3.connect("dairy.db")
    cursor = con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY,
                   login TEXT NOT NULL UNIQUE,
                   pass TEXT NOT NULL,
                   fio TEXT NOT NULL,
                   role CHAR NOT NULL (role IN ('s', 't', 'o')))
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS groups(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   course INTEGER NOT NULL (course IN (1,2,3,4,5)))
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY,
                   user_id INTEGER NOT NULL REFERENSES users(id),
                   pass TEXT NOT NULL,
                   fio TEXT NOT NULL,
                   group_id INTEGER NOT NULL REFERENSES groups(id))
                   ''')
    