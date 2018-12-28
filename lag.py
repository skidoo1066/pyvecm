
def lag(df,features,numlag,type='pd'):
    if len(features)==len(numlag):
        if type == 'sf':
            import sframe as SF

            sf = SF.SFrame(df)

            for j in range(0,len(features)):

                feature = features[j]
                column = sf[feature]

                for i in range(1,numlag[j]+1):
                    lead = [0]*i
                    stri = str(i)
                    lead.extend(column[0:len(column)-i])
                    exec('sf["'+ feature+'lag' +stri+'"] = lead')
            sf = sf[max(numlag):len(sf)]

            return(sf)
        elif type == 'pd':

            import pandas as pd
            sf = pd.DataFrame(df)
            for j in range(0,len(features)):
                feature = features[j]
                column = sf[feature]
                for i in range(1,numlag[j]+1):
                    lead = [0]*i
                    stri = str(i)
                    lead.extend(column[0:len(column)-i])
                    exec('sf["'+ feature+'lag' +stri+'"] = lead')
            sf = sf[max(numlag):len(sf)]
            return(sf)
    else:
        print('len(features) != len(numlag)')
        return(0)
