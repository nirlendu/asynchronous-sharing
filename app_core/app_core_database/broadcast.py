# -*- coding: utf-8 -*-

import inspect
import sys, os

from py2neo import Graph, ServiceRoot

from libs.logger import app_logger as log


def check_parent_broadcast(
        broadcast_parent_id
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Checking parent broadcast')

    graphdb_url = os.environ.get('GRAPHDB_URL')
    graph = ServiceRoot(graphdb_url).graph

    query = "MATCH (p:ExpressionGraph{expression_id:{broadcast_parent_id}}), (e:ExpressionGraph), (p)-[:BROADCAST_OF]->(e) return e"
    is_parent_broadcast = graph.cypher.stream(query, parameters={'broadcast_parent_id': broadcast_parent_id})
    for each in is_parent_broadcast:
        return each[0]['expression_id']
    return None


def new_broadcast_relation(
        transaction,
        expression_id,
        broadcast_parent_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Creating New Broadcast Realationship')

    query = "MATCH (p:ExpressionGraph{expression_id:{broadcast_parent_id}}),(e:ExpressionGraph{expression_id:{expression_id}}) CREATE (e)-[:BROADCAST_OF]->(p)"

    transaction.append(query, parameters={'expression_id': expression_id,
                                          'broadcast_parent_id': broadcast_parent_id})

    return transaction
