
---
title: 'D3.js 7.0 正式发布，数据可视化 JavaScript 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6478'
author: 开源中国
comments: false
date: Sun, 13 Jun 2021 08:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6478'
---

<div>   
<div class="content">
                                                                    
                                                        <p>D3（或者叫 D3.js）7.0 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3%2Freleases%2Ftag%2Fv7.0.0" target="_blank">发布</a>。</p> 
<p>从该版本起，D3 以 ESM 形式提供，因此会要求使用环境安装了 Node.js 12 或更高版本。关于此变化，详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgist.github.com%2Fsindresorhus%2Fa39789f98801d908bbc7ff3ecc99d99c" target="_blank">Sindre Sorhus’s FAQ</a>。</p> 
<p>此外，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-array%2Fblob%2Fmain%2FREADME.md%23bin" target="_blank">d3.bin</a> 现在会忽略空值，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-array%2Fblob%2Fmain%2FREADME.md%23ascending" target="_blank">d3.ascending</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-array%2Fblob%2Fmain%2FREADME.md%23descending" target="_blank">d3.descending</a> 也不再考虑空值的可比性(null comparable)。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-scale%2Fblob%2Fmain%2FREADME.md%23ordinal-scales" target="_blank">Ordinal scales</a> 现在使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmbostock%2Finternmap" target="_blank">InternMap</a> 作为域。域的值通过 object.valueOf 强制转为原始值而不是通过 object.toString 强制转为字符串来实现唯一性。</p> 
<p>类数组（如 NodeList）在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-selection%2Fblob%2Fmain%2FREADME.md%23selectAll" target="_blank">d3.selectAll</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-selection%2Fblob%2Fmain%2FREADME.md%23selection_selectAll" target="_blank">selection .selectAll</a> 中会被转换为数组。</p> 
<p>以上是 D3 v7 的一些破坏性变化，非破坏性变化如下：</p> 
<ul> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-array%2Fblob%2Fmain%2FREADME.md%23mode" target="_blank">d3.mode</a></li> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-array%2Fblob%2Fmain%2FREADME.md%23flatGroup" target="_blank">d3.flatGroup</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-array%2Fblob%2Fmain%2FREADME.md%23flatRollup" target="_blank">d3.flatRollup</a></li> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-transition%2Fblob%2Fmain%2FREADME.md%23selectChild" target="_blank"><em>transition</em>.selectChild</a></li> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-transition%2Fblob%2Fmain%2FREADME.md%23selectChildren" target="_blank"><em>transition</em>.selectChildren</a></li> 
 <li>为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-delaunay" target="_blank">Delaunay triangulation</a> 采用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmourner%2Frobust-predicates" target="_blank">robust predicates</a></li> 
 <li>修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-delaunay%2Fblob%2Fmain%2FREADME.md%23delaunay_voronoi" target="_blank"><em>delaunay</em>.voronoi</a> 计算出的船体共线点的外心</li> 
 <li>允许 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-brush%2Fblob%2Fmain%2FREADME.md%23brush_move" target="_blank"><em>brush</em>.move</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-brush%2Fblob%2Fmain%2FREADME.md%23brush_clear" target="_blank"><em>brush</em>.clear</a> 接受可选事件</li> 
 <li>允许 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-selection%2Fblob%2Fmain%2FREADME.md%23selection_merge" target="_blank"><em>selection</em>.merge</a> 进行转化</li> 
 <li>允许 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-selection%2Fblob%2Fmain%2FREADME.md%23selection_join" target="_blank"><em>selection</em>.join</a> 进行转换</li> 
 <li>为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-contour%2Fblob%2Fmain%2FREADME.md%23contourDensity" target="_blank">d3.contourDensity</a> 应用 linear binning</li> 
 <li>以更好的圆形刻度值生成 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-contour%2Fblob%2Fmain%2FREADME.md%23contours_thresholds" target="_blank"><em>contours</em>.thresholds</a></li> 
 <li>修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-axis%2Fblob%2Fmain%2FREADME.md%23axis_tickArguments" target="_blank"><em>axis</em>.tickArguments</a> 以接受可迭代对象</li> 
 <li>修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-axis%2Fblob%2Fmain%2FREADME.md%23axis_tickValues" target="_blank"><em>axis</em>.tickValues</a> 以接受可迭代对象</li> 
 <li>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-brush%2Fblob%2Fmain%2FREADME.md%23brush_move" target="_blank"><em>brush</em>.move</a> 期间修复未定义事件</li> 
 <li>在必要时，将<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-drag" target="_blank">拖动事件侦听器</a>修复为显式非被动</li> 
 <li>在必要时，将<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-zoom" target="_blank">缩放事件侦听器</a>修复为显式非被动</li> 
 <li>修复 d3-zoom 中的变量初始化错误</li> 
 <li>暴露 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-zoom%2Fblob%2Fmain%2FREADME.md%23zoom-transforms" target="_blank">d3.ZoomTransform</a> 构造函数</li> 
 <li>更新依赖项</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3%2Freleases%2Ftag%2Fv7.0.0" target="_blank">详情查看 release note</a>。</p> 
<p>D3 是数据可视化领域重要的 JavaScript 可视化库，它将强大的可视化交互技术与数据驱动 DOM 方法结合起来, 让你可以充分使用现代浏览器的强大能力自由地对数据进行可视化，在学术界、专业团队中享有极大声誉。</p> 
<p>D3 正如其名，Data Driven Documents 数据驱动文档，它与 G2 、Echarts 等不同，更加接近底层，直接操作 SVG 元素，拥有更大的自由度，几乎可以实现所有的 2D 设计需求，同时也带来了高学习曲线的成本。D3 长于可视化，但不止于可视化，还提供了数据处理、数据分析、DOM 操作等诸多功能。</p>
                                        </div>
                                      
</div>
            