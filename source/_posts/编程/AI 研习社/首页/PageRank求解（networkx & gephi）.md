
---
title: 'PageRank求解（networkx & gephi）'
categories: 
 - 编程
 - AI 研习社
 - 首页
headimg: 'https://gitee.com/misite_J/blog-img/raw/master/img/2020-12-24_01.png'
author: AI 研习社
comments: false
date: Thu, 24 Dec 2020 15:52:21 GMT
thumbnail: 'https://gitee.com/misite_J/blog-img/raw/master/img/2020-12-24_01.png'
---

<div>   
<div class="vditor-toc"><span class="toc-h1"><a class="toc-a" href="https://www.yanxishe.com/columnDetail/24965#PageRank%E6%B1%82%E8%A7%A3-networkx---gephi-">PageRank求解（networkx & gephi）</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/columnDetail/24965#networkx%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C">networkx基本操作</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/columnDetail/24965#Geophi%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C">Geophi基本操作</a></span><br>    <span class="toc-h3"><a class="toc-a" href="https://www.yanxishe.com/columnDetail/24965#%E5%88%A9%E7%94%A8Sigma-js%E6%8F%92%E4%BB%B6%E6%8A%8A%E5%9B%BE%E5%BD%A2%E5%AF%BC%E5%87%BA%E5%88%B0HTML">利用Sigma.js插件把图形导出到HTML</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/columnDetail/24965#networkx%E7%9A%84pagerank">networkx的pagerank</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/columnDetail/24965#%E6%AF%94%E8%BE%83">比较</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/columnDetail/24965#%E5%8F%82%E8%80%83">参考</a></span><br></div>
<h1 id="PageRank求解-networkx---gephi-">PageRank求解（networkx & gephi）</h1>
<h2 id="networkx基本操作">networkx基本操作</h2>
<pre><code class="language-python">import networkx as nx
G = nx.Graph() # 创建空图

G.add_node(1, time='5pm') # 添加节点，并赋节点属性
G.add_edge(1, 2, weight=4.7 ) # 添加边，并赋边属性

# 图显示需要借助matplotlib
import matplotlib.pyplot as plt

nx.draw(G) #绘制网络G
plt.show() # 在窗口中显示这幅图像
nx.write_gexf(G,'your_file_name.gexf') # 将图存为gexf文件，进而使用Gephi可视化


G._node # 节点及其属性的字典
G._adj # 节点及其邻居节点的字典
list(G.nodes()) # 节点列表

# 查找某一节点的邻居节点

