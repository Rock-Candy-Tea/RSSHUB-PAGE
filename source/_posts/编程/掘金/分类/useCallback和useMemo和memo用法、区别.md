
---
title: 'useCallback和useMemo和memo用法、区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b44c4c5beada46fcac95d6675e5505ca~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 22:45:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b44c4c5beada46fcac95d6675e5505ca~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">用法由来</h2>
<p><strong>当数据重新赋值时，整个组件会刷新渲染</strong>，当数据功能复杂且多，且部分数据无需刷新时，会被强制刷新，造成性能浪费，也可能会产出bug。<strong>那么这时候就需要用上useCallback和useMemo来缓存不需要更新的数据，形成memoized值，也就是缓存的值。memo则是用于子组件不重新渲染</strong></p>
<h2 data-id="heading-1">共同作用</h2>
<p>不同形式的减少重复渲染</p>
<h2 data-id="heading-2">memo用法</h2>
<p>假设组件Parent，里面有个子组件Child</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> [num,setBum] = useState(<span class="hljs-number">0</span>)
<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span> setNum(num+1)&#125; >
<span class="hljs-tag"><<span class="hljs-name">Child</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
)
&#125;

const Child = () => &#123;
console.log('child load')
return (
<span class="hljs-tag"><<span class="hljs-name">View</span>></span>child text<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
)
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击Button，Child会随着Parent刷新渲染，控制台打印</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// child load</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>使用memo后</strong></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Child = memo(<span class="hljs-function">() =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child load'</span>)
<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>child text<span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击button后Child不会重新渲染，控制台无打印</li>
<li>memo是一个函数，参数二是控制组件是否刷新的选填扩展函数，用法和shouldComponentUpdate一样</li>
</ul>
<h2 data-id="heading-3">useCallback 的用法</h2>
<p>同上有组件Parent，里面有个子组件Child</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> [num,setBum] = useState(<span class="hljs-number">0</span>)
<span class="hljs-keyword">const</span> clickBtn = <span class="hljs-function">() =></span> &#123;
setNum(num+<span class="hljs-number">1</span>)
&#125;

<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;clickBtn&#125;</span> ></span>
<span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">call</span>=<span class="hljs-string">&#123;clickBtn&#125;</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
)
&#125;

const Child = memo((call) => &#123;
console.log('child load')
return (
<span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;call&#125;</span>></span>child text<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
)
&#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击Button，Child会随着Parent刷新渲染，控制台打印</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// child load</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于打印了推论在给子组件传递函数后memo会无效</p>
<ul>
<li><strong>使用useCallback后</strong></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> [num,setBum] = useState(<span class="hljs-number">0</span>)

<span class="hljs-keyword">const</span> clickBtn = useCallback(<span class="hljs-function">() =></span> &#123;
setNum(num+<span class="hljs-number">1</span>)
&#125;,[]) <span class="hljs-comment">//[]可选填依赖项，不填里面的num是不会更新的，永远都是0</span>

<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;clickBtn&#125;</span> ></span>
<span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">call</span>=<span class="hljs-string">&#123;clickBtn&#125;</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
)
&#125;

const Child = memo((call) => &#123;
console.log('child load')
return (
<span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;call&#125;</span>></span>child text<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
)
&#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击button后Child不会重新渲染，控制台无打印</li>
<li>useCallback参数二[ ]是可选填依赖项，不填里面的num是不会更新的，永远都是num得初始值0，ex: 如果填了[num]，那么clickBtn函数会跟着num的更新而更新。</li>
</ul>
<h2 data-id="heading-4">useMemo用法</h2>
<p>同上有组件Parent，里面有个子组件Child</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> [num,setBum] = useState(<span class="hljs-number">0</span>)

<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;clickBtn&#125;</span> ></span>
<span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">num</span>=<span class="hljs-string">&#123;num</span> + <span class="hljs-attr">1</span>&#125; <span class="hljs-attr">call</span>=<span class="hljs-string">&#123;clickBtn&#125;</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
)
&#125;

const Child = memo((num) => &#123;
console.log('child load')
return (
<span class="hljs-tag"><<span class="hljs-name">View</span>></span>child text &#123;num&#125;<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
)
&#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击Button，Child会随着Parent刷新渲染，控制台打印</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// child load</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于打印了推论出在给子组件传递变量的情况下memo会无效</p>
<ul>
<li><strong>使用useMemo后</strong></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
   <span class="hljs-keyword">const</span> [num,setBum] = useState(<span class="hljs-number">0</span>)
   
   <span class="hljs-keyword">const</span> mockData = useMemo(<span class="hljs-function">() =></span> (&#123;
   <span class="hljs-attr">newNum</span>: num + <span class="hljs-number">1</span>
   &#125;),[]) <span class="hljs-comment">// []可选填依赖项，不填里面的num是不会更新的，永远都是0,那么newNum永远是1</span>
   
   <span class="hljs-keyword">return</span> (
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;clickBtn&#125;</span> ></span>
   <span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">num</span>=<span class="hljs-string">&#123;mockData.newNum&#125;</span> <span class="hljs-attr">call</span>=<span class="hljs-string">&#123;clickBtn&#125;</span> /></span>
   <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
   )
   &#125;
   
   const Child = memo((call) => &#123;
   console.log('child load')
   return (
   <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;call&#125;</span>></span>child text<span class="hljs-tag"></<span class="hljs-name">View</span>></span>
   )
   &#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击button后Child不会重新渲染，控制台无打印，避免了无意义渲染</li>
<li>useMemo参数二[ ]是可选填依赖项，不填里面的num是不会更新的，永远都是num得初始值0，ex: 如果填了[num]，那么mockData对象会跟着num的更新而更新。</li>
</ul>
<h2 data-id="heading-5">区别</h2>
<ul>
<li>memo用于缓存组件</li>
<li>useCallback用于缓存函数</li>
<li>useMemo用于缓存数据对象，写法需要return 对象&#123;&#125;  ，由于ES6语法可简写成() => (&#123;&#125;)  相当于</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>) </span>&#123;
 <span class="hljs-keyword">return</span> &#123;&#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b44c4c5beada46fcac95d6675e5505ca~tplv-k3u1fbpfcp-zoom-1.image" alt="觉得还不错记得点个赞，与君加油" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            