import pandas as pd


# extract file_id data
def get_file_id_data(fitfile):
    df = pd.DataFrame(
        (
            (
                file_id.get_value("time_created").strftime("%Y-%m-%d %H:%M:%S"),
                file_id.get_value("type"),
                file_id.get_value("manufacturer"),
                file_id.get_value("product"),
                file_id.get_value("serial_number"),
            )
            for file_id in fitfile.get_messages("file_id")
        ),
        columns=["time_created", "type", "manufacturer", "product", "serial_number"],
    )

    return df.to_json(orient="records")


# extract record data
def get_record_data(fitfile):
    df = pd.DataFrame(
        (
            (
                record.get_value("timestamp").strftime("%Y-%m-%d %H:%M:%S"),
                record.get_value("position_lat"),
                record.get_value("position_long"),
                record.get_value("distance"),
                record.get_value("speed"),
                record.get_value("heart_rate"),
                record.get_value("enhanced_speed"),
                record.get_value("power"),
                record.get_value("calories"),
            )
            for record in fitfile.get_messages("record")
        ),
        columns=[
            "timestamp",
            "position_lat",
            "position_long",
            "distance",
            "speed",
            "heart_rate",
            "enhanced_speed",
            "power",
            "calories",
        ],
    )
    return df.to_json(orient="records")


# extract event data
def get_event_data(fitfile):
    df = pd.DataFrame(
        (
            (
                event.get_value("timestamp").strftime("%Y-%m-%d %H:%M:%S"),
                event.get_value("event"),
                event.get_value("event_type"),
                event.get_value("event_group"),
                event.get_value("data"),
            )
            for event in fitfile.get_messages("event")
        ),
        columns=["timestamp", "event", "event_type", "event_group", "data"],
    )

    return df.to_json(orient="records")


def get_session_data(fitfile):
    df = pd.DataFrame(
        (
            (
                session.get_value("timestamp").strftime("%Y-%m-%d %H:%M:%S"),
                session.get_value("start_time").strftime("%Y-%m-%d %H:%M:%S"),
                session.get_value("start_position_lat"),
                session.get_value("start_position_long"),
                session.get_value("total_elapsed_time"),
                session.get_value("total_timer_time"),
                session.get_value("total_distance"),
                session.get_value("message_index"),
                session.get_value("total_calories"),
                session.get_value("avg_speed"),
                session.get_value("first_lap_index"),
                session.get_value("num_laps"),
                session.get_value("event"),
                session.get_value("event_type"),
                session.get_value("sport"),
                session.get_value("sub_sport"),
                session.get_value("avg_heart_rate"),
                session.get_value("max_heart_rate"),
                session.get_value("trigger"),
                session.get_value("enhanced_avg_speed"),
            )
            for session in fitfile.get_messages("session")
        ),
        columns=[
            "timestamp",
            "start_time",
            "start_position_lat",
            "start_position_long",
            "total_elapsed_time",
            "total_timer_time",
            "total_distance",
            "message_index",
            "total_calories",
            "avg_speed",
            "first_lap_index",
            "num_laps",
            "event",
            "event_type",
            "sport",
            "sub_sport",
            "avg_heart_rate",
            "max_heart_rate",
            "trigger",
            "enhanced_avg_speed",
        ],
    )

    return df.to_json(orient="records")


# extract activity data
def get_activity_data(fitfile):
    df = pd.DataFrame(
        (
            (
                activity.get_value("timestamp").strftime("%Y-%m-%d %H:%M:%S"),
                activity.get_value("total_timer_time"),
                activity.get_value("local_timestamp").strftime("%Y-%m-%d %H:%M:%S"),
                activity.get_value("num_sessions"),
                activity.get_value("type"),
                activity.get_value("event"),
                activity.get_value("event_type"),
            )
            for activity in fitfile.get_messages("activity")
        ),
        columns=[
            "timestamp",
            "total_timer_time",
            "local_timestamp",
            "num_sessions",
            "type",
            "event",
            "event_type",
        ],
    )
    return df.to_json(orient="records")
