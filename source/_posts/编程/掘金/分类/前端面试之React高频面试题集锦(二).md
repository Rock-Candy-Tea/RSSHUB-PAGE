
---
title: '前端面试之React高频面试题集锦(二)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6503'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 16:32:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=6503'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 什么是虚拟DOM？</h1>
<p>虚拟DOM（VDOM）它是真实DOM的内存表示,一种编程概念，一种模式。它会和真实的DOM同步，比如通过ReactDOM这种库，这个同步的过程叫做调和(reconcilation)。</p>
<p>虚拟DOM更多是一种模式，不是一种特定的技术。</p>
<h1 data-id="heading-1">2.React中的类组件和函数组件之间有什么区别？</h1>
<h2 data-id="heading-2">类组件（Class components）</h2>
<ul>
<li>无论是使用函数或是类来声明一个组件，它决不能修改它自己的 props。
<ul>
<li>所有 React 组件都必须是纯函数，并禁止修改其自身 props。</li>
</ul>
</li>
<li>React是单项数据流，父组件改变了属性，那么子组件视图会更新。
<ul>
<li>属性 props是外界传递过来的，状态 state是组件本身的，状态可以在组件中任意修改</li>
<li>组件的属性和状态改变都会更新视图。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-react.js copyable" lang="react.js">class Welcome extends React.Component &#123;
  render() &#123;
    return (
      <h1>Welcome &#123; this.props.name &#125;</h1>
    );
  &#125;
&#125;
ReactDOM.render(<Welcome name='react' />, document.getElementById('root'));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">函数组件（functional component）</h2>
<p>函数组件接收一个单一的 props 对象并返回了一个React元素</p>
<pre><code class="hljs language-react.js copyable" lang="react.js">function Welcome (props) &#123;
  return <h1>Welcome &#123;props.name&#125;</h1>
&#125;
ReactDOM.render(<Welcome name='react' />, document.getElementById('root'));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">区别</h2>
<ul>
<li>语法上</li>
</ul>
<p>两者最明显的不同就是在语法上，函数组件是一个纯函数，它接收一个props对象返回一个react元素。而类组件需要去继承React.Component并且创建render函数返回react元素，这将会要更多的代码，虽然它们实现的效果相同。</p>
<ul>
<li>状态管理</li>
</ul>
<p>因为函数组件是一个纯函数，你不能在组件中使用setState()，这也是为什么把函数组件称作为无状态组件。</p>
<p>如果你需要在你的组件中使用state，你可以选择创建一个类组件或者将state提升到你的父组件中，然后通过props对象传递到子组件。</p>
<ul>
<li>生命周期钩子</li>
</ul>
<p>你不能在函数组件中使用生命周期钩子，原因和不能使用state一样，所有的生命周期钩子都来自于继承的React.Component中。</p>
<p>因此，如果你想使用生命周期钩子，那么需要使用类组件。</p>
<p><strong>注意</strong>：在react16.8版本中添加了hooks，使得我们可以在函数组件中使用useState钩子去管理state，使用useEffect钩子去使用生命周期函数。因此，2、3两点就不是它们的区别点。从这个改版中我们可以看出作者更加看重函数组件，而且react团队曾提及到在react之后的版本将会对函数组件的性能方面进行提升。</p>
<ul>
<li>调用方式</li>
</ul>
<p>如果SayHi是一个函数，React需要调用它：</p>
<pre><code class="hljs language-react.js copyable" lang="react.js">// 你的代码 
function SayHi() &#123; 
    return <p>Hello, React</p> 
&#125; 
// React内部 
const result = SayHi(props) // » <p>Hello, React</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果SayHi是一个类，React需要先用new操作符将其实例化，然后调用刚才生成实例的render方法：</p>
<pre><code class="hljs language-react.js copyable" lang="react.js">// 你的代码 
class SayHi extends React.Component &#123; 
    render() &#123; 
        return <p>Hello, React</p> 
    &#125; 
