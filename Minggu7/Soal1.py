def TowerOfHanoi(n,fromrod,torod,auxrod):
    if n==0:
        return
    TowerOfHanoi(n-1,fromrod,auxrod,torod)
    print(f"Buku {n} Pindah dari Rak {fromrod} ke {torod}")
    TowerOfHanoi(n-1,auxrod,torod,fromrod)

n=int(input())
TowerOfHanoi(n,'A','C','B')