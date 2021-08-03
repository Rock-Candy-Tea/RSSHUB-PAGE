
---
title: 'React.memo() 和 useMemo() 的用法和区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6928'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 06:29:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=6928'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文翻译自<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Freact-memo-vs-usememo%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/react-memo-vs-usememo/" ref="nofollow noopener noreferrer"> <code>React.memo()</code> vs. <code>useMemo()</code>: Major differences and use cases</a></p>
<p>在软件开发中，我们通常痴迷于性能提升以及如何使我们的应用程序执行得更快，从而为用户提供更好的体验。</p>
<p>Memoization 是优化性能的方法之一。 在本文中，我们将探讨它在 React 中的工作原理。</p>
<h1 data-id="heading-0">什么是 memoization？</h1>
<p>在解释这个概念之前，让我们先来看一个简单的斐波那契程序：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fibonacci</span>(<span class="hljs-params">n</span>)</span>&#123;
  <span class="hljs-keyword">return</span> (n < <span class="hljs-number">2</span>) ? n : fibonacci(n-<span class="hljs-number">1</span>) + fibonacci(n-<span class="hljs-number">2</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然这个算法缓慢的令人绝望，因为做了非常多的冗余计算，这个时候memoization就可以派上用场了！</p>
<p>简单来说，memoization 是一个过程，它允许我们缓存递归/昂贵的函数调用的值，以便下次使用相同的参数调用函数时，返回缓存的值而不必重新计算函数。</p>
<p>这确保了我们的应用程序运行得更快，因为我们通过返回一个已经存储在内存中的值来避免重新执行函数需要的时间。</p>
<h1 data-id="heading-1">为什么在 React 中使用 memoization？</h1>
<p>在 React 函数组件中，当组件中的 props 发生变化时，默认情况下整个组件都会重新渲染。 换句话说，如果组件中的任何值更新，整个组件将重新渲染，包括尚未更改其 values/props 的函数/组件。</p>
<p>让我们看一个发生这种情况的简单示例。 我们将构建一个基本的应用程序，告诉用户哪种酒最适合与它们选择的奶酪搭配。</p>
<p>我们将从设置两个组件开始。 第一个组件将允许用户选择奶酪。 然后它会显示最适合该奶酪的酒的名称。 第二个组件将是第一个组件的子组件。 在这个组件中，没有任何变化。 我们将使用这个组件来跟踪 React 重新渲染的次数。</p>
<blockquote>
<p>注意，本示例中使用的 <code>classNames</code> 来自 Tailwind CSS。</p>
</blockquote>
<p>下面是我们的父组件：<code><ParentComponent /></code>。</p>
<pre><code class="copyable">// components/parent-component.js
import Counts from "./counts";
import Button from "./button";
import &#123; useState, useEffect &#125; from "react";
import constants from "../utils";
const &#123; MOZARELLA, CHEDDAR, PARMESAN, CABERNET, CHARDONAY, MERLOT &#125; = constants;

export default function ParentComponent() &#123;
  const [cheeseType, setCheeseType] = useState("");
  const [wine, setWine] = useState("");
  const whichWineGoesBest = () => &#123;
    switch (cheeseType) &#123;
      case MOZARELLA:
        return setWine(CABERNET);
      case CHEDDAR:
        return setWine(CHARDONAY);
      case PARMESAN:
        return setWine(MERLOT);
      default:
        CHARDONAY;
    &#125;
  &#125;;
  useEffect(() => &#123;
    let mounted = true;
    if (mounted) &#123;
      whichWineGoesBest();
    &#125;
    return () => (mounted = false);
  &#125;, [cheeseType]);

  return (
    <div className="flex flex-col justify-center items-center">
        <h3 className="text-center dark:text-gray-400 mt-10">
          Without React.memo() or useMemo()
        </h3>
      <h1 className="font-semibold text-2xl dark:text-white max-w-md text-center">
        Select a cheese and we will tell you which wine goes best!
      </h1>
      <div className="flex flex-col gap-4 mt-10">
        <Button text=&#123;MOZARELLA&#125; onClick=&#123;() => setCheeseType(MOZARELLA)&#125; />
        <Button text=&#123;CHEDDAR&#125; onClick=&#123;() => setCheeseType(CHEDDAR)&#125; />
        <Button text=&#123;PARMESAN&#125; onClick=&#123;() => setCheeseType(PARMESAN)&#125; />
      </div>
      &#123;cheeseType && (
        <p className="mt-5 dark:text-green-400 font-semibold">
          For &#123;cheeseType&#125;, <span className="dark:text-yellow-500">&#123;wine&#125;</span>&#123;" "&#125;
          goes best.
        </p>
      )&#125;
      <Counts />
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个组件是 <code><Counts /></code> 组件，它跟踪整个 <code><Parent Component /></code> 组件重新渲染的次数。</p>
<pre><code class="copyable">// components/counts.js
import &#123; useRef &#125; from "react";
export default function Counts() &#123;
  const renderCount = useRef(0);
  return (
    <div className="mt-3">
      <p className="dark:text-white">
        Nothing has changed here but I've now rendered:&#123;" "&#125;
        <span className="dark:text-green-300 text-grey-900">
          &#123;(renderCount.current++)&#125; time(s)
        </span>
      </p>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面的例子是我们点击奶酪名字时的效果:</p>
<p><code><ParentComponent /></code> 中的 <code><Counts /></code> 组件计算了因 <code><ParentComponent /></code> 的更改而强制 <code><Counts /></code> 组件重新渲染的次数。</p>
<p>目前，单击奶酪名字将更新显示下面的奶酪名字以及酒名。 除了 <code><ParentComponent /></code> 会重新渲染，<code><Counts /></code> 组件也会重新渲染，即使其中的任何内容都没有改变。</p>
<p>想象一下，有一个组件显示数以千计的数据，每次用户单击一个按钮时，该组件或树中的每条数据都会在不需要更新时重新渲染。 这就是 <code>React.memo()</code> 或 <code>useMemo()</code> 为我们提供性能优化所必需的地方。</p>
<p>现在，让我们探索 <code>React.memo</code> 以及 <code>useMemo()</code>。 之后我们将比较它们之间的差异，并了解何时应该使用一种而不是另一种。</p>
<h1 data-id="heading-2">什么是 React.memo()？</h1>
<p><code>React.memo()</code> 随 <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fblog%2F2018%2F10%2F23%2Freact-v-16-6.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/blog/2018/10/23/react-v-16-6.html" ref="nofollow noopener noreferrer">React v16.6</a> 一起发布。 虽然类组件已经允许您使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Freact-api.html%23reactpurecomponent" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/react-api.html#reactpurecomponent" ref="nofollow noopener noreferrer">PureComponent</a> 或 <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Freact-component.html%23shouldcomponentupdate" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/react-component.html#shouldcomponentupdate" ref="nofollow noopener noreferrer">shouldComponentUpdate</a> 来控制重新渲染，但 React 16.6 引入了对函数组件执行相同操作的能力。</p>
<p><code>React.memo()</code> 是一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Fhigher-order-components.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/higher-order-components.html" ref="nofollow noopener noreferrer">高阶组件 (HOC)</a>，它接收一个组件A作为参数并返回一个组件B，如果组件B的 props（或其中的值）没有改变，则组件 B 会阻止组件 A 重新渲染 。</p>
<p>我们将采用上面相同的示例，但在我们的 <code><Counts /></code> 组件中使用 <code>React.memo()</code>。 我们需要做的就是用 <code>React.memo()</code> 包裹我们的 <code><Counts /> </code>组件，如下所示：</p>
<pre><code class="copyable">import &#123; useRef &#125; from "react";
function Counts() &#123;
  const renderCount = useRef(0);
  return (
    <div className="mt-3">
      <p className="dark:text-white">
        Nothing has changed here but I've now rendered:&#123;" "&#125;
        <span className="dark:text-green-300 text-grey-900">
          &#123;(renderCount.current ++)&#125; time(s)
      </span>
      </p>
    </div>
  );
&#125;
export default React.memo(Counts);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，当我们通过单击选择奶酪类型时，我们的 <code><Counts /></code> 组件将不会重新渲染。</p>
<h1 data-id="heading-3">什么是 useMemo()？</h1>
<p><code>React.memo()</code> 是一个 HOC，而 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Freact-reference-guide-hooks-api%2F%23usememo" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/react-reference-guide-hooks-api/#usememo" ref="nofollow noopener noreferrer">useMemo()</a> 是一个 React Hook。 使用 <code>useMemo()</code>，我们可以返回记忆值来避免函数的依赖项没有改变的情况下重新渲染。</p>
<p>为了在我们的代码中使用 <code>useMemo()</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Frethinking-hooks-memoization%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/rethinking-hooks-memoization/" ref="nofollow noopener noreferrer">React 开发者有一些建议给我们</a>：</p>
<ul>
<li>您可以依赖 <code>useMemo()</code> 作为性能优化，而不是语义保证</li>
<li>函数内部引用的每个值也应该出现在依赖项数组中</li>
</ul>
<p>对于我们的下一个示例，我们将对 <code><ParentComponent /></code> 进行一些更改。 下面的代码仅显示对我们之前创建的 <code><ParentComponent /></code> 的新更改。</p>
<pre><code class="copyable">// components/parent-component.js
.
.
import &#123; useState, useEffect, useRef, useMemo &#125; from "react";
import UseMemoCounts from "./use-memo-counts";

export default function ParentComponent() &#123;
  .
  .
  const [times, setTimes] = useState(0);
  const useMemoRef = useRef(0);

  const incrementUseMemoRef = () => useMemoRef.current++;

  // uncomment the next line to test that <UseMemoCounts /> will re-render every t ime the parent re-renders.
  // const memoizedValue = useMemoRef.current++;

// the next line ensures that <UseMemoCounts /> only renders when the times value changes
const memoizedValue = useMemo(() => incrementUseMemoRef(), [times]);

  .
  .

  return (
    <div className="flex flex-col justify-center items-center border-2 rounded-md mt-5 dark:border-yellow-200 max-w-lg m-auto pb-10 bg-gray-900">
      .
      .
        <div className="mt-4 text-center">
          <button
            className="bg-indigo-200 py-2 px-10 rounded-md"
            onClick=&#123;() => setTimes(times+1)&#125;
          >
            Force render
          </button>

          <UseMemoCounts memoizedValue=&#123;memoizedValue&#125; />
        </div>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，我们引入了非常重要的 <code>useMemo()</code> Hook。 我们还引入了 <code>useRef()</code> Hook 来帮助我们跟踪在我们的组件中发生了多少次重新渲染。 接下来，我们声明一个 <code>times</code> 状态，稍后我们将更新该状态来触发/强制重新渲染。</p>
<p>之后，我们声明一个 <code>memoizedValue</code> 变量，用于存储 <code>useMemo()</code> Hook 的返回值。<code> useMemo()</code> Hook 调用我们的 <code>incrementUseMemoRef</code> 函数，它会在每次依赖项发生变化时将我们的 <code>useMemoRef.current</code> 值加一，即 <code>times</code> 值发生变化。</p>
<p>然后我们创建一个按钮来点击更新<code>times</code>的值。 单击此按钮将触发我们的 <code>useMemo()</code> Hook，更新 <code>memoizedValue</code> 的值，并重新渲染我们的 <code><UseMemoCounts /></code> 组件。</p>
<p>在这个例子中，我们还将 <code><Counts /></code> 组件重命名为 <code><UseMemoCounts /></code>，它现在需要一个 <code>memoizedValue</code> 属性。</p>
<p>这是它的样子：</p>
<pre><code class="copyable">// components/use-memo-counts.js

function UseMemoCounts(&#123;memoizedValue&#125;) &#123;
  return (
    <div className="mt-3">
      <p className="dark:text-white max-w-md">
        I'll only re-render when you click <span className="font-bold text-indigo-400">Force render.</span> 
        </p>
      <p className="dark:text-white">I've now rendered: <span className="text-green-400">&#123;memoizedValue&#125; time(s)</span> </p>
    </div>
  );
&#125;
export default UseMemoCounts;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，当我们单击任何奶酪按钮时，我们的 <code>memoizedValue</code> 不会更新。 但是当我们单击 <strong>Force render</strong> 按钮时，我们看到 <code>memoizedValue</code> 更新并且 <code><UseMemoCounts /></code> 组件重新渲染。</p>
<p>如果您注释掉我们当前的 <code>memoizedValue</code> 行，并取消注释掉它上面的行：</p>
<pre><code class="copyable">const memoizedValue = useMemoRef.current++;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>您将看到 <code><UseMemoCounts /></code> 组件在每次 <code><ParentComponent /></code> 渲染时重新渲染。</p>
<h1 data-id="heading-4">总结：React.memo() 和 useMemo() 的主要区别</h1>
<p>从上面的例子中，我们可以看到 <code>React.memo()</code> 和 <code>useMemo()</code> 之间的主要区别：</p>
<ul>
<li><code>React.memo()</code> 是一个高阶组件，我们可以使用它来包装我们不想重新渲染的组件，除非其中的 props 发生变化</li>
<li><code>useMemo()</code> 是一个 React Hook，我们可以使用它在组件中包装函数。 我们可以使用它来确保该函数中的值仅在其依赖项之一发生变化时才重新计算</li>
</ul>
<p>虽然 memoization 似乎是一个可以随处使用的巧妙小技巧，但只有在绝对需要这些性能提升时才应该使用它。 Memoization 会占用运行它的机器上的内存空间，因此可能会导致意想不到的效果。</p></div>  
</div>
            