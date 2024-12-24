#SIMULATION FOR TWO-WAY ANALYSIS OF VARIANCE (WITH REPLICATION)
from ANOVA import Anova

#fetching data from input and storing it in a 3D list
data = eval(input("Enter data\n--> "))

#using reference object to access the methods in the class Anova
method = Anova(data)
method.correction_term()
method.SS_total()
method.SS_column()
method.SS_row()
method.SS_within_group()
method.Residual_SSE()
method.Degrees_of_freedom()
method.Mean_SS()
method.F_ratio()
method.F_crit()

#displaying the result
print('\n\n\tAnalysis of Variance\n')
method.display_anova()

#displays the decision
print('\n\n\tDecision\n')
method.decision()

# Data set 1
# [[[10,5],[7,4],[9,7],[6,4],[8,5]],[[5,3],[4,4],[6,5],[3,1],[2,2]]]

# Data set 2
# [[[4.8,5,6.4,6.3],[4.4,5.2,6.2,6.4],[3.2,5.6,4.7,5.6],[3.9,4.3,5.5,4.8],[4.4,4.8,5.8,5.8]],[[4.4,4.9,5.8,6],[4.2,5.3,6.2,4.9],[3.8,5.7,6.3,4.6],[3.7,5.4,6.5,5.6],[3.9,4.8,5.5,5.5]]]

# Data set 3
# [[[4,7,10],[5,8,11],[5,9,12],[6,12,19],[5,3,15]],[[4,12,10],[4,12,12],[6,13,13],[6,15,13],[5,13,12]]]
