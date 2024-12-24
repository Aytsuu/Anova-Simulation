#ANOVA

#importing the scipy.stats used to get the F critical
import scipy.stats

class Anova:
    #Initializing variables
    #Variables to store the correction term and sum of squares 
    corr_term, sum_of_squaresT, sum_of_squaresC, sum_of_squaresR, sum_of_squares, residual_sumE = 0, 0, 0, 0, 0, 0

    #Variables to store the Degree of Freedom
    df_rows, df_columns, df_interaction, df_residual = 0, 0, 0, 0

    #Variables to store the mean of sum of squares
    mean_SSR, mean_SSC, mean_SSG, mean_SSE = 0, 0, 0, 0

    #Variables to store the F ratio
    Fvalue_row, Fvalue_column, Fvalue_interaction = 0, 0, 0

    #Variables to store F crit
    Fcrit_row, Fcrit_column, Fcrit_interaction = 0, 0, 0

    #Level of Significance is 95%
    significance = 0.95
    
    #Class constructor
    def __init__(self,data):
        self.__data = data

    #A method to get the correction term
    def correction_term(self):
        sum = 0
        num_of_data = 0
        for g in range(len(self.__data)):
            for r in range(len(self.__data[g])):
                for c in range(len(self.__data[g][r])):
                    sum+=self.__data[g][r][c]
                    num_of_data += 1
        Anova.corr_term = (sum**2)/num_of_data

    #A method to get the Total Sum of Squares
    def SS_total(self):
        sum = 0
        for g in range(len(self.__data)):
            for r in range(len(self.__data[g])):
                for c in range(len(self.__data[g][r])):
                    sum+=(self.__data[g][r][c]**2)     
        Anova.sum_of_squaresT = sum-Anova.corr_term

    #A method to get the Sum of Squares of columns
    def SS_column(self):
        sum = 0
        column_data_count = 0
        for c in range(len(self.__data[0][0])):
            column_sum = 0
            for g in range(len(self.__data)):
                for r in range(len(self.__data[g])):
                    column_sum+=self.__data[g][r][c]
                    if c==1:
                        column_data_count+=1
            sum+=column_sum**2    
        Anova.sum_of_squaresC = (sum/column_data_count) - Anova.corr_term
    
    #A method to get the Sum of Squares of Rows
    def SS_row(self):
        sum = 0
        row_data_count = 0
        for g in range(len(self.__data)):
            row_sum = 0
            for r in range(len(self.__data[g])):
                for c in range(len(self.__data[g][r])):
                    row_sum+=self.__data[g][r][c]
                    if g == 0:
                        row_data_count += 1
            sum+=row_sum**2
        Anova.sum_of_squaresR = (sum/row_data_count) - Anova.corr_term

    #A method to get the Sum of Squares of Within Groups
    def SS_within_group(self):
        sum = 0
        group_data_count = 0
        for g in range(len(self.__data)):
            for c in range(len(self.__data[g][0])):
                group_sum = 0
                for r in range(len(self.__data[g])):
                    group_sum+=self.__data[g][r][c]
                    if c==1 and g==1:
                        group_data_count+=1
                sum+=group_sum**2
        Anova.sum_of_squaresG = (sum/group_data_count) - Anova.corr_term - Anova.sum_of_squaresC  - Anova.sum_of_squaresR
    def Residual_SSE(self):
        Anova.residual_sumE = Anova.sum_of_squaresT - Anova.sum_of_squaresC - Anova.sum_of_squaresR - Anova.sum_of_squaresG

    #A method to get the Degrees of Freedom
    def Degrees_of_freedom(self):
        rows = 0
        columns = 0
        number_of_data = 0
        for g in range(len(self.__data)):
            rows+=1
            for r in range(len(self.__data[g])):
                for c in range(len(self.__data[g][r])):
                    if g==0 and c==0:
                        number_of_data += 1
                    if g==0 and r==0:
                        columns+=1
        Anova.df_rows = rows - 1
        Anova.df_columns = columns - 1
        Anova.df_interaction = Anova.df_rows * Anova.df_columns
        Anova.df_residual = rows * columns * (number_of_data - 1)

    #A method to get the Mean of Sum of Squares 
    def Mean_SS(self):
        Anova.mean_SSR = Anova.sum_of_squaresR/Anova.df_rows
        Anova.mean_SSC = Anova.sum_of_squaresC/Anova.df_columns
        Anova.mean_SSG = Anova.sum_of_squaresG/Anova.df_interaction
        Anova.mean_SSE = Anova.residual_sumE/Anova.df_residual

    #A method to get the F-Ratio
    def F_ratio(self):
        Anova.Fvalue_row = Anova.mean_SSR/Anova.mean_SSE
        Anova.Fvalue_column = Anova.mean_SSC/Anova.mean_SSE
        Anova.Fvalue_interaction = Anova.mean_SSG/Anova.mean_SSE
    
    def F_crit(self):
        Anova.Fcrit_row = scipy.stats.f.ppf(q=Anova.significance,dfn=Anova.df_rows,dfd=Anova.df_residual)
        Anova.Fcrit_column = scipy.stats.f.ppf(q=Anova.significance,dfn=Anova.df_columns,dfd=Anova.df_residual)
        Anova.Fcrit_interaction = scipy.stats.f.ppf(q=Anova.significance,dfn=Anova.df_interaction,dfd=Anova.df_residual)

    #A method that returns a formatted string
    def display_anova(self):
        def display_SS():
            return  (f' Source of Variation     |     SS                   \n'
                    f'_________________________|___________________________\n'
                    f' Rows                    |    {Anova.sum_of_squaresR}\n'
                    f' Columns                 |    {Anova.sum_of_squaresC}\n'
                    f' Interaction             |    {Anova.sum_of_squaresG}\n'
                    f' Within                  |    {Anova.residual_sumE}  \n'
                    f' Total                   |    {Anova.sum_of_squaresT}\n'
                    )    
        def display_df():
            return  (f' Source of Variation     |     df                   \n'
                    f'_________________________|___________________________\n'
                    f' Rows                    |    {Anova.df_rows}        \n'
                    f' Columns                 |    {Anova.df_columns}     \n'
                    f' Interaction             |    {Anova.df_interaction} \n'
                    f' Within                  |    {Anova.df_residual}    \n'
                    f' Total                   |    {Anova.df_rows+Anova.df_columns+Anova.df_interaction+Anova.df_residual}\n'
                    )  
        def display_MS():
            return  (f' Source of Variation     |     MSS                  \n'
                    f'_________________________|___________________________\n'
                    f' Rows                    |    {Anova.mean_SSR}       \n'
                    f' Columns                 |    {Anova.mean_SSC}       \n'
                    f' Interaction             |    {Anova.mean_SSG}       \n'
                    f' Within                  |    {Anova.mean_SSE}       \n'
                    f' Total                   |                           \n'
                    ) 
        def display_Fratio():
            return  (f' Source of Variation     |     Fvalue               \n'
                    f'_________________________|___________________________\n'
                    f' Rows                    |    {Anova.Fvalue_row}     \n'
                    f' Columns                 |    {Anova.Fvalue_column:} \n'
                    f' Interaction             |    {Anova.Fvalue_interaction}\n'
                    f' Within                  |                           \n'
                    f' Total                   |                           \n'
                    )   
        def display_Fcrit():
            return  (f' Source of Variation     |     Fcrit                \n'
                    f'_________________________|___________________________\n'
                    f' Rows                    |    {Anova.Fcrit_row}      \n'
                    f' Columns                 |    {Anova.Fcrit_column:}  \n'
                    f' Interaction             |    {Anova.Fcrit_interaction}\n'
                    f' Within                  |                           \n'
                    f' Total                   |                           \n'
                    )     
        print(display_SS())
        print(display_df())
        print(display_MS())
        print(display_Fratio())
        print(display_Fcrit())
    
    def decision(self):
        accept_Ho = 'F-value is less than F-critical. Therefore, Accept null hypothesis'
        reject_Ho = 'F-value is greater than F-critical. Therefore, Reject null hypothesis'
        print('Row:', reject_Ho + '\n') if Anova.Fvalue_row > Anova.Fcrit_row else print('Row:',accept_Ho + '\n')
        print('Column:', reject_Ho + '\n') if Anova.Fvalue_column > Anova.Fcrit_column else print('Column:',accept_Ho + '\n')
        print('Interaction:', reject_Ho + '\n') if Anova.Fvalue_interaction > Anova.Fcrit_interaction else print('Interaction:',accept_Ho + '\n')