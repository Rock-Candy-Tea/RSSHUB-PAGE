
---
title: '纯JS 实现列表轻点删除、长按拖拽及错位排序动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81c9dba7c3c54191866105ecc609a7f3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 22:30:01 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81c9dba7c3c54191866105ecc609a7f3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81c9dba7c3c54191866105ecc609a7f3~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-07-08上午10.37.40-迅捷PDF转换器.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里简单说下实现轻点、长按列表实现错位排序动画实现思路，这里只用到了JQ，没有使用其他的库。胸有成竹、不屑一顾的大神请直接跳到最后点个赞也好，非常感谢。</p>
<blockquote>
<p><strong>如何用JS区分轻点和长按？</strong></p>
</blockquote>
<p>用户手势交互可以直接使用mouse事件处理（移动端用touch事件），监听mouse事件在对应dom上的状态。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ac329c19bd448a9822d5088f94fd7ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
对于列表item这里采用的className 为menu，当鼠标在列表的item按下时，这里添加一个定时器，定时器延迟操作可以设置长按事件的等待时间。这里记录一下按下时的系统时间。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4411b2ead4414dc588763a30d0e233d1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在mouseup事件里再去获取一次系统时间，若两次的时间差小于设置的长按事件界定时长，那么处理轻点事件，若大于该时长，处理长按事件。</p>
<p>这里就能区分用户操作是轻点还是长按了。</p>
<blockquote>
<p><strong>如何实现轻点删除后的错位动画</strong>？</p>
</blockquote>
<p>这里初始化的所有列表位置布局是用JS创建dom对象并添加CSS样式实现的，本人CSS水平有限，没有想到这类场景如何用CSS去添加动画。创建完所有的item后，计算获取每个item对应位置信息这里标为“rect”属性；先创建rect对象，包含四个属性:x,y,width,height。</p>
<p>获取rect的目的有两个：</p>
<p>1、是在鼠标移动的过程中去检测当前的even触点位置是否在某个可交换的item上。</p>
<p>2、判断进行错位动画时获取需要改变后的调整的位置。</p>
<p>JS动态创建下的dom对象无法改变在文档流中的位置，但是改变后的位置又可能为后续环节使用，所以除了在dom对象上添加了rect属性外，还添加了index属性。这样在排序的过程中，index属性也相应改变，在最后获取排序结果时根据index操作即可。</p>
<p>上面已经分析了如何执行轻点事件，那么当item在执行轻点事件时候进行移除操作，</p>
<p><em><strong>执行移除当前点击的item</strong></em></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2926f263902b413a97d1bdfcfd4819e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为删除了item后面的所有item的index属性都要修改，所以这里添加了一个方法来时现实index的重排。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4d9c808eed14de39a2f57b90dcda36c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注：参数index是要删除item的索引值。</p>
<p><em><strong>依次改变要删除item后面的全部item的rect，并实现错位动画</strong></em></p>
<p>修改rect属性
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e07b3321c1fc4778ac5d578974be59ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加错位动画</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/866ebead21fc428b8d02226cd2e9e2c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，这里就完成了轻点删除及错位动画。</p>
<p><em>在遍历所有item前调用了一个排序方法获取以index为排序依据的dom集合！！！</em></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce28d0ee065c4141bb445de6bd163757~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>如何设置拖拽排序及错位动画？</strong></p>
</blockquote>
<p>这里用到了mousemove方法。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f998620ca33244aaa72b1e5758e2138c~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-07-08上午10.37.40-迅捷PDF转换器.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1、当拖拽开始后，全局保存下当前的所选的item，获取mouse的even的x值跟y值，控制当前所选的item位置跟随触点变化。</p>
<p>2、检测触点移动的位置是否处在可交换的其他item上，若条件符合，根据当前的被拖拽的item的与可交换的item的index属性进行判断，修改二者之间的其他item位置，重置其rect及index属性值。</p>
<blockquote>
<p><strong>目录结构</strong></p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abfef5a48d4241299c9bc692ba787a21~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>源码粘出来想看的可以看看，觉得太长的可以忽略，个人随笔，肯定有不严谨的地方，希望大神留言指正，互相学习。</p>
<p><em><strong>dragPlus.html</strong></em></p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
* &#123;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.wrap</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">380px</span>;
<span class="hljs-attribute">height</span>: auto;
zoom: <span class="hljs-number">1</span>;
<span class="hljs-attribute">overflow</span>: hidden;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#8E8E8E</span>;
<span class="hljs-attribute">margin-top</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">margin-left</span>: <span class="hljs-number">400px</span>;
<span class="hljs-attribute">position</span>: relative;
&#125;

