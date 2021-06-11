
---
title: '什么是react hooks'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9384'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 19:17:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=9384'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与更文挑战的第11天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>Hooks的许多卖点之一是避免了类和高阶组件的复杂性。然而有些人觉得Hooks可能会导致另外的问题。虽然不需要再担心绑定上下文，现在我们需要担心闭包。</p>
<p>闭包是JS里的基本概念。众所周知对许多初学的开发者来说它们令人费解。Kyle Simpson在《你不知道的JS》中对闭包的著名定义如下：</p>
<p>闭包是：当一个函数在它的词法作用域之外执行的时候，仍然可以记得它的词法作用域且可以访问该作用域。</p>
<p>闭包很显然和词法作用域的概念紧密相关，在MDN是这么描述词法作用域的：“当函数被嵌套时，解析器解析函数的变量名的方式”。让我们来看一个实际的例子，可以更好的说明这一点：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Example 0    </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useState</span>(<span class="hljs-params">initialValue</span>) </span>&#123;   
    <span class="hljs-keyword">var</span> _val = initialValue <span class="hljs-comment">//_val是useState创建的局部变量  </span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">state</span>(<span class="hljs-params"></span>) </span>&#123;  
      <span class="hljs-comment">// state 是一个内部函数, 也是一个闭包  </span>
      <span class="hljs-keyword">return</span> _val <span class="hljs-comment">// state() 使用了_val, 该变量由父函数声明 </span>
    &#125;   
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setState</span>(<span class="hljs-params">newVal</span>) </span>&#123; 
      <span class="hljs-comment">// 同样是内部函数    </span>
      _val = newVal <span class="hljs-comment">// 给_val赋值，而不用暴露_val    </span>
    &#125;   
    <span class="hljs-keyword">return</span> [state, setState] <span class="hljs-comment">//将这两个函数暴露到外部  </span>
  &#125; 
  <span class="hljs-keyword">var</span> [foo, setFoo] = useState(<span class="hljs-number">0</span>) <span class="hljs-comment">// 使用了数组解构方法  </span>
  <span class="hljs-built_in">console</span>.log(foo()) <span class="hljs-comment">// logs 0 - 我们给的初始值    </span>
  setFoo(<span class="hljs-number">1</span>) <span class="hljs-comment">// 在useState的作用域内给_val赋值    </span>
  <span class="hljs-built_in">console</span>.log(foo()) <span class="hljs-comment">// logs 1 - 尽管使用了相同的函数调用，得到的是新的初始值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，我们建立了React的 useState hook的原始版本。这里有2个内部函数，state和setState。state返回了上面定义的局部变量_val，setState将传给它的参数（即newVal）赋给该局部变量。</p>
<p>我们的state用getter函数实现，这并不完美，但我们将对此进行改进。这里重要的是，使用foo和setFoo，我们可以访问和操作（即所谓的“封闭”）内部变量_val。这两个函数保留了useState作用域的访问权，而这样的引用被称为闭包。放在在React和其他框架的上下文中，这看起来好像状态，实际上正是如此。</p>
<h3 data-id="heading-0">在函数式组件中的使用</h3>
<p>让我们来把刚做出的useState功能应用到常见的程序中。下面来做一个计数器组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/// Example 1   </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;    
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>) <span class="hljs-comment">// 和上面定义的 useState 相同 </span>
    <span class="hljs-keyword">return</span> &#123;    
      <span class="hljs-attr">click</span>: <span class="hljs-function">() =></span> setCount(count() + <span class="hljs-number">1</span>),   
      <span class="hljs-attr">render</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'render:'</span>, &#123; <span class="hljs-attr">count</span>: count() &#125;)  
    &#125;   
  &#125; 
  <span class="hljs-keyword">const</span> C = Counter()   
  C.render() <span class="hljs-comment">// render: &#123; count: 0 &#125;    </span>
  C.click() 
  C.render() <span class="hljs-comment">// render: &#123; count: 1 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们没有把数据渲染到DOM上，而是仅在控制台输出这些状态。我们让计数器提供一个外部API，这样我们可以直接运行脚本，而不必给它设置click事件处理函数。</p>
