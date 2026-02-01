<h1>Graph-Based Network Analysis</h1>
<h3>Identifying Influence, Structure, and Risk in Relational Data</h3>

<hr>

<h2>Overview</h2>

<p>
Many real-world datasets are fundamentally <strong>relational</strong>: people collaborate, users interact,
systems depend on one another, molecules form structures.
Traditional tabular analysis often misses the structure hidden in these relationships.
</p>

<p>
This repository demonstrates how <strong>graph-based analysis</strong> can be used to extract interpretable insights
about <strong>influence, connectivity, and structural risk</strong> from large relational datasets using
Python and NetworkX.
</p>

<p>
While the example shown here uses an academic collaboration network, the same methods apply broadly to:
</p>

<ul>
  <li>Chemistry and materials science</li>
  <li>Organizational and collaboration networks</li>
  <li>SaaS and marketplace platforms</li>
  <li>Fraud and risk detection</li>
  <li>Knowledge graphs and recommendation systems</li>
</ul>

<hr>

<h2>Problem Framing</h2>

<p>
Large networks often appear robust at first glance, but in practice:
</p>

<ul>
  <li>Influence is concentrated among a small subset of nodes</li>
  <li>Connectivity depends on key structural bridges</li>
  <li>Removing the wrong nodes can fragment the system</li>
</ul>

<p>
This project focuses on answering four practical questions:
</p>

<ol>
  <li>Who are the most influential nodes?</li>
  <li>Which nodes act as bridges between groups?</li>
  <li>How does the network naturally segment into communities?</li>
  <li>How resilient is the network to targeted disruption?</li>
</ol>

<hr>

<h2>Data</h2>

<ul>
  <li><strong>Dataset:</strong> arXiv Condensed Matter collaboration network</li>
  <li><strong>Nodes:</strong> Authors</li>
  <li><strong>Edges:</strong> Co-authorship relationships</li>
  <li><strong>Graph type:</strong> Undirected, unweighted</li>
  <li><strong>Size:</strong> ~23,000 nodes, ~187,000 edges</li>
  <li><strong>Source:</strong> Stanford Network Analysis Project (SNAP)</li>
  <li><strong>License:</strong> Public dataset</li>
</ul>

<p>
The analysis focuses on the <strong>largest connected component</strong> to reflect the core collaboration structure.
</p>

<hr>

<h2>Modelling Choices</h2>

<p>
The network is modelled with intentional simplicity:
</p>

<ul>
  <li>Undirected graph (collaboration is mutual)</li>
  <li>Unweighted edges (focus on structure, not volume)</li>
  <li>Self-loops removed</li>
  <li>No temporal dynamics included</li>
</ul>

<p>
These choices keep the analysis interpretable and aligned with real-world decision-making.
</p>

<hr>

<h2>Analysis Approach</h2>

<p>
A small number of interpretable graph metrics are used, each tied to a concrete question:
</p>

<ul>
  <li><strong>Degree centrality</strong> — Who has the broadest collaborative reach?</li>
  <li><strong>Betweenness centrality</strong> — Which nodes act as structural bridges?</li>
  <li><strong>Community detection</strong> — How does the network naturally cluster?</li>
  <li><strong>Component analysis</strong> — How concentrated or fragmented is collaboration?</li>
</ul>

<p>
The emphasis is on <strong>clarity and insight</strong>, not exhaustive metric coverage.
</p>

<hr>

<h2>Key Findings (High-Level)</h2>

<ul>
  <li>Influence is highly concentrated among a small number of nodes</li>
  <li>A limited set of nodes act as bridges between otherwise weakly connected communities</li>
  <li>The network exhibits strong community structure, indicating specialization</li>
  <li>The system is resilient to random disruption but vulnerable to targeted removal</li>
</ul>

<p>
These patterns are common across many relational systems, not just academic networks.
</p>

<hr>

<h2>Repository Structure</h2>

<pre>
graph-analysis-examples/
│
├── README.md
├── data/
│   └── ca-CondMat.txt
│
├── notebooks/
│   └── network_insights_collaboration_graph.ipynb
│
├── src/
│   └── network_insights.py
│
├── requirements.txt
└── .gitignore
</pre>

<ul>
  <li><strong>Notebook:</strong> Narrative explanation and interpretation</li>
  <li><strong>Script:</strong> Clean, client-ready computation and summary outputs</li>
</ul>

<hr>

<h2>Tools Used</h2>

<ul>
  <li>Python</li>
  <li>NetworkX</li>
  <li>Matplotlib</li>
</ul>

<hr>

<h2>About</h2>

<p>
I am a PhD researcher specialising in <strong>graph-based modelling of molecular and materials systems</strong>,
with a focus on translating complex relational data into interpretable network representations.
</p>

<p>
While my background is in chemistry, the methods demonstrated here apply to
<strong>any domain where relationships, interactions, and structure matter</strong>.
</p>

<hr>

<h2>Notes</h2>

<p>
This repository is intended as a <strong>demonstration of approach and thinking</strong>,
not as a production-ready software package.
Modelling choices and interpretations are deliberately explicit to make the analysis accessible
to non-specialist audiences.
</p>
