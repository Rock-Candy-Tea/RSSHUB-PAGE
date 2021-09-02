
---
title: 'Apache ECharts 5.2.0 发布，新增全局过渡动画、极坐标柱状图标签等功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0902/112139_ZoBP_2720166.jpg'
author: 开源中国
comments: false
date: Thu, 02 Sep 2021 03:40:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0902/112139_ZoBP_2720166.jpg'
---

<div>   
<div class="content">
                                                                                            <p><img src="https://static.oschina.net/uploads/space/2021/0902/112139_ZoBP_2720166.jpg" referrerpolicy="no-referrer"></p> 
<p>Apache ECharts 5.2.0 于 2021.9.1 正式发布，在这个版本中，我们引入了非常酷炫的全局过渡动画，并且对调色盘取色策略、极坐标柱状图标签等做了很多优化和增强，本文将带大家一睹为快！</p> 
<h2>全局过渡动画</h2> 
<p>在 Apache ECharts 中我们一直把自然流畅的过渡动画作为一个重要特性。通过避免数据带来的突变，不仅仅可以改善视觉效果，更为表达数据的关联和演变提供了可能。因此，在 5.2.0 中，我们进一步将过渡动画从表现系列内部数据的变化，泛化到全局能力。接下来，我们会看到这种<strong>全局过渡动画 Universal Transition</strong> 是如何为图表增加表现力和叙事能力的。</p> 
<p>在之前的版本中，过渡动画有一定的局限性：只能用于相同类型的图形的位置、尺寸、形状，而且只能作用在相同类型的系列上。比如，下面例子就是通过饼图中扇区形状的变化反映了数据分布的变化：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113345_to2a_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>而从 5.2.0 开始，我们引入了更强大的全局过渡动画能力，让过渡动画不再局限于相同类型的系列之间。现在，我们可以使用这种跨系列的形变，为任意类型的系列和任意类型的图形做形变动画。</p> 
<p>这会有多酷呢？我们一起来感受一下！</p> 
<h3>跨系列的形变动画</h3> 
<p>在设置<code>universalTransition: true</code>开启全局过渡动画后，从饼图切换成柱状图，或者从柱状图切换成散点图，甚至旭日图和矩形树图这类复杂的图表之间，都可以通过形变的方式自然的进行动画过渡。</p> 
<p>如下，饼图和柱状图之间的切换：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113401_5uqQ_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>更多的常见基础图表之间的过渡：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113455_xyS7_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>这样的动画过渡不再仅仅局限于基础的折、柱、饼中，在柱状图和地图之间:</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113515_JG0c_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>或者旭日图和矩形树图之间，甚至非常灵活的自定义系列之间都可以进行动画的过渡。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113530_tzhS_2720166.gif" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>注意需要配置系列的 id 来保证需要动画过渡的系列之间能够一一对应。</p> 
</blockquote> 
<h3>数据的分裂和合并动画</h3> 
<p>除了常见的数据值的更新，有时候我们还会碰到数据的聚合、下钻等交互后的更新，这个时候我们就不能直接应用一对一的动画过渡，而需要使用更多像分裂、合并这样的动画效果，来通过正确的图形动画表达出数据的变换。</p> 
<p>为了能够表达数据之间可能存在的多对多联系，在 5.2.0 中我们新引入了一个数据组<code>groupId</code>的概念，我们可以通过 series.dataGroupId 设置整个系列所属的组，或者更细粒度的通过 series.data.groupId 设置每个数据所属的组。如果你使用了<code>dataset</code>管理数据则更方便了，可以使用<code>encode.itemGroupId</code>来指定一个维度编码成<code>groupId</code>。</p> 
<p>比如我们要实现一个柱状图下钻的动画，可以将下钻后的整个系列的数据都设置同一个<code>groupId</code>，然后跟下钻前的数据对应起来：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113618_IqJZ_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>通过<code>groupId</code>，我们还可以实现更丰富的聚合，下钻动画。</p> 
<p>数据的聚合：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113636_L0Z3_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>单系列下钻成两个系列：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113652_QxFs_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>全局过渡动画使得数据的关系和演变的表达能力走上新的台阶，为你的可视化创作灵感插上翅膀。</p> 
<p>看到这里，我们知道你已经跃跃欲试了。但是别急，5.2.0 还有更多值得一看的新功能。</p> 
<h2>调色盘的取色策略</h2> 
<p>在上面全局过渡动画的示例中，大家可能有注意到我们使用了一个之前版本没有的<code>colorBy</code>配置项，这个配置项也是我们这个版本新增加的一个特性，用来给系列配置不同粒度的调色盘取色。这个配置目前支持两种策略：</p> 
<ul> 
 <li> <p><code>'series'</code> 按照系列分配调色盘中的颜色，同一系列中的所有数据都是用相同的颜色。</p> </li> 
 <li> <p><code>'data'</code> 按照数据项分配调色盘中的颜色，每个数据项都使用不同的颜色。</p> </li> 
