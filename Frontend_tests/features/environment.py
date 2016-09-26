from page_objects import *
from selenium import webdriver
import logging


def before_all(context):
    context.driver = webdriver.Firefox()


def after_all(context):
    context.driver.close()