&#125; 
// React内部 
const instance = new SayHi(props) // » SayHi &#123;&#125; 
const result = instance.render() // » <p>Hello, React</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可想而知，函数组件重新渲染将重新调用组件方法返回新的react元素，类组件重新渲染将new一个新的组件实例，然后调用render类方法返回react元素，这也说明为什么类组件中this是可变的。</p>
<h1 data-id="heading-5">3. 什么是高阶组件？</h1>
<p>高阶组件就是一个函数，且该函数接受一个组件作为参数，并返回一个新的组件。基本上，这是从React的组成性质派生的一种模式，我们称它们为“纯”组件， 因为它们可以接受任何动态提供的子组件，但它们不会修改或复制其输入组件的任何行为。</p>
<pre><code class="hljs language-react.js copyable" lang="react.js">const EnhancedComponent = higherOrderComponent(WrappedComponent);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>高阶组件（HOC）是 React 中用于复用组件逻辑的一种高级技巧</li>
<li>高阶组件的参数为一个组件返回一个新的组件</li>
<li>组件是将 props 转换为 UI，而高阶组件是将组件转换为另一个组件</li>
</ul>
<h1 data-id="heading-6">4. constructor中super与props参数一起使用的目的是什么？</h1>
<p>在调用方法之前，子类构造函数无法使用this引用super()。</p>
<p>在ES6中，在子类的constructor中必须先调用super才能引用this。</p>
<p>在constructor中可以使用this.props</p>
<ul>
<li>使用props：</li>
</ul>
<pre><code class="hljs language-react.js copyable" lang="react.js">class MyComponent extends React.Component &#123;
    constructor(props) &#123;
        super(props);
        console.log(this.props);  // Prints &#123; name: 'sudheer',age: 30 &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>不使用props：</li>
</ul>
<pre><code class="hljs language-react.js copyable" lang="react.js">class MyComponent extends React.Component &#123;
    constructor(props) &#123;
        super();
        console.log(this.props); // Prints undefined
        // But Props parameter is still available
        console.log(props); // Prints &#123; name: 'sudheer',age: 30 &#125;
    &#125;

    render() &#123;
        // No difference outside constructor
        console.log(this.props) // Prints &#123; name: 'sudheer',age: 30 &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">5. 为什么不能直接使用 this.state 改变数据？</h1>