<p>虽然这种做法也可以工作起来，调用getter函数来访问状态并不是React.useState hook的实际做法。我们来改进它。</p>
<h3 data-id="heading-1">不能更新状态的闭包实现</h3>
<p>如果我们想要做得和实际的React hook一样，状态就应该是一个变量，而不是函数。如果我们简单的将_val暴露出去，而不是将它包裹在函数里面，就会出现bug</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Example 0, 再来看第一个例子 - 这么做是有bug的! </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useState</span>(<span class="hljs-params">initialValue</span>) </span>&#123;   
    <span class="hljs-keyword">var</span> _val = initialValue 
    <span class="hljs-comment">// 不使用state()函数 </span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setState</span>(<span class="hljs-params">newVal</span>) </span>&#123; 
      _val = newVal 
    &#125;   
    <span class="hljs-keyword">return</span> [_val, setState] <span class="hljs-comment">// 直接对外暴露_val   </span>
  &#125; 
  <span class="hljs-keyword">var</span> [foo, setFoo] = useState(<span class="hljs-number">0</span>)   
  <span class="hljs-built_in">console</span>.log(foo) <span class="hljs-comment">// logs 0 不需要进行函数调用  </span>
  setFoo(<span class="hljs-number">1</span>) <span class="hljs-comment">// 在useState作用域内给_val赋值 </span>
  <span class="hljs-built_in">console</span>.log(foo) <span class="hljs-comment">// logs 0 - 糟糕!!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是种闭包不能更新的问题。当我们从useState的输出中解构出foo变量时，foo的值等于对useState初始调用时的_val值，之后就不会再变了！这不是我们想要的结果，通常我们需要让组件的状态能反映出当前的状态，而且状态应该是一个变量而不是一个函数！这两个目标看起来不可兼得。</p>
<h3 data-id="heading-2">模块模式的闭包实现</h3>
<p>我们可以解决这一useState难题……通过将闭包放进另一个闭包中！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Example 2    </span>
<span class="hljs-keyword">const</span> MyReact = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;   
    <span class="hljs-keyword">let</span> _val <span class="hljs-comment">// 将我们的状态保持在模块作用域中 </span>
    <span class="hljs-keyword">return</span> &#123;    
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">Component</span>)</span> &#123;   
        <span class="hljs-keyword">const</span> Comp = Component()    
        Comp.render()   
        <span class="hljs-keyword">return</span> Comp 
      &#125;,    
      <span class="hljs-function"><span class="hljs-title">useState</span>(<span class="hljs-params">initialValue</span>)</span> &#123;  
        _val = _val || initialValue <span class="hljs-comment">// 每次运行都重新赋值    </span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setState</span>(<span class="hljs-params">newVal</span>) </span>&#123; 
          _val = newVal 
        &#125;   
        <span class="hljs-keyword">return</span> [_val, setState] 
      &#125; 
    &#125;   
  &#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们选择使用模块模式来制作我们的微型React hook。像React一样，它可以记录组件的状态（在这个例子中，它只能给每个组件记录一个状态，将状态记录在val中）。该设计允许MyReact渲染你的函数式组件，它可以在每次组件更新时使用和它相应的闭包，对内部的val赋值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 续Example 2   </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;    
    <span class="hljs-keyword">const</span> [count, setCount] = MyReact.useState(<span class="hljs-number">0</span>)   
    <span class="hljs-keyword">return</span> &#123;    
      <span class="hljs-attr">click</span>: <span class="hljs-function">() =></span> setCount(count + <span class="hljs-number">1</span>), 
      <span class="hljs-attr">render</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'render:'</span>, &#123; count &#125;)   
    &#125;   
  &#125; 
  <span class="hljs-keyword">let</span> App   
  App = MyReact.render(Counter) <span class="hljs-comment">// render: &#123; count: 0 &#125; </span>
  App.click()   
  App = MyReact.render(Counter) <span class="hljs-comment">// render: &#123; count: 1 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在看起来更像React里的Hooks了。</p>
