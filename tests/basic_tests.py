from __future__ import print_function
import sys
import os
import time
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygks

def wait(description):
    print(description)
    for x in range(3, 0, -1):
        print(x)
        time.sleep(1)

class Test(unittest.TestCase):
    def test_accessible(self):
        pygks.GetKeyState
        pygks.is_all_pressed
        pygks.is_any_pressed

    def test_GetKeyState(self):
        ret = pygks.GetKeyState(pygks.VK_A)
        self.assertTrue(isinstance(ret, bool))

        wait("Please Press A Key")
        ret = pygks.GetKeyState(pygks.VK_A)
        self.assertTrue(ret)

        wait("Please Press Control Key")
        ret = pygks.GetKeyState(pygks.VK_CONTROL)
        self.assertTrue(ret)

        wait("Please Press Shift Key")
        ret = pygks.GetKeyState(pygks.VK_SHIFT)
        self.assertTrue(ret)

        wait("Please leave all Key")
        ret = pygks.GetKeyState(pygks.VK_A)
        self.assertFalse(ret)

    def test_is_all_pressed(self):
        ret = pygks.is_all_pressed(pygks.VK_A, pygks.VK_CONTROL)
        self.assertTrue(isinstance(ret, bool))

        wait("Please Press Shift + A Key")
        ret = pygks.is_all_pressed(pygks.VK_SHIFT, pygks.VK_A)
        self.assertTrue(ret)

        wait("Please Press Shift + A Key")
        ret = pygks.is_all_pressed(pygks.VK_SHIFT, pygks.VK_A, pygks.VK_CONTROL)
        self.assertFalse(ret)

    def test_is_any_pressed(self):
        ret = pygks.is_any_pressed(pygks.VK_A, pygks.VK_B)
        self.assertTrue(isinstance(ret, bool))

        wait("Please Press A Key")
        ret = pygks.is_any_pressed(pygks.VK_A)
        self.assertTrue(ret)

        wait("Please Press A Key")
        ret = pygks.is_any_pressed(pygks.VK_A)
        self.assertTrue(ret)

        wait("Please leave all Key")
        ret = pygks.is_any_pressed(pygks.VK_A)
        self.assertFalse(ret)

        wait("Please Press Shift + A Key")
        ret = pygks.is_any_pressed(pygks.VK_SHIFT, pygks.VK_A)
        self.assertTrue(ret)

        wait("Please Press Shift + A Key")
        ret = pygks.is_any_pressed(pygks.VK_SHIFT, pygks.VK_A, pygks.VK_CONTROL)
        self.assertTrue(ret)

if __name__ == "__main__":
    unittest.main()
