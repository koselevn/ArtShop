from flask import Flask, request, jsonify
import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    database='ArtGallery',
    cursorclass=pymysql.cursors.DictCursor
)