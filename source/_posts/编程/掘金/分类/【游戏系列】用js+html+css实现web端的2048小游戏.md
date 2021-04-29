
---
title: '【游戏系列】用js+html+css实现web端的2048小游戏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65f7a42508aa4d96a6ea1962689febe1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 00:00:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65f7a42508aa4d96a6ea1962689febe1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前几年2048小游戏风靡一时，很多人下载这个游戏玩，但是作为一个合格且没多少头发的程序员，不应该想一想，这个游戏否是可以自己实现呢？</p>
</blockquote>
<h2 data-id="heading-0">1.html代码块</h2>
<blockquote>
<p>overflow: hidden;此样式解决微信内置浏览器下拉问题</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"overflow: hidden;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c00"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c01"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c02"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c03"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c10"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c11"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c12"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c13"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c20"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c21"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c22"</span>></span> <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c23"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c30"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c31"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c32"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c33"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"keymap"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"score"</span>></span>分数：<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"score"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"game.reset()"</span>></span>重新开始<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2.css样式</h2>
<blockquote>
<p>使用flex弹性布局</p>
</blockquote>
<blockquote>
<p>@media all and (max-device-width: 400px)解决响应式布局</p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.main</span>&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: space-between;
    <span class="hljs-attribute">flex-wrap</span>: wrap;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">background</span>:<span class="hljs-number">#bbada0</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">6px</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">50%</span> - <span class="hljs-number">200px</span>);
    <span class="hljs-attribute">left</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">50%</span> - <span class="hljs-number">200px</span>);
&#125;
<span class="hljs-selector-class">.main</span> <span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">90px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">90px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">6px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#ccc0b3</span>;
    <span class="hljs-attribute">text-align</span>: center;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">90px</span>;
&#125;
<span class="hljs-keyword">@media</span> all <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-device-width</span>: <span class="hljs-number">400px</span>)&#123;
    <span class="hljs-selector-class">.main</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">340px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">340px</span>;
        <span class="hljs-attribute">border-right</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#e0e0e0</span>;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">justify-content</span>: space-between;
        <span class="hljs-attribute">flex-wrap</span>: wrap;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
        <span class="hljs-attribute">background</span>:<span class="hljs-number">#bbada0</span>;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">6px</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">50%</span> - <span class="hljs-number">170px</span>);
        <span class="hljs-attribute">left</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">50%</span> - <span class="hljs-number">180px</span>);
    &#125;

    <span class="hljs-selector-class">.main</span> <span class="hljs-selector-tag">div</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">80px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
    &#125;
&#125;
<span class="hljs-selector-class">.keymap</span>&#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="hljs-selector-class">.score</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">40px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">20px</span>;
&#125;
<span class="hljs-selector-class">.btn-1</span>,<span class="hljs-selector-class">.btn-2</span>,<span class="hljs-selector-class">.btn-3</span>,<span class="hljs-selector-class">.btn-4</span>&#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">flex-flow</span>: row;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.btn-4</span>&#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">40px</span>;
&#125;

<span class="hljs-selector-tag">button</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">80px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">cursor</span>: pointer;
    <span class="hljs-attribute">border-width</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">outline</span>: none;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f59563</span>;
    <span class="hljs-attribute">font-family</span>: KaiTi;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;
<span class="hljs-selector-tag">button</span><span class="hljs-selector-pseudo">:hover</span>&#123;<span class="hljs-comment">/*鼠标移动时的颜色变化*/</span>
    <span class="hljs-attribute">background-color</span>: antiquewhite;
&#125;