<span class="hljs-selector-class">.menu</span> &#123;
<span class="hljs-attribute">background-color</span>: darkred;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#FFFFFF</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
<span class="hljs-attribute">text-align</span>: center;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">display</span>: inline-block;
<span class="hljs-attribute">z-index</span>: <span class="hljs-number">10</span>;
&#125;

<span class="hljs-selector-class">.active</span> &#123;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#8E8E8E</span>;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">display</span>: inline-block;
<span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
&#125;

<span class="hljs-selector-class">.onclick</span> &#123;
<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1.2</span>);
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">background-color</span>: darkred;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
<span class="hljs-attribute">width</span>: <span class="hljs-number">70px</span>;
<span class="hljs-attribute">text-align</span>: center;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#FFFFFF</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"http://libs.baidu.com/jquery/1.9.0/jquery.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./dragPlus.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrap"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"wrap"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> drag = <span class="hljs-keyword">new</span> DragPlus(<span class="hljs-string">'wrap'</span>, [<span class="hljs-string">"测试1"</span>, <span class="hljs-string">"测试2"</span>, <span class="hljs-string">"测试3"</span>, <span class="hljs-string">"测试4"</span>, <span class="hljs-string">"测试5"</span>, <span class="hljs-string">"测试1"</span>, <span class="hljs-string">"测试2"</span>, <span class="hljs-string">"测试3"</span>, <span class="hljs-string">"测试4"</span>, <span class="hljs-string">"测试5"</span>, ], <span class="hljs-number">3</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./dragTouchEven.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><em>dragPlus.js</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DragPlus</span>(<span class="hljs-params">vm, items, column</span>) </span>&#123;
<span class="hljs-built_in">this</span>.contain = $(<span class="hljs-string">"#"</span> + vm);
<span class="hljs-built_in">this</span>.items = items;
<span class="hljs-built_in">this</span>.column = column;
<span class="hljs-built_in">this</span>.sep = <span class="hljs-number">10</span>;
<span class="hljs-built_in">this</span>.reload();
<span class="hljs-built_in">this</span>.duran = <span class="hljs-number">500</span>;
<span class="hljs-built_in">this</span>.currentOptionElement = <span class="hljs-literal">null</span>;
&#125;

