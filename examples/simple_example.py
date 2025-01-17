# -*- coding: utf-8 -*-
#
# Poio Tools for Linguists
#
# Copyright (C) 2009-2012 Poio Project
# Author: António Lopes <alopes@cidles.eu>
# URL: <http://media.cidles.eu/poio/>
# For license information, see LICENSE.TXT

import sys
from graf import Node, Graph, Edge, FeatureStructure, Annotation, GrafRenderer

# Create three nodes
node_one = Node('node_one')
node_two = Node('node_two')
node_three = Node('node_three')

# Create the Annotation Graph and set the values
graph = Graph()

#Adding the nodes
graph.nodes.add(node_one)
graph.nodes.add(node_two)
graph.nodes.add(node_three)

# Create an edge
edge = graph.create_edge(node_one, node_three)

# Add Features
feature_strct = FeatureStructure() # Structure

# Adding two features
# There are two ways to it.
# Use the simple first
# Setting up all the features to the annotation
feature_strct['feature1'] = 'value_1'
feature_strct['feature2'] = 'value_2'

# Adding the features to annotations
annotation = Annotation('label', feature_strct)
annotation.features['another_feature'] = 'value_another'
annotation.features['feature3'] = 'value_3'

# Adding the annotations to the node
node_one.annotations.add(annotation)

# Rendering the Graph
graf_render = GrafRenderer("output.xml")
graf_render.render(graph)
