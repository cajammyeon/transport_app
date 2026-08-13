import pandas as pd

# consolidation 1 - stop and timing
stop_list = pd.read_csv("stops.txt")
timing_list = pd.read_csv("stop_times.txt")
timing_consol = pd.merge(stop_list, timing_list, on = "stop_id")

# consolidation 2 - stop + timing + trip
trip_list = pd.read_csv("trips.txt")
timing_consol = pd.merge(timing_consol, trip_list, on = "trip_id")

# consolidation 3 - stop + timing + trip + route 
routes_list = pd.read_csv("routes.txt")
timing_consol = pd.merge(timing_consol, routes_list, on = "route_id")

# cleanup of unused columns
drop_col = ['zone', 'trip_id', 'stop_sequence', 'timepoint', 'route_id', 'service_id', 'shape_id', 'direction_id', 'agency_id', 'route_type', 'route_color', 'route_text_color', 'fare_rule']
timing_consol = timing_consol.drop(columns = drop_col, axis = 1)

# save to csv
timing_consol.to_csv('consolidated_timing.csv', index=False)