
---
title: 'Echarts标识出曲线中坐标重合的点（找出json中重复的值）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b517de4c84480989267923103baf99~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 18:03:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b517de4c84480989267923103baf99~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">问题描述：单独标出每个图中坐标重合的点，便于H5端查看</h3>
<ul>
<li>绘制图表工具：Echarts</li>
<li>Echarts官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fecharts.apache.org%2Fzh%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://echarts.apache.org/zh/index.html" ref="nofollow noopener noreferrer">echarts.apache.org/zh/index.ht…</a></li>
<li>最终效果预览：</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b517de4c84480989267923103baf99~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>解决思路：将多个数组合并到同一数组中，再遍历出x与y完全相等的坐标点，添加到数组中，最后将所有坐标点一同添加到series中</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ec00de98d4846078964c6663e386984~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
=>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb525fa48ff24ad6b5abb5194c425ed1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>关键代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">//找出JSON中重复项关键代码</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRepeatData</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (data) &#123;
        <span class="hljs-keyword">let</span> result = [];
        <span class="hljs-keyword">let</span> obj = &#123;&#125;;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < data.length; i++) &#123;
            <span class="hljs-keyword">const</span> el = data[i];
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> y = i + <span class="hljs-number">1</span>; y < data.length; y++) &#123;
                <span class="hljs-keyword">const</span> val = data[y];
                    <span class="hljs-keyword">if</span> (el.x == val.x && el.y == val.y) &#123;<span class="hljs-comment">//找出x与y值均重复的对象</span>
                    <span class="hljs-keyword">if</span> (!obj[el.id]) &#123;
                        result.push(el)
                        obj[el.id] = <span class="hljs-literal">true</span>
                    &#125;
                    <span class="hljs-keyword">if</span> (!obj[val.id]) &#123;
                        result.push(val)
                        obj[val.id] = <span class="hljs-literal">true</span>
                    &#125;
                &#125;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;

<span class="hljs-comment">//处理接口返回的JSON数组数据lineNameList</span>
  lineNameList.forEach(<span class="hljs-function">(<span class="hljs-params">e, index</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> dataList = [];
        <span class="hljs-keyword">let</span> crossArr = [];
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> curveChartData) &#123;
            <span class="hljs-keyword">if</span> (i.includes(e)) &#123;
                <span class="hljs-comment">//坐标点汇总</span>
                dataList.push(curveChartData[i])
                <span class="hljs-comment">//合并数组</span>
                crossArr.push.apply(crossArr, curveChartData[i]);
            &#125;
        &#125;
        <span class="hljs-comment">//获取坐标重合点</span>
        <span class="hljs-keyword">let</span> crosspoints = getRepeatData(crossArr);
        <span class="hljs-comment">//将重合点坐标添加到dataList中</span>
        dataList.push(crosspoints);
        <span class="hljs-built_in">console</span>.log(dataList);
        <span class="hljs-built_in">console</span>.log(crossArr);
         <span class="hljs-keyword">let</span> option = &#123;
            <span class="hljs-comment">//标题</span>
            <span class="hljs-attr">title</span>: &#123;
                <span class="hljs-attr">text</span>: e,
                <span class="hljs-attr">left</span>: <span class="hljs-number">5</span>,
                <span class="hljs-attr">top</span>: <span class="hljs-number">5</span>,
            &#125;,
            <span class="hljs-attr">tooltip</span>: &#123;
                <span class="hljs-attr">trigger</span>: <span class="hljs-string">'item'</span>,
                <span class="hljs-attr">axisPointer</span>: &#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-string">'cross'</span>,
                    <span class="hljs-attr">label</span>: &#123;
                        <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'#6a7985'</span>
                    &#125;
                &#125;,
            &#125;,
            <span class="hljs-attr">grid</span>: &#123;
                <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">width</span>: <span class="hljs-string">'85%'</span>,
                <span class="hljs-attr">height</span>: <span class="hljs-string">'70%'</span>,
            &#125;,
            <span class="hljs-attr">toolbox</span>: &#123;
                <span class="hljs-attr">feature</span>: &#123;
                    <span class="hljs-attr">saveAsImage</span>: &#123;
                        <span class="hljs-attr">title</span>: <span class="hljs-string">"保存"</span>
                    &#125;
                &#125;
            &#125;,
            <span class="hljs-attr">xAxis</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
                <span class="hljs-attr">splitNumber</span>: <span class="hljs-number">8</span>,
                <span class="hljs-attr">axisLabel</span>: &#123; <span class="hljs-attr">rotate</span>: <span class="hljs-number">30</span> &#125;,
                <span class="hljs-attr">scale</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">splitLine</span>: &#123;
                    <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                    <span class="hljs-attr">lineStyle</span>: &#123;
                        <span class="hljs-attr">color</span>: <span class="hljs-string">'#333333'</span>
                    &#125;
                &#125;
            &#125;,
            <span class="hljs-attr">yAxis</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
                <span class="hljs-attr">splitNumber</span>: <span class="hljs-number">8</span>,
                <span class="hljs-attr">scale</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">splitLine</span>: &#123;
                    <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                    <span class="hljs-attr">lineStyle</span>: &#123;
                        <span class="hljs-attr">color</span>: <span class="hljs-string">'#333333'</span>
                    &#125;
                &#125;
            &#125;,
            <span class="hljs-attr">series</span>: [
            ],
            <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">"#EAEBF0"</span>
        &#125;;
        <span class="hljs-keyword">let</span> len = dataList.length;
        dataList.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
            option.series.push(&#123;
            <span class="hljs-comment">//重合的坐标点放在最后，只显示点type设置为effectScatter，不显示线</span>
                <span class="hljs-attr">type</span>: index == len - <span class="hljs-number">1</span> ?<span class="hljs-string">'effectScatter'</span>:<span class="hljs-string">'line'</span>,
                <span class="hljs-attr">smooth</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">name</span>: PageBomObj.scheme === <span class="hljs-string">"常规泵"</span> ? item.lineChildName : e,
            &#125;)
            option.series[index].data = item.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123; <span class="hljs-keyword">return</span> [item.x, item.y] &#125;);
        &#125;)
       
        <span class="hljs-comment">//创建dom容器</span>
        $(<span class="hljs-string">".curve-chart"</span>).append(<span class="hljs-string">`<div id=curve-chart-main-<span class="hljs-subst">$&#123;index&#125;</span> ></div>`</span>);
        <span class="hljs-comment">//获取dom容器</span>
        <span class="hljs-keyword">let</span> myChart = echarts.init(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"curve-chart-main-"</span> + index));
        <span class="hljs-comment">// 使用指定的配置项和数据显示图表</span>
        myChart.setOption(option);
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>若要绘制线相交的点 网上参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_35436516%2Farticle%2Fdetails%2F103606467" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_35436516/article/details/103606467" ref="nofollow noopener noreferrer">blog.csdn.net/qq_35436516…</a></li>
</ul></div>  
</div>
            