DragPlus.prototype = &#123;
<span class="hljs-comment">//刷新</span>
<span class="hljs-attr">reload</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> width = $(<span class="hljs-built_in">this</span>.contain).width();
<span class="hljs-keyword">var</span> itemWidth = (width - <span class="hljs-built_in">this</span>.sep * (<span class="hljs-built_in">this</span>.column + <span class="hljs-number">1</span>)) / <span class="hljs-built_in">this</span>.column;
<span class="hljs-keyword">var</span> itemHeight = itemWidth;
<span class="hljs-keyword">var</span> row = <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.items.length / <span class="hljs-built_in">this</span>.column) + ((<span class="hljs-built_in">this</span>.items.length % <span class="hljs-built_in">this</span>.column) ? <span class="hljs-number">1</span> : <span class="hljs-number">0</span>);
<span class="hljs-keyword">var</span> maxY = itemHeight * row + <span class="hljs-built_in">this</span>.sep * (row + <span class="hljs-number">1</span>);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.items.length; i++) &#123;
<span class="hljs-keyword">var</span> text = <span class="hljs-built_in">this</span>.items[i];
<span class="hljs-keyword">var</span> tempDiv = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
$(tempDiv).attr(<span class="hljs-string">'class'</span>, <span class="hljs-string">'menu'</span>)
<span class="hljs-keyword">var</span> x = <span class="hljs-built_in">this</span>.sep + (i % <span class="hljs-built_in">this</span>.column) * (itemWidth + <span class="hljs-built_in">this</span>.sep);
<span class="hljs-keyword">var</span> y = <span class="hljs-built_in">this</span>.sep + <span class="hljs-built_in">parseInt</span>(i / <span class="hljs-built_in">this</span>.column) * (itemWidth + <span class="hljs-built_in">this</span>.sep);
$(tempDiv).css(<span class="hljs-string">"left"</span>, x);
$(tempDiv).css(<span class="hljs-string">"top"</span>, y);
$(tempDiv).text(text);
$(tempDiv).width(itemWidth);
$(tempDiv).height(itemHeight);
$(<span class="hljs-built_in">this</span>.contain).append(tempDiv);
<span class="hljs-keyword">var</span> rect = &#123;&#125;
rect.x = x;
rect.y = y;
rect.width = itemWidth;
rect.height = itemHeight;
$(tempDiv).attr(<span class="hljs-string">"rect"</span>, <span class="hljs-built_in">JSON</span>.stringify(rect))
&#125;
$(<span class="hljs-built_in">this</span>.contain).height(maxY)
<span class="hljs-built_in">this</span>.resetIndex(<span class="hljs-literal">null</span>);
&#125;,
<span class="hljs-comment">//删除</span>
<span class="hljs-attr">deleteItem</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>) </span>&#123;
<span class="hljs-keyword">var</span> index = $(item).attr(<span class="hljs-string">"index"</span>);
<span class="hljs-keyword">var</span> rect = $.parseJSON($(item).attr(<span class="hljs-string">"rect"</span>));
<span class="hljs-built_in">this</span>.items.splice(index, <span class="hljs-number">1</span>);
$(item).remove()
<span class="hljs-built_in">this</span>.resetIndex(index);
<span class="hljs-built_in">this</span>.addChangePositionAnimate(index, rect);
&#125;,
<span class="hljs-comment">//改变位置动画</span>
<span class="hljs-attr">addChangePositionAnimate</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">index, rect</span>) </span>&#123;
<span class="hljs-keyword">var</span> items = <span class="hljs-built_in">this</span>.resort();
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = items.length - <span class="hljs-number">1</span>; i >= index; i--) &#123;
<span class="hljs-keyword">var</span> item = items[i];
<span class="hljs-keyword">var</span> newRect = (i == index) ? rect : $.parseJSON($(items[i - <span class="hljs-number">1</span>]).attr(<span class="hljs-string">"rect"</span>));
$(item).attr(<span class="hljs-string">"rect"</span>, <span class="hljs-built_in">JSON</span>.stringify(newRect));
<span class="hljs-built_in">this</span>.animate(item, newRect);
&#125;
<span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
that.resetParentRect();
&#125;, that.duran);
&#125;,
<span class="hljs-comment">//添加动画</span>
<span class="hljs-attr">animate</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item, rect</span>) </span>&#123;
<span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
$(item).animate(&#123;
<span class="hljs-attr">left</span>: rect.x + <span class="hljs-string">'px'</span>,
<span class="hljs-attr">top</span>: rect.y + <span class="hljs-string">'px'</span>
&#125;, that.duran);
&#125;,
<span class="hljs-comment">//重置item索引属性</span>
<span class="hljs-attr">resetIndex</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">index</span>) </span>&#123;
<span class="hljs-keyword">if</span> (index == <span class="hljs-literal">null</span>) &#123;
<span class="hljs-keyword">var</span> items = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">"menu"</span>);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;
<span class="hljs-keyword">var</span> item = items[i];
$(item).attr(<span class="hljs-string">"index"</span>, i)
&#125;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">var</span> items = <span class="hljs-built_in">this</span>.resort();
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = index; i < items.length; i++) &#123;
<span class="hljs-keyword">var</span> item = items[i];
<span class="hljs-keyword">var</span> nowIndex = $(item).attr(<span class="hljs-string">"index"</span>);
$(item).attr(<span class="hljs-string">"index"</span>, nowIndex - <span class="hljs-number">1</span>);
&#125;

&#125;
&#125;,
<span class="hljs-comment">//重置父视图高度</span>
<span class="hljs-attr">resetParentRect</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.items.length == <span class="hljs-number">0</span>) &#123;
$(<span class="hljs-built_in">this</span>.contain).height(<span class="hljs-built_in">this</span>.sep);
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">var</span> width = $(<span class="hljs-built_in">this</span>.contain).width();
<span class="hljs-keyword">var</span> itemHeight = (width - <span class="hljs-built_in">this</span>.sep * (<span class="hljs-built_in">this</span>.column + <span class="hljs-number">1</span>)) / <span class="hljs-built_in">this</span>.column;
<span class="hljs-keyword">var</span> row = <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.items.length / <span class="hljs-built_in">this</span>.column) + ((<span class="hljs-built_in">this</span>.items.length % <span class="hljs-built_in">this</span>.column) ? <span class="hljs-number">1</span> : <span class="hljs-number">0</span>);
<span class="hljs-keyword">var</span> maxY = itemHeight * row + <span class="hljs-built_in">this</span>.sep * (row + <span class="hljs-number">1</span>);
$(<span class="hljs-built_in">this</span>.contain).height(maxY)
&#125;
&#125;,
<span class="hljs-comment">//创建old占位div</span>
<span class="hljs-attr">createOldPlaceholderElement</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">rect, index</span>) </span>&#123;
<span class="hljs-keyword">var</span> tempDiv = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
$(tempDiv).attr(<span class="hljs-string">'class'</span>, <span class="hljs-string">'active'</span>)
$(tempDiv).attr(<span class="hljs-string">'id'</span>, <span class="hljs-string">'old'</span>)
<span class="hljs-keyword">var</span> x = rect.x;
<span class="hljs-keyword">var</span> y = rect.y;
$(tempDiv).css(<span class="hljs-string">"left"</span>, x);
$(tempDiv).css(<span class="hljs-string">"top"</span>, y);
$(tempDiv).width(rect.width);
$(tempDiv).height(rect.height);
$(tempDiv).attr(<span class="hljs-string">"rect"</span>, <span class="hljs-built_in">JSON</span>.stringify(rect))
$(tempDiv).attr(<span class="hljs-string">"index"</span>, index);
$(<span class="hljs-built_in">this</span>.contain).append(tempDiv);
&#125;,
<span class="hljs-comment">//移动区间模块</span>
<span class="hljs-attr">moveInterval</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">oldElement, newElement</span>) </span>&#123;

