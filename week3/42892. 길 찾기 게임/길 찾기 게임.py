import sys
sys.setrecursionlimit(100000)

def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)) :
        nodeinfo[i].append(i+1)
        
    nodeinfo.sort(key=lambda x : x[1])
    maxx = -1
    layers = []
    c = 0
    layer = []
    for i in range(len(nodeinfo)) :
        if nodeinfo[i][1] > maxx :
            c += 1
            maxx = nodeinfo[i][1]
            layers.append(layer)
            layer = []
        nodeinfo[i][1] = c
        layer.append(nodeinfo[i])
    layers.append(layer)
    
    nodeinfo.sort(key=lambda x : -x[1])
    root = nodeinfo[0][2]
    
    nodeinfo.sort(key=lambda x: x[2])
    
    left = [-1 for _ in range(len(nodeinfo)+1)]
    right = [-1 for _ in range(len(nodeinfo)+1)]
    
    def make_tree(l, r, cur, level) :
        if level == 1 : return
        x, y, id = nodeinfo[cur-1]
        for nx, ny, nid in layers[level-1] :
            if l<nx<x :
                left[cur] = nid
                make_tree(l, x, nid, level-1)
            elif x<nx<r :
                right[cur] = nid
                make_tree(x, r, nid, level-1)
    
    make_tree(-1, 100001, root, c)


    pre = []
    def pre_order(cur) :
        pre.append(cur)
        if left[cur] != -1 :
            pre_order(left[cur])
        if right[cur] != -1 :
            pre_order(right[cur])
    pre_order(root)
    
    post = []
    def post_order(cur) :
        if left[cur] != -1 :
            post_order(left[cur])
        if right[cur] != -1 :
            post_order(right[cur])
        post.append(cur)
    post_order(root)
        
        
    answer.append(pre)
    answer.append(post)
        
    return answer