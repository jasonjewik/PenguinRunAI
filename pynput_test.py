#!/usr/bin/env python
# coding: utf-8

# In[39]:


from pynput import keyboard
from pynput.keyboard import Key, Controller

from threading import Timer


# In[45]:


kb = Controller()


# In[41]:


def press_and_release_space():
    kb.press(Key.space)
    kb.release(Key.space)


# In[47]:


t = Timer(3, press_and_release_space)
t.start()


# In[42]:


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


# In[43]:


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


# In[46]:


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


# In[ ]:




