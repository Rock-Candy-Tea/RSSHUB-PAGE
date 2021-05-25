
---
title: 'React Hooks  useState&useEffect&自定义hook'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6913'
author: 掘金
comments: false
date: Mon, 24 May 2021 01:39:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=6913'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一、作用：</p>
<pre><code class="copyable">Hook 是 React 16.8 的新增特性。它可以让你在不编写 class 的情况下使用 state 以及其他的 React 特性。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、规则</p>
<p>只能在函数最外层调用 Hook。不要在循环、条件判断或者子函数中调用。
只能在 React 的函数组件中调用 Hook。不要在其他 JavaScript 函数中调用。</p>
<p>三、用法</p>
<p>1、useState</p>
<pre><code class="copyable">import React,&#123;useState&#125; from "react";
const [state, setState] = useState(initialState);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用useState 返回一个 包含state以及更新 state 函数的数组</p>
<p>在初始化时，返回的state 与传入的initialState 值相同。</p>
<p>setState 函数用于更新 state，接收一个新的 state 值并将组件重新渲染。</p>
<p>setState(newState);
在后续的重新渲染中，useState 返回的第一个值将始终是更新后最新的 state。</p>
<p>下面介绍一下setState的两种用法，函数组件中的调用也如类组件中this.setState一样有两种写法。</p>
<p>方法一：调用setState,参数为想要更新的结果，这是我们使用useState常用的更新方法。</p>
<p>方法二：参数传如一个更新函数，函数的参数为上一次更新后的结果。</p>
<p>下面进行两种方法的示例展示。</p>
<pre><code class="copyable">const Counter = () => &#123;
    const [count, setCount] = useState(0);
    const changeCount = () => &#123;
      setCount(count + 1)
    &#125;
    const addCount =() =>&#123;
      setCount((prevCount) => &#123;
          return prevCount + 1
      &#125;)
    &#125;
    return (
      <div>
        &#123;count&#125;
        <button onClick=&#123;changeCount&#125;>+</button>
        <button onClick=&#123;addCount&#125;>+</button>
      </div>
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样看起来两者似乎并没有什么不同，实现的结果也是相同的，但是我们只要稍加变化，将其包装成异步，这时候两种不同的写法却有了不同的实现结果。</p>
<pre><code class="copyable">const Counter = () => &#123;
    const [count, setCount] = useState(0);
    const changeCount = () => &#123;
      setTimeout(() => &#123;
        setCount(count + 1)
      &#125;, 3000);
    &#125;
    const addCount =() =>&#123;
      setTimeout(() => &#123;
        setCount((prevCount) => &#123;
          return prevCount + 1
        &#125;)
      &#125;, 3000);
    &#125;
    return (
      <div>
        &#123;count&#125;
        <button onClick=&#123;changeCount&#125;>+</button>
        <button onClick=&#123;addCount&#125;>+</button>
      </div>
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如例所示，我们在定时器3s的时间内进行连续点击，第一种写法只更新了一次，结果是1，因为定义的count并没有发生变化。</p>
<p>而第二种写法的结果一直保持是最新的，因为在进行更新时并不是以初始化定义的count进行加1操作，而是已上一次更新之后的结果为基础，这样保持了count的实时性。</p>
<p>两种写法和类组件中的setState相似，可以直接进行更新，也可以进行函数式更新。</p>
<pre><code class="copyable">const changeCount = () => &#123;
    this.setState(&#123;count:this.state.count+1&#125;)
&#125;
    
const addCount = () => &#123;
    this.setState((prevState)=>&#123;
       count:prevState.count+1
    &#125;)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外有一点，class组件中setState更新数据是进行合并，而hooks中更新是进行数据的替换。</p>
<pre><code class="copyable">    constructor(props) &#123;
        super(props);
        this.state = &#123; count: 0, name: \'58\' &#125;;
    &#125;

    this.setState((state) => &#123;
        return &#123;count: state.count + 1&#125;
    &#125;)

    // 运行一次后的state结果是&#123; count: 1, name: \'58\' &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、useEffect</p>
<p>副作用钩子，常在此钩子中进行数据获取，发布订阅。</p>
<p>可以把useEffect看成类组件中componentDidMount，componentDidUpdate和componentWillUnmount三个生命周期的组合。</p>
<p>对于useEffect的常用方法一般有两种，一种为需要清除和不需要清除的。</p>
<p>不需要清除
如例所示，我们使用hooks实现一个把当前点击数量展示到document的title中的功能。</p>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from \'react\';

function Example() &#123;
  const [count, setCount] = useState(0);

  useEffect(() => &#123;
    document.title = `You clicked $&#123;count&#125; times`;
  &#125;);

  return (
    <div>
      <p>You clicked &#123;count&#125; times</p>
      <button onClick=&#123;() => setCount(count + 1)&#125;>
        Click me
      </button>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的写法使我们的effect在每次组件重新渲染时都会进行执行一次，让我们不需要考虑当前是挂载还是更新阶段。</p>
<p>在类组件中我们需要将这些副作用函数分别在componentDidMount和componentDidUpload两个生命周期函数中进行重复使用，这样才能保证实现点击次数的实时更新。</p>
<pre><code class="copyable">class Example extends React.Component &#123;
    constructor(props) &#123;
  
     super(props);
      this.state = &#123;
        count: 0
      &#125;;
    &#125;
  
    componentDidMount() &#123;
      document.title = `You clicked $&#123;this.state.count&#125; times`;
    &#125;
    componentDidUpdate() &#123;
      document.title = `You clicked $&#123;this.state.count&#125; times`;
    &#125;
  
    render() &#123;
      return (
        <div>
          <p>You clicked &#123;this.state.count&#125; times</p>
          <button onClick=&#123;() => this.setState(&#123; count: this.state.count + 1 &#125;)&#125;>
            Click me
          </button>
        </div>
      );
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相比之下useEffect看起来更加简洁，也减少了一些重复代码的书写。</p>
<p>需要清除
在平时的工作中，我们可能会在代码中进行发布订阅操作，为了防止内存泄漏，常用的方法就是在componentDidMount中进行订阅，在componentWillUnmount中进行清除订阅。</p>
<pre><code class="copyable">  componentDidMount() &#123;
    ChatAPI.subscribeToFriendStatus(
      this.props.friend.id,
      this.handleStatusChange
    );
  &#125;
  componentWillUnmount() &#123;
    ChatAPI.unsubscribeFromFriendStatus(
      this.props.friend.id,
      this.handleStatusChange
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而在hooks中我们只需要在useEffect钩子中返回一个清除函数，那么react就会在组件卸载的时候执行当前函数，进行清除操作。</p>
<pre><code class="copyable">    useEffect(() => &#123;
      ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
      return () => &#123;
        ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
      &#125;;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两个例子的effect在每次组件重新渲染时都会重新执行，这样的话就会造成一些不必要的调用或者渲染，接下来我们对上面的例子做一些优化，使其能够在effect中依赖项未发生变化时不重新执行。</p>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from \'react\';

function Example() &#123;
  const [count, setCount] = useState(0);
  const [number, setNumber] = useState(0);

  useEffect(() => &#123;
    document.title = `You clicked $&#123;count&#125; times`;
  &#125;，[count]);

  return (
    <div>
      <p>You clicked &#123;count&#125; times</p>
      <button onClick=&#123;() => setCount(count + 1)&#125;>
        Click me
      </button>
      <button onClick=&#123;() => setNumber(number + 1)&#125;>
        Click me
      </button>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在useEffect的第二个参数中，我们可以加入一个deps数组，当数组里的任意一项发生变化时，再重新执行当前的effect，这样就避免了一些不必要的调用和渲染。</p>
<p>我们在调用setNumber时，count并未发生变化，所以document的title不需要进行变化，effect也就不需要重新执行。</p>
<p>但当我们不把count加入依赖数组时，number的每一次变化也会使得effects重新进行一次调用，而这一步是我们所不想看到的。</p>
<p>将count加入依赖数组时，每次组件重新渲染时，effect会判断当前是否发生变化，发生改变时才会重新执行当前effect，这一步我看来更像在shouldComponentUpdata中进行pervState.count===state.count判断一样。</p>
<p>3、自定义hook
在使用函数组件时，难免会遇到两个组件之间存在共同逻辑。将相同逻辑拷贝在不同组件中，这未免不是一种低效的办法，这时候就轮到自定义hook发挥作用的时候了。</p>
<p>通过对相同逻辑hook的封装，我们即可实现高效的办公效率和减少一些重复代码。</p>
<p>自定义规则
自定义hook是一个函数，名称必须以use开头，函数内部可以调用其他的hook。</p>
<p>在自定义hook中我们可以制定想要接受的参数，和在当前hook中需要做什么，以及hook返回的结果，这些规则都可以根据我们的需求进行改变。</p>
<pre><code class="copyable">import &#123; useState, useEffect &#125; from \'react\';

function useFriendStatus(friendID) &#123;
  const [isOnline, setIsOnline] = useState(null);

  useEffect(() => &#123;
    function handleStatusChange(status) &#123;
      setIsOnline(status.isOnline);
    &#125;

    ChatAPI.subscribeToFriendStatus(friendID, handleStatusChange);
    return () => &#123;
      ChatAPI.unsubscribeFromFriendStatus(friendID, handleStatusChange);
    &#125;;
  &#125;);

  return isOnline;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上面代码为例，我们想要在不同组件中获取不同用户的登录状态，并在当前组件卸载是进行清除。对此我们把获取在线状态的hook提取出来，在组件中进行调用，只需要将当前用户ID传递就可接受一个是否在线的返回结果。</p>
<pre><code class="copyable">function FriendStatus(props) &#123;
    const isOnline = useFriendStatus(props.friend.id);

    return isOnline ? \'Online\' : \'Offline\';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>四、小结</p>
<p>尽管在写这篇文章之前就已经使用过很长一段时间的hooks，但在写的时候依旧有一些不知从何处写起的感觉，还是对一些内部的实现原理说的不是很清楚。通过这次对官方文档以及相关文章的阅读，也是加强了一些对hooks逻辑整理，文章如有观点偏差，还请大家指正。</p>
<p>革命尚未成功，同志仍需努力.</p>
<p>最后推荐一篇对于了解hook实现很有帮助的文章。<a href="https://overreacted.io/a-complete-guide-to-useeffect/" target="_blank" rel="nofollow noopener noreferrer">overreacted.io/a-complete-…</a></p></div>  
</div>
            