<span class="hljs-selector-class">.n2</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#eee3da</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n4</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#ede0c8</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n8</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#f2b179</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n16</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#f59563</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n32</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#f67c5f</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n64</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#f65e3b</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n128</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#edcf72</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n256</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#edcc61</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n512</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#9c0</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n1024</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#33b5e5</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n2048</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#09c</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n4096</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#a6c</span> <span class="hljs-meta">!important</span>&#125;
<span class="hljs-selector-class">.n8192</span>&#123;<span class="hljs-attribute">background-color</span>:<span class="hljs-number">#93c</span> <span class="hljs-meta">!important</span> &#125;
<span class="hljs-selector-class">.n2</span>,<span class="hljs-selector-class">.n4</span>&#123;<span class="hljs-attribute">color</span>:<span class="hljs-number">#776e65</span> <span class="hljs-meta">!important</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.js逻辑处理</h2>
<h3 data-id="heading-3">3.1声明一个game对象</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> game = &#123;
        <span class="hljs-attr">score</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">status</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">data</span>: [
            [],
            [],
            [],
            []
        ],
        <span class="hljs-attr">start</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status == <span class="hljs-number">1</span>)&#123;
                alert(<span class="hljs-string">'游戏已开始'</span>);
                <span class="hljs-keyword">return</span>
            &#125;
            <span class="hljs-built_in">this</span>.status = <span class="hljs-number">1</span>;
            <span class="hljs-keyword">let</span> data = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'data'</span>);
            <span class="hljs-keyword">if</span>(data)&#123;
                <span class="hljs-keyword">let</span> arr = data.split(<span class="hljs-string">','</span>);
                <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<arr.length;i++)&#123;
                    <span class="hljs-keyword">if</span>(i<<span class="hljs-number">4</span>)&#123;
                        <span class="hljs-built_in">this</span>.data[<span class="hljs-number">0</span>][i]=<span class="hljs-built_in">parseInt</span>(arr[i]);
                    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(i<<span class="hljs-number">8</span>)&#123;
                        <span class="hljs-built_in">this</span>.data[<span class="hljs-number">1</span>][i-<span class="hljs-number">4</span>]=<span class="hljs-built_in">parseInt</span>(arr[i]);
                    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(i<<span class="hljs-number">12</span>)&#123;
                        <span class="hljs-built_in">this</span>.data[<span class="hljs-number">2</span>][i-<span class="hljs-number">8</span>]=<span class="hljs-built_in">parseInt</span>(arr[i]);
                    &#125;<span class="hljs-keyword">else</span>&#123;
                        <span class="hljs-built_in">this</span>.data[<span class="hljs-number">3</span>][i-<span class="hljs-number">12</span>]=<span class="hljs-built_in">parseInt</span>(arr[i]);
                    &#125;
                &#125;
            &#125;<span class="hljs-keyword">else</span>&#123;
                <span class="hljs-built_in">this</span>.data = [
                    [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>],
                    [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>],
                    [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>],
                    [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>]
                ];
                <span class="hljs-built_in">this</span>.randomData();
            &#125;
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'score'</span>))&#123;
                <span class="hljs-built_in">this</span>.score = <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'score'</span>))
            &#125;
            <span class="hljs-built_in">this</span>.renderView();
        &#125;,
        <span class="hljs-attr">randomData</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">for</span>(;;)&#123;
                <span class="hljs-keyword">let</span> a = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">4</span>);
                <span class="hljs-keyword">let</span> b = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">4</span>);
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b] == <span class="hljs-number">0</span>)&#123;
                    <span class="hljs-keyword">var</span> num = <span class="hljs-built_in">Math</span>.random()><span class="hljs-number">0.3</span> ? <span class="hljs-number">2</span>:<span class="hljs-number">4</span>;
                    <span class="hljs-built_in">this</span>.data[a][b]=num;
                    <span class="hljs-keyword">break</span>;
                &#125;
            &#125;
        &#125;,
        <span class="hljs-comment">//更新视图</span>
        <span class="hljs-attr">renderView</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.data.length; i++)&#123;
                <span class="hljs-keyword">let</span> row = <span class="hljs-built_in">this</span>.data[i];
                <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j<row.length; j++)&#123;
                    <span class="hljs-keyword">let</span> cell = row[j];
                    <span class="hljs-keyword">let</span> dom = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'c'</span>+i+j);
                    <span class="hljs-keyword">if</span>(cell != <span class="hljs-number">0</span>)&#123;
                        dom.innerText=cell;
                        dom.className=<span class="hljs-string">'n'</span>+cell;
                    &#125;<span class="hljs-keyword">else</span>&#123;
                        dom.innerText=<span class="hljs-string">''</span>;
                        dom.className=<span class="hljs-string">''</span>;
                    &#125;
                &#125;
            &#125;
            <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'score'</span>,<span class="hljs-built_in">this</span>.score);
            <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'score'</span>).innerText=<span class="hljs-built_in">this</span>.score;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">reset</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">localStorage</span>.clear();
            <span class="hljs-built_in">this</span>.data = [
                [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>],
                [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>],
                [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>],
                [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>]
            ]
            <span class="hljs-built_in">this</span>.score = <span class="hljs-number">0</span>;
            <span class="hljs-built_in">this</span>.randomData();
            <span class="hljs-built_in">this</span>.renderView();
        &#125;,
        <span class="hljs-attr">checkGameOver</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.data.length; i++)&#123;
                <span class="hljs-keyword">let</span> row = <span class="hljs-built_in">this</span>.data[i];
                <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j<row.length; j++)&#123;
                    <span class="hljs-keyword">let</span> cell = row[j];
                    <span class="hljs-keyword">if</span>(cell == <span class="hljs-number">0</span>)&#123;
                        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
                    &#125;
                    <span class="hljs-keyword">if</span>(i < <span class="hljs-built_in">this</span>.data.length-<span class="hljs-number">1</span> && <span class="hljs-built_in">this</span>.data[i][j]== <span class="hljs-built_in">this</span>.data[i+<span class="hljs-number">1</span>][j])&#123;
                        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
                    &#125;
                    <span class="hljs-keyword">if</span>(j < <span class="hljs-built_in">this</span>.data.length-<span class="hljs-number">1</span> && <span class="hljs-built_in">this</span>.data[i][j]== <span class="hljs-built_in">this</span>.data[i][j+<span class="hljs-number">1</span>])&#123;
                        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
                    &#125;
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;,
        <span class="hljs-attr">moveLeft</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">let</span> before = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">this</span>.data);
            <span class="hljs-comment">//遍历行</span>
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>; a < <span class="hljs-built_in">this</span>.data.length; a++)&#123;
                <span class="hljs-built_in">this</span>.moveLeftInRow(a);
            &#125;
            <span class="hljs-keyword">let</span> after = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">this</span>.data);
            <span class="hljs-keyword">if</span>(before != after)&#123;
                <span class="hljs-built_in">this</span>.randomData();
                <span class="hljs-built_in">this</span>.renderView();
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.checkGameOver())&#123;
                    alert(<span class="hljs-string">'游戏结束'</span>)
                &#125;
            &#125;
            <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'data'</span>,<span class="hljs-built_in">this</span>.data.join(<span class="hljs-string">','</span>))
        &#125;,
        <span class="hljs-attr">moveLeftInRow</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> b = <span class="hljs-number">0</span>; b < <span class="hljs-built_in">this</span>.data.length - <span class="hljs-number">1</span>; b++)&#123;
                <span class="hljs-keyword">let</span> nextb = <span class="hljs-built_in">this</span>.getNextInRow(a,b);
                <span class="hljs-keyword">if</span>(nextb != -<span class="hljs-number">1</span>)&#123;
                    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b] == <span class="hljs-number">0</span>)&#123;
                        <span class="hljs-built_in">this</span>.data[a][b] = <span class="hljs-built_in">this</span>.data[a][nextb];
                        <span class="hljs-built_in">this</span>.data[a][nextb] = <span class="hljs-number">0</span>;
                        b--;   
                    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b] == <span class="hljs-built_in">this</span>.data[a][nextb])&#123;
                        <span class="hljs-built_in">this</span>.data[a][b] *= <span class="hljs-number">2</span>;
                        <span class="hljs-built_in">this</span>.score += <span class="hljs-built_in">this</span>.data[a][b]
                        <span class="hljs-built_in">this</span>.data[a][nextb] = <span class="hljs-number">0</span>
                    &#125;
                &#125;<span class="hljs-keyword">else</span>&#123;
                    <span class="hljs-keyword">break</span>;
                &#125;
            &#125;
        &#125;,
        <span class="hljs-attr">getNextInRow</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a,b</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = b+<span class="hljs-number">1</span>; i<<span class="hljs-built_in">this</span>.data.length; i++)&#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][i] != <span class="hljs-number">0</span>)&#123;
                    <span class="hljs-keyword">return</span> i;
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
        &#125;,
        <span class="hljs-attr">moveRight</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">let</span> before = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">this</span>.data);
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>; a < <span class="hljs-built_in">this</span>.data.length; a++)&#123;
                <span class="hljs-built_in">this</span>.moveRightInRow(a);
            &#125;
            <span class="hljs-keyword">let</span> after = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">this</span>.data);
            <span class="hljs-keyword">if</span>(before != after)&#123;
                <span class="hljs-built_in">this</span>.randomData();
                <span class="hljs-built_in">this</span>.renderView();
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.checkGameOver())&#123;
                    alert(<span class="hljs-string">'游戏结束'</span>)
                &#125;
            &#125;
            <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'data'</span>,<span class="hljs-built_in">this</span>.data.join(<span class="hljs-string">','</span>))
        &#125;,
        <span class="hljs-attr">moveRightInRow</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> b=<span class="hljs-built_in">this</span>.data.length-<span class="hljs-number">1</span>; b > <span class="hljs-number">0</span>; b--)&#123;
                <span class="hljs-keyword">let</span> nextb = <span class="hljs-built_in">this</span>.moveNextRight(a,b);
                <span class="hljs-keyword">if</span>(nextb != -<span class="hljs-number">1</span>)&#123;
                    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b] == <span class="hljs-number">0</span>)&#123;
                        <span class="hljs-built_in">this</span>.data[a][b] = <span class="hljs-built_in">this</span>.data[a][nextb];
                        <span class="hljs-built_in">this</span>.data[a][nextb] = <span class="hljs-number">0</span>;
                        b++;    
                    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b] == <span class="hljs-built_in">this</span>.data[a][nextb])&#123;
                        <span class="hljs-built_in">this</span>.data[a][b] *= <span class="hljs-number">2</span>;
                        <span class="hljs-built_in">this</span>.score += <span class="hljs-built_in">this</span>.data[a][b]
                        <span class="hljs-built_in">this</span>.data[a][nextb] = <span class="hljs-number">0</span>
                    &#125;
                &#125;<span class="hljs-keyword">else</span>&#123;
                    <span class="hljs-keyword">break</span>;
                &#125;
            &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">moveNextRight</span>(<span class="hljs-params">a,b</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = b-<span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--)&#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][i] != <span class="hljs-number">0</span>)&#123;
                    <span class="hljs-keyword">return</span> i;
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
        &#125;,
        <span class="hljs-attr">moveUp</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">let</span> before = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">this</span>.data);
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> b=<span class="hljs-number">0</span>; b < <span class="hljs-built_in">this</span>.data.length; b++)&#123;
                <span class="hljs-built_in">this</span>.moveUpInRow(b);
            &#125;
            <span class="hljs-keyword">let</span> after = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">this</span>.data);
            <span class="hljs-keyword">if</span>(before != after)&#123;
                <span class="hljs-built_in">this</span>.randomData();
                <span class="hljs-built_in">this</span>.renderView();
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.checkGameOver())&#123;
                    alert(<span class="hljs-string">'游戏结束'</span>)
                &#125;
            &#125;
            <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'data'</span>,<span class="hljs-built_in">this</span>.data.join(<span class="hljs-string">','</span>))
        &#125;,
        <span class="hljs-function"><span class="hljs-title">moveUpInRow</span>(<span class="hljs-params">b</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> a = <span class="hljs-number">0</span>; a < <span class="hljs-number">3</span>; a++)&#123;
                <span class="hljs-keyword">let</span> nexta = <span class="hljs-built_in">this</span>.moveNextUp(a,b);
                <span class="hljs-keyword">if</span>(nexta != -<span class="hljs-number">1</span>)&#123;
                    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b] == <span class="hljs-number">0</span>)&#123;
                        <span class="hljs-built_in">this</span>.data[a][b] = <span class="hljs-built_in">this</span>.data[nexta][b];
                        <span class="hljs-built_in">this</span>.data[nexta][b] = <span class="hljs-number">0</span>;
                        a--;    
                    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b] == <span class="hljs-built_in">this</span>.data[nexta][b])&#123;
                        <span class="hljs-built_in">this</span>.data[a][b] *= <span class="hljs-number">2</span>;
                        <span class="hljs-built_in">this</span>.score += <span class="hljs-built_in">this</span>.data[a][b]
                        <span class="hljs-built_in">this</span>.data[nexta][b] = <span class="hljs-number">0</span>
                    &#125;
                &#125;<span class="hljs-keyword">else</span>&#123;
                    <span class="hljs-keyword">break</span>;
                &#125;
            &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">moveNextUp</span>(<span class="hljs-params">a,b</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = a+<span class="hljs-number">1</span>; i<<span class="hljs-number">4</span>; i++)&#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[i][b] != <span class="hljs-number">0</span>)&#123;
                    <span class="hljs-keyword">return</span> i;
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
        &#125;,
        <span class="hljs-attr">moveDown</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">let</span> before = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">this</span>.data);
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> b=<span class="hljs-number">0</span>; b< <span class="hljs-built_in">this</span>.data.length; b++)&#123;
                <span class="hljs-built_in">this</span>.moveDownInRow(b);
            &#125;
            <span class="hljs-keyword">let</span> after = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">this</span>.data);
            <span class="hljs-keyword">if</span>(before != after)&#123;
                <span class="hljs-built_in">this</span>.randomData();
                <span class="hljs-built_in">this</span>.renderView();
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.checkGameOver())&#123;
                    alert(<span class="hljs-string">'游戏结束'</span>)
                &#125;
            &#125;
            <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'data'</span>,<span class="hljs-built_in">this</span>.data.join(<span class="hljs-string">','</span>))
        &#125;,
        <span class="hljs-attr">moveDownInRow</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">b</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> a=<span class="hljs-number">3</span>; a><span class="hljs-number">0</span>; a--)&#123;
                <span class="hljs-keyword">var</span> nexta = <span class="hljs-built_in">this</span>.moveNextDown(a,b)
                <span class="hljs-keyword">if</span>(nexta != -<span class="hljs-number">1</span>)&#123;
                    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b]==<span class="hljs-number">0</span>)&#123;
                        <span class="hljs-built_in">this</span>.data[a][b] = <span class="hljs-built_in">this</span>.data[nexta][b];
                        <span class="hljs-built_in">this</span>.data[nexta][b] = <span class="hljs-number">0</span>;
                        a++;  
                    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[a][b] == <span class="hljs-built_in">this</span>.data[nexta][b])&#123;
                        <span class="hljs-built_in">this</span>.data[a][b] *= <span class="hljs-number">2</span>;
                        <span class="hljs-built_in">this</span>.score += <span class="hljs-built_in">this</span>.data[a][b]
                        <span class="hljs-built_in">this</span>.data[nexta][b] = <span class="hljs-number">0</span>;
                    &#125;
                &#125;<span class="hljs-keyword">else</span>&#123;
                    <span class="hljs-keyword">break</span>;
                &#125;
            &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">moveNextDown</span>(<span class="hljs-params">a,b</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = a-<span class="hljs-number">1</span>;i >= <span class="hljs-number">0</span>;i--)&#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data[i][b] != <span class="hljs-number">0</span>)&#123;
                    <span class="hljs-keyword">return</span> i;
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.2监听键盘上下左右按键</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'keyup'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(event.keyCode==<span class="hljs-number">37</span>)<span class="hljs-comment">//左</span>
        game.moveLeft();
    <span class="hljs-keyword">if</span>(event.keyCode==<span class="hljs-number">39</span>)<span class="hljs-comment">//右</span>
        game.moveRight();
    <span class="hljs-keyword">if</span>(event.keyCode==<span class="hljs-number">38</span>)<span class="hljs-comment">//上</span>
        game.moveUp();
    <span class="hljs-keyword">if</span>(event.keyCode==<span class="hljs-number">40</span>)<span class="hljs-comment">//下</span>
        game.moveDown();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3.3封装移动端滑动事件</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> eventUtil = &#123;
        <span class="hljs-attr">addHandler</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">element, type, handler</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (element.addEventListener)
                element.addEventListener(type, handler, <span class="hljs-literal">false</span>);
            <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (element.attachEvent)
                element.attachEvent(<span class="hljs-string">"on"</span> + type, handler);
            <span class="hljs-keyword">else</span>
                element[<span class="hljs-string">"on"</span> + type] = handler;
        &#125;,
        <span class="hljs-attr">removeHandler</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">element, type, handler</span>) </span>&#123;
            <span class="hljs-keyword">if</span>(element.removeEventListener)
                element.removeEventListener(type, handler, <span class="hljs-literal">false</span>);
            <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(element.detachEvent)
                element.detachEvent(<span class="hljs-string">"on"</span> + type, handler);
            <span class="hljs-keyword">else</span>
                element[<span class="hljs-string">"on"</span> + type] = handler;
        &#125;,
        <span class="hljs-comment">/**
        * 监听触摸的方向
        * <span class="hljs-doctag">@param </span>target            要绑定监听的目标元素
        * <span class="hljs-doctag">@param </span>isPreventDefault  是否屏蔽掉触摸滑动的默认行为（例如页面的上下滚动，缩放等）
        * <span class="hljs-doctag">@param </span>upCallback        向上滑动的监听回调（若不关心，可以不传，或传false）
        * <span class="hljs-doctag">@param </span>rightCallback     向右滑动的监听回调（若不关心，可以不传，或传false）
        * <span class="hljs-doctag">@param </span>downCallback      向下滑动的监听回调（若不关心，可以不传，或传false）
        * <span class="hljs-doctag">@param </span>leftCallback      向左滑动的监听回调（若不关心，可以不传，或传false）
        */</span>
        <span class="hljs-attr">listenTouchDirection</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target, isPreventDefault, upCallback, rightCallback, downCallback, leftCallback</span>) </span>&#123;
            <span class="hljs-built_in">this</span>.addHandler(target, <span class="hljs-string">"touchstart"</span>, handleTouchEvent);
            <span class="hljs-built_in">this</span>.addHandler(target, <span class="hljs-string">"touchend"</span>, handleTouchEvent);
            <span class="hljs-built_in">this</span>.addHandler(target, <span class="hljs-string">"touchmove"</span>, handleTouchEvent);
            <span class="hljs-keyword">var</span> startX;
            <span class="hljs-keyword">var</span> startY;
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleTouchEvent</span>(<span class="hljs-params">event</span>) </span>&#123;
                <span class="hljs-keyword">switch</span> (event.type)&#123;
                    <span class="hljs-keyword">case</span> <span class="hljs-string">"touchstart"</span>:
                        startX = event.touches[<span class="hljs-number">0</span>].pageX;
                        startY = event.touches[<span class="hljs-number">0</span>].pageY;
                        <span class="hljs-keyword">break</span>;
                    <span class="hljs-keyword">case</span> <span class="hljs-string">"touchend"</span>:
                        <span class="hljs-keyword">var</span> spanX = event.changedTouches[<span class="hljs-number">0</span>].pageX - startX;
                        <span class="hljs-keyword">var</span> spanY = event.changedTouches[<span class="hljs-number">0</span>].pageY - startY;

                        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Math</span>.abs(spanX) > <span class="hljs-built_in">Math</span>.abs(spanY))&#123;      <span class="hljs-comment">//认定为水平方向滑动</span>
                            <span class="hljs-keyword">if</span>(spanX > <span class="hljs-number">30</span>)&#123;         <span class="hljs-comment">//向右</span>
                                <span class="hljs-keyword">if</span>(rightCallback)
                                    rightCallback();
                            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(spanX < -<span class="hljs-number">30</span>)&#123; <span class="hljs-comment">//向左</span>
                                <span class="hljs-keyword">if</span>(leftCallback)
                                    leftCallback();
                            &#125;
                        &#125; <span class="hljs-keyword">else</span> &#123;                                    <span class="hljs-comment">//认定为垂直方向滑动</span>
                            <span class="hljs-keyword">if</span>(spanY > <span class="hljs-number">30</span>)&#123;         <span class="hljs-comment">//向下</span>
                                <span class="hljs-keyword">if</span>(downCallback)
                                    downCallback();
                            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (spanY < -<span class="hljs-number">30</span>) &#123;<span class="hljs-comment">//向上</span>
                                <span class="hljs-keyword">if</span>(upCallback)
                                    upCallback();
                            &#125;
                        &#125;

                        <span class="hljs-keyword">break</span>;
                    <span class="hljs-keyword">case</span> <span class="hljs-string">"touchmove"</span>:
                        <span class="hljs-comment">//阻止默认行为</span>
                        <span class="hljs-keyword">if</span>(isPreventDefault)
                            event.preventDefault();
                        <span class="hljs-keyword">break</span>;
                &#125;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3.4 监听滑动</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">eventUtil.listenTouchDirection(<span class="hljs-built_in">document</span>.documentElement,<span class="hljs-literal">true</span>,
    <span class="hljs-function">()=></span>&#123;game.moveUp()&#125;,
    <span class="hljs-function">()=></span>&#123;game.moveRight()&#125;,
    <span class="hljs-function">()=></span> &#123;game.moveDown()&#125;,
    <span class="hljs-function">()=></span>&#123;game.moveLeft()&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="http://game.52fansite.com/2048.html" target="_blank" rel="nofollow noopener noreferrer">预览地址</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65f7a42508aa4d96a6ea1962689febe1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            