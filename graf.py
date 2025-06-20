import networkx as nx

def input_graph(n):
    print(f"\nInput untuk Graf {n}")
    V = int(input("Jumlah simpul: "))
    E = int(input("Jumlah sisi: "))
    G = nx.Graph()
    print("Masukkan sisi sebagai pasangan u v (dipisah spasi):")
    for _ in range(E):
        u, v = input().split()
        G.add_edge(u, v)
    return G

def main():
    print("== Cek Isomorfisme Dua Graf ==")
    G1 = input_graph("G1")
    G2 = input_graph("G2")

    if nx.is_isomorphic(G1, G2):
        print("\n✔️ Graf G1 dan G2 adalah isomorfik")
    else:
        print("\n❌ Graf G1 dan G2 tidak isomorfik")

if __name__ == "__main__":
    main()