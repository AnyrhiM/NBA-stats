#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:29:03 2018

@author: patrickmcfarlane

playbyplay.py contains the PlayByPlay class that
enables API calls for two play-by-play (pbp) endpoints
"""

from __init__ import api_call, parse_api_call

class PlayByPlay:
    """ The PlayByPlay class contains all resources needed to use the pbp-
    related API calls. stats.nba.com has the following pbp-related
    API endpoints:
        - playbyplay: Game play-by-play with basic fields, such as
        play desscription, score, margin, period, and game time.
        - playbyplayv2: Game play-by-play with the basic fields above,
        as well as player information of those involved in the play.

    The PlayByPlay class has the following required parameters:

        @param start_period (StartPeriod in the API): String of an integer
        that corresponds to the period for which the boxscore begins.

        @param end_period (EndPeriod in the API): String of an integer that
        corresponds to the period for which the boxscore ends (Overtime
        increments logically, e.g. '5' is the first overtime period).

    Attributes:

        api_resp: JSON object of the API response. The API response
        has three keys. The 'resource' key describes the type of
        response returned ('playbyplay' in this instance). The 'parameters'
        key describes the parameters provided in the API call. The
        'resultSets' key contains the data returned in the API call.

        data: A dictionary of response names. Each response name is a
        key to a list of dictionaries containing the corresponding data.
    """

    def __init__(self, game_id, endpoint='playbyplay',
                 start_period='1', end_period='10'):

        # Controlling the parameters depending on the endpoint
        params = {'GameID': game_id,
                  'StartPeriod': start_period,
                  'EndPeriod': end_period}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)