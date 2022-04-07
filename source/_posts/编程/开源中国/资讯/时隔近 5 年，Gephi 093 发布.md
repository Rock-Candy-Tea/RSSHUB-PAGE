
---
title: '时隔近 5 年，Gephi 0.9.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8467'
author: 开源中国
comments: false
date: Thu, 07 Apr 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8467'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Gephi 0.9.3 现已发布，该软件的上一次版本发布是在 2017 年 9 月。Gephi 是一个用于可视化和操作大型图形的开源平台。它可以在 Windows、Mac OS X 和 Linux 上运行。有英语、法语、西班牙语、日语、俄语、巴西葡萄牙语、中文、捷克语和德语的本地化版本。 </span></p> 
<p><span style="color:#000000">版本更新内容如下：</span></p> 
<p><span style="color:#000000"><strong>New features</strong></span></p> 
<ul> 
 <li>添加了 Statistical Inference 社区检测算法，Modularity 的更高级替代方案 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fpull%2F2431" target="_blank">#2431</a></li> 
 <li>Windows 和 Linux 版本现在也嵌入了 JRE，因此不再需要单独安装 Java <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2336" target="_blank">#2336</a></li> 
 <li>现在默认在所有平台上使用 FlatLaf 外观 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2415" target="_blank">#2415</a></li> 
 <li>分区中使用的颜色等外观属性现在保存在项目中 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1861" target="_blank">#1861</a></li> 
 <li>Last Export settings 现在被保存为首选项，因此它们在不同的会话之间会持续存在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1790" target="_blank">#1790</a></li> 
</ul> 
<p><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul> 
 <li>改进 UI 以更好地适应 HighDPI 显示器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2332" target="_blank">#2332</a></li> 
 <li>图形工具栏项目在较小的屏幕尺寸上重叠 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F765" target="_blank">#765</a></li> 
 <li>一些布局作用于 settled nodes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2385" target="_blank">#2385</a></li> 
 <li>忽略 GraphML desc standard tags <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2030" target="_blank">#2030</a></li> 
 <li>java.util.MissingResourceException gephi 版本 0.9.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2063" target="_blank">#2063</a></li> 
 <li>过滤具有空属性值的 datalab 列时出现 NullpointerException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2015" target="_blank">#2015</a></li> 
 <li>未选中“Create missing nodes”不会产生预期的效果<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1878" target="_blank">#1878</a></li> 
 <li>“Interval”未复制到新工作区<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1988" target="_blank">#1988</a></li> 
 <li>CSV Edges 文件未导入，因为 Gephi 未检测到 Source 和 Target 列<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2178" target="_blank">#2178</a></li> 
 <li>删除节点时出现 ArrayIndexOutOfBoundsException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1623" target="_blank">#1623</a></li> 
 <li>Gephic Mac 0.9.2 的 Appearance panel 中没有模式指示器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2098" target="_blank">#2098</a></li> 
 <li>Neighbors Network filter 在最大深度时冻结 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2099" target="_blank">#2099</a></li> 
 <li>无法导入大文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1841" target="_blank">#1841</a></li> 
 <li>更新崩溃报告器并使其符合 GDPR <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2340" target="_blank">#2340</a></li> 
 <li>ClassCastException: org.gephi.graph.api.types.TimestampSet 不能转换为 org.gephi.graph.api.types.TimeMap <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2297" target="_blank">#2297</a></li> 
 <li>在 GEXF 中支持 INF、-INF 的 double-type ±∞ values <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2158" target="_blank">#2158</a></li> 
 <li>标准化时，大图的 Node betweenness 为负 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2139" target="_blank">#2139</a></li> 
 <li>generatePalette 错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F2112" target="_blank">#2112</a></li> 
 <li>加载具有 0-weighted edges 的 gexf 文件会导致导入崩溃<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1945" target="_blank">#1945</a></li> 
 <li>导出 VNA 图形文件时崩溃<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1909" target="_blank">#1909</a></li> 
 <li>导入 CSV error edges <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1848" target="_blank">#1848</a></li> 
 <li>graphml 的导入仍然会混淆 d3 和 label 字段<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1840" target="_blank">#1840</a></li> 
 <li>向 CSV 解析器添加对字节顺序标记的支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1840" target="_blank">#1815</a></li> 
 <li>当字符串中的双引号用反斜杠分隔时，不再正确导入 CSV 文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1812" target="_blank">#1812</a></li> 
 <li>EdgeTypeFilter 上的 NullPointerException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1811" target="_blank">#1811</a></li> 
 <li>GephiFormatException 会导致 ArrayIndexOutOfBoundsException: 0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1810" target="_blank">#1810</a></li> 
 <li>在某些情况下，no-merge strategy 会出现异常。不应创建不兼容的 edge <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1802" target="_blank">#1802</a></li> 
 <li>NullPointerException: fileObject 参数不能为空<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1789" target="_blank">#1789</a></li> 
 <li>GephiFormatException：Gephi 保存项目失败。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Fissues%2F1788" target="_blank">#1788</a></li> 
 <li>......</li> 
