#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 01:54:04 2020

@author: apn
"""

import logging
logging.basicConfig(level=logging.DEBUG, filename='website.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logging.info(f"New Session started \n {'-'*80}")
logging.debug('Debug message')
logging.info('All running good')
logging.warning('Watch out!')

logger = logging.getLogger("website_logger")