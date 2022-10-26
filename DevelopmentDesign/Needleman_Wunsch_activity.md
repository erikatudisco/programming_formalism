First copy the pseudo code into the markdown code ticks
```
for i in length(A):
   F(i,0) = p * i
for j in length(B):
   F(0,j) = p * j
for i in length(A):
   for j in length(B):
      match = F(i-1, j-1) + S(A(i), B(j))
      delete = F(i-1, j) + p
      insert = F(i, j-1) + p
      F(i,j) = max(match, delete, insert)
```
```plantuml
@startuml
start
repeat: i in length(A);
   -F(i,0) = p * i
repeat while
repeat: j in length(B);
   -F(0,j) = p * j
repeat while 
repeat: i in length(A);
    repeat: j in length(B);
        -match = F(i-1, j-1) + S(A(i), B(j))
        -delete = F(i-1, j) + p
        -insert = F(i, j-1) + p
        - F(i,j) = max(match, delete, insert)
    repeat while 
repeat while (i < length(A)) is (true) not(F(i,j)) 
stop
@enduml
```

```plantuml
@startuml

@enduml
```