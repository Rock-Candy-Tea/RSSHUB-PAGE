
---
title: 'React Hooks初探（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9731'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 04:28:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=9731'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>hooks引入react里已经很长时间了，在项目中一直使用，文档也没仔细阅读，今天打算再重新看看文档，领略一下当初学习的感受。</p>
</blockquote>
<p><strong>这是我参与8月更文挑战的第16天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<p>今天继续学习几个高阶的Hooks：<code>useMemo</code>、<code>useRef</code>、<code>useReducer</code>。</p>
<h2 data-id="heading-0">useMemo</h2>
<p>useMemoo用于进行值的依赖更新，可以用于在每次渲染时避免昂贵的计算。如官网给的例子：</p>
<pre><code class="copyable">//非常昂贵的计算
function computeExpensiveValue(a,b)&#123;
    let sum = 0;
    for(var i = 0; i < 10000; i++ )&#123;
        sum += (a+b);
    &#125;
    return sum;
&#125;
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
//只有当a,b发送变化时才会重新计算memoizedValue

<span class="copy-code-btn">复制代码</span></code></pre>
<p>另:<code>useMemo(()=>fn,dependencies)</code>等于<code>useCallback(fn,dependencies)</code>.</p>
<h2 data-id="heading-1">useRef</h2>
<p>该Hook用于获取DOM节点的引用。现在都在用框架开发网页应用。然后有一些场景还是需要使用原生的力量：DOM操作。</p>
<p>举个例子：输入一些内容，点击按钮打印内容。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Input:React.FC<&#123;&#125;> = <span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">const</span> inputEl = React.useRef<HTMLInputElement>(<span class="hljs-literal">null</span>);
    <span class="hljs-keyword">const</span> onButtonClick = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(inputEl.current?.value);
    &#125;;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;inputEl&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onButtonClick&#125;</span>></span>获取输入内容<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></></span></span>
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先在使用时需要注意两点：</p>
<ul>
<li>DOM节点对应的元素类型。比如input输入框:<code>HTMLInputElement</code>,div:<code>HTMLDivElement</code>，这些节点用于设置useRef的泛型。如<code>React.useRef<HTMLInputElement></code></li>
<li>初始值设置为<code>null</code></li>
</ul>
<h2 data-id="heading-2">useReducer</h2>
<p>reducer,相信大家都不陌生，redux里的一个重要的概念，用于修改应用里的store数据。相信react也是借用了这个概念吧，毕竟现在React的核心开发者是redux的作者。</p>
<p>首先看一下它的语法结构：
<code>const [state, dispatch] = useReducer(reducer, initialArg, init);</code></p>
<p>我们拿官方例子来说明：</p>
<pre><code class="copyable">const initialState = &#123;count: 0&#125;;

function reducer(state, action) &#123;
  switch (action.type) &#123;
    case 'increment':
      return &#123;count: state.count + 1&#125;;
    case 'decrement':
      return &#123;count: state.count - 1&#125;;
    default:
      throw new Error();
  &#125;
&#125;

function Counter() &#123;
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <>
      Count: &#123;state.count&#125;
      <button onClick=&#123;() => dispatch(&#123;type: 'decrement'&#125;)&#125;>-</button>
      <button onClick=&#123;() => dispatch(&#123;type: 'increment'&#125;)&#125;>+</button>
    </>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实你会发现这跟<code>useState</code>非常类似，都提供了state的引用和state的<code>setter</code>。然而对于那些复杂的数据，官方推荐使用<code>useReducer</code>的方式。</p>
<p>上面的例子里的初始state是默认声明好的，还有一种可以接收参数作为默认值的方式：</p>
<pre><code class="copyable">function init(initialCount) &#123;  return &#123;count: initialCount&#125;;&#125;
function reducer(state, action) &#123;
  //省略。。。
&#125;

function Counter(&#123;initialCount&#125;) &#123;
  const [state, dispatch] = useReducer(reducer, initialCount, init);  return (
    <>
      //省略。。。
    </>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">最后</h2>
<p>感谢阅读。</p></div>  
</div>
            