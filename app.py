from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    log_file = "/home/darshak/lineage-tracker/logs/metadata_log.txt"
    timestamps = []

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            timestamps = f.readlines()

    return render_template("index.html", timestamps=timestamps)

if __name__ == "__main__":
    app.run(debug=True)

