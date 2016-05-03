from . import keycode
import ctypes

__version__ = '0.1.0'

user32 = ctypes.windll.user32

def get_key_state(key):
    """Check the key pressed

    Args:
        key (str): 'a-z' or '0-9' or Windows Virtual-Key Codes("https://msdn.microsoft.com/ja-jp/library/windows/desktop/dd375731")

    Returns:
        bool: Whether the key is pressed

    Raises:
        KeyError: If key is not supported in this module

    Examples:
        >>get_key_state('a')
        True
        >>get_key_state('VK_SHIFT')
        False

    """
    code = keycode.convert_to_keycode(key)
    if user32.GetKeyState(code) & 0x8000:
        return True
    else:
        return False

def is_all_pressed(*key_args):
    """Check the given keys all pressed

    Args:
        *key_args: keys which you want to check it pressed

    Returns:
        bool: Whether the key is pressed

    Raises:
        KeyError: If the key is not supported in this module

    Examples:
        >>is_all_pressed('VK_SHIFT', 'VK_CONTROL', 'n')
        True

    """
    for key in key_args:
        if not get_key_state(key):
            return False
    return True

def is_any_pressed(*key_list):
    """Check any of the given keys pressed

    Args:
        *key_args: keys which you want to check it pressed

    Returns:
        bool: Whether any of the keys is pressed

    Raises:
        KeyError: If the key is not supported in this module

    Examples:
        >>is_all_pressed('VK_SHIFT', 'VK_CONTROL', 'n')
        True

    """
    for key in key_args:
        if get_key_state(key):
            return True
    return False
