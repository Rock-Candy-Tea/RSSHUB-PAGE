
---
title: 'Echarts实例 - 树形图表的实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd0b181e60c34801b7ff44d7169d7989~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 05:20:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd0b181e60c34801b7ff44d7169d7989~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>树图主要用来可视化树形数据结构，是一种特殊的层次类型。</p>
<p>实现方法，将series->type设置为tree。</p>
<p>Echarts的树形图表，可以是正交的，也可以是径向的。</p>
<p>正交树：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd0b181e60c34801b7ff44d7169d7989~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>径向树：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9c49600f959489da2c1362a20014d9d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现方法，修改：series->layout设置，orthogonal为正向，radial为径向。</p>
<p>可以自定义，如从右向左：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b58fb70334f041a9b893ebd115333156~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现方法，修改：series->orient设置，支持LR、RL、TB、BT，其中RL，就是从右向左。</p>
<p>可以自定义图标：支持'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'</p>
<p>实现方法，修改：series->symbol设置</p>
<p>图标是方形的树形图表：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d5f623e093244a38845aa241609584a~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以自定义，直线还是曲线：</p>
<p>实现方法，修改：series->edgeShape设置，支持curve 和 polyline</p>
<p>直线图表：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/704bbade5f9a4cedafd32a745db62b9b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>initialTreeDepth：</p>
<p>默认展开的深度，默认为2，多于2层的的节点可以点击父节点来展示和隐藏。如果设置为 <code>-1</code> 或者 <code>null</code> 或者 <code>undefined</code>，所有节点都将展开。</p>
<p>itemStyle：
修改树形图表项的样式。
可以修改颜色、大小等</p>
<p>label：
图表项中文字的处理。
可以通过formatter来给图表的文字增加丰富的效果。</p>
<p>lineStyle：
图表中线的处理。</p>
<p>修改lineStyle样式的效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0ce53625d624e4d950604a50f3ef8fe~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>emphasis： 聚焦,设置了聚焦后，鼠标放到项，其他无关项就会暂时隐藏。</p>
<p>'none' 不淡出其它图形，默认使用该配置。
'self' 只聚焦（不淡出）当前高亮的数据的图形。</p>
<p>'series' 聚焦当前高亮的数据所在的系列的所有图形。</p>
<p>'ancestor' 聚焦所有祖先节点
'descendant' 聚焦所有子孙节点</p>
<pre><code class="copyable">
emphasis: &#123;
    focus: 'ancestor',
    blurScope: 'coordinateSystem'
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>树形图表的数据结构：</p>
<p>name: 图表项默认项显示的名称
children： 这个项的子节点</p>
<p>当然，你在数据里可以定义任意属性，如value、num等，可以配合label中的formatter来实现更加丰富的显示效果。</p>
<p>最后是完整的代码：</p>
<p>index.html</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Echarts实例 - 图例<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../echarts.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 500px;height:500px;"</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.js</p>
<pre><code class="copyable">var chart = echarts.init(document.getElementById("container"));

var data = &#123;
    name: 'Throwable',
    children: [&#123;
        name: 'Error',
        children: [&#123;
            name: 'VirtualMachineError',
            children: [&#123;
                name: 'StackOverflowError'
            &#125;, &#123;
                name: 'OutOfMemoryError'
            &#125;]
        &#125;, &#123;
            name: 'AWTError'
        &#125;]
    &#125;, &#123;
        name: 'Exception'
    &#125;]
&#125;


var data2 = &#123;
    name: '龙珠人物',
    children: [&#123;
        name: '孙悟空'
    &#125;, &#123;
        name: '布尔玛'
    &#125;, &#123;
        name: '猪悟能'
    &#125;, &#123;
        name: '雅木茶'
    &#125;, &#123;
        name: '龟仙人'
    &#125;, &#123;
        name: '小林'
    &#125;, &#123;
        name: '短笛'
    &#125;, &#123;
        name: '鹤仙人'
    &#125;, &#123;
        name: '天津饭'
    &#125;, &#123;
        name: '饺子'
    &#125;]
&#125;

chart.setOption(&#123;
    title: &#123;
        text: 'Java异常结构图'
    &#125;,
    series: [&#123;
        layout: 'orthogonal',
        data: [data],
        right: '60%',
        type: 'tree',
        edgeShape: 'polyline', // curve 和 polyline
        symbol: 'rect', // 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none',
        initialTreeDepth: 2,
        itemStyle: &#123;
            color: 'cyan'
        &#125;,
        lineStyle: &#123;
            color: 'red'
        &#125;,
        /**
         * 
         * 
         * 'none' 不淡出其它图形，默认使用该配置。
'self' 只聚焦（不淡出）当前高亮的数据的图形。

'series' 聚焦当前高亮的数据所在的系列的所有图形。

'ancestor' 聚焦所有祖先节点
'descendant' 聚焦所有子孙节点
         */
        emphasis: &#123;
            focus: 'ancestor',
            blurScope: 'coordinateSystem'
        &#125;,
    &#125;, &#123;
        layout: 'radial',
        left: '60%',
        data: [data2],
        type: 'tree',
        symbol: 'rect',
        symbolSize: 15
    &#125;]
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            