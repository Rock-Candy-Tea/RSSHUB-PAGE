
---
title: '第 19 题：让一个 div 水平垂直居中有几种方式？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://noxussj.top:3000/19/1.png'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 01:52:14 GMT
thumbnail: 'https://noxussj.top:3000/19/1.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://noxussj.top:3000/19/1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现上方效果，下面列举几个常用的方法，个人比较推荐用 flex 布局实现</p>
<h2 data-id="heading-0">方式 1（利用 margin 和绝对定位）</h2>
<p>html</p>
<pre><code class="copyable"><div class="container">
    <div class="box"></div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css</p>
<pre><code class="copyable">.container &#123;
    position: relative;
    width: 150px;
    height: 150px;
    background-color: #000;

    .box &#123;
        margin: auto;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        width: 50px;
        height: 50px;
        background-color: #fff;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">方式 2（利用 flex 布局）</h2>
<p>html</p>
<pre><code class="copyable"><div class="container">
    <div class="box"></div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css</p>
<pre><code class="copyable">.container &#123;
    position: relative;
    width: 150px;
    height: 150px;
    background-color: #000;
    display: flex;
    justify-content: center;
    align-items: center;

    .box &#123;
        width: 50px;
        height: 50px;
        background-color: #fff;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2"></h1>
<h2 data-id="heading-3"><strong>文章的内容/灵感都从下方内容中借鉴</strong></h2>
<ul>
<li>
<p>【持续维护/更新 500+前端面试题/笔记】<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnoxussj%2FInterview-Questions%2Fissues" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/noxussj/Interview-Questions/issues" ref="nofollow noopener noreferrer">github.com/noxussj/Int…</a></p>
</li>
<li>
<p>【大数据可视化图表插件】<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fns-echarts" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/ns-echarts" ref="nofollow noopener noreferrer">www.npmjs.com/package/ns-…</a></p>
</li>
<li>
<p>【利用 THREE.JS 实现 3D 城市建模（珠海市）】<a href="https://link.juejin.cn/?target=https%3A%2F%2F3d.noxussj.top%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://3d.noxussj.top/" ref="nofollow noopener noreferrer">3d.noxussj.top/</a></p>
</li>
</ul></div>  
</div>
            