

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple, Any
import heapq

# -----------------------------
# Building ADT
# -----------------------------
@dataclass
class Building:
    building_id: int
    name: str
    location: str

    def __repr__(self):
        return f"({self.building_id}) {self.name}: {self.location}"

# -----------------------------
# Binary Search Tree (BST)
# -----------------------------
class BSTNode:
    def __init__(self, building: Building):
        self.building = building
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

class BinarySearchTree:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, building: Building):
        def _insert(node: Optional[BSTNode], building: Building) -> BSTNode:
            if node is None:
                return BSTNode(building)
            if building.building_id < node.building.building_id:
                node.left = _insert(node.left, building)
            elif building.building_id > node.building.building_id:
                node.right = _insert(node.right, building)
            else:
                # duplicate id - update
                node.building = building
            return node
        self.root = _insert(self.root, building)

    def search(self, building_id: int) -> Optional[Building]:
        node = self.root
        while node:
            if building_id == node.building.building_id:
                return node.building
            elif building_id < node.building.building_id:
                node = node.left
            else:
                node = node.right
        return None

    def inorder(self) -> List[Building]:
        res: List[Building] = []
        def _in(node: Optional[BSTNode]):
            if not node: return
            _in(node.left)
            res.append(node.building)
            _in(node.right)
        _in(self.root)
        return res

    def preorder(self) -> List[Building]:
        res: List[Building] = []
        def _pre(node: Optional[BSTNode]):
            if not node: return
            res.append(node.building)
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
        return res

    def postorder(self) -> List[Building]:
        res: List[Building] = []
        def _post(node: Optional[BSTNode]):
            if not node: return
            _post(node.left)
            _post(node.right)
            res.append(node.building)
        _post(self.root)
        return res

    def height(self) -> int:
        def _h(node: Optional[BSTNode]) -> int:
            if not node: return 0
            return 1 + max(_h(node.left), _h(node.right))
        return _h(self.root)

# -----------------------------
# AVL Tree
# -----------------------------
class AVLNode:
    def __init__(self, building: Building):
        self.building = building
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.height: int = 1

class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def _get_height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _update_height(self, node: AVLNode):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _balance_factor(self, node: Optional[AVLNode]) -> int:
        if not node: return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right
        # rotation
        x.right = y
        y.left = T2
        # update heights
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left
        # rotation
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    def insert(self, building: Building):
        def _insert(node: Optional[AVLNode], building: Building) -> AVLNode:
            if not node:
                return AVLNode(building)
            if building.building_id < node.building.building_id:
                node.left = _insert(node.left, building)
            elif building.building_id > node.building.building_id:
                node.right = _insert(node.right, building)
            else:
                node.building = building
                return node

            self._update_height(node)
            bf = self._balance_factor(node)
            # LL
            if bf > 1 and building.building_id < node.left.building.building_id:
                return self._rotate_right(node)
            # RR
            if bf < -1 and building.building_id > node.right.building.building_id:
                return self._rotate_left(node)
            # LR
            if bf > 1 and building.building_id > node.left.building.building_id:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
            # RL
            if bf < -1 and building.building_id < node.right.building.building_id:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
            return node
        self.root = _insert(self.root, building)

    def _traverse_inorder(self, node: Optional[AVLNode], res: List[Building]):
        if not node: return
        self._traverse_inorder(node.left, res)
        res.append(node.building)
        self._traverse_inorder(node.right, res)

    def inorder(self) -> List[Building]:
        res: List[Building] = []
        self._traverse_inorder(self.root, res)
        return res

    def height(self) -> int:
        return self._get_height(self.root)

