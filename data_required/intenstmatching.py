
from main import *
def definefun():
    speak("Please specify more clearly.")
    return "Please specify more clearly."
intent_to_function = {
    "open_email": lambda _:send_email(),
    "send_whatsapp_message":send_whatsapp_message,
    "open_whatsapp": open_whatsapp,
    "open_command_prompt": open_cmd,
    "open_settings": opensetting,
    "open_camera": open_camera,
    "capture_photo": capture_photo,
    "open_notepad": open_notepad,
    "jarwis_status_sleep":lambda _: toggle_jarwis_mode("sleep"),
    "jarwis_status_wakeup":lambda _: toggle_jarwis_mode("wakeup"),
    "open_discord": open_discord,
    "send_email": lambda _:send_email(),
    "tell_joke": tell_random_joke,
    "translate_text":lambda query: translate_text(query),
    "open_google": open_google,
    "search_wikipedia":lambda query: get_wikipedia_summary(query),
    "search_google":lambda query: search_google(query),
    "open_youtub": open_youtube,
    "search_youtube":lambda query: search_youtube(query),
    "check_battery": battey_persentage,
    "previous_activities": remind_last_activity,
    "minimize_window": minimize_screen,
    "maximize_window": maximize_screen,
    "close_window":close_window,
    "tell_time":tell_time,
    "exit":exit,
    "uncomplete":definefun,

}


