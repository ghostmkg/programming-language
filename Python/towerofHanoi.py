def TowerOfHanoi(n , source, destination, auxiliary):
    if n == 1:
        print(f"1:{source}->{destination}")
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print(f"{n}:{source}->{destination}")
    TowerOfHanoi(n - 1, auxiliary, destination, source)