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
                   course INTEGER NOT NULL (mark BETWEEN 1 AND 5))
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY,
                   user_id INTEGER NOT NULL REFERENSES users(id),
                   pass TEXT NOT NULL,
                   fio TEXT NOT NULL,
                   group_id INTEGER NOT NULL REFERENSES groups(id))
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS marks(
                   id INTEGER PRIMARY KEY,
                   student_id INTEGER NOT NULL REFERENSES students(id) ON DELETE CASCADE,
                   lesson_id INTEGER NOT NULL REFERENSES lessons(id),
                   mark INTEGER NOT NULL CHECK(mark BETWEEN 2 AND 5),
                   date DATE NOT NULL,
                   semester INTEGER NOT NULL)
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS attendance(
                   id INTEGER PRIMARY KEY,
                   student_id INTEGER NOT NULL REFERENSES students(id) ON DELETE CASCADE,
                   lesson_id INTEGER NOT NULL REFERENSES lessons(id),
                   date DATE NOT NULL,
                   status TEXT NOT NULL (status IN ('P', 'N', 'NB', 'NU')))
                   ''')

    con.commit()
    con.close()
    