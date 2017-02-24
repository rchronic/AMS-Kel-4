import snap

# save and load from a text file
snap.SaveEdgeList(Graph, "facebook_combined.txt", "Save as tab-separated list of edges")
Graph = snap.LoadEdgeList(PUNGraph, "facebook_combined.txt", 0, 1)
# Graph.Dump()
snap.PlotInDegDistr(Graph, "try_facebook_combined", "Undirected Graph - In-Degree Distribution")