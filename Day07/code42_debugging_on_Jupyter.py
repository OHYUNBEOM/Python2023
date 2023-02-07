# %% [markdown]
# # 주피터 노트북 사용법 학습
# 
# ## 마크다운, 파이썬 셀 추가, 파이썬 셀 실행 : 단축키
# - 현재 셀 앞에 셀 추가 : a
# - 현재 셀 뒤에 셀 추가 : b
# - 현재 셀을 마크다운으로 변경 : m 
# - 현재 셀을 코드 셀로 변경 : y
# - 셀 실행 : Ctrl + Enter
# - 셀 실행 + 다음 셀로 이동(셀 없을 시 생성) : Shift + Enter
# - 셀 실행 + 다음 셀 생성 : Alt + Enter
# - 주석 처리 : Ctrl + K + C

# %%
print('Hello Jupyter!')

# %% [markdown]
# # 디버깅
# - 디버그 쉘 : Ctrl + Shift + Alt + Enter

# %%
arr = [1,'2',True,'Hello',3.14]
for i in arr:
    print(i)

# %% [markdown]
# ## 함수 디버깅

# %%
def add(x,y):
    return x+y
def div(x,y):
    return x/y
print(add(15,15))
print(div(15,0))

# %%
print(div(15,0))


