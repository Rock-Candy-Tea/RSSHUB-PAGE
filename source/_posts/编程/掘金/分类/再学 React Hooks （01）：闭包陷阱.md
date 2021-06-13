
---
title: '再学 React Hooks （01）：闭包陷阱'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b60ec14dc724c60aaa417f32d14e9de~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 05:08:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b60ec14dc724c60aaa417f32d14e9de~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 9 天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">什么是闭包陷阱</h2>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> FunctionComponent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [value, setValue] = useState(<span class="hljs-number">1</span>)
  <span class="hljs-keyword">const</span> log = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      alert(value)
    &#125;, <span class="hljs-number">1000</span>);
  &#125;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>FunctionComponent<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>value: &#123;value&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setValue(value + 1)&#125;>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;log&#125;</span>></span>alert<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的函数式组件中，我们点击 <strong>alert</strong> 按钮后会在 2s 后弹出 <strong>value</strong> 的值，我们在这 2s 的时间内可以继续点击 <strong>add</strong> 按钮增加 <strong>value</strong> 的值。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b60ec14dc724c60aaa417f32d14e9de~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210612154401986" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是我们操作的结果。我们发现弹出的值和当前页面显示的值不相同。换句话说：<strong>log 方法内的 value 和点击动作触发那一刻的 value 相同，value 的后续变化不会对 log 方法内的 value 造成影响</strong>。这种现象被称为“闭包陷阱”或者被叫做“Capture Value” ：函数式组件每次render 都会生产一个新的 log 函数，这个新的 log 函数会产生一个在当前这个阶段 value 值的闭包。</p>
