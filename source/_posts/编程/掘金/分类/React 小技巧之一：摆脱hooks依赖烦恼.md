
---
title: 'React 小技巧之一：摆脱hooks依赖烦恼'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7064'
author: 掘金
comments: false
date: Fri, 14 May 2021 09:22:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=7064'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>react项目中，很常见的一个场景:</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> [watchValue, setWatchValue] = useState(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> [otherValue1, setOtherValue1] = useState(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> [otherValue2, setOtherValue2] = useState(<span class="hljs-string">''</span>);

useEffect(<span class="hljs-function">() =></span> &#123;
    doSomething(otherValue1, otherValue2);
&#125;, [watchValue, otherValue1, otherValue2]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们想要<code>watchValue</code>改变的时候执行<code>useEffect</code>，里面会引用其他值。</p>
<p>这时有个让人烦恼的问题：</p>
<ul>
<li>如果不把<code>otherValue1, otherValue2</code>加入依赖数组的话，<code>useEffect</code>里面很可能会引用到<code>otherValue1, otherValue2</code>旧的变量，从而发生意想不到的错误（如果安装hooks相关eslint的话，会提示警告）。</li>
<li>反之，如果把<code>otherValue1, otherValue2</code>加入依赖数组的话，这两个值改变的时候<code>useEffect</code>里面的函数也会执行，这并不是我们想要的。</li>
</ul>
<hr>
<p>把<code>otherValue1, otherValue2</code>变成<code>ref</code>可以解决这个问题：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> [watchValue, setWatchValue] = useState(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> other1 = useRef(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> other2 = useRef(<span class="hljs-string">''</span>);

useEffect(<span class="hljs-function">() =></span> &#123;
    doSomething(other1.current, other2.current);
&#125;, [watchValue, other1, other2]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样<code>other1, other2</code>不会变，解决了前面的问题，但是又引入了一个新的问题：<code>other1, other2</code>的值<code>current</code>改变的时候，不会触发组件重新渲染(<code>useRef</code>的<code>current</code>值改变不会触发组件渲染)，从而值改变时候界面不会更新！</p>
<hr>
<p>这就是<code>hooks</code>里面的一个头疼的地方，<code>useState</code>会触发重新渲染，但不好作为<code>useEffect</code>的依赖（会触发不需要的<code>useEffect</code>）, <code>useRef</code>可以放心作为<code>useEffect</code>依赖，但是又不会触发组件渲染，界面不更新。</p>
<p>如何解决？</p>
<p>可以将<code>useRef</code>和<code>useState</code>的特性结合起来，构造一个新的<code>hooks</code>函数: <code>useStateRef</code>。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> &#123; useState, useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-comment">// 使用 useRef 的引用特质， 同时保持 useState 的响应性</span>
<span class="hljs-keyword">type</span> StateRefObj<T> = &#123;
  <span class="hljs-attr">value</span>: T;
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useStateRef</span><<span class="hljs-title">T</span>>(<span class="hljs-params">
  initialState: T | (() => T)
</span>): <span class="hljs-title">StateRefObj</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">const</span> [state, setState] = useState(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> initialState === <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-keyword">return</span> (initialState <span class="hljs-keyword">as</span> () => T)();
    &#125;
    <span class="hljs-keyword">return</span> initialState;
  &#125;);
  <span class="hljs-keyword">const</span> stateRef = useRef(state);
  stateRef.current = state;
  <span class="hljs-keyword">const</span> [ref] = useState<StateRefObj<T>>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">v: T</span>) &#123;
        setState(v);
      &#125;,
      <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
        <span class="hljs-keyword">return</span> stateRef.current;
      &#125;,
    &#125;;
  &#125;);
  <span class="hljs-keyword">return</span> ref;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就能这样用：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> watch = useStateRef(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> other1 = useStateRef(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> other2 = useStateRef(<span class="hljs-string">''</span>);

<span class="hljs-comment">// 这样改变值：watch.value = "new";</span>

useEffect(<span class="hljs-function">() =></span> &#123;
    doSomething(other1.value, other2.value);
&#125;, [watch.value, other1, other2]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，<code>other1, other2</code>既有<code>useRef</code>的引用特性，不会触发<code>useEffect</code>不必要的执行。而我么把<code>watch.value</code>（而不是<code>watch</code>）加入依赖数组，这样<code>watch</code>的值改变时也会执行<code>useEffect</code>，达到<code>watch</code>的效果。</p>
<p>同时，又保持了<code>useState</code>的响应特性，通过<code>.value</code>改变值得时候，同时也会触发组件渲染和界面更新。</p>
<blockquote>
<p>注：这里之所以用<code>.value</code>而不用<code>.current</code>, 是刻意为了保持和<code>useRef</code>的区别。</p>
</blockquote></div>  
</div>
            