import fitparse
import datetime
import pandas as pd

# Load the FIT file
fitfile = fitparse.FitFile("/Users/smdedar/Downloads/884_16370262203526325.fit")


## extract file_id data
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


print(get_file_id_data(fitfile))


def get_record_data(fitfile):
    df = pd.DataFrame(
        (
            (
                record.get_value("timestamp"),
                record.get_value("position_lat"),
                record.get_value("position_long"),
                record.get_value("distance"),
                record.get_value("speed"),
                record.get_value("heart_rate"),
                record.get_value("enhanced_speed"),
                record.get_value("power"),
                record.get_value("calories"),
                record.get_value("battery_soc"),
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
            "battery_soc",
        ],
    )

    return df.to_json(orient="records")

print(get_record_data(fitfile))

