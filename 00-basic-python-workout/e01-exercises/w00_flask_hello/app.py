import sqlite3
from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/api/songs", methods=["GET", "POST"])
def collection():
    if request.method == "GET":
        all_songs = get_all_songs()
        return json.dumps(all_songs)
    elif request.method == "POST":
        data = request.form
        result = add_song(data["artist"], data["title"], data["rating"])
        return jsonify(result)


@app.route("/api/songs/<song_id>", methods=["GET", "PUT", "DELETE"])
def resource(song_id):
    if request.method == "GET":
        song = get_single_song(song_id)
        return json.dumps(song)
    elif request.method == "PUT":
        data = request.form
        result = edit_song(song_id, data["artist"], data["title"], data["rating"])
        return jsonify(result)
    elif request.method == "DELETE":
        result = remove_song(song_id)
        return jsonify(result)


def add_song(artist, title, rating):
    try:
        with sqlite3.connect("songs.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO songs
                  (artist, title, rating)
                VALUES
                  (?, ?, ?)
            """, (artist, title, rating))
            result = {"status": "OK", "message": "Song added"}
    except Exception as err:
        result = {"status": "ERROR", "message": f"Error adding song: {err}"}

    return result


def get_all_songs():
    with sqlite3.connect("songs.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM songs ORDER BY id asc
        """)
        all_songs = cursor.fetchall()
        return all_songs


def get_single_song(song_id):
    with sqlite3.connect("songs.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM songs WHERE id = ?
        """, (song_id)
        )
        song = cursor.fetchone()
        return song

def edit_song(song_id, artist, title, rating):
    try:
        with sqlite3.connect("songs.db") as connection:
            connection.execute("""
                UPDATE songs
                   SET artist = ?,
                       title = ?,
                       rating = ?
                 WHERE ID = ?;
            """, (artist, title, rating, song_id))
            result = {"status": "OK", "message": "song edited"}
    except Exception as err:
        result = {"status": "ERROR", "message": f"Error while updating song: {err}"}

    return result


def remove_song(song_id):
    try:
        with sqlite3.connect("songs.db") as connection:
            connection.execute("""
                DELETE FROM songs
                 WHERE ID = ?;
            """, (song_id))
            result = {"status": "OK", "message": "song removed"}
    except Exception as err:
        result = {"status": "ERROR", "message": f"error while removing song: {err}"}

    return result

if __name__ == "__main__":
    app.debug = True
    app.run()
