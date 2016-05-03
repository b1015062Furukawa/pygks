import ctypes
from . import keycode

user32 = ctypes.windll.user32

def GetKeyState(keycode):
    """Check the key pressed

    Args:
        key (int): such as pygks.VK_A, pygks.VK_SHIFT, ...

    Returns:
        bool: Whether the key is pressed

    Raises:
        KeyError: If key is not supported in this module

    Examples:
        >>get_key_state(pygks.VK_A)
        True
        >>get_key_state('VK_SHIFT')
        False

    """
    if user32.GetKeyState(keycode) & 0x8000:
        return True
    else:
        return False

def is_all_pressed(*keycode_args):
    """Check the given keys all pressed

    Args:
        *keycode_args: keys which you want to check it pressed

    Returns:
        bool: Whether the key is pressed

    Raises:
        KeyError: If the key is not supported in this module

    Examples:
        >>is_all_pressed('VK_SHIFT', 'VK_CONTROL', 'n')
        True

    """
    for key in keycode_args:
        if not GetKeyState(key):
            return False
    return True

def is_any_pressed(*keycode_args):
    """Check any of the given keys pressed

    Args:
        *keycode_args: keys which you want to check it pressed

    Returns:
        bool: Whether any of the keys is pressed

    Raises:
        KeyError: If the key is not supported in this module

    Examples:
        >>is_all_pressed('VK_SHIFT', 'VK_CONTROL', 'n')
        True

    """
    for key in keycode_args:
        if GetKeyState(key):
            return True
    return False
