
---
title: '_React Hooks长文总结系列一_初出茅庐，状态与副作用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1909'
author: 掘金
comments: false
date: Mon, 29 Mar 2021 19:10:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=1909'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">写在开头</h2>
<p><code>React Hooks</code>在我的上一个项目中得到了充分的使用，对于这个项目来说，我们跳过传统的类组件直接过渡到函数组件，确实是一个不小的挑战。在项目开发过程中也发现项目中的其他小伙伴（包括我自己）有时候会存在使用不当的情况，因此对官方的几个钩子函数做一个较为全面的总结。</p>
<h2 data-id="heading-1">函数式组件出现的原因</h2>
<p>为什么会出现函数式组件，因为传统的类组件确实有不少缺点：</p>
<ul>
<li>类组件中的 <code>this</code> 指向有点绕</li>
<li>通过选项去组织代码，在组件比较大的时候会很痛苦，因为类组件天生分离，不符合内聚性原则</li>
<li>组件复用不方便，尤其是 <code>mixin</code>，很容易带来数据来源指向不清楚的问题</li>
</ul>
<h2 data-id="heading-2">函数式组件居然“有状态了”</h2>
<p>我们知道，在过去，函数式组件被称作“傻瓜组件”，因为它并不具有自身的状态，通常被用来做一些渲染视图的工作，即<code>UI = render(props)</code>。这是一个纯粹的输入输出模型，无任何副作用。但是<code>React Hooks</code>的出现，让函数式组件拥有自身的状态成为了可能。</p>
<p>函数式组件在运行过程中会被调用很多次，假如我们将状态保存在函数体里面，毫无疑问是不可行的。因为函数是一种“用完即销毁”的东西。</p>
<p>这正是是<code>Hooks</code>所做的事情：<strong>将一个函数组件的状态保存在函数外面</strong>。准确来说，是这个函数组件对应的<code>Hooks</code>链表。当函数式组件需要用到该状态的时候，通过<code>Hooks</code>这一钩子将状态从函数体外部“钩进来”。</p>
<h2 data-id="heading-3">函数式组件其实也有“生命周期”</h2>
<p>函数式组件的生命周期可以分为以下三部分：</p>
<p>初次渲染（<code>first-render</code>） ---> 重渲染 (<code>re-render</code>) ---> 销毁（<code>destroy</code>）</p>
<p>当我们第一次使用函数式组件的时候，会触发初次渲染（<code>first-render</code>）；若其 props 改变，就会调用该 render 函数，触发重渲染(<code>re-render</code>)。</p>
<p>每一次的渲染，都是独立的。这正是函数式组件的美妙之处。</p>
<p>那么react如何决定要不要调用 <code>render</code> 函数来更新 UI 视图呢？这取决于<code>data</code>有没有更新。从整个组件树来看，<code>data</code>指的是整个组件的<code>state</code>；从具体到某个功能组件来看，<code>data</code>也可以被认为是<code>props</code>和自身<code>state</code>的结合体。</p>
<p><code>render</code> 的执行取决于 <code>data</code> 变化，而 <code>data</code> 中的 <code>state</code> 数据是保存在链表中的。</p>
<blockquote>
<p>链表的特性是啥？就是每个元素都有一个<code>next</code>指针指向下一个元素，一环扣一环关联起来。所以为什么 hooks 不能用在条件判断/循环/嵌套中，因为这些都不能保证每次渲染时读取 hooks 链表的顺序是完全一致的。尤其对于状态读取来说，读取顺序和初次渲染链表记录的顺序不一致，会直接导致一些 <code>useState</code> 钩子读取到错误的状态值。</p>
</blockquote>
<h2 data-id="heading-4">useSate，状态保存之处</h2>
<h3 data-id="heading-5">用法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">原理</h3>
<p>首先，<code>useState</code> 会生成一个状态和修改状态的函数。这个状态会保存在函数式组件外面，每次重渲染时，这一次渲染都会去外面把这个状态钩回来，读取成常量并写进该次渲染中。</p>
<p>通过调用修改状态的函数，会触发重渲染。到这里我们总结：<code>props</code> 的改变和 <code>setState</code> 的调用，都会触发 <code>re-render</code>。</p>
<p>由于每次渲染都是独立的，所以每次渲染都会读到一个独立的状态值，这个状态值，就是通过钩子钩到的 <code>state</code> 并读取到的常量。</p>
<p>这就是所谓的<code>capture value</code>特性，每次的渲染都是独立的，每次渲染的状态其实都只是常量罢了。</p>
<h3 data-id="heading-7">深入本质</h3>
<p>让我们看深入一下本质，看看 <code>useState</code> 和 <code>re-render</code> 到底如何关联起来：</p>
<ol>
<li>函数式组件初次渲染，一个个的 <code>useState</code> 依次执行，生成hooks链表，里面记录了每个 <code>state</code> 的初始值和对应的 <code>setter</code> 函数</li>
<li>这个链表会挂在这个函数式组件的外面，可以被 <code>useState</code> 或相应 <code>setter</code> 访问</li>
<li>当某个时刻调用了 <code>setSetter</code>，将会直接改变这个hooks链表</li>
<li>hooks链表其实就是这个函数式组件的状态表，它的改变等效于状态改变，会引起函数式组件重渲染</li>
<li>这个函数式组件重渲染，执行到 <code>useState</code> 时，因为初次执行已经挂载过一个 hooks 链表了，这个时候就会直接读取链表的相应值</li>
</ol>
<p>这也就是为什么叫<code>useState</code>，而不是<code>createState</code>。</p>
<h2 data-id="heading-8">useRef，DOM访问与外部状态保存</h2>
<h3 data-id="heading-9">useRef有啥用</h3>
<p>useRef主要有两个作用：</p>
<ul>
<li>用来访问DOM；</li>
<li>用来保存变量到当前函数式组件外部。</li>
</ul>
<h3 data-id="heading-10">访问DOM</h3>
<p>我们先来看看前者怎么用吧：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">const inputRef = useRef(null);