</ul> 
<p>在之前我们是按照系列的类型固定了这个策略，比如柱状图就是固定<code>'series'</code>的策略，而饼图则是固定<code>'data'</code>的策略。</p> 
<p>而现在新增这个配置项后，我们可以在柱状图中给每个数据项都分配不同的颜色：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e93b96d87de2e49a228ef5803761051f807.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-javascript">option = &#123;
  series: [
    &#123;
      data: [...],
      type: 'bar',
      colorBy: 'data'
    &#125;
  ], ...
&#125;;</code></pre> 
<p>或者在饼图中统一使用一个颜色：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113819_Meek_2720166.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-javascript">option = &#123;
  series: &#123;
    type: 'pie',
    colorBy: 'series',
    itemStyle: &#123;
      borderColor: '#fff',
      borderWidth: 1
    &#125;,
    data: [...]
  &#125;
&#125;;</code></pre> 
<p>这一配置项可以让我们避免了去找调色盘颜色然去一一设置的麻烦，可能在特定的场景需求中提供便捷。后续我们会对这个配置项做进一步的增强，提供更多的调色盘取色的策略。</p> 
<h2>极坐标柱状图的标签</h2> 
<p>这个版本中我们实现了极坐标上的柱状图的标签，并且支持丰富的标签定位配置。下面是一个最常见的标签显示在端点的进度图：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113840_VSmN_2720166.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-javascript">option = &#123;
  series: [
    &#123;
      type: 'bar',
      data: [3, 4, 5, 6],
      colorBy: 'data',
      roundCap: true,
      label: &#123;
        show: true,
        // 试试改成 'insideStart'
        position: 'start',
        formatter: '&#123;b&#125;'
      &#125;,
      coordinateSystem: 'polar'
    &#125;
  ], ...
&#125;;</code></pre> 
<p>更多标签位置的配置：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113853_rPNf_2720166.jpg" referrerpolicy="no-referrer"></p> 
<p>这一灵活的标签位置配置项大大丰富了极坐标柱状图的表达能力，让文字清晰地匹配对应的数据。</p> 
<h2>空数据的饼图样式</h2> 
<p>在之前的版本中，如果饼图没有数据，画面中可能就是完全空白的。因为没有任何的视觉元素，所以用户会疑惑是不是出现了 bug 导致图中没有内容。</p> 
<p>为了解决这个问题，这个版本我们会默认在无可显示数据的时候显示一个灰色的占位圆以防止画面中完全空白。我们可以通过<code>emptyCircleStyle</code>配置这个占位圆的样式。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0902/113907_QORx_2720166.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-javascript">option = &#123;
  series: [
    &#123;
      type: 'pie',
      data: [],
      // showEmptyCircle: false,
      emptyCircleStyle: &#123;
        // 将样式改为空心圆
        color: 'transparent',
        borderColor: '#ddd',
        borderWidth: 1
      &#125;
    &#125;
  ]