<p>react中不能直接修改state，因为并不会重新触发render。</p>
<p>以如下方式更新状态，组件不会重新渲染。</p>
<pre><code class="hljs language-react.js copyable" lang="react.js">//Wrong
This.state.message =”Hello world”;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而是需要使用setState()方法，状态改变时，组件通过重新渲染做出响应。</p>
<pre><code class="hljs language-react.js copyable" lang="react.js">//Correct
This.setState(&#123;message: ‘Hello World’&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setState通过一个队列机制来实现 state 更新。当执行 setState 的时候，会将需要更新的 state 合并后放入状态队列，而不会立刻更新 this.state。队列机制可以高效的批量更新 state，如果不通过 setState 而直接修改 this.state，那么该 state 将不会被放入状态队列中，当下次调用 setState 并对状态队列进行合并时，将会忽略之前被直接修改的 state，而造成无法预知的错误。</p>
<h1 data-id="heading-8">6. 使用React Hooks有什么优势？</h1>
<p>hooks 是react 16.8 引入的特性，他允许你在不写class的情况下操作state 和react的其他特性。</p>
<p>React Hooks 要解决的问题是状态共享，是继 render-props 和 higher-order components 之后的第三种状态共享方案，不会产生 JSX 嵌套地狱问题。</p>
<p>这个状态指的是状态逻辑，所以称为状态逻辑复用会更恰当，因为只共享数据处理逻辑，不会共享数据本身。</p>
<h1 data-id="heading-9">7. React Fiber是什么？</h1>
<h2 data-id="heading-10">Fiber 出现的背景</h2>
<p>首先要知道的是，JavaScript 引擎和页面渲染引擎两个线程是互斥的，当其中一个线程执行时，另一个线程只能挂起等待。</p>
<p>在这样的机制下，如果 JavaScript 线程长时间地占用了主线程，那么渲染层面的更新就不得不长时间地等待，界面长时间不更新，会导致页面响应度变差，用户可能会感觉到卡顿。</p>
<p>而这正是 React 15 的 Stack Reconciler 所面临的问题，即是 JavaScript 对主线程的超时占用问题。Stack Reconciler 是一个同步的递归过程，使用的是 JavaScript 引擎自身的函数调用栈，它会一直执行到栈空为止，所以当 React 在渲染组件时，从开始到渲染完成整个过程是一气呵成的。如果渲染的组件比较庞大，js 执行会占据主线程较长时间，会导致页面响应度变差。</p>
<p>而且所有的任务都是按照先后顺序，没有区分优先级，这样就会导致优先级比较高的任务无法被优先执行。</p>
<h2 data-id="heading-11">Fiber 是什么</h2>
<p>Fiber 的中文翻译叫纤程，与进程、线程同为程序执行过程，Fiber 就是比线程还要纤细的一个过程。纤程意在对渲染过程实现进行更加精细的控制。</p>
<p>从架构角度来看，Fiber 是对 React 核心算法（即调和过程）的重写。</p>
<p>从编码角度来看，Fiber 是 React 内部所定义的一种数据结构，它是 Fiber 树结构的节点单位，也就是 React 16 新架构下的"虚拟 DOM"。</p>
<p>一个 fiber 就是一个 JavaScript 对象，Fiber 的数据结构如下：</p>
<pre><code class="copyable">type Fiber = &#123;
  // 用于标记fiber的WorkTag类型，主要表示当前fiber代表的组件类型如FunctionComponent、ClassComponent等
  tag: WorkTag,
  // ReactElement里面的key
  key: null | string,
  // ReactElement.type，调用`createElement`的第一个参数
  elementType: any,
  // The resolved function/class/ associated with this fiber.
  // 表示当前代表的节点类型
  type: any,
  // 表示当前FiberNode对应的element组件实例
  stateNode: any,

  // 指向他在Fiber节点树中的`parent`，用来在处理完这个节点之后向上返回
  return: Fiber | null,
  // 指向自己的第一个子节点
  child: Fiber | null,
  // 指向自己的兄弟结构，兄弟节点的return指向同一个父节点
  sibling: Fiber | null,
  index: number,

  ref: null | (((handle: mixed) => void) & &#123; _stringRef: ?string &#125;) | RefObject,

  // 当前处理过程中的组件props对象
  pendingProps: any,
  // 上一次渲染完成之后的props
  memoizedProps: any,

  // 该Fiber对应的组件产生的Update会存放在这个队列里面
  updateQueue: UpdateQueue<any> | null,

  // 上一次渲染的时候的state
  memoizedState: any,

  // 一个列表，存放这个Fiber依赖的context
  firstContextDependency: ContextDependency<mixed> | null,

  mode: TypeOfMode,

  // Effect
  // 用来记录Side Effect
  effectTag: SideEffectTag,

  // 单链表用来快速查找下一个side effect
  nextEffect: Fiber | null,

  // 子树中第一个side effect
  firstEffect: Fiber | null,
  // 子树中最后一个side effect
  lastEffect: Fiber | null,

  // 代表任务在未来的哪个时间点应该被完成，之后版本改名为 lanes
  expirationTime: ExpirationTime,

  // 快速确定子树中是否有不在等待的变化
  childExpirationTime: ExpirationTime,

  // fiber的版本池，即记录fiber更新过程，便于恢复
  alternate: Fiber | null,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">Fiber 如何解决问题的</h2>
<p>Fiber 把一个渲染任务分解为多个渲染任务，而不是一次性完成，把每一个分割得很细的任务视作一个"执行单元"，React 就会检查现在还剩多少时间，如果没有时间就将控制权让出去，故任务会被分散到多个帧里面，中间可以返回至主进程控制执行其他任务，最终实现更流畅的用户体验。</p>
<p>即是实现了"增量渲染"，实现了可中断与恢复，恢复后也可以复用之前的中间状态，并给不同的任务赋予不同的优先级，其中每个任务更新单元为 React Element 对应的 Fiber 节点。</p>
<h2 data-id="heading-13">Fiber 实现原理</h2>
<p>实现的方式是requestIdleCallback这一 API，但 React 团队 polyfill 了这个 API，使其对比原生的浏览器兼容性更好且拓展了特性。</p>
<blockquote>
<p>window.requestIdleCallback()方法将在浏览器的空闲时段内调用的函数排队。这使开发者能够在主事件循环上执行后台和低优先级工作，而不会影响延迟关键事件，如动画和输入响应。函数一般会按先进先调用的顺序执行，然而，如果回调函数指定了执行超时时间 timeout，则有可能为了在超时前执行函数而打乱执行顺序。</p>
</blockquote>
<p>requestIdleCallback回调的执行的前提条件是当前浏览器处于空闲状态。</p>
<p>即requestIdleCallback的作用是在浏览器一帧的剩余空闲时间内执行优先度相对较低的任务。首先 React 中任务切割为多个步骤，分批完成。在完成一部分任务之后，将控制权交回给浏览器，让浏览器有时间再进行页面的渲染。等浏览器忙完之后有剩余时间，再继续之前 React 未完成的任务，是一种合作式调度。</p>
<p>简而言之，由浏览器给我们分配执行时间片，我们要按照约定在这个时间内执行完毕，并将控制权还给浏览器。</p>
<p>React 16 的Reconciler基于 Fiber 节点实现，被称为 Fiber Reconciler。</p>
<p>作为静态的数据结构来说，每个 Fiber 节点对应一个 React element，保存了该组件的类型（函数组件/类组件/原生组件等等）、对应的 DOM 节点等信息。</p>
<p>作为动态的工作单元来说，每个 Fiber 节点保存了本次更新中该组件改变的状态、要执行的工作。</p>
<p>每个 Fiber 节点有个对应的 React element，多个 Fiber 节点是如何连接形成树呢？靠如下三个属性：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 指向父级Fiber节点</span>
<span class="hljs-built_in">this</span>.return = <span class="hljs-literal">null</span>
<span class="hljs-comment">// 指向子Fiber节点</span>
<span class="hljs-built_in">this</span>.child = <span class="hljs-literal">null</span>
<span class="hljs-comment">// 指向右边第一个兄弟Fiber节点</span>
<span class="hljs-built_in">this</span>.sibling = <span class="hljs-literal">null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">8. React.PureComponent 和 React.Component 有什么区别？</h1>
<p>PureComponent 和 Component的区别是：Component需要手动实现 shouldComponentUpdate，而 PureComponent 通过浅对比默认实现了 shouldComponentUpdate 方法。</p>
<p>浅比较(shallowEqual)，即react源码中的一个函数，然后根据下面的方法进行是不是PureComponent的判断，帮我们做了本来应该我们在 shouldComponentUpdate 中做的事情</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._compositeType === CompositeTypes.PureClass) &#123;
  shouldUpdate = !shallowEqual(prevProps, nextProps) || ! shallowEqual(inst.state, nextState);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意： 浅比较只比较了第一层，复杂数据结构可能会导致更新问题</p>
<p>总结: PureComponent 不仅会影响本身，而且会影响子组件，所以 PureComponent 最佳情况是展示组件</p>
<h1 data-id="heading-15">9. React中，能否直接将 props 的值复制给 state？</h1>
<p>应该避免这种写法：</p>
<pre><code class="hljs language-react.js copyable" lang="react.js">constructor(props) &#123;
 super(props);
 // 不要这样做
 this.state = &#123; color: props.color &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为这样做毫无必要（你可以直接使用 this.props.color），同时还产生了 bug（更新 prop 中的 color 时，并不会影响 state）。</p>
<p>只有在你刻意忽略 prop 更新的情况下使用。</p>
<p>此时，应将 prop 重命名为 initialColor 或 defaultColor。必要时，你可以修改它的 key，以强制 <strong>重置</strong> 其内部 state。</p>
<h1 data-id="heading-16">10. React 的事件代理机制和原生事件绑定有什么区别？</h1>
<ul>
<li>事件传播与阻止事件的传播： React 的合成事件并没有实现事件捕获 只支持了事件冒泡。阻止事件传播 React 做了兼容性处理，只需要 e.preventDefault() 即可，原生存在兼容性问题。</li>
<li>事件类型：React 是 原生事件类型 的一个子集（React 只是实现了 DOM level3 的事件接口，有些事件 React 并没有实现，比如 window 的 resize 事件。）阻止 React 事件冒泡的行为只能用于 React 合成事件系统，但是 在原生事件中的阻止冒泡行为，却可以阻止 React 合成事件的传播。</li>
<li>事件的绑定方式：原生事件系统中支持多种不同的绑定事件的方式，React 中只有一种</li>
<li>事件对象：原生中存在 IE 的兼容性问题，React 做了兼容处理。</li>
</ul>
<hr>
<blockquote>
<p>更多面试题请看个人资料</p>
</blockquote></div>  
</div>
            