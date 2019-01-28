#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

class logg ():
        def __init__(self):
                logging.debug("Start process")

        def inf (self, message):
                logging.info(message)

        def db (self, message):
                logging.debug(message)