&#125;;</code></pre> 
<p>如果不想要显示这个灰色的圆，也可以设置<code>showEmptyCircle: false</code>关闭。</p> 
<h2>高维数据的性能增强</h2> 
<p>我们从 4.0 开始引入了 dataset 用来管理图表的数据，通常情况下<code>dataset</code>提供了更方便的数据管理方式而且跟传统的方式不会有什么性能上的差别。但是在一些极端的特别高维（>100）数据的场景下，我们还是会碰到一些性能急剧下降的问题，比如下面这种通过一千个系列去可视化千维数据的场景（#11907），甚至可能会卡住。</p> 
<pre><code class="language-javascript">const indices = Array.from(Array(1000), (_, i) => &#123;
  return `index$&#123;i&#125;`;
&#125;);
const option = &#123;
  xAxis: &#123; type: 'category' &#125;,
  yAxis: &#123;&#125;,
  dataset: &#123;
    // dimension: ['date', ...indices],
    source: Array.from(Array(10), (_, i) => &#123;
      return &#123;
        date: i,
        ...indices.reduce((item, next) => &#123;
          item[next] = Math.random() * 100;
          return item;
        &#125;, &#123;&#125;)
      &#125;;
    &#125;)
  &#125;,
  series: indices.map(index => &#123;
    return &#123; type: 'line', name: index &#125;;
  &#125;)
&#125;;</code></pre> 
<p>产生这个性能问题是因为我们在底层每个系列都会按照其需要处理一遍这个 dataset，然后保存一份处理过后的数据以及维度等元信息。这意味着刚才那个例子中需要处理并保存<code>1000 x 1000</code>个维度的信息，这带来了巨大的内存和垃圾回收的压力，从而导致了高维度的性能的急剧下降。</p> 
<p>在新版本中我们对这个问题做了优化，所有系列都尽可能共享 dataset 的数据（能否共享取决于系列怎么使用这份数据）存储而非每个系列都处理并存储一次，并且只处理和存储了使用到的维度。这些优化保证了内存不会随着 dataset 维度和系列的增长而爆炸，大幅度的提升了极端场景下的初始化性能。刚才例子的渲染耗时也从卡住降低到了可接受的 300 毫秒以下。</p> 
<p>这次优化带来收益的还不只是这种高维的场景，在使用维度不高但是数据量很大的 dataset 的时候，因为数据的共享所以多个系列只处理了一遍数据，因此也可以带来显著的性能提升。</p> 
<h2>自定义系列的类型优化</h2> 
<p>自定义系列提供了非常灵活的创建系列图形的方式，相对于其它系列，自定义系列的学习曲线可能有些陡峭，而且容易出错。因此在这个版本中，我们进一步的优化了自定义系列中的核心方法<code>renderItem</code>的类型，对于<code>renderItem</code>的参数和返回值类型做了更精确的推断，从而可以根据返回的图形类型推断出可以设置该图形的哪些属性：</p> 
<pre><code class="language-javascript">series = &#123;
  type: 'custom',
  renderItem(params) &#123;
    return &#123;
      type: 'group',
      // group 类型使用 children 存储其它类型的子元素
      children: [
        &#123;
          type: 'circle',
          // circle 拥有下面这些可以配置的 shape 属性
          shape: &#123; r: 10, cx: 0, cy: 0 &#125;,
          // 可以配置的样式
          style: &#123; fill: 'red' &#125;
        &#125;,
        &#123;
          type: 'rect',
          // rect 拥有下面这些可以配置的 shape 属性
          shape: &#123; x: 0, y: 0, width: 100, height: 100 &#125;
        &#125;,
        &#123;
          type: 'path',
          // 自定义路径图形
          shape: &#123; d: '...' &#125;
        &#125;
      ]
    &#125;;
  &#125;
&#125;;</code></pre> 
<h2>小结</h2> 
<p>以上我们介绍了 5.2.0 中的新特性以及优化，如果你对其中的一些特性感兴趣，不妨更新到最新版本的 Apache ECharts 亲自体验一下。</p> 
<p>如果你对 Apache ECharts 接下来的计划感兴趣，也可以在 GitHub Milestone（https://github.com/apache/echarts/milestones）关注我们的开发计划。也非常欢迎加入我们的贡献者行列（在 GitHub Wiki 中了解更多）。</p> 
<h3>版本更新记录</h3> 
<h4>非兼容改动</h4> 
<ul> 
 <li> <p>[Fix][pie] 负值会被作为非法值过滤。#15095 (ssthouse)</p> </li> 
</ul> 
<h4>所有改动</h4> 
<ul> 
 <li> <p><strong>[Feature] 新增全局过渡动画。#15208 (pissang)</strong></p> </li> 
 <li> <p>[Feature][color] 新增<code>series.colorBy</code>配置不同粒度的取色。#13788 (Ovilia)</p> </li> 
 <li> <p>[Feature][label] 极坐标系柱状图支持标签显示。#15182 (Ovilia)</p> </li> 
 <li> <p>[Feature][effectscatter] 新增<code>rippleEffect.number</code>配置涟漪数目。#15335 (plainheart)</p> </li> 
 <li> <p>[Feature][gauge] 新增<code>pointer.showAbove</code>配置指针和标签的显示层级。#15337 (AmosChenYQ) #15326 (susiwen8)</p> </li> 
 <li> <p>[Feature][emphasis] <code>emphasis.color</code>支持设置为<code>'inherit'</code>关闭高亮。#15172 (Foreverwzh)</p> </li> 
 <li> <p>[Feature][pie] 无数据的时候默认显示灰色的占位圆。#15095 (ssthouse)</p> </li> 
 <li> <p>[Fix][dataset] 优化高维数据<code>dataset</code>的性能。#15355 (pissang)</p> </li> 
 <li> <p>[Fix][axis] 优化时间轴刻度标签的格式化显示。#15465 (leavest) #15434 (zhiyuc123)</p> </li> 
 <li> <p>[Fix][custom] 优化旧代码对于<code>font</code>的兼容性。#15454 (AmosChenYQ)</p> </li> 
 <li> <p>[Fix][memory] 优化实例销毁后依旧持有实例时的内存占用。#15417 (pissang)</p> </li> 
 <li> <p>[Fix][line] 优化有无穷大数据时的渐变色显示。#15416 (plainheart)</p> </li> 
 <li> <p>[Fix][date] 优化<code>date</code>数据的解析。#15410 (quillblue)</p> </li> 
 <li> <p>[Fix][line] 修复渲染出错。#788 (pissang)</p> </li> 
 <li> <p>[Fix][candlestick] 修复样式可能在<code>setOption</code>后丢失的问题。#15368 (pissang)</p> </li> 
 <li> <p>[Fix][sankey] 修复垂直布局时的渐变色边。#15363 (susiwen8)</p> </li> 
 <li> <p>[Fix][tooltip] 修复在设置<code>tooltip.position</code>后<code>formatter</code>返回 DOM 对象会被解析成字符串的问题。#15313 (plainheart)</p> </li> 
 <li> <p>[Fix][tooltip] <code>formatter</code>返回<code>null</code>时清空内容。#15313 (plainheart)</p> </li> 
 <li> <p>[Fix][bar] 标签位置设置为<code>'middle'</code>时应该显示在图形中间。#15309 (Ovilia)</p> </li> 
 <li> <p>[Fix][marker] 修复可能会在极坐标柱状图报<code>'clampData' is undefined</code>的错误。#15297 (AmosChenYQ)</p> </li> 
 <li> <p>[Fix][treemap] 修复关闭动画后更新可能旧节点不会被移除的问题。#15283 (villebro)</p> </li> 
 <li> <p>[Fix][tree] 修复更新数据时边可能会不被移除的问题。#15251 (ssthouse)</p> </li> 
 <li> <p>[Fix][pie/sunburst] 修复<code>borderRadius</code>被设置为<code>null</code>或者<code>undefined</code>时无法重置的问题。#15243 (plainheart)</p> </li> 
 <li> <p>[Fix][canvas] 修复<code>fillStyle</code>被设置为<code>'none'</code>或者<code>null</code>时 FireFox 浏览器下会报警告的问题。#784 (plainheart)</p> </li> 
 <li> <p>[Fix][highlight] 修复<code>chart.dispatchAction</code>高亮多个系列可能会不正确的问题。#15207 (ssthouse)</p> </li> 
 <li> <p>[Fix][sankey] 修复使用<code>series.nodes</code>作为数据时拖拽功能失效的问题。#15199 (DuLinRain)</p> </li> 
 <li> <p>[Fix][svg] 优化导出的 SVG 文件在 Powerpoint 中的兼容性。#767 (plainheart)</p> </li> 
 <li> <p>[Fix][legend] 修复<code>text.lineHeight</code>不生效。#773 (ssthouse)</p> </li> 
 <li> <p>[Fix][pie] 将默认的<code>borderJoin</code>设置为<code>round</code>。#15145 (plainheart)</p> </li> 
 <li> <p>[Fix][radar] 将默认的<code>borderJoin</code>设置为<code>round</code>。#15381 (Ovilia)</p> </li> 
 <li> <p>[Fix][treemap] 修复设置<code>label.show</code>为<code>false</code>会报错。#15141 (susiwen8)</p> </li> 
 <li> <p>[Fix][pictorialbar] 修复零数据标签的显示问题。#15132 (ssthouse)</p> </li> 
 <li> <p>[Fix][lines] 修复调用<code>chart.clear()</code>可能会无法清除线条的问题。#15088 (plainheart)</p> </li> 
 <li> <p>[Fix][endlabel] 修复端点标签只设置<code>emphasis.show</code>为<code>true</code>时可能无法显示的问题。#15072 (Ovilia)</p> </li> 
 <li> <p>[Fix][svg] 修复矩形路径没有合并的问题。#767 (plainheart)</p> </li> 
 <li> <p>[Fix][treemap] 在回调函数参数中添加<code>treeAncestors</code>属性。#14976 (pissang)</p> </li> 
 <li> <p>[Fix][tree] 修复调用<code>setOption</code>两次更新数据时可能报错的问题。#14930 (Map1en)</p> </li> 
 <li> <p>[Fix][radar] 修复图形边框被缩放的问题。#15396 (pissang)</p> </li> 
 <li> <p>[Fix][marker] 修复<code>symbolOffset</code>和<code>symbolKeepAspect</code>配置项不生效的问题。#14737 (plainheart)</p> </li> 
 <li> <p>[Fix][gauge] 支持进度条和指针的点击事件。#14688 (yufeng04)</p> </li> 
 <li> <p>[Fix][tooltip] 优化箭头的边框宽度，跟配置同步。#14393 (g7i)</p> </li> 
 <li> <p>[Fix][geo] 修复地理坐标组件从<code>show: false</code>配置为<code>show: true</code>后依旧不显示的问题。#15361 (pissang)</p> </li> 
 <li> <p>[Fix][type] 优化自定义系列<code>renderItem</code>的类型推断。</p> </li> 
 <li> <p>[Fix][type] 优化<code>echarts.init</code>的配置项类型。#15487 (John60676)</p> </li> 
 <li> <p>[Fix][type] 修复类型中<code>polarIndex</code>配置项丢失的问题。#15281 (Map1en)</p> </li> 
 <li> <p>[Fix][type] 优化 SVG 数据源的类型。#15263 (leosxie)</p> </li> 
 <li> <p>[Fix][type] 优化饼图和地图系列中的数据类型。#15144 (plainheart)</p> </li> 
</ul>
                                        </div>
                                      
</div>
            