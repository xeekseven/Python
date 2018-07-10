int[] parents = null;
private int Find (int x) {
    if (x == parents[x]) {
        return x;
    }
    return parents[x] = Find (parents[x]); // 路径压缩
}

private void Union (int x, int y) {
    int px = Find (x);
    int py = Find (y);
    parents[px] = py;
}


int[] parents = new int[weakGridList.Count];
for (int i = 0; i < parents.Length; ++i) {
    parents[i] = i;
}
Dictionary<int, List<WeakGrid>> idItemsDic = new Dictionary<int, List<WeakGrid>> ();
//计算连续栅格
for (int i = 0; i < weakGridList.Count - 1; ++i) {
    for (int j = 0; j < weakGridList.Count; ++j) {
        double dDistance = MathFuncs.GetDistance (weakGridList[i].CentLng, weakGridList[i].CentLat, weakGridList[j].CentLng, weakGridList[j].CentLat);
        if (dDistance < 2 * GridSize) {
            Union (i, j);
        }
    }
}
// 同类合并
for (int i = 0; i < parents.Length; ++i) {
    int par = Find (i);
    if (!idItemsDic.ContainsKey (par)) {
        idItemsDic.Add (par, new List<WeakGrid> ());
    }
    idItemsDic[par].Add (weakGridList[i]);
}