<p>复制useEffect功能
目前为止，我们已经实现了useState，这是最基本的React Hook。下一个重要的Hook是useEffect。不像setState，useEffect是异步执行的，这意味着更容易遇到闭包问题。</p>
<p>我们可以扩展这个微型React模型，加入下面代码：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// Example 3    </span>
<span class="hljs-keyword">const</span> MyReact = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;   
    <span class="hljs-keyword">let</span> _val, _deps <span class="hljs-comment">// 在作用域内保持状态和依赖 </span>
    <span class="hljs-keyword">return</span> &#123;    
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">Component</span>)</span> &#123;   
        <span class="hljs-keyword">const</span> Comp = Component()    
        Comp.render()   
        <span class="hljs-keyword">return</span> Comp 
      &#125;,    
      <span class="hljs-function"><span class="hljs-title">useEffect</span>(<span class="hljs-params">callback, depArray</span>)</span> &#123;   
        <span class="hljs-keyword">const</span> hasNoDeps = !depArray 
        <span class="hljs-keyword">const</span> hasChangedDeps = _deps ? !depArray.every(<span class="hljs-function">(<span class="hljs-params">el, i</span>) =></span> el === _deps[i]) : <span class="hljs-literal">true</span>   
        <span class="hljs-keyword">if</span> (hasNoDeps || hasChangedDeps) &#123;  
          callback()    
          _deps = depArray  
        &#125;   
      &#125;,    
      <span class="hljs-function"><span class="hljs-title">useState</span>(<span class="hljs-params">initialValue</span>)</span> &#123;  
        _val = _val || initialValue 
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setState</span>(<span class="hljs-params">newVal</span>) </span>&#123; 
          _val = newVal 
        &#125;   
        <span class="hljs-keyword">return</span> [_val, setState] 
      &#125; 
    &#125;   
  &#125;)()  
  <span class="hljs-comment">// 使用方法   </span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;  
    <span class="hljs-keyword">const</span> [count, setCount] = MyReact.useState(<span class="hljs-number">0</span>)   
    MyReact.useEffect(<span class="hljs-function">() =></span> &#123;   
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'effect'</span>, count)  
    &#125;, [count]) 
    <span class="hljs-keyword">return</span> &#123;    
      <span class="hljs-attr">click</span>: <span class="hljs-function">() =></span> setCount(count + <span class="hljs-number">1</span>), 
      <span class="hljs-attr">noop</span>: <span class="hljs-function">() =></span> setCount(count),  
      <span class="hljs-attr">render</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'render'</span>, &#123; count &#125;)    
    &#125;   
  &#125; 
  <span class="hljs-keyword">let</span> App   
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// effect 0   </span>
  <span class="hljs-comment">// render &#123;count: 0&#125;  </span>
  App.click()   
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// effect 1   </span>
  <span class="hljs-comment">// render &#123;count: 1&#125;  </span>
  App.noop()    
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// // no effect run   </span>
  <span class="hljs-comment">// render &#123;count: 1&#125;  </span>
  App.click()   
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// effect 2   </span>
  <span class="hljs-comment">// render &#123;count: 2&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了追踪依赖项（因为useEffect只有在依赖项发生变化才会重新运行callback），我们引入了另一个变量_deps。</p>
<h3 data-id="heading-3">没有魔法，只是数组而已</h3>
<p>我们已经很好的复制了useState和useEffect的功能，但是它们是实现得很差的单态（只允许一个状态，一个副作用，多了就会有bug）。为了让事情变得更有意思，我们需要扩展它使之可以接受任意数量的状态和副作用。幸运的是，正如Rudi Yardley所写的，React Hooks不是什么魔法，仅仅是数组而已。因此我们会使用到一个hooks数组。我们把val和deps全都放在同一个数组中，因为它们是互不干扰的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Example 4    </span>
<span class="hljs-keyword">const</span> MyReact = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;   
    <span class="hljs-keyword">let</span> hooks = [], 
      currentHook = <span class="hljs-number">0</span> <span class="hljs-comment">// hooks数组, 和一个iterator!  </span>
    <span class="hljs-keyword">return</span> &#123;    
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">Component</span>)</span> &#123;   
        <span class="hljs-keyword">const</span> Comp = Component() <span class="hljs-comment">// 运行 effects  </span>
        Comp.render()   
        currentHook = <span class="hljs-number">0</span> <span class="hljs-comment">// 复位，为下一次render做准备 </span>
        <span class="hljs-keyword">return</span> Comp 
      &#125;,    
      <span class="hljs-function"><span class="hljs-title">useEffect</span>(<span class="hljs-params">callback, depArray</span>)</span> &#123;   
        <span class="hljs-keyword">const</span> hasNoDeps = !depArray 
        <span class="hljs-keyword">const</span> deps = hooks[currentHook] <span class="hljs-comment">// type: array | undefined  </span>
        <span class="hljs-keyword">const</span> hasChangedDeps = deps ? !depArray.every(<span class="hljs-function">(<span class="hljs-params">el, i</span>) =></span> el === deps[i]) : <span class="hljs-literal">true</span> 
        <span class="hljs-keyword">if</span> (hasNoDeps || hasChangedDeps) &#123;  
          callback()    
          hooks[currentHook] = depArray 
        &#125;   
        currentHook++ <span class="hljs-comment">// 本hook运行结束  </span>
      &#125;,    
      <span class="hljs-function"><span class="hljs-title">useState</span>(<span class="hljs-params">initialValue</span>)</span> &#123;  
        hooks[currentHook] = hooks[currentHook] || initialValue <span class="hljs-comment">// type: any    </span>
        <span class="hljs-keyword">const</span> setStateHookIndex = currentHook <span class="hljs-comment">// 给setState的闭包准备的变量! </span>
        <span class="hljs-keyword">const</span> setState = <span class="hljs-function"><span class="hljs-params">newState</span> =></span> (hooks[setStateHookIndex] = newState)  
        <span class="hljs-keyword">return</span> [hooks[currentHook++], setState] 
      &#125; 
    &#125;   
  &#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Example 4 续 - 使用hook </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;    
    <span class="hljs-keyword">const</span> [count, setCount] = MyReact.useState(<span class="hljs-number">0</span>)   
    <span class="hljs-keyword">const</span> [text, setText] = MyReact.useState(<span class="hljs-string">'foo'</span>) <span class="hljs-comment">// 第二个 state hook!  </span>
    MyReact.useEffect(<span class="hljs-function">() =></span> &#123;   
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'effect'</span>, count, text)    
    &#125;, [count, text])   
    <span class="hljs-keyword">return</span> &#123;    
      <span class="hljs-attr">click</span>: <span class="hljs-function">() =></span> setCount(count + <span class="hljs-number">1</span>), 
      <span class="hljs-attr">type</span>: <span class="hljs-function"><span class="hljs-params">txt</span> =></span> setText(txt),    
      <span class="hljs-attr">noop</span>: <span class="hljs-function">() =></span> setCount(count),  
      <span class="hljs-attr">render</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'render'</span>, &#123; count, text &#125;)  
    &#125;   
  &#125; 
  <span class="hljs-keyword">let</span> App   
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// effect 0 foo   </span>
  <span class="hljs-comment">// render &#123;count: 0, text: 'foo'&#125; </span>
  App.click()   
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// effect 1 foo   </span>
  <span class="hljs-comment">// render &#123;count: 1, text: 'foo'&#125; </span>
  App.type(<span class="hljs-string">'bar'</span>)   
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// effect 1 bar   </span>
  <span class="hljs-comment">// render &#123;count: 1, text: 'bar'&#125; </span>
  App.noop()    
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// // no effect run   </span>
  <span class="hljs-comment">// render &#123;count: 1, text: 'bar'&#125; </span>
  App.click()   
  App = MyReact.render(Counter) 
  <span class="hljs-comment">// effect 2 bar   </span>
  <span class="hljs-comment">// render &#123;count: 2, text: 'bar'&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以基本的思路是使用数组存放hook的状态和依赖，调用每个hook只需增加索引号操作相应的数组项，当组件render完毕后复位索引。</p>