# -----------------------------
# Graph (Adjacency List and Matrix)
# -----------------------------
class CampusGraph:
    def __init__(self):
        self.nodes: Dict[int, Building] = {}  # id -> Building
        self.adj_list: Dict[int, List[Tuple[int, float]]] = {}  # id -> list of (neighbor_id, weight)

    def add_building(self, building: Building):
        self.nodes[building.building_id] = building
        if building.building_id not in self.adj_list:
            self.adj_list[building.building_id] = []

    def add_edge(self, id1: int, id2: int, weight: float = 1.0, undirected: bool = True):
        if id1 not in self.adj_list or id2 not in self.adj_list:
            raise KeyError('Both nodes must be added before adding an edge')
        self.adj_list[id1].append((id2, weight))
        if undirected:
            self.adj_list[id2].append((id1, weight))

    def adjacency_matrix(self) -> Tuple[List[List[float]], List[int]]:
        ids = sorted(self.nodes.keys())
        id_to_index = {bid: i for i, bid in enumerate(ids)}
        n = len(ids)
        INF = float('inf')
        mat = [[INF] * n for _ in range(n)]
        for i in range(n):
            mat[i][i] = 0.0
        for u, neighbors in self.adj_list.items():
            for v, w in neighbors:
                i = id_to_index[u]
                j = id_to_index[v]
                mat[i][j] = w
        return mat, ids

    def bfs(self, start_id: int) -> List[int]:
        from collections import deque
        visited = set()
        order: List[int] = []
        q = deque([start_id])
        visited.add(start_id)
        while q:
            u = q.popleft()
            order.append(u)
            for v, _ in self.adj_list.get(u, []):
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return order

    def dfs(self, start_id: int) -> List[int]:
        visited = set()
        order: List[int] = []
        def _dfs(u: int):
            visited.add(u)
            order.append(u)
            for v, _ in self.adj_list.get(u, []):
                if v not in visited:
                    _dfs(v)
        _dfs(start_id)
        return order

    def dijkstra(self, source_id: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
        dist: Dict[int, float] = {node: float('inf') for node in self.nodes}
        prev: Dict[int, Optional[int]] = {node: None for node in self.nodes}
        dist[source_id] = 0.0
        heap = [(0.0, source_id)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in self.adj_list.get(u, []):
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(heap, (alt, v))
        return dist, prev

    def shortest_path(self, src: int, dest: int) -> Tuple[float, List[int]]:
        dist, prev = self.dijkstra(src)
        if dist[dest] == float('inf'):
            return float('inf'), []
        path = []
        u = dest
        while u is not None:
            path.append(u)
            u = prev[u]
        path.reverse()
        return dist[dest], path

    def kruskal_mst(self) -> Tuple[float, List[Tuple[int,int,float]]]:
        # gather edges
        edges: List[Tuple[float,int,int]] = []
        for u, nbrs in self.adj_list.items():
            for v, w in nbrs:
                edges.append((w, u, v))
        # for undirected graph each edge appears twice; keep only u<v to avoid duplicates
        edges_unique = []
        seen = set()
        for w,u,v in edges:
            key = tuple(sorted((u,v)))
            if key in seen: continue
            seen.add(key)
            edges_unique.append((w,u,v))
        edges_unique.sort()
        # DSU
        parent = {node: node for node in self.nodes}
        rank = {node: 0 for node in self.nodes}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry: return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True
        mst_edges: List[Tuple[int,int,float]] = []
        total_cost = 0.0
        for w,u,v in edges_unique:
            if union(u,v):
                mst_edges.append((u,v,w))
                total_cost += w
        return total_cost, mst_edges

# -----------------------------
# Expression Tree (for energy bill calculations)
# -----------------------------
class ExprNode:
    def __init__(self, value: Any, left: Optional[ExprNode] = None, right: Optional[ExprNode] = None):
        self.value = value
        self.left = left
        self.right = right

class ExpressionTree:
    def __init__(self):
        self.root: Optional[ExprNode] = None

    @staticmethod
    def build_from_postfix(tokens: List[str]) -> ExprNode:
        stack: List[ExprNode] = []
        operators = set(['+', '-', '*', '/', '^'])
        for t in tokens:
            if t not in operators:
                stack.append(ExprNode(float(t)))
            else:
                # operator
                right = stack.pop()
                left = stack.pop()
                stack.append(ExprNode(t, left, right))
        return stack[-1]

    @staticmethod
    def evaluate(node: ExprNode) -> float:
        if node is None:
            return 0.0
        if node.left is None and node.right is None:
            return float(node.value)
        op = node.value
        l = ExpressionTree.evaluate(node.left)
        r = ExpressionTree.evaluate(node.right)
        if op == '+': return l + r
        if op == '-': return l - r
        if op == '*': return l * r
        if op == '/': return l / r
        if op == '^': return l ** r
        raise ValueError('Unknown operator ' + str(op))

# -----------------------------
# Demonstration / Example Usage
# -----------------------------
def demo():
    # Sample buildings
    buildings = [
        Building(10, 'Admin Block', 'Central administrative offices'),
        Building(20, 'Library', 'East side, 3 floors'),
        Building(5, 'Canteen', 'North quad'),
        Building(15, 'Computer Science', 'Block B, 2nd floor'),
        Building(25, 'Auditorium', 'South complex'),
        Building(7, 'Laboratory', 'Block C, ground floor'),
        Building(30, 'Hostel', 'West wing')
    ]

    print('\n---- BST and AVL Demonstration ----')
    bst = BinarySearchTree()
    avl = AVLTree()
    for b in buildings:
        bst.insert(b)
        avl.insert(b)

    print('\nBST traversals (inorder):')
    print(bst.inorder())
    print('\nBST traversals (preorder):')
    print(bst.preorder())
    print('\nBST traversals (postorder):')
    print(bst.postorder())
    print('\nBST height:', bst.height())

    print('\nAVL inorder:')
    print(avl.inorder())
    print('AVL height:', avl.height())

    print('\n---- Graph Demonstration ----')
    g = CampusGraph()
    for b in buildings:
        g.add_building(b)
    # add weighted undirected edges (distances in meters)
    g.add_edge(10, 20, 100)
    g.add_edge(10, 5, 50)
    g.add_edge(5, 7, 30)
    g.add_edge(20, 15, 70)
    g.add_edge(15, 25, 120)
    g.add_edge(7, 15, 90)
    g.add_edge(25, 30, 200)

    print('\nAdjacency List:')
    for k,v in sorted(g.adj_list.items()):
        print(k, '->', v)

    mat, ids = g.adjacency_matrix()
    print('\nAdjacency Matrix (rows/cols ordered by building IDs):', ids)
    for row in mat:
        # show INF as -
        print(['-' if x==float('inf') else x for x in row])

    start = 10
    print('\nBFS from Admin Block (10):', g.bfs(start))
    print('DFS from Admin Block (10):', g.dfs(start))

    # Dijkstra from Admin Block to Hostel
    dist, path = g.shortest_path(10, 30)
    if dist == float('inf'):
        print('\nNo path found from 10 to 30')
    else:
        print(f'\nShortest path 10 -> 30: distance = {dist}, path = {path}')

    # Kruskal MST
    cost, mst_edges = g.kruskal_mst()
    print('\nKruskal MST total cost:', cost)
    print('MST edges (u,v,w):', mst_edges)

    print('\n---- Expression Tree Demonstration ----')
    # Example: energy bill expression: (units * rate) + fixed_charge
    # For demonstration, tokens are in postfix: units rate * fixed +
    tokens = ['350', '2.5', '*', '50', '+']  # (350 * 2.5) + 50
    expr_root = ExpressionTree.build_from_postfix(tokens)
    bill = ExpressionTree.evaluate(expr_root)
    print('Energy bill (for 350 units @2.5 + 50 fixed):', bill)

if __name__ == '__main__':
    demo()







































