from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'JohnCalls'),
    ('Alarm', 'MaryCalls')
])

cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, 
                        values=[[0.999, 0.71, 0.06, 0.05], 
                                [0.001, 0.29, 0.94, 0.95]], 
                        evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2])
cpd_johncalls = TabularCPD(variable='JohnCalls', variable_card=2, 
                            values=[[0.95, 0.1], [0.05, 0.9]], 
                            evidence=['Alarm'], evidence_card=[2])
cpd_marycalls = TabularCPD(variable='MaryCalls', variable_card=2, 
                            values=[[0.99, 0.3], [0.01, 0.7]], 
                            evidence=['Alarm'], evidence_card=[2])

model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls)

assert model.check_model()

inference = VariableElimination(model)
prob_burglary_given_johncalls = inference.query(variables=['Burglary'], evidence={'JohnCalls': 1})
print(prob_burglary_given_johncalls)
