
# coding: utf-8

# # LAB 2
# ## 2. Logistic regression
# 
# 
# ### 데이터 설명
# 
# - 설명변수 (25개) 
#     - ID, AGE, INCOME, SEX, MARRIED (1: 결혼, 0: 미혼)
#     - FICO (신용점수), OWNHOME (자가 주택 소유 여부, 1: 소유), LOC (거주지, A-H)
#     - BUY6, 12, 18 (최근 6, 12, 18개월 간의 구입 횟수),VALUE24 (지난 24개월 간의 구입 총액),ORGSRC (고객 분류), DISCBUY (할인 고객 여부, 1: 할인 고객), RETURN24 (지난 24개월 간 상품 반품 여부), COA6 (6개월 간의 주소변경 여부, 1: 주소변경)
# - 반응변수: RESPOND (DM에 대한 반응 여부)
# 
# ### 데이터 불러오기

# In[1]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split

buy=pd.read_table('buytest.txt', delimiter=" ")

print('Data head \n', buy.head())
print('Data shape: ',buy.shape)


# In[2]:


print('The number of missing data: ', buy.isnull().sum())

# 결측치 제거
buy_com = buy.dropna()
buy_com = buy_com.drop(["ID"], axis = 1)
print(buy_com.shape)
buy_com.describe().transpose()


# - 범주형 변수에 대해 가변수 생성 : SEX, LOC, ORGSRC

# In[3]:


buy_com = pd.get_dummies(buy_com, drop_first=True,                            
                         columns= ['SEX', 'LOC', 'ORGSRC'])


# In[4]:


buy_com.shape


# - C1~C7, PURCHTOT은 RESPOND의 원인이 아니라 결과이므로 입력변수에서 제외

# In[5]:


buydata = buy_com.drop(["C1","C2","C3","C4","C5","C6","C7","PURCHTOT","CLIMATE"]
                       , axis = 1)


# - 데이터셋 분할

# In[6]:


train, test = train_test_split(buydata, test_size = 0.3, random_state = 1)
print('train dim: ',train.shape,'\n test dim:', test.shape)
y_train = train.loc[:,"RESPOND"]
X_train = train.drop("RESPOND", axis = 1)

y_test = test.loc[:,"RESPOND"]
X_test = test.drop("RESPOND", axis = 1)
print(X_train.shape, y_train.shape)


# ### 탐색적 자료 분석
# - 반응 변수의 분포

# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns
count = y_train.value_counts()
ratio = count[0]/count[1]
count.plot(kind = 'bar')
plt.title('The distribution of RESPOND in Training set'+
          "\n# of (Y=0): # of (Y=1) =  %0.2f" % ratio + ": 1")
plt.ylabel('Frequency')
plt.show()


# In[8]:


count = y_test.value_counts()
ratio = count[0]/count[1]
count.plot(kind = 'bar')
plt.title('The distribution of RESPOND in Test set'+
          "\n# of (Y=0): # of (Y=1) =  %0.2f" % ratio + ": 1")
plt.ylabel('Frequency')
plt.show()


# ### 로지스틱 회귀분석

# In[9]:


import statsmodels.api as sm


X_train["intercept"] = 1.0 # for intercept
print('X_train dim: ',X_train.shape)
print('rank of X_train^TX_train: ',np.linalg.matrix_rank(X_train.values))

logit = sm.Logit(y_train,X_train)
logit_res = logit.fit(maxiter = 1000)
print(logit_res.summary2())


# - 오즈비

# In[10]:


print(np.exp(logit_res.params))


# - 확률 예측

# In[11]:


pred = logit_res.predict(X_train) # fitted probability
pred


# ### 사후 추출법을 이용하여 표본 생성

# In[12]:


cc_train0 = train.loc[y_train == 0,:]
cc_train1 = train.loc[y_train == 1,:]     
print('train dim: ', train.shape , '\n train y=0 dim:', cc_train0.shape,
      '\n train y=1 dim:', cc_train1.shape)


# In[13]:


cc_train, dummy= train_test_split(cc_train0, train_size = 2000, random_state = 123)
print(cc_train.shape)


# In[14]:


cc_train = pd.concat([cc_train, cc_train1], axis=0)

y_train1 = cc_train["RESPOND"]
X_train1 = cc_train.drop("RESPOND", axis = 1)
X_train1["intercept"] = 1

print("case control X train dim",X_train1.shape)
print("case control y train dim",y_train1.shape)


# In[15]:


count = y_train1.value_counts()
ratio = count[0]/count[1]
count.plot(kind = 'bar')
plt.title('The distribution of RESPOND in Case-Control Train set'+
          "\n# of (Y=0): # of (Y=1) =  %0.2f" % ratio + ": 1")
plt.show()


# - 로지스틱 회귀모형 적합

# In[16]:


# logistic
logit1 = sm.Logit(y_train1,X_train1)
logit_cc = logit1.fit(maxiter = 1000)
print(logit_cc.summary2())
print('rank of X_train^TX_train: ',np.linalg.matrix_rank(X_train1.values))


# - 오즈비 비교

# In[17]:


np.exp(logit_res.params)


# In[18]:


np.exp(logit_cc.params)


# ### 참고: scikit-learn 모듈을 이용한 로지스틱 회귀분석
# 
# - 목적함수:
# $$ \frac{1}{2} \sum_{j=1}^p \beta_j^2 + C*(-\text{log-likelihood})$$

# In[19]:


from sklearn.linear_model import LogisticRegression
logit = LogisticRegression(penalty = 'l2', C = 1e10, fit_intercept = False,
                          random_state = 42).fit(X_train, y_train)


# In[20]:


logit.coef_


# In[21]:


pred_class = logit.predict(X_train)
pred_prob = logit.predict_proba(X_train)

print(pred_class[:5])
print(pred_prob[:5])

