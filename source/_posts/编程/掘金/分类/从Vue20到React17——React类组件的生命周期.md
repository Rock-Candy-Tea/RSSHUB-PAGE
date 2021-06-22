
---
title: '从Vue2.0到React17——React类组件的生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f504869612c54958b465d65ba5e8dbb7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 04:28:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f504869612c54958b465d65ba5e8dbb7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“这是我参与更文挑战的第3天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”</p>
<h2 data-id="heading-0">前言</h2>
<p>Vue组件的生命周期分为创造、挂载、更新、销毁四大阶段，并在生命周期每个阶段的前后会触发各自的钩子函数，如：</p>
<ul>
<li>组件创造前会执行<code>beforeCreate</code>钩子函数；</li>
<li>组件创造后<code>created</code>钩子函数；</li>
<li>组件挂载前<code>beforeMount</code>钩子函数；</li>
<li>组件挂载后<code>mounted</code>钩子函数；</li>
<li>组件更新前<code>beforeUpdate</code>钩子函数；</li>
<li>组件更新后<code>updated</code>钩子函数；</li>
<li>组件销毁前<code>beforeDestroy</code>钩子函数；</li>
<li>组件销毁后<code>destroyed</code>钩子函数。</li>
</ul>
<p>而React组件的生命周期分为挂载、更新、卸载阶段，学习生命周期最主要是弄清楚每个生命周期的阶段会触发那些钩子函数。先用一张图来展示React提供哪些生命周期钩子函数，不过该图展示的是React16.4版本后的生命周期钩子函数，且只能在类组件中使用，而函数组件中的生命周期钩子函数用React Hook来实现，在后续文章中介绍。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f504869612c54958b465d65ba5e8dbb7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">1、React组件挂载阶段</h2>
<p>在React组件挂载阶段会按顺序调用<code>constructor</code>、<code>getDerivedStateFromProps</code>、<code>componentDidMount</code>、<code>render</code>这些钩子函数。</p>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123; title: 'hello React' &#125;;
    console.log('执行constructor')
  &#125;
  static getDerivedStateFromProps(props, state)&#123;
    console.log('执行getDerivedStateFromProps')
    return null;
  &#125;
  componentDidMount()&#123;
    console.log('执行componentDidMount')
  &#125;
  render() &#123;
    console.log('执行render')
    return (
      <div>&#123;this.state.title&#125;</div>
    );
  &#125;
&#125;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行以上代码，在控制台的打印结果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b75cfc40c3aa4c298fe1830a9c32369a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">1.1 constructor</h3>
<p><code>constructor</code>其实是React.Component 子类的构造函数。在其中我们一般做三件事情。</p>
<ul>
<li>在其他语句之前前调用<code>super(props)</code>，否则<code>this.props</code>为<code>undefined</code>；</li>
<li>通过给 this.state 赋值对象来初始化state；</li>
<li>为事件处理函数绑定实例，否在函数中无法使用<code>this</code>。</li>
</ul>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123; title: 'hello React' &#125;;
    this.handleClick = this.handleClick.bind(this);
  &#125;
  handleClick() &#123;
    console.log(this)
  &#125;
  render() &#123;
    return (
      <div onClick=&#123;handleClick&#125;>&#123;this.state.title&#125;</div>
    );
  &#125;
