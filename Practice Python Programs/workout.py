workout_log= [1,1,1,0,1,0,1,0,1,1,1,0,1]
curnt_stk=0
max_stk=0
for i in workout_log:
    if i==1:
        curnt_stk+=1
        max_stk=max(curnt_stk, max_stk)
    else:
        curnt_stk=0
    
    
    print(f"At {i} streak is {curnt_stk}")
    
print(max_stk)
