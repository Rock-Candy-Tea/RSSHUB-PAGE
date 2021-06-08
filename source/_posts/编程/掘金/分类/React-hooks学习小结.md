
---
title: 'React-hooks学习小结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05699cf2e7224d45ab1020a440b09f83~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 02:36:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05699cf2e7224d45ab1020a440b09f83~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<ul>
<li>Hook 在 class 内部是<strong>不</strong>起作用的。</li>
<li>什么时候用hooks？ 编写组件时需要添加一些state时，而不想使用class组件时</li>
</ul>
<h3 data-id="heading-0">useSate</h3>
<ul>
<li>
<p>返回一个对值，包含当前状态和一个更新它的函数</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05699cf2e7224d45ab1020a440b09f83~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508105045952" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [count,setCount] =useSate(<span class="hljs-number">0</span>) <span class="hljs-comment">//count初始值设置为0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">useEffect</h3>
<h4 data-id="heading-2">基本使用</h4>
<ul>
<li>相当于 componentDidMount 和 componentDidUpdate:</li>
<li>页面初次渲染完成时，和state改变页面重新渲染后（dom更新完成时）执行</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'count 改变了'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">指定state改变时触发useEffect</h4>
<ul>
<li>state更新时可控，但是第一次渲染完成时还是会触发</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'count 改变了'</span>)
&#125;, [count]) <span class="hljs-comment">//最后一个参数为数组，指定需要监听的state</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">取消订阅</h4>
<pre><code class="hljs language-js copyable" lang="js">  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'count 改变了'</span>)
    <span class="hljs-keyword">let</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'已经订阅'</span>)
    &#125;, <span class="hljs-number">1000</span>)
    <span class="hljs-comment">// 返回一个函数，组件销毁时执行，取消某些订阅</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">clearInterval</span>(timer)
    &#125;
  &#125;, [age])

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">多个useEffect</h4>
<ul>
<li>
<p>存在多个时，每个useEffect都会触发，这就存在一个触发顺序的问题？</p>
</li>
<li>
<p>useEffect的执行顺序与它代码书写的顺序是一致的,</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">let</span> [count, setCount] = useState(<span class="hljs-number">0</span>)
  useEffect(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">countEff</span>(<span class="hljs-params"></span>) </span>&#123;  
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'count改变了'</span>)
  &#125;)
  <span class="hljs-keyword">let</span> [age, setAge] = useState(<span class="hljs-number">1</span>)
  useEffect(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ageEff</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'age改变了'</span>)
  &#125;)
<span class="hljs-comment">//输出：</span>
<span class="hljs-comment">//count改变了</span>
<span class="hljs-comment">//age改变了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">useContext</h3>
<ul>
<li>
<p>用于多层组件传值的情况，类似vue的privide/inject</p>
</li>
<li>
<p>举个例子</p>
<ul>
<li>
<p>爷组件</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">const</span> themes = &#123;
  <span class="hljs-attr">light</span>: &#123;
    <span class="hljs-attr">foreground</span>: <span class="hljs-string">"#000000"</span>,
    <span class="hljs-attr">background</span>: <span class="hljs-string">"#eeeeee"</span>
  &#125;,
  <span class="hljs-attr">dark</span>: &#123;
    <span class="hljs-attr">foreground</span>: <span class="hljs-string">"#ffffff"</span>,
    <span class="hljs-attr">background</span>: <span class="hljs-string">"#222222"</span>
  &#125;
&#125;;

<span class="hljs-keyword">const</span> ThemeContext = React.createContext(themes.light);  <span class="hljs-comment">// createContext创建，      参数为默认值，可选</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ThemeContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;themes.dark&#125;</span>></span> //通过value绑定要传入的值
      <span class="hljs-tag"><<span class="hljs-name">Toolbar</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">ThemeContext.Provider</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>父组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Toolbar</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ThemedButton</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>子组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ThemedButton</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> theme = useContext(ThemeContext); <span class="hljs-comment">//使用useContext接收传来的值</span>
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">background:</span> <span class="hljs-attr">theme.background</span>, <span class="hljs-attr">color:</span> <span class="hljs-attr">theme.foreground</span> &#125;&#125;></span>
      I am styled by theme context!
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-7">useReducer</h3>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ReducerDemo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [count,dispatch] =useReducer(<span class="hljs-function">(<span class="hljs-params">state,action</span>)=></span>&#123;
        <span class="hljs-keyword">switch</span>(action)&#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'add'</span>: <span class="hljs-keyword">return</span> state+<span class="hljs-number">1</span>
            <span class="hljs-keyword">case</span> <span class="hljs-string">'sub'</span>: <span class="hljs-keyword">return</span> state-<span class="hljs-number">1</span>
            <span class="hljs-attr">default</span> :<span class="hljs-keyword">return</span> state
        &#125;
    &#125;,<span class="hljs-number">0</span>)<span class="hljs-comment">//传入一个reducer和一个初始值</span>
    <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch('add')&#125;><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch('sub')&#125;><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">useCallback与useMemo</h3>
<ul>
<li>缓存函数，避免重复渲染</li>
<li>usecallback监听a和b两个状态，改变时触发里面的doSomething</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> memoizedCallback = useCallback(
  <span class="hljs-function">() =></span> &#123;
    doSomething(a, b);
  &#125;,
  [a, b],
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">useMemo</h3>
<ul>
<li>与usecallback用法相似</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> memoizedCallback = useMemo(
  <span class="hljs-function">() =></span> &#123;
    doSomething(a, b);
  &#125;,
  [a, b],
);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>不同点：</p>
<ul>
<li>
<p>useCallback创建时（渲染页面）不去执行里面的函数</p>
</li>
<li>
<p>useMemo创建时（渲染页面）会执行一次</p>
<pre><code class="hljs language-js copyable" lang="js">useCallback(<span class="hljs-function">()=></span>&#123;&#125;, deps) 
<span class="hljs-comment">//相当于</span>
useMemo(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">//返回一个函数</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function">()=></span>&#123;
        
    &#125;
&#125;, deps)。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-10">自定义hook</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useBodyScrollPosition</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [scrollPosition, setScrollPosition] = useState(<span class="hljs-literal">null</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> handleScroll = <span class="hljs-function">() =></span> setScrollPosition(<span class="hljs-built_in">window</span>.scrollY);
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'scroll'</span>, handleScroll);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span>
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'scroll'</span>, handleScroll);
  &#125;, []);

  <span class="hljs-keyword">return</span> scrollPosition;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            