def read_matrix(line):
    
    size, data = line.strip().split(':')
    rows, cols = map(int, size.lower().split('x'))
    if len(data) != rows * cols:
        raise ValueError("Data length does not match matrix size")
    matrix = []
    for r in range(rows):
        row = [int(data[r*cols + c]) for c in range(cols)]
        matrix.append(row)
    return matrix, rows, cols

def neighbors(r, c, rows, cols):
   
    for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def is_isolated_cluster(matrix, cluster_cells, rows, cols):
    for r, c in cluster_cells:
        for nr, nc in neighbors(r, c, rows, cols):
            if matrix[nr][nc] == 1 and (nr, nc) not in cluster_cells:
                return False
    return True

def find_clusters(matrix, rows, cols):
    visited = [[False]*cols for _ in range(rows)]
    clusters = []

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                # DFS pentru cluster
                stack = [(r,c)]
                cluster_cells = set()
                while stack:
                    cr, cc = stack.pop()
                    if visited[cr][cc]:
                        continue
                    visited[cr][cc] = True
                    cluster_cells.add((cr,cc))
                    for nr, nc in neighbors(cr, cc, rows, cols):
                        if matrix[nr][nc] == 1 and not visited[nr][nc]:
                            stack.append((nr,nc))
                clusters.append(cluster_cells)
    return clusters

def count_clusters_by_size(matrix, clusters, rows, cols):
    counts = {1:0, 2:0, 3:0}
    for cluster in clusters:
        size = len(cluster)
        if size in counts and is_isolated_cluster(matrix, cluster, rows, cols):
            counts[size] += 1
    return counts

def main():
    with open('mat.in', 'r') as fin, open('mat.out', 'w') as fout:
        for line in fin:
            if not line.strip():
                continue
            matrix, rows, cols = read_matrix(line)
            clusters = find_clusters(matrix, rows, cols)
            counts = count_clusters_by_size(matrix, clusters, rows, cols)
            fout.write(f"{counts[1]} {counts[2]} {counts[3]}\n")

if __name__ == "__main__":
    main()
