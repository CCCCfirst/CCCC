import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':

    al_pd=pd.read_pickle('user_activity_log.pkl').astype(int)
    tmp0=al_pd
    tmp0['v']=1
    tmp=tmp0[['user_id','day','v']]
    x=tmp.pivot_table('v', index='user_id', columns='day', aggfunc='sum', margins=True, fill_value=0).astype(int)
    x['user_id']=x.index
    x.reset_index(drop=True,inplace=True)
    #print(x[1])
    #print(x)
    print('begin')
    for s in range(7,8):
        print(s)
        for i in range(1,31-s):
            print(i)
            nbegin=i
            nend=i+s
            tmp=x[[d for d in range(nbegin,nend)]]
            #print([d for d in range(nbegin, nend)])
            x['sum_'+str(s)+'_'+str(i)]=tmp.apply(lambda x:x.sum(),axis=1)
            #print(tmp)
            #os.system('pause')
    #print(x)
    x.to_pickle('user_activity_log_train.pkl')

    '''

    #os.system('pause')

    register_day_num=ur_pd['action_type']#.hist(bins=5,rwidth=0.8,log=True)
    print(register_day_num.value_counts())
    os.system('pause')
    register_day_num.plot()
    plt.show()
    '''