<p>上面例子 “闭包陷阱” 的分析：</p>
<ol>
<li>初始次渲染，生成一个 log 函数（value = 1）</li>
<li>value 为 1 时，点击 alert 按钮执行 log 函数（value = 1）</li>
<li>点击按钮增加 value，比如 value 增加到 6，组件 render ，生成一个新的 log 函数（value = 6）</li>
<li>计时器触发，log 函数（value = 1）弹出闭包内的 value 为 1</li>
</ol>
<h2 data-id="heading-1">解决闭包陷阱的方案</h2>
<h3 data-id="heading-2">使用 useRef 解决闭包陷阱的问题</h3>
<pre><code class="copyable">const FunctionComponent = () => &#123;
  const [value, setValue] = useState(1)
  const countRef = useRef(value)

  useEffect(() => &#123;
    countRef.current = value
  &#125;, [value])

  const log = useCallback(
    () => &#123;
      setTimeout(() => &#123;
        alert(countRef.current)
      &#125;, 1000);
    &#125;,
    [value],
  )

  return (
    <div>
      <p>FunctionComponent</p>
      <div>value: &#123;value&#125;</div>
      <button onClick=&#123;() => setValue(value + 1)&#125;>add</button>
      <br/>
      <button onClick=&#123;log&#125;>alert</button>
    </div>
  )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>useRef</strong> 每次 render 时都会返回<strong>同一个引用类型的对象</strong>，我们设置值和读取值都在这个对象上处理，这样就能获取到最新的 value 值了。</p>
<h3 data-id="heading-3">更新 State 时的回调函数</h3>
<blockquote>
<p><em>Effect Hook</em> 可以让你在函数组件中执行副作用操作</p>
</blockquote>
<p>假设现在我们要开一个每秒自增的计数器，我们一般会写出下面这样的代码：</p>
<pre><code class="copyable">const Counter = () => &#123;
  const [value, setValue] = useState(0)

  useEffect(() => &#123;
    const timer = setInterval(() => &#123;
      console.log('new value:', value+1)
      setValue(value + 1)
    &#125;, 1000);
    return () => &#123;
      clearInterval(timer)
    &#125;
  &#125;, [])

  return (
    <div>
      <p>Counter</p>
      <div>count: &#123;value&#125;</div>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中，我们在 <code>useEffect</code> 中不断更新 value 的值，但是结合我们之前的闭包陷阱问题来分析，我们可以发现定时器的value值永远都会是 0，这就导致每次设置的 value 值都是 1，下图是运行的结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8ebab428eae434cb098cdeff5a60dfc~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210612163548629" loading="lazy" referrerpolicy="no-referrer"></p>
<p>“闭包陷阱” 最大的问题就是在函数数内无法获取的最新的 state 的值，那 React 提供了哪些方法来解决呢？</p>
<ol>
<li>useRef 上面已有介绍</li>
<li>useState 更新值时传入回调函数</li>
</ol>
<p>除了上面介绍的 <strong>useRef</strong> 的方法外，我们也可以在更新 state 时我们传入回调函数（回调函数里取到的值是最新的）。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> [value, setValue] = useState(<span class="hljs-number">0</span>)

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 回调函数的最新值</span>
      setValue(<span class="hljs-function"><span class="hljs-params">value</span> =></span> value + <span class="hljs-number">1</span>)
    &#125;, <span class="hljs-number">1000</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">clearInterval</span>(timer)
    &#125;
  &#125;, [])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfe72dcf06ef40c88ebabe05e21fa3d4~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210612170112557" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">闭包陷阱和 Hooks 依赖</h2>
<p><strong>useEffect</strong>、<strong>useLayoutEffect</strong>、<strong>useCallback</strong>、<strong>useMemo</strong> 的第二个参数为依赖数组，依·赖数组中任意一个依赖变化（浅比较）会有如下效果：</p>
<ol>
<li><strong>useEffect</strong>、<strong>useLayoutEffect</strong> 内部的副作用函数会执行，并且副作用函数可以获取到当前所有依赖的最新值。</li>
<li><strong>useCallback</strong>、<strong>useMemo</strong> 会返回新的函数或对象，并缺内部的函数也能获取到当前所有依赖的最新值。</li>
</ol>
<p>利用这个机制理论可以解决“闭包陷阱”，但是在某种情况下不适用：</p>
<pre><code class="hljs language-diff copyable" lang="diff">const Counter = () => &#123;
  const [value, setValue] = useState(0)

  useEffect(() => &#123;
    const timer = setInterval(() => &#123;
      console.log('tick:', value+1)
      setValue(value + 1)
    &#125;, 1000);
    return () => &#123;
    console.log('clear')
      clearInterval(timer)
    &#125;
  - &#125;, [])
  + &#125;, [value])

  return (
    <div>
      <p>Counter</p>
      <div>count: &#123;value&#125;</div>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码我们把 value 作为依赖项加入到依赖数组，却是能够实现功能，但是每次都会经历 <code>clearInterval -> setValue ->clearInterval  </code> 的循环。这就<strong>造成了不必要的性能消耗</strong>。还有一种极端的情况，如果我们没有返回取消定时器的函数，<strong>就会不断增加新的定时器</strong>。</p>
<h3 data-id="heading-5">使用 Hook 依赖的注意事项</h3>
<p><strong>事件订阅</strong></p>
<p>现在我们有如下的场景</p>
<pre><code class="copyable">useEffect(() =>&#123;
someThing.subscribe(() => &#123;
// do something with value
&#125;)
&#125;, [value])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中，value 变化会不断订阅新的事件。所以在 <strong>EffectHook</strong> 中我们记得返回取消副作用的函数</p>
<pre><code class="copyable">useEffect(() =>&#123;
someThing.subscribe(() => &#123;
// do something with value
&#125;)
return () => &#123;
+ // 添加取消副作用的函数
&#125;
&#125;, [value])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>防抖节流</strong></p>
<pre><code class="copyable">function BadDemo() &#123;
  const [count, setCount] = useState(1);
  const [, setRerender] = useState(false);
  const handleClick = debounce(() => &#123;
    setCount(c => ++c);
  &#125;, 1000);
  useEffect(() => &#123;
    // 每500ms，组件重新render
    setInterval(() => &#123;
      setRerender(r => !r);
    &#125;, 500);
  &#125;, []);
  return <div onClick=&#123;handleClick&#125;>&#123;count&#125;</div>;
&#125;

作者：蚂蚁保险体验技术
链接：https://juejin.cn/post/6844904090032406536
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如上面的代码，我们有一个需要防抖的 <code>handleClick</code> 函数，但是我们函数会不时地渲染，每次 render 都会生成一个新的函数，那么这个<strong>防抖的函数就失去了作用</strong>。</p>
<h2 data-id="heading-6">总结</h2>
<p>最后总结一下：</p>
<ol>
<li><strong>React Hooks</strong> 存在“闭包渲染”的问题，每次 render 都会闭包缓存当前render对应的 state</li>
<li>可以通过 <strong>useRef</strong>、<strong>state 更新时的回调函数</strong>来解决这个问题</li>
<li>使用 <strong>EffectHook</strong> 依赖时要注意取消副作用</li>
</ol>
<h2 data-id="heading-7">参考资料</h2>
<ul>
<li><a href="https://zh-hans.reactjs.org/docs/hooks-intro.html" target="_blank" rel="nofollow noopener noreferrer">Hook  官方文档</a></li>
<li><a href="https://github.com/ascoders/weekly/blob/v2/095.%E7%B2%BE%E8%AF%BB%E3%80%8AFunction%20VS%20Class%20%E7%BB%84%E4%BB%B6%E3%80%8B.md" target="_blank" rel="nofollow noopener noreferrer">精读《Function VS Class 组件》</a></li>
<li><a href="https://github.com/ascoders/weekly/blob/v2/096.%E7%B2%BE%E8%AF%BB%E3%80%8AuseEffect%20%E5%AE%8C%E5%85%A8%E6%8C%87%E5%8D%97%E3%80%8B.md" target="_blank" rel="nofollow noopener noreferrer">精读《useEffect 完全指南》</a></li>
<li><a href="https://juejin.cn/post/6844904090032406536#heading-5" target="_blank">写React Hooks前必读</a></li>
</ul></div>  
</div>
            