</ul> 
<h3><span style="color:#24292f">API 更改</span></h3> 
<ul> 
 <li>Graph API 
  <ul> 
   <li>添加<code>getEdges(int type)</code>到<code>Graph</code>允许仅检索特定类型的 edges。</li> 
   <li>添加<code>getEdgeTypeLabels(boolean)</code>到<code>GraphModel</code>.</li> 
   <li>将 <span style="color:#24292f">min/max </span>添加到<code>TimeSet</code>和<code>Element.getTimeBounds()</code>。</li> 
   <li>添加<code>Column.exists()</code>为新实用程序。</li> 
   <li>在<code>Graph</code>的 API 中添加<code>GraphLock</code>，以 expose locking states。</li> 
   <li>让表成为列的集合。</li> 
   <li>添加新方法<code>Column.isDynamicAttribute()</code>。</li> 
   <li>除了<code>toCollection()</code>之外，在元素迭代器中添加<code>toSet()</code>。</li> 
   <li>添加新<code>Table.countColumns(Origin)</code>方法。</li> 
   <li>在提供 Table 时为 GraphModel 增加 getElementIndex() 方法。</li> 
   <li>添加<code>isNodeTable()</code>和<code>isEdgeTable()</code>方法到<code>Table</code>.</li> 
  </ul> </li> 
 <li><span style="color:#24292f">Appearance API</span>（开发中） 
  <ul> 
   <li>Partition 和 Ranking 现在总是接收 Graph 作为参数，用于所有需要访问底层索引的方法，以促进本地规模支持。</li> 
   <li>在 Ranking 中添加 getColumn()，使其与 Partition 保持一致</li> 
   <li>在 Ranking 中添加 getNormalizedValue()，以便更容易地检索标准化的值。</li> 
   <li>当没有找到给定值的颜色时，Partition 现在有一个静态的 DEFAULT_COLOR。</li> 
   <li>删除<code>Partition.setColors()</code>，因为它容易引起混淆。</li> 
   <li>添加<code>transformAll(Iterable<? extends Element>)</code>到<code>Function</code>.</li> 
   <li>在 AppearanceModel 中将 isLocalScale() 拆分为 isRankingLocalScale() 和 isPartitionLocalScale()。</li> 
   <li>让 AppearanceModel 中的 Function getters 独立于 Graph，因为这应该根据本地/全局状态自动处理。</li> 
  </ul> </li> 
 <li>Preview API 
  <ul> 
   <li>一个 postProcess() 方法已被添加到 Renderer SPI 中，以便在所有项目被 render 后进行自定义。</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgephi%2Fgephi%2Freleases%2Ftag%2Fv0.9.3" target="_blank">https://github.com/gephi/gephi/releases/tag/v0.9.3</a></p>
                                        </div>
                                      
</div>
            