const handleClick = () => &#123;
  inputRef.current?.focus();
&#125;

return (
  <input ref=&#123;inputRef&#125; />
  <button onClick=&#123;handleClick&#125;>点击</button>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以方便地访问DOM节点。</p>
<h3 data-id="heading-11">保存可变值</h3>
<p>前面我们提到，<code>useState</code>可以方便地保存状态值，但是由于函数式组件的<code>capture value</code>特性，使得我们并不能以一种比较方便的形式获取到更改后的状态值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [num, setNum] = useState(<span class="hljs-number">0</span>);

<span class="hljs-keyword">const</span> increaseNum = <span class="hljs-function">() =></span> &#123;
    setNum(<span class="hljs-function"><span class="hljs-params">prev</span> =></span> prev + <span class="hljs-number">1</span>);
    <span class="hljs-built_in">console</span>.log(num); <span class="hljs-comment">// 打印的仍然是旧值，因为num在这一帧被常量化了</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<code>useRef</code>将会创建一个<code>ref</code>对象，并把这个<code>ref</code>对象保存在函数式组件外部，这样的好处在于：</p>
<ol>
<li>独立于<code>capture value</code>之外存储，不用担心获得过时变量的问题；</li>
<li>可以同步修改状态。</li>
</ol>
<p>我们试验如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> numRef = useRef(<span class="hljs-number">0</span>);

<span class="hljs-keyword">const</span> increaseNum = <span class="hljs-function">() =></span> &#123;
    numRef.current += <span class="hljs-number">1</span>;
    <span class="hljs-built_in">console</span>.log(numRef.current); <span class="hljs-comment">// 能获取最新值</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是要注意⚠️：<strong>由于引用没变，上述操作并不会引起函数式组件的重渲染。</strong> 这是一个很容易引起错误的地方！</p>
<h2 data-id="heading-12">useEffect，生命周期与观察者</h2>
<h3 data-id="heading-13">用法及建议</h3>
<p><code>useEffect</code> 的模型十分之简洁，如下：</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(effectFn, deps);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>useEffect 可以模拟旧时代的三个生命周期：<code>componentDidMount</code>、<code>shouldComponentUpdate</code>、<code>componentWillUnmount</code>，相当于三个生命周期合并为一个 api。</p>
<p>所谓<code>shouldComponentUpdate</code>，其实就是去除<code>deps</code>依赖数组，如此一来这个副作用的 <code>effectFn</code> 会在首次渲染之后和每次重渲染之后执行，相当于模拟了 <code>shouldComponentUpdate</code> 这一生命周期，如下：</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// xxx</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而所谓<code>componentDidMount</code>，则是传入一个空数组作为依赖，因为当有 <code>deps</code> 数组时，里面 <code>effectFn</code> 是否执行取决于 <code>deps</code> 数组内的数据是否变化，空数组內无数据，所以对比自然也就无变化，使用如下：</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// xxx</span>
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<code>componentWillUnmount</code>，则是在<code>effectFn</code>中返回一个清除函数，如下：</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 执行副作用</span>
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 清除上面的副作用</span>
    <span class="hljs-comment">// ...</span>
  &#125;;
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外我们应该始终遵循一个原则：<strong>那就是不要对 deps 依赖撒谎</strong>。否则会引发一系列 bug。当然编辑器的 linter 也不会允许我们这样做，这一点非常关键。</p>
<h3 data-id="heading-14">原理</h3>
<p><code>effectFn</code> 就是当依赖变化时执行的副作用函数，这里的副作用，并不是一个贬义词，而是一个中性词。</p>
<p>函数内部与外部发生的任何交互都算副作用，比如打印个日志、开启一个定时器，发一个请求，读取全局变量等等等等。</p>
<p>好，现在这个 <code>effectFn</code> 可以返回一个清理函数<code>cleanUp</code>，用于清除这个副作用。典型的清理函数，如：<code>clearInterval</code>、<code>clearTimeout</code>，如：</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"over"</span>), <span class="hljs-number">1000</span>);
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> clearTimout(timer);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useEffect</code> 其实是每次渲染完成后都会执行，但是 <code>effectFn</code> 是否执行，就要看依赖有没有变化了。执行 <code>useEffect</code> 的时候，会拿这次渲染的依赖跟上次渲染的对应依赖对比，如果没变化，就不执行 <code>effectFn</code>，如果有变化，才执行 <code>effectFn</code>。</p>
<p>如果连依赖都没有，那 react 就认为每次都有变化，每次运行 <code>useEffect</code> 必运行 <code>effectFn</code>。</p>
<p><code>useEffect</code> 有典型的三大特点：</p>
<ul>
<li>会在每次渲染完成后才执行，不会阻塞渲染，从而提高性能</li>
<li>在每次运行 <code>effectFn</code> 之前，要把前一次运行 <code>effectFn</code> 遗留的<code>cleanUp</code>函数执行掉（如果有的话）</li>
<li>在组件销毁时，会把最后一次运行<code>effectFn</code> 遗留的 <code>cleanUp</code> 函数执行掉。</li>
</ul>
<p>deps 数组里面的各个依赖与上次的依赖是否相同，需要通过<code>Object.is</code>来比较，比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.is(<span class="hljs-number">22</span>, <span class="hljs-number">22</span>); <span class="hljs-comment">// true</span>

