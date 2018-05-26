import lightgbm as lgb
import pandas as pd

def classfy(x,y,ntrain):

    train_x=x.iloc[:ntrain]
    train_y=y.iloc[:ntrain]
    valid_x=x.iloc[ntrain:]
    valid_y=y.iloc[ntrain:]

    params = {
        'learning_rate': 0.01,
        'boosting_type': 'gbdt',
        'metric': 'binary_logloss',
        'sub_feature': 0.7,
        'num_leaves': 60,
        'colsample_bytree': 0.7,
        'feature_fraction': 0.7,
        'min_data': 100,
        'min_hessian': 1,
        'verbose': 1,
    }

    lgb_train = lgb.Dataset(data=train_x.values, label=train_y.values)
    lgb_valid = lgb.Dataset(data=valid_x.values, label=valid_y.values)
    gbm = lgb.train(params,
                    lgb_train,
                    num_boost_round=1400,
                    #valid_sets=lgb_valid,
                    verbose_eval=100
                    #fobj=loglikelood,
                    #early_stopping_rounds=100,
                    #feval=score
                    )
    #pred=gbm.predict(valid_x)
    gbm.save_model('gbm_model')

if __name__ == '__main__':
    ua_pd = pd.read_pickle('user_activity_log_train.pkl')
    vc_pd = pd.read_pickle('video_create_log_train.pkl')
    al_pd = pd.read_pickle('app_launch_log_train.pkl')

    train_line=[x for x in al_pd.columns if 'sum_7' in str(x)]

    al_pd_t = al_pd[al_pd['sum_7_16'] > 0]
    vc_pd_t = vc_pd[vc_pd['sum_7_16'] > 0]
    ua_pd_t = ua_pd[ua_pd['sum_7_16'] > 0]

    al_pd_te = al_pd[al_pd['sum_7_9'] > 0]
    vc_pd_te = vc_pd[vc_pd['sum_7_9'] > 0]
    ua_pd_te = ua_pd[ua_pd['sum_7_9'] > 0]

    train_label=pd.concat([al_pd_t['user_id'],vc_pd_t['user_id'],ua_pd_t['user_id']],axis=0)
    train_th=pd.concat([al_pd_te['user_id'],vc_pd_te['user_id'],ua_pd_te['user_id']],axis=0)

    sublist = train_label.value_counts().index.values
    tr = [x for x in sublist if x != 'All']

    sublist2 = train_th.value_counts().index.values
    te = [x for x in sublist2 if x != 'All']

    train=pd.Series(tr).to_frame('user_id')
    train['v_train']=1

    test = pd.Series(te).to_frame('user_id')
    test['v_test'] = 1

    all=pd.merge(train,test,on='user_id',how='outer').fillna(0)
    #print(all)
    from utils import *
    def fls_pd(data):
        return f1s(data['v_test'], data['v_train'])
    f1_bef=all.apply(fls_pd,axis=1)
    ele=f1_bef.value_counts().to_dict()
    tl=precesion(ele['TP'],0, ele['FN'], ele['FP'])
    print(tl)


