from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Burglary', 'Alarm')])

cpd_burglary = TabularCPD(
    variable='Burglary',
    variable_card=2,
    values=[[0.999], [0.001]]
)

cpd_alarm = TabularCPD(
    variable='Alarm',
    variable_card=2,
    values=[
        [0.99, 0.05],
        [0.01, 0.95]
    ],
    evidence=['Burglary'],
    evidence_card=[2]
)

model.add_cpds(cpd_burglary, cpd_alarm)

print("Model Valid:", model.check_model())

infer = VariableElimination(model)

result = infer.query(
    variables=['Burglary'],
    evidence={'Alarm': 1}
)

print(result)