</code></pre>
<h2 id="Geophi基本操作">Geophi基本操作</h2>
<ul>
<li>
<p>官网下载，安装后可能会提醒<code>cannot find Java 1.8 or higher</code>；<strong>解决方法</strong>，在<code>Gephi安装目录/etc/gephi.conf</code>中取消<code>jdkhome=“/path/to/jdk</code>的注释，将将其更改为<code>C:\Program Files\Java\jdk-9.0.1</code>（你的jdk安装目录，如未安装需首先安装jdk）。</p>
</li>
<li>
<p>打开‘.gexf’文件，初始状态为一个密集的正方形快，点击左下角的‘布局’进行更改，我选择了‘ForceAtlas2’，感觉布局时间比其他一些的要长很多；</p>
<p><img src="https://gitee.com/misite_J/blog-img/raw/master/img/2020-12-24_01.png" alt referrerpolicy="no-referrer"></p>
</li>
<li>
<p>点击右下角的‘统计’选项，选择‘pagerank’执行pagerank算法，具体计算结果可见上方的‘数据资料’部分。</p>
</li>
</ul>
<h3 id="利用Sigma-js插件把图形导出到HTML">利用Sigma.js插件把图形导出到HTML</h3>
<ul>
<li>
<p>在该网站<a href="https://gephi.org/plugins/#/">https://gephi.org/plugins/#/</a>下载插件，sigmaexporter-0.9.0.nbm；</p>
</li>
<li>
<p>从Gephi的菜单栏选择“工具 >插件>添加插件>安装“，安装完成后重启软件；</p>
<p><img src="https://gitee.com/misite_J/blog-img/raw/master/img/2020-12-25_01.png" alt referrerpolicy="no-referrer"></p>
</li>
<li>
<p>文件输出格式此时可选“Sigma.js template...”；</p>
<p><img src="https://gitee.com/misite_J/blog-img/raw/master/img/2020-12-25_02.png" alt referrerpolicy="no-referrer"></p>
</li>
<li>
<p>选择导出项目所在的目录，其他信息可默认或自行更改，包括图形的标题、图例、描述、悬停和许多其他细节，选择完成后，点击“确定”；</p>
<p><img src="https://gitee.com/misite_J/blog-img/raw/master/img/2020-12-25_03.png" alt referrerpolicy="no-referrer"></p>
</li>
<li>
<p>导出后得到一个叫network的文件夹，利用该文件夹实现html交互可视化。</p>
<p><img src="https://gitee.com/misite_J/blog-img/raw/master/img/2020-12-25_04.png" alt referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 id="networkx的pagerank">networkx的pagerank</h2>
<ul>
<li>
<p>PR值：<span class="vditor-math">PR(u)=\sum_&#123;v\in Bu&#125; \frac&#123;PR(v)&#125;&#123;L(v)&#125;</span>，u为待更新节点，Bu为u的入度节点集合，L(v)为节点v的出度。</p>
</li>
<li>
<p>等级泄露（Rank Leak）：如果一个节点只有入度，没有出度，吸收了其他节点的PR值而不释放，最终会导致其他节点的 PR 值为 0。</p>
</li>
<li>
<p>等级沉没（Rank Sink）：如果一个节点只有出度，没有入度，最终导致这个节点的 PR 值为 0。</p>
</li>
<li>
<p>为解决上述两个问题，拉里·佩奇提出改进的PageRank的随机浏览模型，该模型基于这样一个场景：在浏览网页时，用户并不总是依据链接跳转的方式，还有可能是用户就是要直接输入网址访问其他页面，虽然这个概率比较小。具体，定义阻尼因子d，表示用户通过链接跳转进入新的网页，一般设置为0.85，<span class="vditor-math">PR(u)=\frac&#123;1-d&#125;&#123;N&#125;+d \sum_&#123;v\in Bu&#125; \frac&#123;PR(v)&#125;&#123;L(v)&#125;</span>。</p>
<p><code>networkx.pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)</code></p>
</li>
<li>
<p>在networkx.pagerank中，PR值得计算为：<em>PR=alpha*(A*PR+dangling分配)+(1-alpha)*平均分配</em></p>
</li>
<li>
<p><strong>G</strong>：NetworkX图，对于无向图，默认会转化为双向有向图进行计算；</p>
</li>
<li>
<p><strong>alpha</strong>：即阻尼因子；</p>
</li>
<li>
<p><strong>personalization</strong>：自定义节点的PR值分配，默认为均匀分配；</p>
</li>
<li>
<p><strong>max_iter</strong>：最大迭代次数；</p>
</li>
<li>
<p><strong>tol</strong>：迭代阈值，若两次迭代差值低于该值，则跳出迭代；</p>
</li>
<li>
<p><strong>nstart</strong>：自定义网络各节点PageRank初始值，自定义的初始化PR值会在函数中自动归一化，见以下部分源码；</p>
<pre><code class="language-python">if nstart is None:  
    x = dict.fromkeys(W, 1.0 / N)  #和为1
else:
    # 归一化nstart vector
    s = float(sum(nstart.values()))
    x = dict((k, v / s) for k, v in nstart.items())
</code></pre>
</li>
<li>
<p><strong>weight</strong>：默认为“weight”，边权重值；没有时默认为1。</p>
</li>
<li>
<p><strong>dangling</strong>：对于dangling节点（出度为0的节点），自定义其PR值得分配，默认为均匀分配。多数情况下，<strong>personalization</strong>和<strong>dangling</strong>是相同的。</p>
</li>
<li>
<p><strong>Returns</strong> – 字典，每个节点及其对应的PR值。</p>
</li>
</ul>
<pre><code class="language-python"># 计算每个节点的 PR 值，并作为节点的 pagerank 属性
pagerank = nx.pagerank(G)
# 将 pagerank 数值作为节点的属性
nx.set_node_attributes(G, name = 'pagerank', values=pagerank)
</code></pre>
<h2 id="比较">比较</h2>
<ul>
<li>可以看到，networkx和gephi计算得到的PR值是相近的。</li>
</ul>
<p><img src="https://gitee.com/misite_J/blog-img/raw/master/img/2020-12-24_02.png" alt referrerpolicy="no-referrer"></p>
<h2 id="参考">参考</h2>
<p><a href="https://zhuanlan.zhihu.com/p/133233438">【白话机器学习】算法理论+实战之PageRank算法</a></p>
<p><a href="https://blog.csdn.net/qq_39805362/article/details/106956210">networkx pagerank</a></p>
  
</div>
            