<span class="hljs-built_in">Object</span>.is([], []); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就会有一个隐患，当 <code>deps</code> 数组里面的子元素为引用类型的时候，每次对比都会是<code>false</code>，从而执行<code>effectFn</code>。因为 <code>Object.is</code> 对比引用类型的时候，比较的是两个指针是否指向堆内存中的同一个地址。</p>
<p><code>useEffect</code> 的执行机制，是在初次渲染时，执行到 <code>useEffect</code> 就将内部的 <code>effectFn</code> 放到两个地方：一个是 <code>hooks</code> 链表中，另外一个则是<code>EffectList</code> 队列中。在渲染完成后，会依次执行 <code>EffectList</code> 里面的 <code>effectFn</code> 集合。</p>
<p>所以，说白了，要不要 <code>re-render</code>，完全取决于链表里面的东西有没有变化。</p>
<h3 data-id="heading-15">细节</h3>
<p>不同于 vue 里面有<code>async mounted</code>，在 <code>useEffect</code> 里面的 <code>effectFn</code>，应该始终坚持一个原则：<strong>要么不返回，要么返回一个 cleanUp 清除函数</strong>。像下面这样写是不行的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 错误的用法❌</span>
useEffect(<span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">"..."</span>);
  <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外我们很容易发现：我们并不需要把 <code>useState</code> 返回的第二个 <code>Setter</code> 函数作为<code>useEffect</code> 的依赖。实际上，React 内部已经对 <code>Setter</code> 函数做了 <code>Memoization</code> 处理，因此每次渲染拿到的 <code>Setter</code> 函数都是完全一样的，不需要把这个<code>Setter</code>函数放到<code>deps</code>数组里面。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            