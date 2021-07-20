
---
title: '第 16 题：如何通过 CSS 绘制一个三角形？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://noxussj.top:3000/16/1.png'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 00:07:02 GMT
thumbnail: 'https://noxussj.top:3000/16/1.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>虽然网上有很多关于绘制三角形的代码，但是我相信还是有一部分人是不知道如何实现的。我下面举个栗子。</p>
<p>这种情况应该都能理解，不就是设置一个边框嘛</p>
<pre><code class="copyable">width: 100px;
height: 100px;
border: 20px solid;
border-color: #000;
box-sizing: border-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://noxussj.top:3000/16/1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二步，把边框颜色改一下，应该也能看懂</p>
<pre><code class="copyable">width: 100px;
height: 100px;
border: 20px solid;
border-color: green blue red orange;
box-sizing: border-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://noxussj.top:3000/16/2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三步，把边框放大，使得里面的白色区域减少到没有为止</p>
<pre><code class="copyable">width: 100px;
height: 100px;
border: 50px solid;
border-color: green blue red orange;
box-sizing: border-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://noxussj.top:3000/16/3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第四步，把其他边框颜色改为透明色试试</p>
<pre><code class="copyable">width: 100px;
height: 100px;
border: 50px solid;
border-color: green transparent transparent transparent;
box-sizing: border-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://noxussj.top:3000/16/4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>就是这么简单，通过 border-color 控制三角形方向，通过 width、height、border 宽度来调整三角形大小和形状</p>
<h1 data-id="heading-0"></h1>
<h2 data-id="heading-1"><strong>附加</strong></h2>
<ul>
<li>
<p>此文章通过自媒体多平台发布，发布后不再进行维护，如对内容有任何异议可以到下方的 GitHub 中进行讨论</p>
</li>
<li>
<p>【持续维护/更新 500+前端面试题/笔记】<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnoxussj%2FInterview-Questions%2Fissues" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/noxussj/Interview-Questions/issues" ref="nofollow noopener noreferrer">github.com/noxussj/Int…</a></p>
</li>
<li>
<p>【利用 THREE.JS 实现 3D 城市建模（珠海市）】<a href="https://link.juejin.cn/?target=https%3A%2F%2F3d.noxussj.top%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://3d.noxussj.top/" ref="nofollow noopener noreferrer">3d.noxussj.top/</a></p>
</li>
</ul></div>  
</div>
            