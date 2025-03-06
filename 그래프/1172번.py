from collections import defaultdict, deque

def find_connected_components(n, edges):
    # 그래프 생성 (인접 리스트 방식)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)  # 정점 u에 연결된 정점 v 추가
        graph[v].append(u)  # 정점 v에 연결된 정점 u 추가 (무방향 그래프)

    # 방문 여부를 저장하는 리스트 (1부터 n까지 사용)
    visited = [False] * (n + 1)
    # 연결 요소의 개수
    component_count = 0

    def bfs(start):
        # BFS를 위한 큐 초기화
        queue = deque([start])
        while queue:
            node = queue.popleft()  # 큐에서 노드 추출
            for neighbor in graph[node]:  # 현재 노드의 인접 노드 탐색
                if not visited[neighbor]:
                    visited[neighbor] = True  # 인접 노드를 방문 처리
                    queue.append(neighbor)  # 큐에 인접 노드 추가

    # 모든 정점을 확인하며 BFS 수행
    for i in range(1, n + 1):
        if not visited[i]:  # 방문하지 않은 정점 발견 시
            visited[i] = True  # 현재 정점을 방문 처리
            bfs(i)  # 해당 정점으로부터 BFS 수행
            component_count += 1  # 연결 요소의 개수 증가

    return component_count

if __name__ == "__main__":
    # 입력 받기
    n, m = map(int, input().split())  # 정점의 개수(n)와 간선의 개수(m)
    edges = [tuple(map(int, input().split())) for _ in range(m)]  # 간선 정보 입력

    # 연결 요소의 개수 계산
    result = find_connected_components(n, edges)
    print(result)  # 결과 출력
