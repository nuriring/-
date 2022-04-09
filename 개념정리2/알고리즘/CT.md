# 명제

![image-20220326152527124](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326152527124.png)

### 부정

![image-20220326152541005](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326152541005.png)



### 논리곱 AND

![image-20220326152601243](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326152601243.png)





### 논리합 OR

![image-20220326152611037](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326152611037.png)





### 배타적 논리합 XOR

![image-20220326152635643](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326152635643.png)



### 조건명제

![image-20220326152755979](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326152755979.png)

![image-20220326153041787](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326153041787.png)

### 역, 이, 대우

![image-20220326153057771](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326153057771.png)



### 합성

![image-20220326153221548](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326153221548.png)



### 컴퓨터는 밑이 2인 log를 사용

<img src="C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326164000874.png" alt="image-20220326164000874" style="zoom:150%;" />



![image-20220326163940236](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326163940236.png)





### 수와 표현

![image-20220326164636785](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326164636785.png)



![image-20220326164741162](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326164741162.png)





### 집합과 조합론

![image-20220326165340225](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326165340225.png)





**귀류법** : 명제의 부정을 참이라 가정하고 모순을 증명해서, 원래 명제가 참임을 보임

![image-20220326165741817](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326165741817.png)







### 기초수식

**어떠한 재귀함수의 연산량을 식으로 표현한 것**

![image-20220326170314568](C:\Users\don\AppData\Roaming\Typora\typora-user-images\image-20220326170314568.png)

```md
문제 1  T(n) = T(n-1) + 1, T(0) = 1

T(n) = T(n-1) + 1        

 = T(n-2) + 1 + 1 = T(n-2) + 2        

 = T(n-3) + 1 + 1 + 1 = T(n-3) + 3       

  = T(n-k) + 1 + ... + 1 = T(n-k) + k        

 = T(n-n) + n = T(0) + n = n+1

 O(n) = n  
```

