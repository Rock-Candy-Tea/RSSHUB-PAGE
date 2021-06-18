
---
title: '前端 JavaScript 之『防抖』的简单代码实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d24ab1a062bc48d3a5f8992bd4c366f5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 04:54:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d24ab1a062bc48d3a5f8992bd4c366f5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第17天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前戏 🌰</h2>
<p>经过上一篇文章的总结，我们知道：短时间内高频率地触发事件，可能会导致不良后果。</p>
<p>具体到我们开发界来说，如果数据一直处于一种高频率更新的状态，那么可能会引发的问题如下：</p>
<ul>
<li>前后端数据交互频率过高，导致流量浪费。</li>
<li>界面高频率渲染更新，引发页面延迟、卡顿或假死等状况，影响体验。</li>
</ul>
<p>在进入正题之前，我们先来看下面这个例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">""</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"example-form"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"name"</span>></span>名称<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> 
               <span class="hljs-attr">name</span>=<span class="hljs-string">"name"</span> 
               <span class="hljs-attr">id</span>=<span class="hljs-string">"name"</span> 
               <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"please input your name"</span>
         ></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"res"</span>></span>输入<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"multipart"</span> 
                  <span class="hljs-attr">name</span>=<span class="hljs-string">"res"</span> 
                  <span class="hljs-attr">id</span>=<span class="hljs-string">"res"</span> 
                  <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"这里是每一次输入的结果"</span>
        ></span><span class="hljs-tag"></<span class="hljs-name">textarea</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> inputEle = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#name"</span>);
    <span class="hljs-keyword">const</span> resEle = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#res"</span>);
    inputEle.addEventListener(<span class="hljs-string">"input"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.value);
        resEle.value += <span class="hljs-string">`\n<span class="hljs-subst">$&#123; <span class="hljs-built_in">this</span>.value &#125;</span>`</span>
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d24ab1a062bc48d3a5f8992bd4c366f5~tplv-k3u1fbpfcp-zoom-1.image" alt="频繁触发" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在输入框的 input 事件中，将该输入框的当前值输出在多行文本框中。可以看到，每输入一个拼音字母，都会有一条输出记录，触发频率取决于人的打字速度。</p>
<h2 data-id="heading-1">新需求 🤬</h2>
<p>假如，现在有这么一个新需求，要我们在 input 事件中加入新的逻辑：将输入框的当前值发往后台进行存储。</p>
<p>可以想象，这种情况下的前后端交互频率该有多高，其中很多数据都是没有必要即刻发送保存的，纯属浪费流量。</p>
<p>我们可以考虑对这个需求进行一下优化，只要控制一下交互频率就好，主要有以下两个方向：</p>
<ul>
<li>每隔几秒发送一次数据 —— 节流</li>
<li>每当用户停止输入之后，开始计时，一定时间后发送一次数据 —— 防抖</li>
</ul>
<h2 data-id="heading-2">实现防抖</h2>
<p>首先，我们从防抖的方向进行实现：只有当用户停止输入一段时间后，才会将输入内容输出在多行文本框中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> resEle = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#res"</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeOutputVal</span>(<span class="hljs-params">value</span>) </span>&#123;
        resEle.value += <span class="hljs-string">`\n<span class="hljs-subst">$&#123; value &#125;</span>`</span>;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn, delay = <span class="hljs-number">1000</span></span>) </span>&#123;
        <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(args);
            <span class="hljs-keyword">if</span> (timer) &#123;
                <span class="hljs-built_in">clearTimeout</span>(timer);
                timer = <span class="hljs-literal">null</span>;
            &#125;

            timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                fn.apply(<span class="hljs-built_in">this</span>, args);
            &#125;, delay);
        &#125;
    &#125;

    <span class="hljs-keyword">const</span> outputRes = debounce(changeOutputVal, <span class="hljs-number">1000</span>);

    <span class="hljs-keyword">const</span> inputEle = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#name"</span>);

    inputEle.addEventListener(<span class="hljs-string">"input"</span>, <span class="hljs-function">(<span class="hljs-params">eve</span>) =></span> &#123;
        outputRes(eve.target.value);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码说明：</p>
<ol>
<li>每一次事件被触发，都会清除当前的 timer 然后重新设置超时调用，即重新计时。 这就会导致每一次高频事件都会取消前一次的超时调用，导致事件处理程序不能被触发；</li>
<li>只有当高频事件停止，最后一次事件触发的超时调用才能在delay时间后执行。</li>
</ol>
<p>运行效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc7bc6c8c6c34a219092f4a9ac5ea2e6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，在加入防抖代码之后，input 事件并不会每次输入都会输出在多行文本，而是会在用户停止输入 delay 时间之后触发输出，频率确实低了很多。从某种程度上来说，的确优化了页面显示效果，给人的视觉感受比较舒服。</p>
<h2 data-id="heading-3">总结</h2>
<p>巧用防抖函数的，既可以优化性能，又能优化显示效果，一举两得。</p>
<p>~</p>
<p>~</p>
<p>代码比较粗糙，也比较基础，后面会逐步向着复杂的方向迭代，望各位看官海涵🙏</p>
<p>~</p>
<p>~</p>
<p>~ 本文完</p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好！我是〖编程三昧〗的作者 <strong>隐逸王</strong>，我的公众号是『编程三昧』，欢迎关注，希望大家多多指教！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07851b63df1845089be01a50f69a64e9~tplv-k3u1fbpfcp-zoom-1.image" alt="mianshi" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            