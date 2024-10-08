from concurrent.futures import ThreadPoolExecutor
from dateutil import parser
from itertools import repeat

from utility import constants
from utility.util import timing_decorator

@timing_decorator
def get_taken_players(manager, user_id: int, user_name: str):
    taken_players = []

    transfers = manager.get_transfers_raw(manager.league.id, user_id)
    transfers = sorted(transfers, key=lambda e: e['date'])
    transfers.reverse()

    for player in manager.api.league_user_players(manager.league, user_id):
        # Default values in case the player got randomly assigned on league join
        buy_value = 0
        bought_date = constants.CUTOFF_DATE

        # Get date and value of newest buy transfer for that player
        for transfer in transfers:
            if transfer['type'] != 12 or transfer['meta']['pid'] != player.id:
                continue

            buy_value = transfer['meta']['p']
            bought_date = parser.parse(transfer['date'])

            break

        taken_players.append({'first_name': player.first_name,
                              'last_name': player.last_name,
                              'team_id': player.team_id,
                              'market_value': player.market_value,
                              'buy_price': buy_value,
                              'user': user_name,
                              'player_id': player.id,
                              'date': bought_date,
                              'position': constants.POSITIONS[player.position],
                              'trend': player.market_value_trend})

    return taken_players

@timing_decorator
def get_free_players(manager, taken_players):
    free_players = []

    taken_player_ids = [x['player_id'] for x in taken_players]

    for team_id in constants.TEAM_IDS:
        for player in manager.api.team_players(team_id):
            if player.id not in taken_player_ids:
                free_players.append({'player_id': player.id,
                                     'first_name': player.first_name,
                                     'last_name': player.last_name,
                                     'market_value': player.market_value,
                                     'points': player.totalPoints,
                                     'team_id': player.team_id,
                                     'position': constants.POSITIONS[player.position],
                                     'trend': player.market_value_trend,
                                     'averagePoints': player.averagePoints,})

    return free_players

@timing_decorator
def get_player_data(manager, team_id):
    players_data = []
    for player in manager.api.team_players(team_id):
        player_stats = manager.get(f'/leagues/{manager.league.id}/players/{player.id}/stats')

        if 'leaguePlayer' in player_stats.keys():
            manager_name = player_stats['leaguePlayer']['userName']
        else:
            manager_name = 'Computer'

        market_values = player_stats['marketValues']
        market_values.reverse()

        last_mw = {}
        for i in range(5):
            last_mw[i] = market_values[i]['m']

        players_data.append({'player_id': player.id,
                             'first_name': player.first_name,
                             'last_name': player.last_name,
                             'market_value': player_stats['marketValue'],
                             'one_day_ago': last_mw[0] - last_mw[1],
                             'two_days_ago': last_mw[1] - last_mw[2],
                             'three_days_ago': last_mw[2] - last_mw[3],
                             'team_id': player.team_id,
                             'manager': manager_name,
                             'averagePoints': player.averagePoints})

    return players_data

@timing_decorator
def get_players_mw_change(manager):
    players = []
    with ThreadPoolExecutor() as executor:
        team_ids = constants.TEAM_IDS
        players_data = executor.map(get_player_data, repeat(manager), team_ids)

        for team_data in players_data:
            players.extend(team_data)

    return players