<span class="hljs-keyword">var</span> oIndex = <span class="hljs-built_in">parseInt</span>($(oldElement).attr(<span class="hljs-string">"index"</span>));
<span class="hljs-keyword">var</span> nIndex = <span class="hljs-built_in">parseInt</span>($(newElement).attr(<span class="hljs-string">"index"</span>));

<span class="hljs-comment">//console.log('oIndex=' + oIndex + ',' + 'nIndex=' + nIndex);</span>
<span class="hljs-keyword">var</span> rect = $.parseJSON($(newElement).attr(<span class="hljs-string">"rect"</span>));
<span class="hljs-keyword">var</span> oldRect = $.parseJSON($(oldElement).attr(<span class="hljs-string">"rect"</span>));
$(oldElement).css(&#123;
<span class="hljs-string">"left"</span>: rect.x,
<span class="hljs-string">"top"</span>: rect.y
&#125;);

<span class="hljs-keyword">var</span> items = <span class="hljs-built_in">this</span>.resort();

<span class="hljs-keyword">if</span> (oIndex < nIndex) &#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = nIndex; i > oIndex; i--) &#123;
<span class="hljs-keyword">var</span> item = items[i];
<span class="hljs-keyword">if</span> (item) &#123;
<span class="hljs-keyword">var</span> tempRect = $.parseJSON($(items[i - <span class="hljs-number">1</span>]).attr(<span class="hljs-string">"rect"</span>))
<span class="hljs-keyword">var</span> newRect = (i == oIndex + <span class="hljs-number">1</span>) ? oldRect : tempRect;
$(item).attr(<span class="hljs-string">"rect"</span>, <span class="hljs-built_in">JSON</span>.stringify(newRect));
<span class="hljs-keyword">var</span> tempIndex = $(items[i - <span class="hljs-number">1</span>]).attr(<span class="hljs-string">"index"</span>);
<span class="hljs-keyword">var</span> index = (i == oIndex + <span class="hljs-number">1</span>) ? oIndex : $(items[i - <span class="hljs-number">1</span>]).attr(<span class="hljs-string">"index"</span>);
$(item).attr(<span class="hljs-string">"index"</span>, index);
<span class="hljs-built_in">this</span>.animate(item, newRect);
&#125;
&#125;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = nIndex; i < oIndex; i++) &#123;
<span class="hljs-keyword">var</span> item = items[i];
<span class="hljs-keyword">if</span> (item) &#123;
<span class="hljs-keyword">var</span> tempRect = $.parseJSON($(items[i + <span class="hljs-number">1</span>]).attr(<span class="hljs-string">"rect"</span>))
<span class="hljs-keyword">var</span> newRect = (i == oIndex - <span class="hljs-number">1</span>) ? oldRect : tempRect;
$(item).attr(<span class="hljs-string">"rect"</span>, <span class="hljs-built_in">JSON</span>.stringify(newRect));
<span class="hljs-keyword">var</span> tempIndex = $(items[i + <span class="hljs-number">1</span>]).attr(<span class="hljs-string">"index"</span>);
<span class="hljs-keyword">var</span> index = (i == oIndex - <span class="hljs-number">1</span>) ? oIndex : $(items[i + <span class="hljs-number">1</span>]).attr(<span class="hljs-string">"index"</span>);
$(item).attr(<span class="hljs-string">"index"</span>, index);
<span class="hljs-built_in">this</span>.animate(item, newRect);
&#125;
&#125;
&#125;
$(oldElement).attr(<span class="hljs-string">"rect"</span>, <span class="hljs-built_in">JSON</span>.stringify(rect))
$(oldElement).attr(<span class="hljs-string">"index"</span>, nIndex);
<span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
$(that.currentOptionElement).attr(<span class="hljs-string">"rect"</span>, <span class="hljs-built_in">JSON</span>.stringify(rect))
$(that.currentOptionElement).attr(<span class="hljs-string">"index"</span>, nIndex);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
that.resetParentRect();
&#125;, that.duran + <span class="hljs-number">10</span>);
&#125;,
<span class="hljs-comment">//重新排序</span>
<span class="hljs-attr">resort</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> itemsOld = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">"menu"</span>);
<span class="hljs-keyword">var</span> dic = &#123;&#125;;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < itemsOld.length; i++) &#123;
<span class="hljs-keyword">var</span> item = itemsOld[i];
dic[$(item).attr(<span class="hljs-string">"index"</span>)] = item;
&#125;
<span class="hljs-keyword">var</span> items = [];

<span class="hljs-built_in">Object</span>.keys(dic).sort().forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key</span>) </span>&#123;
items.push(dic[key]);
&#125;);
<span class="hljs-keyword">return</span> items;
&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>dragTouchEven.js</em></p>
<pre><code class="copyable">$(function() &#123;
var action = false; //定义一个全局变量来判断鼠标动作，默认为false
var mouseTapX = 0;
var mouseTapY = 0;
var timer = null;
var isLongPress = false;
var currentTime = 0;
var longpressTime = 500;
var animateTime = 500;
var currentSelectItem = null;
$(document).on("mousedown", ".menu", function(event) &#123; //鼠标按下事件
var that = this;
currentSelectItem = that;
isLongPress = true;
drag.currentOptionElement = that;
currentTime = Date.parse(new Date());
timer = setTimeout(function() &#123;
if (isLongPress) &#123;
action = true;
if ($(".onclick").length < 1) &#123;
var left = $(that).offset().left - $(".wrap").offset().left; //获取在wrap内的偏移量
var top = $(that).offset().top - $(".wrap").offset().top;
mouseTapX = event.pageX - $(that).offset().left;
mouseTapY = event.pageY - $(that).offset().top;
var rect = $.parseJSON($(that).attr("rect"));
var index = $(that).attr("index");
drag.createOldPlaceholderElement(rect, index);
//$(that).before("<div class='active' id='old'></div>"); //鼠标按下时在原位置创建一个活动的空div
$(that).css(&#123;
"left": left,
"top": top,
&#125;);
&#125;
&#125;
&#125;, longpressTime);

&#125;)
$(document).on("mousemove", ".wrap", function(event) &#123; //wrap上的鼠标移动事件，menu 移动
if (action == true) &#123;
var x = event.pageX - $(".wrap").offset().left; //获取鼠标在wrap的偏移量
var y = event.pageY - $(".wrap").offset().top;
$(currentSelectItem).css(&#123;
"left": x - mouseTapX,
"top": y - mouseTapY
&#125;); //补充内边距
judgeInsertLeftOrRight(x, y);
&#125;
&#125;)

$(document).on("mouseup", function() &#123; //鼠标弹起时将移动的menu 放入新的接受div里，并移除原div位置上的空div

var nowTime = Date.parse(new Date());
isLongPress = (nowTime - currentTime >= longpressTime);
if (!isLongPress) &#123;
//单点
drag.deleteItem(currentSelectItem);
&#125; else &#123;
//长按
var oldElement = $("#old");
if ($(oldElement).attr("rect")) &#123;
var rect = $.parseJSON($(oldElement).attr("rect"));
var oIndex = $(oldElement).attr("index");
$(currentSelectItem).attr("rect", JSON.stringify(rect))
$(currentSelectItem).attr("index", oIndex);
$(currentSelectItem).animate(&#123;
left: rect.x + 'px',
top: rect.y + 'px',
&#125;, 200);
$("#old").remove();
&#125;
&#125;
action = false;
&#125;)
&#125;)

function deleteItem(currentSelectItem) &#123;
if (currentSelectItem) &#123;
drag.deleteItem(currentSelectItem);
&#125;
&#125;

//判断当前的鼠标点的位置在其他标签的位置
function judgeInsertLeftOrRight(mx, my) &#123;
var items = document.getElementsByClassName("menu");
for (var i = 0; i < items.length; i++) &#123;
var item = items[i];
var rect = $.parseJSON($(item).attr("rect"));
if (mx > rect.x && mx < rect.x + rect.width && my > rect.y && my < rect.y + rect.height) &#123;
insertPlaceholderElement(item);
return;
&#125;
&#125;
&#125;

//标签前后插入新的占位标签
function insertPlaceholderElement(item) &#123;
drag.moveInterval($("#old"), item);
&#125;


        


<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            