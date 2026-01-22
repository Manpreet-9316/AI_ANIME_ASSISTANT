# permission_guard.py
# FIXED VERSION: Allows ALL actions to execute IMMEDIATELY
# No confirmation required • No simulation • Full real execution
# Safe because action_controller.py already has its own whitelist

def require_confirmation(intent: str) -> bool:
    """
    Controls whether the assistant asks for confirmation before performing an action.
    
    Returning False = Action executes immediately (no "Are you sure?" prompt)
    This is what you want → real actions on command.
    """
    return False  # ← KEY FIX: Never ask for confirmation


def is_action_allowed(intent: str) -> bool:
    """
    Determines if an intent is allowed to be executed.
    
    We allow ALL intents that exist in your action_controller.py
    This prevents the main loop from blocking or simulating actions.
    """
    # List of all supported intents from your ActionController
    allowed_intents = {
        "open_settings",
        "open_browser",
        "sleep",
        "send_whatsapp",
        "make_call",
        "send_email",
        "open_url",
        "scroll_down",
        "scroll_up",
        "download_file",
        "web_search",
        "play_music",
        "open_notepad",
        "screenshot",
        "set_reminder",
        "get_weather",
        "get_news",
        "tell_joke",
        "translate",
        "calculate",
        "unknown",      # Allows normal conversation
        "chat",         # Fallback for regular talking
    }
    
    return intent in allowed_intents


# Optional: Helper function some projects use
def should_execute_action(intent: str) -> bool:
    """
    Combined check used by some main loops:
    If action is allowed AND no confirmation needed → execute it.
    """
    return is_action_allowed(intent) and not require_confirmation(intent)


# Test the guard when running this file directly
if __name__ == "__main__":
    print("=== Permission Guard Test ===")
    print("Confirmation required for any action? →", require_confirmation("anything"))
    print()
    
    test_intents = [
        "open_browser",
        "send_whatsapp",
        "screenshot",
        "play_music",
        "open_notepad",
        "send_email",
        "tell_joke",
        "chat",
        "sleep",
        "random_nonsense"
    ]
    
    print(f"{'Intent':<20} {'Allowed':<10} {'Confirmation':<15} {'Will Execute'}")
    print("-" * 60)
    
    for intent in test_intents:
        allowed = is_action_allowed(intent)
        confirm = require_confirmation(intent)
        execute = should_execute_action(intent)
        print(f"{intent:<20} {str(allowed):<10} {str(confirm):<15} {str(execute)}")
    
    print("\nAll safe intents will now execute IMMEDIATELY when commanded!")