<p>还可以很容易的实现自定义hooks：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// Example 4, revisited </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Component</span>(<span class="hljs-params"></span>) </span>&#123;  
    <span class="hljs-keyword">const</span> [text, setText] = useSplitURL(<span class="hljs-string">'www.netlify.com'</span>)  
    <span class="hljs-keyword">return</span> &#123;    
      <span class="hljs-attr">type</span>: <span class="hljs-function"><span class="hljs-params">txt</span> =></span> setText(txt),    
      <span class="hljs-attr">render</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(&#123; text &#125;)   
    &#125;   
  &#125; 
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useSplitURL</span>(<span class="hljs-params">str</span>) </span>&#123;   
    <span class="hljs-keyword">const</span> [text, setText] = MyReact.useState(str)   
    <span class="hljs-keyword">const</span> masked = text.split(<span class="hljs-string">'.'</span>)  
    <span class="hljs-keyword">return</span> [masked, setText]    
  &#125; 
  <span class="hljs-keyword">let</span> App   
  App = MyReact.render(Component)   
  <span class="hljs-comment">// &#123; text: [ 'www', 'netlify', 'com' ] &#125;  </span>
  App.type(<span class="hljs-string">'www.reactjs.org'</span>)   
  App = MyReact.render(Component)   
  <span class="hljs-comment">// &#123; text: [ 'www', 'reactjs', 'org' ] &#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是hooks的实际原理，自定义hooks只需简单的利用框架提供的原语，不管是React里的还是我们这里制作的微型hook版本都是如此。</p>
<h3 data-id="heading-4">使用hook的法则</h3>
<p>现在你可以很容易理解使用Hooks的第一个法则：只在最顶层调用Hooks。因为我们使用currentHook变量，需要根据调用次序对React的依赖建模。你可以对照着我们的代码实现，去阅读Hooks法则的解释，就可以完全理解所有内容。</p>
<p>第二条法则，“仅在React函数中调用Hooks”。使用我们这一实现方法，这条法则不是必须遵守的，但是明确的界定代码的哪一部分依赖于有状态的逻辑是相当好的实践方式。（这也可以让我们更容易编写工具来确保遵守第一个法则。你不会在无意中包裹有状态的函数，在循环和条件语句中当成一般的函数包裹它们。遵守第二条法则有助于遵守第一条法则）</p>
<h3 data-id="heading-5">结论</h3>
<p>到这里，我们已经把最初的例子扩展的很远了。你可以尝试使用一行代码实现useRef，或者让render函数接受JSX并挂载到DOM上，或者实现无数种其他重要的细节，在这28行的hook版本里我们忽略掉了。希望现在你已经收获一些在上下文中使用闭包的经验，并且在头脑中有一个有用的模型，可以解释React Hooks是如何工作的。</p></div>  
</div>
            