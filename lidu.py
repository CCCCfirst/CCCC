import pandas as pd
import os

def bef_ana():
    t=pd.read_pickle('user_activity_log_all.pkl')
    ur_pd=pd.read_pickle('user_register_log.pkl')

    for nbefored in range(2,13):
        #nbegin = i
        #nend = i + s
        s_fin=pd.DataFrame()
        for d in range(1,31-nbefored-7):
            print(d)
            reg_usr=ur_pd[ur_pd['register_day']<=d]
            reg_tmp=reg_usr[['user_id']]
            #print([x for x in range(d,nbefored+d)])
            #print([x for x in range(nbefored+d, nbefored + d+7)])
            tmp=t[['user_id','sum_'+str(nbefored)+'_'+str(d),'sum_'+str(7)+'_'+str(nbefored+d)]]
            fin=pd.merge(reg_tmp,tmp,how='inner',on='user_id')
            fin['i']=nbefored+d
            fin.columns=['user_id','bef','label','i']
            print(fin.shape)
            s_fin=pd.concat([s_fin,fin],axis=0)
        s_fin.to_pickle('tmp/bef_ua_'+str(nbefored)+'.pkl')
    print(t.columns)
    print(t.head(10))

if __name__ == '__main__':
    f1_bef_list=[]
    bef_ana()
    for i in range(2,13):
        print(i)
        tmp=pd.read_pickle('tmp/bef_ua_' + str(i) + '.pkl')
        f1_relation=tmp.apply(f1s_pd,axis=1 )
        f1_bef_list.append(f1_relation.value_counts().to_dict())
    k=2
    for ele in f1_bef_list:
        print(ele)
        print(k,':  ',precesion(ele['TP'],ele['TN'],ele['FN'],ele['FP']))
        k=k+1