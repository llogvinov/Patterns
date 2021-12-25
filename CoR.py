#!/usr/bin/env python
# coding: utf-8

# In[30]:


from abc import abstractmethod


# In[47]:


class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


# In[93]:


class EventGet:
    def __init__(self, _type):
        self._type = _type
        self.name = "get"

class EventSet:
    def __init__(self, value):
        self.value = value
        self.name = "set"


# In[109]:


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


# In[113]:


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.name == "get":
            if event._type is int:
                return obj.integer_field
            
        elif event.name == "set":
            if isinstance(event.value, int):
                obj.integer_field = event.value
                return
            
        return super().handle(obj, event)

class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.name == "get":
            if event._type is float:
                return obj.float_field
            
        elif event.name == "set":
            if isinstance(event.value, float):
                obj.float_field = event.value
                return
            
        return super().handle(obj, event)

class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.name == "get":
            if event._type is str:
                return obj.string_field
            
        elif event.name == "set":
            if isinstance(event.value, str):
                obj.string_field = event.value
                return
            
        return super().handle(obj, event)

