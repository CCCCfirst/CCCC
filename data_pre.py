import pandas as pd

'''
仔细看看能不能得到特殊日期，周六日一类的

某个id的粉丝，出了就看，可能性
'''

def read_csv(name,col):
    pd_tmp=pd.read_csv(name,header=None,sep='\t')
    #print(pd_tmp)
    pd_tmp.columns=col
    return pd_tmp


if __name__ == '__main__':

    ur_pd_col=['user_id','register_day','register_type','device_type']
    ur_pd=read_csv('user_register_log.txt',ur_pd_col)

    al_pd_col=['user_id','day']
    al_pd=read_csv('app_launch_log.txt',al_pd_col)

    vc_pd_col=['user_id','day']
    vc_pd=read_csv('video_create_log.txt', vc_pd_col)

    ua_pd_col=['user_id','day','page','video_id','author_id','action_type']
    ua_pd=read_csv('user_activity_log.txt', ua_pd_col)

    #user_id=pd.concat([ur_pd['user_id'],al_pd['user_id']],axis=0)
    #print(user_id.value_counts())

    xpd=al_pd

    for col in xpd:
        print (col)
        print(xpd[col].value_counts())
