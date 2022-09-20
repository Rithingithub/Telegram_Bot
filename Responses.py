from datetime import datetime


def resp(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "hey how you doin !"

    if user_message in "Time":
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y , %H:%m:%S")

        return str(date_time)

   # return "error !"
