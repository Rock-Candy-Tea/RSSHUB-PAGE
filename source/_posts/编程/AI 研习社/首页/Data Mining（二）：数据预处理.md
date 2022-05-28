
---
title: 'Data Mining（二）：数据预处理'
categories: 
 - 编程
 - AI 研习社
 - 首页
headimg: 'https://gitee.com/misite_J/blog-img/raw/master/img/2021-01-04_01.png'
author: AI 研习社
comments: false
date: Tue, 05 Jan 2021 02:26:52 GMT
thumbnail: 'https://gitee.com/misite_J/blog-img/raw/master/img/2021-01-04_01.png'
---

<div>   
<div class="vditor-toc"><span class="toc-h1"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E6%8D%AE%E8%B4%A8%E9%87%8F%E8%AF%84%E4%BC%B0%E6%8C%87%E6%A0%87">数据质量评估指标</a></span><br><span class="toc-h1"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E6%8D%AE%E6%B8%85%E7%90%86">数据清理</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E7%BC%BA%E5%A4%B1%E5%80%BC">缺失值</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E5%99%AA%E5%A3%B0%E6%95%B0%E6%8D%AE">噪声数据</a></span><br><span class="toc-h1"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E6%8D%AE%E9%9B%86%E6%88%90">数据集成</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E5%AE%9E%E4%BD%93%E8%AF%86%E5%88%AB%E9%97%AE%E9%A2%98">实体识别问题</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E5%86%97%E4%BD%99%E5%92%8C%E7%9B%B8%E5%85%B3%E6%80%A7%E5%88%86%E6%9E%90">冗余和相关性分析</a></span><br><span class="toc-h1"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E6%8D%AE%E5%BD%92%E7%BA%A6">数据归约</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E7%BB%B4%E5%BD%92%E7%BA%A6">维归约</a></span><br>    <span class="toc-h3"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E5%B0%8F%E6%B3%A2%E5%8F%98%E6%8D%A2">小波变换</a></span><br>    <span class="toc-h3"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90">主成分分析</a></span><br>    <span class="toc-h3"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E5%B1%9E%E6%80%A7%E5%AD%90%E9%9B%86%E9%80%89%E6%8B%A9">属性子集选择</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E9%87%8F%E5%BD%92%E7%BA%A6">数量归约</a></span><br>    <span class="toc-h3"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E5%8F%82%E6%95%B0%E6%96%B9%E6%B3%95">参数方法</a></span><br>      <span class="toc-h4"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E5%9B%9E%E5%BD%92%E5%92%8C%E5%AF%B9%E6%95%B0-%E7%BA%BF%E6%80%A7%E6%A8%A1%E5%9E%8B">回归和对数-线性模型</a></span><br>    <span class="toc-h3"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E9%9D%9E%E5%8F%82%E6%95%B0%E6%96%B9%E6%B3%95">非参数方法</a></span><br>      <span class="toc-h4"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E7%9B%B4%E6%96%B9%E5%9B%BE">直方图</a></span><br>      <span class="toc-h4"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E8%81%9A%E7%B1%BB">聚类</a></span><br>      <span class="toc-h4"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%8A%BD%E6%A0%B7">抽样</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E6%8D%AE%E5%8E%8B%E7%BC%A9">数据压缩</a></span><br><span class="toc-h1"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E6%8D%AE%E5%8F%98%E6%8D%A2%E4%B8%8E%E6%95%B0%E6%8D%AE%E7%A6%BB%E6%95%A3%E5%8C%96">数据变换与数据离散化</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E6%8D%AE%E8%A7%84%E8%8C%83%E5%8C%96">数据规范化</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E6%95%B0%E6%8D%AE%E7%A6%BB%E6%95%A3%E5%8C%96">数据离散化</a></span><br>  <span class="toc-h2"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#TODO">TODO</a></span><br><span class="toc-h1"><a class="toc-a" href="https://www.yanxishe.com/blogDetail/25056#%E5%8F%82%E8%80%83">参考</a></span><br></div>
<h1 id="数据质量评估指标">数据质量评估指标</h1>
<ul>
<li>准确性</li>
<li>完整性</li>
<li>一致性</li>
<li>时效性</li>
<li>可信性</li>
<li>可解释性</li>
</ul>
<h1 id="数据清理">数据清理</h1>
<p><strong>数据清理（data cleaning）</strong>：通过填写缺失的值，光滑噪声数据，识别并删除离群点并解决不一致性来清理数据。数据清洗通常是一个两步迭代过程，包括偏差检测和数据变换。</p>
<h2 id="缺失值">缺失值</h2>
<ul>
<li>忽略元组</li>
<li>人工填写缺失值</li>
<li>使用一个全局变量填充缺失值</li>
<li>使用数据的中心度量填充缺失值：对于对称数据分布，选择均值；而倾斜数据分布使用中位数</li>
<li>使用与给定元组数同一类的所有样本的属性均值或中位数</li>
<li>使用最有可能的值填充：通过回归、决策树等</li>
</ul>
<h2 id="噪声数据">噪声数据</h2>
<p><strong>噪声</strong>（noise）是被测量的变量的随机误差或方差。</p>
<p><strong>数据光滑技术</strong>：</p>
<ul>
<li>分箱（binning）：分箱方法通过考察数据的邻近值来光滑有序数据值（局部光滑）。有序数据分享后，可分别根据箱均值、箱中位数、箱边界光滑</li>
<li>回归（regression）：用一个函数你和数据来光滑数据，包括线性回归和多元线性回归</li>
<li>离群点分析（outlier analysis）：可通过聚类的方法检测离群点</li>
</ul>
<h1 id="数据集成">数据集成</h1>
<p><strong>数据集成（data integration）</strong>：集成多个数据库、数据立方体或文件以分析来自多个数据源的数据。</p>
<ul>
<li>实体识别问题</li>
<li>属性冗余</li>
<li>元组重复</li>
<li>数据值冲突</li>
</ul>
<h2 id="实体识别问题">实体识别问题</h2>
<p>将来自现实世界的多个信息源的等价实体进行匹配，例如异名同义属性名的匹配。</p>
<ul>
<li>属性的元数据包括名字、含义、数据类型和属性的允许取值范围，以及处理空白、零和Null值的空值规则</li>
</ul>
<h2 id="冗余和相关性分析">冗余和相关性分析</h2>
<p><strong>冗余</strong>：一个属性可有另一个或一组属性导出；或是属性和维命名的不一致也可能导致冗余。</p>
<p>部分冗余可由<strong>相关分析</strong>检测，即度量一个属性在多大程度上蕴涵另一个。</p>
<ul>
<li>
<p>标称数据，使用卡方检验<span class="vditor-math">\chi ^2</span>进行相关分析；</p>
<ul>
<li>
<p><img src="https://gitee.com/misite_J/blog-img/raw/master/img/2021-01-04_01.png" alt referrerpolicy="no-referrer"></p>
</li>
<li>
<p>将两个属性描述数据表为相依表，列为属性A的c个值，行为属性B的r个值，见上图；</p>
</li>
<li>
<p><span class="vditor-math">\chi^&#123;2&#125;=\sum_&#123;i=1&#125;^&#123;c&#125; \sum_&#123;j=1&#125;^&#123;r&#125; \frac&#123;\left(o_&#123;i j&#125;-e_&#123;i j&#125;\right)^&#123;2&#125;&#125;&#123;e_&#123;i j&#125;&#125;</span>，其中<span class="vditor-math">o_&#123;i j&#125;</span>是联合事件<span class="vditor-math">(A_i,B_j)</span>的观测频度（即实际计数），<span class="vditor-math">e_&#123;i j&#125;</span>是<span class="vditor-math">(A_i,B_j)</span>的期望频度，<span class="vditor-math">e_&#123;i j&#125;=\frac&#123;\operatorname&#123;count&#125;\left(A=a_&#123;i&#125;\right) \times \operatorname&#123;count&#125;\left(B=b_&#123;j&#125;\right)&#125;&#123;n&#125;</span>，其中n是数据元组的个数，<span class="vditor-math">\operatorname&#123;count&#125;\left(A=a_&#123;i&#125;\right)</span>是A中具有值<span class="vditor-math">a_i</span>的元组个数，<span class="vditor-math">\operatorname&#123;count&#125;\left(B=b_&#123;j&#125;\right)</span>是B中具有值<span class="vditor-math">b_j</span>的元组个数；</p>
</li>
<li>
<p>根据<span class="vditor-math">\chi ^2</span>分布的百分点表，查找自由度<span class="vditor-math">(r-1)\times(c-1)</span>下的显著水平，计算值大于该值，拒绝假设，两属性相关，反之独立。</p>
<p><img src="https://gitee.com/misite_J/blog-img/raw/master/img/2021-01-04_02.png" alt referrerpolicy="no-referrer"></p>
</li>
<li>
<p><span class="vditor-math">\chi ^2</span>统计检验假设A和B是独立的；</p>
</li>
<li>
<p>对<span class="vditor-math">\chi ^2</span>值贡献最大的单元是实际计数与期望技术很不相同的单元。</p>
</li>
</ul>
</li>
<li>
<p>数值数据，使用相关系数和协方差进行相关分析。</p>
<ul>
<li>属性A和B的相关系数（Pearson积矩系数）：<span class="vditor-math">r_&#123;A, B&#125;=\frac&#123;\sum_&#123;i=1&#125;^&#123;n&#125;\left(a_&#123;i&#125;-\bar&#123;A&#125;\right)\left(b_&#123;i&#125;-\bar&#123;B&#125;\right)&#125;&#123;n \sigma_&#123;A&#125; \sigma_&#123;B&#125;&#125;=\frac&#123;\sum_&#123;i=1&#125;^&#123;n&#125;\left(a_&#123;i&#125; b_&#123;i&#125;\right)-n \bar&#123;A&#125; \bar&#123;B&#125;&#125;&#123;n \sigma_&#123;A&#125; \sigma_&#123;B&#125;&#125;</span>，其中，n为元组个数，<span class="vditor-math">\bar A</span>、<span class="vditor-math">\bar B</span>分别为对应均值，<span class="vditor-math">\sigma_&#123;A&#125;</span>、<span class="vditor-math"> \sigma_&#123;B&#125;</span>分别为A/B的标准差。
<ul>
<li><span class="vditor-math">r_&#123;A,B&#125;</span>取值范围为[-1,1]，该值大于0时，表示正相关，值越大相关性越高；反之亦然。</li>
<li>散点图可用来观测属性之间的相关性；</li>
<li>相关性并不蕴涵因果关系。</li>
</ul>
</li>
<li>属性A和B的协方差：<span class="vditor-math">\operatorname&#123;Cov&#125;(A, B)=E((A-\bar&#123;A&#125;)(B-\bar&#123;B&#125;))=\frac&#123;\sum_&#123;i=1&#125;^&#123;n&#125;\left(a_&#123;i&#125;-\bar&#123;A&#125;\right)\left(b_&#123;i&#125;-\bar&#123;B&#125;\right)&#125;&#123;n&#125;=E(A·B)-\bar A \bar B</span>。
<ul>
<li><span class="vditor-math">r_&#123;A,B&#125;=\frac&#123;\operatorname&#123;Cov&#125;(A,B)&#125;&#123;\sigma_a \sigma_b&#125;</span>；</li>
<li>如果A和B独立，<span class="vditor-math">E(A,B)=E(A)·E(B)</span>，<span class="vditor-math">Cov(A,B)=0</span>；然而，<strong>其逆不成立</strong>，即某些随机变量对的协方差可能为0，却是非独立的；</li>
<li>方差是协方差的特殊情况，其中两个属性相同，即属性与其自身的协方差。</li>
</ul>
</li>
</ul>
</li>
</ul>
<h1 id="数据归约">数据归约</h1>
<p><strong>数据归约</strong>（data reduction）：得到数据集的简化表示，它小得多，但能够产生同样的分析结果。</p>
<ul>
<li>花费在数据归约上的时间不应超过或“抵消”在规约后的数据上挖掘所节省的时间。</li>
</ul>
<h2 id="维归约">维归约</h2>
<p><strong>维归约</strong>：减少所考虑的随机变量数量或属性的个数。</p>
<h3 id="小波变换">小波变换</h3>
<p><strong>离散小波变换（DWT）<strong>是一种线性信号处理技术，用于将数据向量<span class="vditor-math">X</span>变换为不同的数值</strong>小波系数</strong>向量<span class="vditor-math">X^&#123;'&#125;</span>，两个向量具有相同的长度。</p>
<ul>
<li><strong>小波系数</strong>：一个信号无论进行连续小波变换（CWT）或是离散小波变换（DWT），变换完的结果就叫小波系数；小波系数是没有量纲单位的结果，需要经过重构这些系数得到实际有量纲的信号。</li>
<li>虽然小波变换后的数据与原数据长度相等，但小波变换后的数据可以截短，进存放一部分最强的小波系数，就能保留近似的压缩数据；</li>
<li>DWT也可用于消除噪声，而不会光滑掉数据的主要特征；</li>
<li>给定一组小波系数，使用所用的DWT的逆，可以构造原数据的近似；</li>
<li>与离散傅里叶变换（DFT）相比，DWT是一种更好的有损压缩（相同数目系数时DWT更接近原数据；相同近似下DWT需要的空间更小）；小波空间相比DFT的局部性更好，有助于保留局部细节；只有一种DFT，担忧若干族DWT；</li>
<li>DWT一般使用层次金字塔算法，在每次迭代时数据减半，计算速度很快。
<ol>
<li>输入数据向量的长度L必须为2的整数幂，必要时在数据后添加0；</li>
<li>每个变换应用两个函数，第一个<strong>求和或加权平均</strong>进行数据光滑；第二个进行<strong>加权差分</strong>，提取数据的细节特征；</li>
<li>两个函数分别作用于原数据的所有数据点对<span class="vditor-math">(x_&#123;2i&#125;,x_&#123;2i+1&#125;)</span>，得到两个长度为L/2的数据集，分别代表输入数据的光滑后的版本或低频版本和它的高频内容；</li>
<li>递归上述过程，直到得到的结果数据集的长度为2；</li>
<li>由以上迭代得到的数据集中选择的值被指定为数据变换的小波系数。</li>
</ol>
</li>
<li>对输入数据应用矩阵乘法，也可以得到小波系数；通过将矩阵分解成几个稀疏矩阵的乘积，对于长度为n的输入向量，“快速DWT”算法的复杂度为<span class="vditor-math">O(n)</span>。</li>
</ul>
<h3 id="主成分分析">主成分分析</h3>
<p><strong>主成分分析PCA</strong>：将n维特征映射到k维上，这k维是全新的正交特征也被称为主成分，是在原有n维特征的基础上重新构造出来的k维特征。基本过程为：</p>
<ul>
<li>
<p>对数据规范化，使得每个属性都落入相同的区间，避免较大定义域属性对其他属性的支配；</p>
</li>
<li>
<p>PCA计算k个标准正交向量，作为规范化输入数据的基（输入数据是主成分的线性组合）；</p>
<ul>
<li>计算数据矩阵的协方差矩阵；</li>
<li>计算协方差矩阵的特征值和特征向量；
<ul>
<li>特征值分解协方差矩阵</li>
<li>奇异值分解协方差矩阵</li>
</ul>
</li>
<li>选择特征值最大（即方差最大）的k个特征所对应的特征向量组成矩阵；</li>
<li>将数据矩阵转换到新的空间当中，实现数据特征的降维。</li>
</ul>
</li>
<li>
<p>与小波变换相比，PCA可以更好的处理稀疏数据，而小波变换更适合高维数据。</p>
</li>
</ul>
<h3 id="属性子集选择">属性子集选择</h3>
<p><strong>属性子集选择（特征子集选择）</strong>：检测并删除不相关、弱相关或冗余的属性或维。</p>
<ul>
<li>属性子集选择通常使用压缩搜索空间的启发式算法，例如典型的贪心算法：
<ul>
<li>逐步向前选择：每一步在原属性集中确定最好的属性，将其加入归约集；</li>
<li>逐步向后删除：每一步删除现有属性集中最差的属性；</li>
<li>逐步向前选择和逐步向后删除的组合：每一步选择一个最好的属性，并删除剩余属性中最差的属性；</li>
<li>决策树归纳：由给定的数据构造决策树，不出现在树中的所有属性被认为是“无意义”属性，出现在树中的属性形成规约后的属性子集。</li>
</ul>
</li>
<li>属性构造：通过组合属性（如高度和宽度组合为面积属性），发现属性间联系的缺失信息。</li>
</ul>
<h2 id="数量归约">数量归约</h2>
<p><strong>数量规约</strong>：用替代的、较小的数据表示形式替换原数据。</p>
<ul>
<li>参数方法：使用模型估计数据，只需存放模型参数而不是实际数据；</li>
<li>非参数方法</li>
</ul>
<h3 id="参数方法">参数方法</h3>
<h4 id="回归和对数-线性模型">回归和对数-线性模型</h4>
<ul>
<li><strong>线性回归</strong>：利用线性回归方程的<strong>最小二乘</strong>函数对一个或多个自变量和因变量之间关系进行建模的一种回归分析，包括简单线性回归和多元线性回归。</li>
<li><strong>对数线性模型</strong>：在线性模型的基础上通过复合函数（sigmoid/softmax/entropy ）将其映射到概率区间，使用对数损失构建目标函数，包括逻辑回归、最大熵模型和条件随机场等。</li>
</ul>
<h3 id="非参数方法">非参数方法</h3>
<h4 id="直方图">直方图</h4>
<ul>
<li>等宽直方图：每个桶的区间范围一致；</li>
<li>等频直方图：每个桶大致包含相同个数的邻近数据样本。</li>
</ul>
<h4 id="聚类">聚类</h4>
<p>聚类：将对象划分为群或簇，使得同一个簇内的对象相似，而与其他簇内的对象相异。</p>
<ul>
<li>簇质量的度量：
<ul>
<li>直径——卒中两个对象的最大距离；</li>
<li>形心距离——簇中每个对象到簇形心的平均距离。</li>
</ul>
</li>
</ul>
<h4 id="抽样">抽样</h4>
<ul>
<li>
<p>无放回简单随机抽样SRSWOR</p>
</li>
<li>
<p>有放回简单随机抽样SRSWR</p>
</li>
<li>
<p>簇抽样</p>
</li>
<li>
<p>分层抽样：数据分层（分类）后，在每层按比例采样</p>
</li>
<li>
<p>采用抽样进行数据规约的好处：花费时间正比于样本集的大小，而不是数据集的大小，因此抽样复杂度可能亚线性（sublinear）于数据的大小；</p>
</li>
<li>
<p>对于固定大小的样本，抽样复杂度随数据维数线性增加，而其他技术复杂度呈指数增加。</p>
</li>
</ul>
<h2 id="数据压缩">数据压缩</h2>
<p><strong>数据压缩</strong>：使用变换，得到原数据的规约或“压缩”表示。如果原数据可由压缩后的数据重构，而不损失任何信息，称为无损压缩，否则是有损的。</p>
<h1 id="数据变换与数据离散化">数据变换与数据离散化</h1>
<p><strong>数据变换（data transformation）</strong>：包括规范化、数据离散化和概念分层产生等。</p>
<h2 id="数据规范化">数据规范化</h2>
<p>规范化：把数据属性按比例缩放，使之落入一个特定的小区间。</p>
<ul>
<li>最小-最大规范化：<span class="vditor-math">x^&#123;'&#125;_&#123;i&#125;=\frac&#123;x_i-min&#125;&#123;mxa-min&#125;(max_&#123;new&#125;-min_&#123;new&#125;)+min_&#123;new&#125;</span>；
<ul>
<li>最小-最大规范化<strong>保持原始数据之间的联系</strong>；</li>
<li>规范化后区间范围<span class="vditor-math">[min_&#123;new&#125;,max_&#123;new&#125;]</span>。</li>
</ul>
</li>
<li>z分数规范化（零均值规范化）：<span class="vditor-math">x^&#123;'&#125;_&#123;i&#125;=\frac&#123;x_i-\bar x&#125;&#123;\sigma_x&#125;</span>；
<ul>
<li>当数据的最大最小值未知，或离群值左右最小-最大化规范时，使用该方法；</li>
<li>规范化后的区间范围<span class="vditor-math">[\frac&#123;x_&#123;min&#125;-\bar&#123;x&#125;&#125;&#123;\sigma_x&#125;,\frac&#123;x_&#123;max&#125;-\bar&#123;x&#125;&#125;&#123;\sigma_x&#125;]</span>。</li>
<li>上式中的标准差<span class="vditor-math">\sigma_x</span>可以用均值绝对偏差<span class="vditor-math">s_x</span>替换，<span class="vditor-math">s_&#123;x&#125;=\frac&#123;1&#125;&#123;n&#125;\left(\left|x_&#123;1&#125;-\bar&#123;x&#125;\right|+\left|x_&#123;2&#125;-\bar&#123;x&#125;\right|+\cdots+\left|x_&#123;n&#125;-\bar&#123;x&#125;\right|\right)</span>，这样<span class="vditor-math">x^&#123;'&#125;_&#123;i&#125;=\frac&#123;x_i-\bar x&#125;&#123;s_x&#125;</span>；</li>
<li>对于离群点，<strong>均值绝对偏差<span class="vditor-math">s_x</span>比标准差<span class="vditor-math">\sigma_x</span>更加鲁棒</strong>。</li>
</ul>
</li>
<li>小数定标规范化：通过移动数据的小数点未知进行规范化，<span class="vditor-math">x_&#123;i&#125;^&#123;'&#125;=\frac&#123;x_i&#125;&#123;10^j&#125;</span>，其中j是使得<span class="vditor-math">max(|x_i^&#123;'&#125;|)<1</span>成立得最小整数；
<ul>
<li><strong>规范化后的区间范围<span class="vditor-math">(-1,1)</span></strong>。</li>
</ul>
</li>
</ul>
<h2 id="数据离散化">数据离散化</h2>
<ul>
<li>通过分箱离散化：等宽或等频分箱，用箱均值或中位数替换箱中的每个值，将属性离散化；</li>
<li>通过直方图分析离散化：等宽直方图或等频直方图；</li>
<li>通过聚类、决策树和相关分析离散化
<ul>
<li>聚类——自顶向下的划分策略或自底向上的合并策略；非监督的；</li>
<li>决策树——自顶向下的划分方法；有监督的；主要思想是，选择划分点使得一个给定的结果分区包含尽可能多的同类元组，其中，熵是最常用的划分点度量；</li>
<li>相关性度量可用于离散化——例如<em>ChiMerge</em>是一种基于<span class="vditor-math">\chi^&#123;2&#125;</span>的离散化方法。
<ul>
<li><em>ChiMerge</em>是自底向上的策略；有监督的；</li>
<li><em>ChiMerge</em>过程如下：初始时，将数据按序排好，将数值属性的每个值看作一个区间；对每个相邻区间进行<span class="vditor-math">\chi^&#123;2&#125;</span>检验；将具有最小<span class="vditor-math">\chi^&#123;2&#125;</span>值的相邻区间合并在一起；递归合并过程，直到满足预定义的终止条件。</li>
</ul>
</li>
</ul>
</li>
<li>标称数据的概念分层
<ul>
<li>基于模式定义或每个属性的不同值个数产生；</li>
<li>启发式规则：定义在较高概念层的属性（如country）与定义在较低概念层的属性（如street）相比，一般包含较少的不同值，因此，可以根据给定属性集中每个属性不同值的个数，自动地产生概念分层，但并不绝对。</li>
</ul>
</li>
</ul>
<h2 id="TODO">TODO</h2>
<ul>
<li>小波变换</li>
<li>主成分分析（基于特征值 vs 基于SVD）<a href="https://blog.csdn.net/program_developer/article/details/80632779">https://blog.csdn.net/program_developer/article/details/80632779</a></li>
<li>简单线性回归模型 <a href="https://zhuanlan.zhihu.com/p/73494604">https://zhuanlan.zhihu.com/p/73494604</a></li>
<li>多元线性回归 <a href="https://zhuanlan.zhihu.com/p/48541799">https://zhuanlan.zhihu.com/p/48541799</a> <a href="https://zhuanlan.zhihu.com/p/124902625">https://zhuanlan.zhihu.com/p/124902625</a></li>
<li>对数线性模型 <a href="https://zhuanlan.zhihu.com/p/112816694">https://zhuanlan.zhihu.com/p/112816694</a></li>
</ul>
<h1 id="参考">参考</h1>
<ol>
<li>《数据挖掘：概念与技术》第三章</li>
<li>小波系数 <a href="https://blog.csdn.net/hai_girl/article/details/85105540">https://blog.csdn.net/hai_girl/article/details/85105540</a></li>
<li>小波变换通俗解释 <a href="http://blog.sina.com.cn/s/blog_13bb711fd0102w9x1.html">http://blog.sina.com.cn/s/blog_13bb711fd0102w9x1.html</a></li>
<li>白话解释“差分”、“一阶差分” <a href="https://zhuanlan.zhihu.com/p/46699931">https://zhuanlan.zhihu.com/p/46699931</a></li>
</ol>
  
</div>
            