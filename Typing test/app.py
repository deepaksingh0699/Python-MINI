from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        typed_text = request.form["typedText"]
        start_time = float(request.form["startTime"])
        end_time = time.time()

        word_count = len(typed_text.strip().split())
        time_taken = round(end_time - start_time, 2)
        wpm = round((word_count / time_taken) * 60, 2) if time_taken > 0 else 0

        return render_template("index.html", result={
            "word_count": word_count,
            "time_taken": time_taken,
            "wpm": wpm
        })

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
