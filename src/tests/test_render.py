# -*- coding: utf-8 -*-
#
# Poio Tools for Linguists
#
# Copyright (C) 2009-2012 Poio Project
# Author: António Lopes <alopes@cidles.eu>
# URL: <http://www.cidles.eu/ltll/poio>
# For license information, see LICENSE.TXT
"""This module contains the tests to the class
GrafRenderer.

This test serves to ensure the viability of the
methods of the class GrafRenderer in io module.
"""

import os

from xml.etree import ElementTree

from graf import Annotation, Graph, GrafRenderer, Node

class TestGrafRenderer:
    """
    This class contains the test methods of the class GrafRenderer.

    """

    def setUp(self):
        self.graph = Graph()

    def test_renderer(self):
        filename = os.path.dirname(__file__) +\
                   '/sample_files/rend-file.xml'

        comparation_filename = os.path.dirname(__file__) +\
                          '/sample_files/expected-rend-file.xml'

        node = Node('node_one')

        annotation = Annotation('Annotation_label', None, 'annotation-1')

        node.annotations.add(annotation)

        self.graph.nodes.add(node)

        graf_render = GrafRenderer(filename)
        graf_render.render(self.graph)

        expected_tree = ElementTree.parse(comparation_filename)
        result_tree = ElementTree.parse(filename)

        expected_result = set(ElementTree.tostring(i)
            for i in expected_tree.getroot())
        result = set(ElementTree.tostring(i)
            for i in result_tree.getroot())

        assert(result == expected_result)