
---
title: '使用 jQuery 实现鼠标悬停显示隐藏内容的 vue 自定义指令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faee4e0e300442ebae35470c36d3d07b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 23:02:07 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faee4e0e300442ebae35470c36d3d07b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ol>
<li>在vue项目中引入jQuery</li>
<li>新建 <code>directive</code> 文件夹，新建 <code>overflow.js</code>，代码如下</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// overflow.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousePosition</span>(<span class="hljs-params">ev</span>) </span>&#123;
    ev = ev || <span class="hljs-built_in">window</span>.event;
    <span class="hljs-keyword">if</span> (ev.pageX || ev.pageY) &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">x</span>: ev.pageX,
            <span class="hljs-attr">y</span>: ev.pageY
        &#125;;
    &#125;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">x</span>: ev.clientX + <span class="hljs-built_in">document</span>.body.scrollLeft - <span class="hljs-built_in">document</span>.body.clientLeft,
        <span class="hljs-attr">y</span>: ev.clientY + <span class="hljs-built_in">document</span>.body.scrollTop - <span class="hljs-built_in">document</span>.body.clientTop
    &#125;;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindMapMouseTitle</span>(<span class="hljs-params">selector, value</span>) </span>&#123;
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@param <span class="hljs-type">&#123;object&#125;</span> </span>selector jquery对象
     * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>value title字符串
     */</span>
    <span class="hljs-keyword">let</span> self = <span class="hljs-built_in">this</span>;
    selector.mouseover(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-keyword">let</span> text = value || $(<span class="hljs-built_in">this</span>).html();
        <span class="hljs-keyword">let</span> mousePos = mousePosition(e);
        <span class="hljs-keyword">if</span> (selector.get(<span class="hljs-number">0</span>).clientWidth < selector.get(<span class="hljs-number">0</span>).scrollWidth) &#123;
            $(<span class="hljs-string">"#overflow-title"</span>).html(text).show().css(&#123;
                <span class="hljs-string">"top"</span>: mousePos.y,
                <span class="hljs-string">"left"</span>: mousePos.x
            &#125;);
        &#125;
    &#125;);
    <span class="hljs-comment">/* 增加click事件， fix元素隐藏后无法触发mouseout事件 = 模拟html title属性行为 */</span>
    selector.bind(<span class="hljs-string">'click mouseout'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>)</span>&#123;
        $(<span class="hljs-string">"#overflow-title"</span>).html(<span class="hljs-string">""</span>).hide();
    &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-comment">/** text过长title */</span>
    <span class="hljs-attr">bind</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">element, binding</span>) </span>&#123;
        <span class="hljs-keyword">let</span> value = binding.value;
        bindMapMouseTitle($(element), value);
    &#125;,
    <span class="hljs-attr">update</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">element, binding</span>) </span>&#123;
        <span class="hljs-keyword">let</span> value = binding.value;
        bindMapMouseTitle($(element), value);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在 <code>main.js</code> 中全局注册指令</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> overflow <span class="hljs-keyword">from</span> <span class="hljs-string">'./directive/overflow'</span>

Vue.directive(<span class="hljs-string">'overflow'</span>, overflow)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>在 <code>App.vue</code> 中添加显示盒子</li>
</ol>
<pre><code class="copyable"><template>
    <div id="app">
        <router-view />
        <div id="overflow-title"></div>
    </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>添加盒子样式(为你的盒子添加你喜欢的样式吧)</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#overflow-title</span> &#123;
    <span class="hljs-attribute">max-width</span>: <span class="hljs-number">250px</span>;
    <span class="hljs-attribute">word-wrap</span>: break-word;
    <span class="hljs-attribute">display</span>: none;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">8px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">23px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#666</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f3f3f3</span>;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">2px</span> <span class="hljs-number">1px</span> <span class="hljs-number">3px</span> <span class="hljs-number">0</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.07</span>);
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">6px</span>;
    <span class="hljs-attribute">border</span>: solid <span class="hljs-number">1px</span> <span class="hljs-number">#ddd</span>;
    <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9999999</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>使用</li>
</ol>
<pre><code class="copyable"><div v-overflow>XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>效果</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faee4e0e300442ebae35470c36d3d07b~tplv-k3u1fbpfcp-watermark.image" alt="1625727597(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            