## change to sframes
def diff(df,features,numlag,type='pd'):
    if type == 'pd':
        import pandas as pd
        sf = pd.DataFrame(df)
        for j in range(0,len(features)):
            feature = features[j]
            exec("sf['d"+feature+"1']= sf['"+feature+"']-sf['"+feature+"lag1']")
            for i in range(2,numlag[j]+1):
                stri = str(i)
                stri1 = str(i-1)
                exec('sf["d'+feature+stri+'"] = sf["'+feature+'lag'+stri1+'"]-sf["'+feature+'lag'+stri+'"]')
        return(sf)

    if type == 'sf':
        import sframe as SF
        sf = SF.SFrame(df)
        for j in range(0,len(features)):
            feature = features[j]
            exec("sf['d"+feature+"1']= sf['"+feature+"']-sf['"+feature+"lag1']")
            for i in range(2,numlag[j]+1):
                stri = str(i)
                stri1 = str(i-1)
                exec('sf["d'+feature+stri+'"] = sf["'+feature+'lag'+stri1+'"]-sf["'+feature+'lag'+stri+'"]')
        return(sf)
