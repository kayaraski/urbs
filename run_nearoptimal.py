import os
import shutil
import nopt
import ipdb

input_files = 'Intertemporal-Germany'  # for single year file name, for intertemporal folder name
input_dir = 'Input'
input_path = os.path.join(input_dir, input_files)

result_name = 'Int-DE'
result_dir = nopt.prepare_result_directory(result_name)  # name + time stamp

# copy input file to result directory
try:
    shutil.copytree(input_path, os.path.join(result_dir, input_dir))
except NotADirectoryError:
    shutil.copyfile(input_path, os.path.join(result_dir, input_files))
# copy run file to result directory
shutil.copy(__file__, result_dir)

# objective is a list of tuples. Last element of the Tuple must be the optimization objective. Objectives must be chosen from input process list
# Site names that will be subjected to the minimization must be given before the objective name.
# No site name indicates minimize/maximize total capacity of all sites
# example objectives
# [(site A, site B, Process A),(site C, Process B)] or
# [(process A), (site B, process B)] or
# [(site A, cost)]

objective = [('Photovoltaics')]
# Choose Solver (cplex, glpk, gurobi, ...)
solver = 'gurobi'

# simulation timesteps
(offset, length) = (300, 24)  # time step selection
timesteps = range(offset, offset+length+1)
dt = 1  # length of each time step (unit: hours)

# detailed reporting commodity/sites
report_tuples = [(2050, ['Germany'], 'Elec'),
(2040, ['Germany'], 'Elec'),
(2030, ['Germany'], 'Elec'),
(2020, ['Germany'], 'Elec')

    ]

# optional: define names for sites in report_tuples
report_sites_name = {}

# plotting commodities/sites
plot_tuples = [  (2050, ['Germany'], 'Elec')]

# optional: define names for sites in plot_tuples
plot_sites_name = {}

# plotting timesteps
plot_periods = {
    'all': timesteps[1:]
}

# add or change plot colors
my_colors = {}
for country, color in my_colors.items():
    nopt.COLORS[country] = color

# select scenarios to be run
scenarios = [
             nopt.scenario_TM80_ccs,
            ]

for scenario in scenarios:
    prob = nopt.run_scenario(input_path, solver, timesteps, scenario,
                             result_dir, dt, objective,
                             plot_tuples=plot_tuples,
                             plot_sites_name=plot_sites_name,
                             plot_periods=plot_periods,
                             report_tuples=report_tuples,
                             report_sites_name=report_sites_name)
