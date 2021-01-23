# 인접 리스트 방식

# 행이 3개인 2차원 리스트로 인접 리스트를 표현한다.
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보(노드, 거리)를 저장한다.
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보를 저장한다.
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보를 저장한다.
graph[2].append((0, 5))

print(graph)

# 인접 행렬 방식에 비해 특정 두 노드가 연결되어 있는지에 대한 정보를 얻는 것이 느리다.
# 연결된 데이터를 하나하나 확인해야 하기 때문이다.

# 예를 들어 노드 1과 7이 연결되어 있는지 보려면 인접 행렬에서는 graph[1][7]을 보면 된다.
# 인접 리스트 방식에서는 노드 1의 리스트를 앞에서부터 차례대로 확인해야 한다.
# 그래서 특정 노드와 연결된 모든 인접 노드를 순회해야 한다면 인접 리스트가 메모리 낭비가 적다.