"""
Tests for PyPoE.poe.file.psg

Overview
===============================================================================

+----------+------------------------------------------------------------------+
| Path     | tests/PyPoE/poe/file/test_psg.py                                 |
+----------+------------------------------------------------------------------+
| Version  | 1.0.0a0                                                          |
+----------+------------------------------------------------------------------+
| Revision | $Id$                  |
+----------+------------------------------------------------------------------+
| Author   | Omega_K2                                                         |
+----------+------------------------------------------------------------------+

Description
===============================================================================



Agreement
===============================================================================

See PyPoE/LICENSE
"""

# =============================================================================
# Imports
# =============================================================================

# 3rd-party
import pytest

# Python
from PyPoE.poe.file import psg
from PyPoE.poe.file.dat import DatFile

# self

# =============================================================================
# Setup
# =============================================================================

# =============================================================================
# Fixtures
# =============================================================================

# =============================================================================
# Tests
# =============================================================================


def test_psg(file_system, rr):
    f = psg.PSGFile(passive_skills_dat_file=rr)
    f.read(file_system.get_file("Metadata/PassiveSkillGraph.psg"))