&#125;
export default HelloWorld;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外要特别注意以下两点：</p>
<ul>
<li>不能使用<code>this.setState()</code>来初始内部state，如下所示：</li>
</ul>
<pre><code class="copyable">constructor(props) &#123;
    super(props);
    this.setState(&#123;
      title:'hello world'
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>不能将props直接赋值给state，然后使用state，而不直接使用props，这样做，当props更新时对应的state不会更新。</li>
</ul>
<pre><code class="copyable">constructor(props) &#123;
    super(props);
    this.state(&#123;
      title:this.props.title
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.2 getDerivedStateFromProps</h3>
<p>这是一个不常用的钩子函数，其作用是用组件的props来派生出一个新的state。<code>getDerivedStateFromProps</code>钩子函数接收组件的props和state作为参数，函数最后返回一个对象或者null，若返回一个对象，则用这个对象来更新state，若返回null，则不更新state。</p>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.Component &#123;
  constructor(props: any) &#123;
    super(props);
    this.state=&#123;
        info:'hello world'
    &#125;;
  &#125;
  static getDerivedStateFromProps(props, state)&#123;
    let stateName = props.state == 1? '处理中':'已完成';
    return &#123;
      stateName
    &#125;;
  &#125;
  render() &#123;
    return (
      <div>&#123;this.state.stateName&#125;</div>
    );
  &#125;
&#125;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>getDerivedStateFromProps</code>钩子函数时要注意以下三点：</p>
<ul>
<li>要派生出新的state，不要修改原来的state；</li>
<li>函数最后必须返回一个对象或者null；</li>
<li>钩子函数中无法使用<code>this</code>。</li>
</ul>
<h3 data-id="heading-4">1.3 render</h3>
<p><code>render</code>函数应该为纯函数，在其中不应该去修改state和props。在用JSX书写React元素时，通过state和props来给React元素绑定数据。最后必须返回一些React元素，且这些React元素必须只有一个根元素。若不想在DOM中额外增加一个无用的标签，可以使用<code><React.Fragment></code>作为根元素。</p>
<pre><code class="copyable">render() &#123;
  <React.Fragment>
    <div>&#123;this.state.title&#125;</div>
    <div>&#123;this.props.info&#125;</div>
  </React.Fragment>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.4 componentDidMount</h3>
<p><code>componentDidMount</code>钩子函数会在组件挂载后（插入 DOM 树中）立即调用，跟Vue中的<code>mounted</code>钩子函数的作用非常相似。</p>
<p>在其中我们一般可以做以下操作</p>
<ul>
<li>获取DOM元素；</li>
<li>请求服务端数据；</li>
<li>监听事件，必须在<code>componentWillUnmount()</code>中取消监听；</li>
<li>可以调用<code>this.setState()</code>来改变state数据。</li>
</ul>
<pre><code class="copyable">componentDidMount()&#123;
  this.setState(&#123;
    title:'hello world'
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2、React组件更新阶段</h2>
<p>在React组件更新阶段会按顺序调用<code>getDerivedStateFromProps</code>、<code>shouldComponentUpdate</code>、<code>render</code>、<code>getSnapshotBeforeUpdate</code>、<code>componentDidUpdate</code>这些钩子函数。</p>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.Component &#123;
  constructor(props: any) &#123;
    super(props);
    this.state = &#123;
      title: 'hello world'
    &#125;
    this.update = this.update.bind(this);
  &#125;
  static getDerivedStateFromProps(props, state) &#123;
    console.log('执行getDerivedStateFromProps');
    return null;
  &#125;
  shouldComponentUpdate(nextProps, nextState) &#123;
    console.log('执行shouldComponentUpdate');
    return true;
  &#125;
  getSnapshotBeforeUpdate(prevProps, prevState) &#123;
    console.log('执行getSnapshotBeforeUpdate');
    return null;
  &#125;
  componentDidUpdate() &#123;
    console.log('执行componentDidUpdate')
  &#125;
  update() &#123;
    this.setState(&#123;
      title: 'hello react'
    &#125;)
  &#125;
  render() &#123;
    console.log('执行render')
    return (
      <div onClick=&#123;this.update&#125;>&#123;this.state.title&#125;</div>
    )
  &#125;
&#125;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行以上代码，在控制台的打印结果如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3bfa46290ad415d8632162925a3bb29~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在React中有三个操作会引起组件更新：</p>
<ul>
<li>
<p>组件的props发生变化；</p>
</li>
<li>
<p>执行<code>this.setState()</code>；</p>
<p><code>this.setState(updater, [callback])</code>其中<code>undater</code>可以为一个对象或函数
<code>(state, props) => stateChange</code>，<code>stateChange</code>中要返回一个对象，这个对象在React内部会和
<code>this.state</code>进行合并来更新state。另外通过函数的参数state和props可以获取组件最新的state和props。</p>
<p>执行<code>this.setState()</code>并不总是立即更新组件，它会批量推迟更新。这使得在调用<code>this.setState()</code>后立即
读取<code>this.state</code>成为了隐患。所以<code>this.setState</code>的第二个参数<code>callback</code>为可选的回调函数，在回调函数去读取更新后的state。</p>
<pre><code class="copyable">handleClick()&#123;
  this.setState((state,props) =>&#123;
    const count= state.count + 1;
    return &#123;
      count,
    &#125;
  &#125;,() =>&#123;
    console.log(this.state.count)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>执行<code>this.forceUpdate()</code>。</p>
<p>执行<code>this.forceUpdate()</code>强制让组件重新渲染，相当Vue中的<code>vm.$forceUpdate()</code>。</p>
<pre><code class="copyable">handleClick()&#123;
  this.forceUpdate();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行<code>this.forceUpdate()</code>引起组件更新，会跳过<code>shouldComponentUpdate</code>钩子函数。
但其子组件会触发正常的生命周期钩子函数，包括<code>shouldComponentUpdate</code>钩子函数。</p>
</li>
</ul>
<h3 data-id="heading-7">2.1  getDerivedStateFromProps</h3>
<p><code>getDerivedStateFromProps</code>钩子函数在组件挂载阶段会被调用，在组件更新阶段也会被调用，且函数接收的state和props都是更新后的。</p>
<p>那么在其中派生出来的state，完全受props控制，即使用<code>this.setState()</code>改变也不起作用。</p>
<h3 data-id="heading-8">2.2 shouldComponentUpdate</h3>
<p><code>shouldComponentUpdate</code>钩子函数接收更新之后的state和props，通过和更新前的state和props对比，来判断是否更新组件，如果函数最后返回<code>true</code>则更新组件，反之返回<code>false</code>则不更新组件，一般用于性能优化。</p>
<pre><code class="copyable">shouldComponentUpdate(nextProps, nextState) &#123;
  if (this.props.color !== nextProps.color) &#123;
    return true;
  &#125;
  if (this.state.count !== nextState.count) &#123;
    return true;
  &#125;
  return false;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>shouldComponentUpdate</code>钩子函数时要注意以下三点：</p>
<ul>
<li>
<p>在组件中执行<code>this.forceUpdate()</code>触发组件更新，则不会执行该钩子函数；</p>
</li>
<li>
<p>在其中执行<code>this.setState()</code>时，必须在一个条件语句里中，否会陷入无限更新的死循环，导致程序崩溃。</p>
</li>
<li>
<p>函数最后必须返回<code>true</code>或<code>false</code>，若返回<code>false</code>，后续<code>render</code>、<code>getSnapshotBeforeUpdate</code>、<code>componentDidUpdate</code>钩子函数不再被调用。</p>
</li>
</ul>
<h3 data-id="heading-9">2.3 render</h3>
<p>执行<code>render()</code>重新渲染组件。</p>
<h3 data-id="heading-10">2.4 getSnapshotBeforeUpdate</h3>
<p><code>getSnapshotBeforeUpdate</code>钩子函数相当Vue中<code>beforeUpdate</code>钩子函数。</p>
<p><code>getSnapshotBeforeUpdate</code>钩子函数调用时，props和state已经更新了，故该钩子函数接收更新前的props和state作为参数，作为比较使用。</p>
<p><code>getSnapshotBeforeUpdate</code>钩子函数最后返回一个值，该值会被<code>componentDidUpdate</code>钩子函数的第三个参数<code>snapshot</code>接收。</p>
<p><code>getSnapshotBeforeUpdate</code>钩子函数是在组件重新渲染后挂载到DOM之前被调用，故在该钩子函数中获取到的 DOM 还是更新的 DOM ，一般用组件UI更新前后的交互操作。</p>
<p>例如下面的示例，通过<code>isOpen</code>这个prop来看控制一个列表的显示隐藏，列表的高度自适应。当<code>isOpen</code>改变导致组件更新时，在<code>getSnapshotBeforeUpdate</code>钩子函数中可以获取到隐藏前的列表高度，用于UI交互。</p>
<pre><code class="copyable">import React from 'react';
class List extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.listRef = React.createRef();
  &#125;
  getSnapshotBeforeUpdate(prevProps, prevState) &#123;
    console.log(prevProps)
    if (prevProps.isOpen) &#123;
      const listEl = this.listRef.current;
      return listEl.height;
    &#125;
    return null;
  &#125;
  componentDidUpdate(prevProps, prevState, snapshot) &#123;
    console.log(snapshot)
  &#125;
  render() &#123;
    return (
      <div>
        &#123;this.props.isOpen &&
          <div
            ref=&#123;this.listRef&#125;
          >
            &#123;/* ...contents... */&#125;
          </div>&#125;
      </div>
    );
  &#125;
&#125;
export default List;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>getSnapshotBeforeUpdate</code>钩子函数时要注意以下三点：</p>
<ul>
<li>
<p>在其中执行<code>this.forceUpdate()</code>或<code>this.setState()</code>时，必须在一个条件语句里中，否会陷入无限更新的死循环，导致程序崩溃；</p>
</li>
<li>
<p>函数最后必须返回一个值或null，否则代码会报错；</p>
</li>
<li>
<p>必须和<code>componentDidUpdate</code>钩子函数一起调用，否则代码会报错。</p>
</li>
</ul>
<h3 data-id="heading-11">2.5 componentDidUpdate</h3>
<p><code>componentDidUpdate</code>钩子函数在组件重新渲染后并挂载到DOM中后才执行的，函数参数接收更新前的state和props，还用<code>snapshot</code>参数接收<code>getSnapshotBeforeUpdate</code>钩子函数返回值。</p>
<pre><code class="copyable">componentDidUpdate(prevProps, prevState, snapshot)&#123;
  //...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>componentDidUpdate</code>钩子函数时要注意以下两点：</p>
<ul>
<li>
<p>在其中执行<code>this.forceUpdate()</code>或<code>this.setState()</code>时，必须在一个条件语句里中，否会陷入无限更新的死循环，导致程序崩溃；</p>
</li>
<li>
<p>如果<code>shouldComponentUpdate</code>钩子函数返回值为<code>false</code>，则不会调用<code>componentDidUpdate</code>钩子函数。</p>
</li>
</ul>
<h2 data-id="heading-12">3、React组件卸载阶段</h2>
<h3 data-id="heading-13">3.1 componentWillUnmount</h3>
<p><code>componentWillUnmount</code>会在组件卸载及销毁之前调用。我们一般在其中处理以下事项：</p>
<ul>
<li>清除定时器；</li>
<li>取消网络请求；</li>
<li>解绑在<code>componentDidMount</code>钩子函数中监听的事件。</li>
</ul>
<pre><code class="copyable">componentWillUnmount()&#123;
  //...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">4、React父组件挂载阶段</h2>
<p>在React父组件挂载阶段，在调用父组件<code>render</code>函数后，会去调用子组件的<code>constructor</code>函数，直到子组件的<code>componentDidMount</code>钩子函数被调用后，才会去调用父组件的<code>componentDidMount</code>钩子函数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a33fa1ff685470f945bc6ad12472875~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假如子组件中还有孙子组件，同理在调用子组件<code>render</code>函数后，会去调用孙子组件的<code>constructor</code>函数，直到孙子组件的<code>componentDidMount</code>钩子函数被调用后，才会去调用子组件的<code>componentDidMount</code>钩子函数，最后才调用父组件的<code>componentDidMount</code>钩子函数。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4433c928ec3f481d87993c6f2172f426~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一层层调用下去，直到最后一个孙子组件的<code>componentDidMount</code>钩子函数被调用后，才会去调用父组件的<code>componentDidMount</code>钩子函数。</p>
<h2 data-id="heading-15">5、React父组件更新阶段</h2>
<p>React更新是自顶向下的进行递归更新的，不管你嵌套了多少层组件，都会触发到最后一层组件的更新。</p>
<p>而Vue的更新只到当前组件，不会去触发子组件的更新，触发子组件的props发生了改变。</p>
<p>所以React父组件更新了，会引起子组件更新阶段的钩子函数的调用，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4babb8effe84651b1baa7dd15074bd5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>父组件更新时，在调用<code>render</code>函数后，会去调用子组件的<code>getDerivedStateFromProps</code>钩子函数，直到子组件的<code>getSnapshotBeforeUpdate</code>钩子函数被调用后，再去调用父组件的<code>getSnapshotBeforeUpdate</code>钩子函数，然后调用子组件的<code>componentDidUpdate</code>钩子函数，最后才调用父组件的<code>componentDidUpdate</code>钩子函数。</p>
<p>再来看子组件还有孙子组件的场景下，调用孙子组件的<code>getSnapshotBeforeUpdate</code>钩子函数，接着调用子组件的<code>getSnapshotBeforeUpdate</code>钩子函数，然后调用父组件的<code>getSnapshotBeforeUpdate</code>钩子函数，才会去调用各组件的<code>componentDidUpdate</code>钩子函数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e81c857cc1284701b68490f35b59c74a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">6、React父组件卸载阶段</h2>
<p>React父组件卸载后。其内部嵌套最深一层组件先调用<code>componentWillUnmount</code>钩子函数，然后依次往外调用各组件的<code>componentWillUnmount</code>构造函数。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a5468d254004f4a9efeccba219babb7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">+</p>
<h2 data-id="heading-17">7、React组件更新的优化</h2>
<p>React中父组件更新，不管子组件的state和props是否发生变化，都会被迫更新。习惯了Vue开发，会感到非常不可思议，按常理是传递给子组件的props变化了，子组件才会更新。React这种更新机制可能导致性能问题，可以用<code>React.PureComponent</code>来创建那种更新计算开销很大的子组件，来优化性能。</p>
<p><code>React.PureComponent</code>会创建一个自行调用<code>shouldComponentUpdate</code>钩子函数的组件，故在此组件中不能再次调用<code>shouldComponentUpdate</code>钩子函数。</p>
<p>在<code>shouldComponentUpdate</code>钩子函数中自动浅层对比props和state，若数据有变化，返回<code>true</code>，触发组件更新。</p>
<p>要注意只是浅层对比props和state，下面用一个例子来直观的解释什么是浅层对比。</p>
<pre><code class="copyable">import React from 'react';
class HelloWorld extends React.PureComponent &#123;
  constructor(props: any) &#123;
    super(props);
  &#125;
  componentDidUpdate() &#123;
    console.log('子组件执行componentDidUpdate')
  &#125;
  render() &#123;
    const &#123; title, arr, obj &#125; = this.props;
    return (
      <div>
        <div>&#123;title&#125;</div>
        &#123;arr.map((item,index) =>&#123;
          return (
            <span key=&#123;index&#125;>&#123;item&#125;</span>
          )
        &#125;)&#125;
        <div>&#123;obj.a&#125;</div>
      </div>
    )
  &#125;
&#125;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import React from 'react';
import HelloWorld from './HelloWorld';
class Index extends React.Component &#123;
  constructor(props: any) &#123;
    super(props);
    this.state = &#123;
      title: 'hello world',
      arr:[1,2,3],
      obj:&#123;
        a:1
      &#125;
    &#125;
    this.handleClick = this.handleClick.bind(this);
  &#125;
  handleClick() &#123;
    let &#123;arr,obj&#125; = this.state;
    arr.push(4);
    obj.a =4;
    this.setState(&#123;
      arr,
      obj,
    &#125;)
  &#125;
  render() &#123;
    return (
      <div onClick=&#123;this.handleClick&#125;>
        <HelloWorld title=&#123;this.state.title&#125; arr=&#123;this.state.arr&#125;  obj=&#123;this.state.obj&#125;></HelloWorld>
      </div>
    )
  &#125;
&#125;
export default Index;
export default HelloWorld;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>“浅层对比”：只对比到<code>this.props</code>的属性值的一层，比如属性值是数组或对象时不去对比里面的嵌套数据，</p>
<p>换句话来说，只要该属性值的引用地址不改变，就认为该属性值未改变。数组和对象都是引用类型。</p>
<p>在上述例子中给<code>this.state.arr</code>数组中添加一个4，将<code>this.state.obj.a</code>的值改变成4，都不会触发子组件的更新。</p>
<p>要触发组件的更新，要给<code>this.state.arr</code>或<code>this.state.obj</code>赋值个新数组或对象，也就是将其引用地址改变。</p>
<p>那么用<code>React.PureComponent</code>来创建的子组件，在父组件中，只有传递给子组件的props经过浅层对比后发现改变了，才会触发子组件的更新，避免父组件数据变动时子组件也被迫一起更新，从而优化了性能。</p>
<p>另外可以调用<code>forceUpdate</code>强制触发子组件的更新。</p>
<pre><code class="copyable">import React from 'react';
import HelloWorld from './HelloWorld';
export default class Index extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.myCom = React.createRef();
    this.handleClick = this.handleClick.bind(this);
  &#125;
  handleClick() &#123;
    this.myCom.current.forceUpdate();
  &#125;
  render() &#123;
    return (
      <div onClick=&#123;this.handleClick&#125; >
        <HelloWorld ref=&#123;this.myCom&#125;></HelloWorld>
      </div>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            