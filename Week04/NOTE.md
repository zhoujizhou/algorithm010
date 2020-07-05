#DFS模板：
递归方法
visited=set()

def dfs(node,visited):
      if node in visited:
             return

       visited.add(node)

      for next_node in nodel.children():
	if next_node not in visited:
	       dfs(next_node,visited)

非递归方法
def DFS(self,tree):
      if tree.root is None:
             return []
      visited,stack=[],[tree.toor]
      while stack:
            node=stack/pop()
            visited.add(node)
            
            process(node)
            nodes=generate_related_nodes(node)
            stack.push(nodes)

            ...

#BFS模板：
def BFS(graph,start,end):
      visited=set()
      queue=[]
      queue.append([start])
      
      while queue:
             node=queue.pop()
             visited.add(node)
             
             process(node)
             nodes= generate_related_nodes(node)
             queue.push(nodes)

      ...