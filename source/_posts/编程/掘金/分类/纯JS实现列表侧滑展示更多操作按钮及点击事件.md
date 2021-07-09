
---
title: '纯JS实现列表侧滑展示更多操作按钮及点击事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ccb91fb720f4c1693f5f0b1dd10b578~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 00:21:16 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ccb91fb720f4c1693f5f0b1dd10b578~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>直接进入主题，先看一下效果图</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ccb91fb720f4c1693f5f0b1dd10b578~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-07-09下午3.26.11-迅捷PDF转换器.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39224166164c41a9b7ba798469cb6198~tplv-k3u1fbpfcp-watermark.image" alt="点击事件.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大概就是这样的一个效果，这样的效果在iOS上很常见，本人就是做iOS开发，iOS上面的UITableView 在系统框架上是会提供这样的用户操作API的。</p>
<p>在web中同样也想实现这样的用户操作应该怎么做？这里简单的说一下思路，大神、大佬，凡是“大”字辈儿的觉得“班门弄斧”的可以最后点个赞，非常感谢。</p>
<blockquote>
<p><strong>封装对象，监管所有的用户操作</strong></p>
</blockquote>
<p>对象初始化方法
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4a12d200a1041ebb12662edbe3f07c4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对象初始化
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80e236cefa0f4946abb235840e18993a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里创建了一个dragMoreOption对象，顾名思义就是拖拽展示更多用户操作。</p>
<p><em><strong>参数说明</strong></em></p>
<p>vm：父类容器id；</p>
<p>cellClassName:子类做侧滑dom对象的class；</p>
<p>items:需要展示自定义内容及其他配置项，这里只添加了一个背景颜色值；</p>
<p><em><strong>给对象添加 initTouchEven 方法，实现鼠标的mousedown、mousemove、mouseup方法</strong></em></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db766ef26cbd448f94a98b079b5d726e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>步骤一、给全部的cell（这里指需要侧滑操作的dom对象，iOS下称为cell，细胞的意思）添加mousedown方法，获取当前鼠标点击的初始位置（这里用一个自定义point的对象保存，保存evenX,evenY），这之所以个cell添加mousedown事件是要获取并全局保存一下当前的cell。</p>
<p>步骤二、给最外层的父节点添加拖拽mousemove事件，这里由于进行侧滑手势，所以只需要处理当前even.x值即可。当然，这里也用自定义point对象保存了一下移动中的even.x和even.y，由于只要求左滑，那么就处理移动过程点的x值小于一开始的mousedown记录点的x值即可，获取二者的差值，修改当前全局保存的cell的css中的left值。</p>
<p>步骤三、给每个cell添加可操作的item(dom对象)块，index（索引）及expend（是否展开的标示）。</p>
<p>步骤四、当cell处于展开的位置时，将它对应的可操作的item的'z-index'值设置到cell的上面。当cell处于收起状态时可操作的item的'z-index'值设置到cell的下面。这样就为可操作的item添加了点击事件而不会cellmousedown事件有冲突。</p>
<p>步骤五、简单处理一下手势滑动的位置判定，超过可展示item全部宽度的一半时抬起鼠标自动打开，小于一半时抬起鼠标自动恢复原状。</p>
<blockquote>
<p><strong>最后直接上代码，思路总是次要的，代码诚不欺我</strong></p>
</blockquote>
<p><strong>目录结构</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5442eb5b244043dcb13a4c764efd4bd9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>dragMoreOption.html</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
* &#123;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.wrap</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">380px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
zoom: <span class="hljs-number">1</span>;
<span class="hljs-attribute">overflow-x</span>: scroll;
<span class="hljs-attribute">overflow-y</span>: hidden;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#8E8E8E</span>;
<span class="hljs-attribute">margin-top</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">margin-left</span>: <span class="hljs-number">400px</span>;
<span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-selector-class">.cell</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">45px</span>;
<span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">#8E8E8E</span> solid <span class="hljs-number">1px</span>;
<span class="hljs-attribute">background-color</span>: lightgray;
<span class="hljs-attribute">position</span>: relative;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"http://libs.baidu.com/jquery/1.9.0/jquery.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"dragMoreOption.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrap"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"wrap"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cell"</span>></span>测试1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cell"</span>></span>测试2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cell"</span>></span>测试3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> dragMoreOption = <span class="hljs-keyword">new</span> DragMoreOption(<span class="hljs-string">'wrap'</span>, <span class="hljs-string">'cell'</span>,
[&#123;
<span class="hljs-string">'title'</span>: <span class="hljs-string">'删除'</span>,
<span class="hljs-string">'color'</span>: <span class="hljs-string">'red'</span>
&#125;, &#123;
<span class="hljs-string">'title'</span>: <span class="hljs-string">'编辑'</span>,
<span class="hljs-string">'color'</span>: <span class="hljs-string">'green'</span>
&#125;]);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>dragMoreOption.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DragMoreOption</span>(<span class="hljs-params">vm, cellClassName, items</span>) </span>&#123;
<span class="hljs-built_in">this</span>.contain = $(<span class="hljs-string">"#"</span> + vm);
<span class="hljs-built_in">this</span>.vmName = vm;
<span class="hljs-built_in">this</span>.containWidth = $(<span class="hljs-built_in">this</span>.contain).width();
<span class="hljs-built_in">this</span>.cellClassName = cellClassName;
<span class="hljs-built_in">this</span>.items = items;
<span class="hljs-built_in">this</span>.action = <span class="hljs-literal">false</span>; <span class="hljs-comment">//定义一个全局变量来判断鼠标动作，默认为false</span>
<span class="hljs-built_in">this</span>.mouseTapX = <span class="hljs-number">0</span>;
<span class="hljs-built_in">this</span>.mouseTapY = <span class="hljs-number">0</span>;
<span class="hljs-built_in">this</span>.currentSelectItem = <span class="hljs-literal">null</span>;
<span class="hljs-built_in">this</span>.beginPoint = &#123;&#125;;
<span class="hljs-built_in">this</span>.moveX = <span class="hljs-literal">null</span>;
<span class="hljs-built_in">this</span>.itemBtnWidth = <span class="hljs-number">80</span>;
<span class="hljs-built_in">this</span>.isBounceActive = <span class="hljs-literal">false</span>;
<span class="hljs-built_in">this</span>.bounceInterval = <span class="hljs-number">300</span>; <span class="hljs-comment">//弹簧效果时长</span>
<span class="hljs-built_in">this</span>.totleWidth = <span class="hljs-built_in">this</span>.itemBtnWidth * <span class="hljs-built_in">this</span>.items.length;
<span class="hljs-built_in">this</span>.isHaveExpend = <span class="hljs-literal">false</span>;
<span class="hljs-built_in">this</span>.isOptionSameItem = <span class="hljs-literal">false</span>;
<span class="hljs-built_in">this</span>.initTouchEven();
<span class="hljs-built_in">this</span>.addCellPrototype();

&#125;

DragMoreOption.prototype = &#123;
<span class="hljs-comment">//初始化touchEven</span>
<span class="hljs-attr">initTouchEven</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
$(<span class="hljs-built_in">document</span>).on(<span class="hljs-string">"mousedown"</span>, <span class="hljs-string">"."</span> + that.cellClassName, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
<span class="hljs-comment">//鼠标按下事件</span>
that.action = <span class="hljs-literal">true</span>;
that.isOptionSameItem = (<span class="hljs-built_in">this</span> == that.currentSelectItem);
that.beginPoint.x = event.pageX;
that.beginPoint.y = event.pageY;
that.moveX = <span class="hljs-number">0</span>;
<span class="hljs-keyword">if</span>(that.isHaveExpend)&#123;
that.optionItemBeforeOrBelow(<span class="hljs-literal">false</span>);
$(that.currentSelectItem).animate(&#123;
<span class="hljs-attr">left</span>: <span class="hljs-number">0</span> + <span class="hljs-string">'px'</span>,
&#125;, that.bounceInterval);
&#125;
that.currentSelectItem = <span class="hljs-built_in">this</span>;

&#125;)
$(<span class="hljs-built_in">document</span>).on(<span class="hljs-string">"mousemove"</span>, <span class="hljs-string">"."</span> + that.vmName, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
<span class="hljs-comment">//wrap上的鼠标移动事件，menu 移动</span>
<span class="hljs-keyword">if</span> (that.action == <span class="hljs-literal">true</span> && !that.isBounceActive && !that.isOptionSameItem) &#123;

<span class="hljs-keyword">var</span> currentPoint = &#123;&#125;;
currentPoint.x = event.pageX;
currentPoint.y = event.pageY;
<span class="hljs-keyword">var</span> changeX = currentPoint.x - that.beginPoint.x;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.abs(changeX) > that.totleWidth) &#123;
changeX = -(that.totleWidth);
&#125;
that.moveX = <span class="hljs-built_in">Math</span>.abs(changeX);
<span class="hljs-keyword">if</span> (changeX < <span class="hljs-number">0</span>) &#123;
$(that.currentSelectItem).css(&#123;
<span class="hljs-string">"left"</span>: changeX + <span class="hljs-string">'px'</span>,
&#125;);
&#125;
&#125;
&#125;)

$(<span class="hljs-built_in">document</span>).on(<span class="hljs-string">"mouseup"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-comment">//鼠标弹起时将移动的menu 放入新的接受div里，并移除原div位置上的空div</span>
that.isBounceActive = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> isNeedExpend = that.moveX > (that.totleWidth) / <span class="hljs-number">2.0</span>
<span class="hljs-keyword">if</span> (!isNeedExpend) &#123;
$(that.currentSelectItem).animate(&#123;
<span class="hljs-attr">left</span>: <span class="hljs-number">0</span> + <span class="hljs-string">'px'</span>,
&#125;, that.bounceInterval);
&#125; <span class="hljs-keyword">else</span> &#123;
$(that.currentSelectItem).animate(&#123;
<span class="hljs-attr">left</span>: - that.totleWidth + <span class="hljs-string">'px'</span>,
&#125;, that.bounceInterval);
&#125;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
that.isBounceActive = <span class="hljs-literal">false</span>;
$(that.currentSelectItem).attr(<span class="hljs-string">"expend"</span>, isNeedExpend);
that.isHaveExpend = isNeedExpend;
<span class="hljs-keyword">if</span>(!isNeedExpend) &#123;
that.currentSelectItem = <span class="hljs-literal">null</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
that.optionItemBeforeOrBelow(<span class="hljs-literal">true</span>);
&#125;
&#125;, that.bounceInterval + <span class="hljs-number">10</span>);
that.action = <span class="hljs-literal">false</span>;
&#125;)
&#125;,
<span class="hljs-comment">//添加cell index（索引）、expend（是否为操作状态）属性</span>
<span class="hljs-attr">addCellPrototype</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> items = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-built_in">this</span>.cellClassName);
<span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;
<span class="hljs-keyword">var</span> item = items[i];
$(item).attr(<span class="hljs-string">"index"</span>, i);
$(item).attr(<span class="hljs-string">"expend"</span>, <span class="hljs-literal">false</span>);
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>;j < <span class="hljs-built_in">this</span>.items.length;j++)&#123;
<span class="hljs-comment">//添加操作选项</span>
<span class="hljs-keyword">var</span> cellObj = <span class="hljs-built_in">this</span>.items[j];
<span class="hljs-keyword">var</span> y = $(item).offset().top - $(<span class="hljs-built_in">this</span>.contain).offset().top;
<span class="hljs-keyword">var</span> tempDiv = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
$(tempDiv).css(<span class="hljs-string">"left"</span>, <span class="hljs-built_in">this</span>.containWidth - <span class="hljs-built_in">this</span>.itemBtnWidth * (j + <span class="hljs-number">1</span>));
$(tempDiv).css(<span class="hljs-string">"top"</span>, y-<span class="hljs-number">1</span>);
$(tempDiv).css(<span class="hljs-string">"width"</span>, <span class="hljs-built_in">this</span>.itemBtnWidth);
$(tempDiv).css(<span class="hljs-string">"height"</span>, $(item).height() + <span class="hljs-number">1</span> + <span class="hljs-string">'px'</span>);
$(tempDiv).css(<span class="hljs-string">"position"</span>, <span class="hljs-string">'absolute'</span>);
$(tempDiv).css(<span class="hljs-string">"text-align"</span>, <span class="hljs-string">'center'</span>);
$(tempDiv).css(<span class="hljs-string">"display"</span>, <span class="hljs-string">'inline-block'</span>);
$(tempDiv).css(<span class="hljs-string">"background-color"</span>, cellObj.color);
$(tempDiv).css(<span class="hljs-string">"lineHeight"</span>, $(item).height() + <span class="hljs-number">1</span> + <span class="hljs-string">'px'</span>);
$(tempDiv).css(<span class="hljs-string">"z-index"</span>, <span class="hljs-string">'-1'</span>);
$(tempDiv).css(<span class="hljs-string">"color"</span>, <span class="hljs-string">'white'</span>);
$(tempDiv).attr(<span class="hljs-string">'class'</span>, <span class="hljs-string">'itemStyle'</span>)
$(tempDiv).text(cellObj.title);
<span class="hljs-keyword">var</span> indexPath = &#123;<span class="hljs-string">'row'</span>:i,<span class="hljs-string">'column'</span>:j&#125;;
$(tempDiv).attr(<span class="hljs-string">"indexPath"</span>, <span class="hljs-built_in">JSON</span>.stringify(indexPath))
$(<span class="hljs-built_in">this</span>.contain).append(tempDiv);
$(tempDiv).click(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  that.optionItemClickEven($.parseJSON($(<span class="hljs-built_in">this</span>).attr(<span class="hljs-string">"indexPath"</span>)));
&#125;);
&#125;
&#125;
&#125;,
<span class="hljs-comment">//添加item点击事件</span>
<span class="hljs-attr">optionItemClickEven</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">indexPath</span>)</span>&#123;
<span class="hljs-keyword">var</span> title = <span class="hljs-built_in">this</span>.items[indexPath.column].title;
alert(<span class="hljs-string">'你点击了'</span> + title);
&#125;,
<span class="hljs-comment">//展开后将可操作的item移到最上层或最下层</span>
<span class="hljs-attr">optionItemBeforeOrBelow</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">isUp</span>)</span>&#123;
<span class="hljs-keyword">var</span> index = $(<span class="hljs-built_in">this</span>.currentSelectItem).attr(<span class="hljs-string">'index'</span>);
<span class="hljs-keyword">var</span> items = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">'itemStyle'</span>);
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;i < items.length;i++)&#123;
<span class="hljs-keyword">var</span> item = items[i];
<span class="hljs-keyword">var</span> indexPath = $.parseJSON($(item).attr(<span class="hljs-string">"indexPath"</span>));
<span class="hljs-keyword">if</span>(indexPath.row == index)&#123;
$(item).css(<span class="hljs-string">"z-index"</span>, isUp ? <span class="hljs-string">'10'</span> : <span class="hljs-string">'-1'</span>);
&#125;
&#125;
&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里代码里有些细节，比如如何确定点击的item的位置代码中是有处理的，就是为cell添加index属性，给每个item添加indexPath属性。</p>
<p><strong>好了，代码都是自己手敲的，要多简朴有多简朴，大家多担待，互相学习，共同进步。</strong></p></div>  
</div>
            