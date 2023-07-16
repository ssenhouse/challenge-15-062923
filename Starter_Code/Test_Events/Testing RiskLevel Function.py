

def get_recommendation(risk_level):
    risk_level = 'None'
    risklevels = {'None':'100% bonds (AGG), 0% equities (SPY)',
                  'low':'60% bonds (AGG), 40% equities (SPY)',
                  'medium':'40% bonds (AGG), 60% equities (SPY)',
                  'high':'20% bonds (AGG), 80% equities (SPY)'}
    
    return risklevels[risk_level]

    print[risk_level]