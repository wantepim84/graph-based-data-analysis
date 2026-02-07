import networkx as nx
import matplotlib.pyplot as plt
import random
from statistics import median
from networkx.algorithms.community import greedy_modularity_communities

# 1. LOAD + PREPARE NETWORK

print("\nLOADING NETWORK")
print("----------------")
G = nx.read_edgelist(
    "ca-CondMat.txt",
    comments="#",
    delimiter="\t",
    nodetype=int,
    create_using=nx.Graph()
)
G.remove_edges_from(nx.selfloop_edges(G))

# Focus on largest connected component
largest_cc = max(nx.connected_components(G), key=len)
G = G.subgraph(largest_cc).copy()

print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
print(f"Density: {nx.density(G):.6f}")

print("\nInterpretation:")
print("Sparse collaboration structure indicates localized interaction patterns.")

# 2. INFLUENCE ANALYSIS

def analyze_influence(G):
    print("\nINFLUENCE ANALYSIS")
    print("------------------")
    deg = nx.degree_centrality(G)
    top = sorted(deg.items(), key=lambda x: x[1], reverse=True)[:10]
    for i, (node, score) in enumerate(top, 1):
        print(f"{i}. Actor {node} | Influence Score: {score:.4f}")

    print("\nExecutive framing:")
    print("These actors function as collaboration hubs accelerating knowledge flow.")

    # Visual: Top hubs
    plt.figure(figsize=(7, 4))
    plt.bar([str(n) for n, _ in top], [v for _, v in top])
    plt.title("Top Collaboration Hubs")
    plt.xlabel("Actor")
    plt.ylabel("Degree Centrality")
    plt.tight_layout()
    plt.show()

    return top

top_influencers = analyze_influence(G)

# 3. STRUCTURAL RESILIENCE SCORE

def resilience_score(G, removal_fraction=0.01):
    bet = nx.betweenness_centrality(G, k=500, seed=42)
    remove_n = max(1, int(len(G) * removal_fraction))
    critical = sorted(bet, key=bet.get, reverse=True)[:remove_n]
    H = G.copy()
    H.remove_nodes_from(critical)
    largest = len(max(nx.connected_components(H), key=len))
    score = largest / len(G)
    return score

resilience = resilience_score(G)
print("\nRESILIENCE SCORE")
print("----------------")
print(f"Score: {resilience:.3f}")
print("\nInterpretation:")
print("Measures how much collaboration connectivity survives targeted disruption.")

# 4. STRUCTURAL VULNERABILITY INDEX

def structural_vulnerability(G):
    bet = nx.betweenness_centrality(G, k=500, seed=42)
    concentration = max(bet.values())
    articulation_ratio = len(list(nx.articulation_points(G))) / len(G)
    return concentration + articulation_ratio

vulnerability = structural_vulnerability(G)
print("\nSTRUCTURAL VULNERABILITY INDEX")
print("------------------------------")
print(f"Index: {vulnerability:.3f}")
print("\nInterpretation:")
print("Higher values indicate concentrated structural dependency.")

# 5. COMMUNITY ANALYSIS + COHESION

communities = list(greedy_modularity_communities(G))
sizes = sorted([len(c) for c in communities], reverse=True)

def community_cohesion(G, communities):
    results = []
    for c in communities:
        sub = G.subgraph(c)
        results.append({
            "size": len(c),
            "density": nx.density(sub),
            "clustering": nx.average_clustering(sub)
        })
    return results

cohesion = community_cohesion(G, communities)
print("\nCOMMUNITY STRUCTURE")
print("-------------------")
print(f"Communities detected: {len(communities)}")
print(f"Largest size: {sizes[0]}")
print(f"Median size: {median(sizes)}")

print("\nExecutive interpretation:")
print("Clusters represent specialized collaboration ecosystems.")

# Visual: Top community sizes
plt.figure(figsize=(7, 4))
plt.bar(range(1, 11), sizes[:10])
plt.title("Top Community Sizes")
plt.xlabel("Community Rank")
plt.ylabel("Size")
plt.tight_layout()
plt.show()

# 6. DIFFUSION SIMULATION

def diffusion_simulation(G, seed, p=0.2, steps=5):
    active = {seed}
    for _ in range(steps):
        new_active = set(active)
        for node in active:
            for nbr in G.neighbors(node):
                if random.random() < p:
                    new_active.add(nbr)
        active = new_active
    return len(active) / len(G)

seed_actor = top_influencers[0][0]
diffusion = diffusion_simulation(G, seed_actor)

print("\nDIFFUSION SIMULATION")
print("--------------------")
print(f"Reach from hub actor: {diffusion:.3f}")
print("\nInterpretation:")
print("Estimates how efficiently knowledge spreads across the network.")

# 7. VISUAL — EGO NETWORK

ego = nx.ego_graph(G, seed_actor)
if ego.number_of_nodes() > 200:
    ego = ego.subgraph(list(ego.nodes())[:200])

plt.figure(figsize=(6, 5))
nx.draw(ego, node_size=60, edge_color="gray", with_labels=False)
plt.title("Local Collaboration Structure")
plt.tight_layout()
plt.show()

# 8. STRATEGIC INTERVENTIONS

print("\nSTRATEGIC INTERVENTIONS")
print("----------------------")
if resilience < 0.8:
    print("• Diversify collaboration bridges to improve resilience")
if vulnerability > 0.2:
    print("• Reduce dependency on structural bottlenecks")
print("• Encourage cross-community partnerships")
print("• Build redundancy in collaboration pathways")

# 9. EXECUTIVE SUMMARY

print("\nEXECUTIVE SUMMARY")
print("-----------------")
if resilience > 0.8:
    print("Network demonstrates strong resilience.")
else:
    print("Network shows vulnerability under targeted disruption.")

if vulnerability > 0.2:
    print("Structural dependencies create concentration risk.")

if diffusion > 0.5:
    print("Knowledge propagation is efficient across hubs.")

print("Collaboration clusters indicate specialization with opportunity for integration.")

# 10. MODEL BOUNDARIES

print("\nMODEL BOUNDARIES")
print("----------------")
print("Analysis reflects structural topology only.")
print("Temporal dynamics and collaboration quality not modeled.")
print("\nEND OF ANALYSIS")
