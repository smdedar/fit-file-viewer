from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import fitparse
import json
import pathlib

from .utils import (
    get_file_id_data,
    get_record_data,
    get_event_data,
    get_session_data,
    get_activity_data,
)

app = Flask(__name__)


@app.route("/wakeup", methods=["GET"])
def wakeup():
    return jsonify({"message": "Server Wakeup"})


@app.route("/servercheck", methods=["POST"])
def server_check():
    if "file" not in request.files:
        return jsonify({"status": "error", "message": "No file part"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"status": "error", "message": "No selected file"})

    filename = secure_filename(file.filename)
    file_extension = pathlib.Path(filename).suffix

    if file_extension not in [".fit", ".txt"]:
        return jsonify(
            {"status": "error", "message": "File extension is not .fit or .txt"}
        )

    try:
        fitfile = fitparse.FitFile(file)

        file_id_raw = get_file_id_data(fitfile)
        file_id_data = json.loads(file_id_raw)
        record_raw = get_record_data(fitfile)
        record_data = json.loads(record_raw)
        event_raw = get_event_data(fitfile)
        event_data = json.loads(event_raw)
        session_raw = get_session_data(fitfile)
        session_data = json.loads(session_raw)
        activity_raw = get_activity_data(fitfile)
        activity_data = json.loads(activity_raw)

        data = {
            "status": "ok",
            "file_id": file_id_data,
            "record": record_data,
            "event": event_data,
            "session": session_data,
            "activity": activity_data,
        }
        return jsonify(data)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
