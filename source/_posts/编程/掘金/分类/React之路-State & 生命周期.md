
---
title: 'React之路-State & 生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9985'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 23:07:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=9985'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">改装之前的计时器案例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Clock</span>(<span class="hljs-params">props</span>)</span>&#123;
  <span class="hljs-keyword">return</span>(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前时间 &#123;new Date().toLocaleTimeString()&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTime</span>(<span class="hljs-params"></span>) </span>&#123;
  ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Clock</span> <span class="hljs-attr">date</span>=<span class="hljs-string">&#123;new</span> <span class="hljs-attr">Date</span>()&#125; /></span></span>,
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
  )
&#125;

<span class="hljs-built_in">setInterval</span>(getTime, <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们希望只编写一次代码，便可以让 Clock 组件自我更新,所以需要使用state, state 是私有,并且完全受控于当前组件</p>
<h3 data-id="heading-1">使用state实现组件的自我更新</h3>
<h4 data-id="heading-2">修改函数组件成class组件</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前时间 &#123;this.props.date.toLocaleTimeString()&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
    &#125;
&#125;

<span class="hljs-comment">//新建Clock class继承React.Compant</span>
<span class="hljs-comment">//新建一个render函数</span>
<span class="hljs-comment">//将函数组件返回的react对象迁移到新的render函数中</span>
<span class="hljs-comment">//将使用props的位置修改成this.props</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">在组件内部使用局部的state</h4>
<p>1.把 render() 方法中的 this.props.date 替换成 this.state.date</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前时间 &#123;this.state.date.toLocaleTimeString()&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.添加一个 class 构造函数，然后在该函数中为 this.state 赋初值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;<span class="hljs-attr">date</span>:<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()&#125;;
  &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前时间 &#123;this.state.date.toLocaleTimeString()&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.移除  元素中的 date 属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTime</span>(<span class="hljs-params"></span>) </span>&#123;
  ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Clock</span> /></span></span>,
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">使用生命周期</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//挂载componentDidMount</span>
<span class="hljs-comment">//卸载componentWillUnmount</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;<span class="hljs-attr">date</span>:<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()&#125;;
  &#125;
  <span class="hljs-comment">// 挂载</span>
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.timeId = <span class="hljs-built_in">setInterval</span>(
      <span class="hljs-function">() =></span><span class="hljs-built_in">this</span>.getTime(),<span class="hljs-number">1000</span>
    )
  &#125;
  <span class="hljs-comment">// 卸载</span>
  <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timeId)
  &#125;
  <span class="hljs-function"><span class="hljs-title">getTime</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">date</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
    &#125;);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span>(
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前时间 &#123;this.state.date.toLocaleTimeString()&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Clock</span> /></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
);

<span class="hljs-comment">//在执行ReactDOM.render时,会加载Clock组件</span>
<span class="hljs-comment">//组件执行会先加载构造函数,初始化this.state</span>
<span class="hljs-comment">//再去执行组件中的render函数更新展示DOM渲染输出</span>
<span class="hljs-comment">//在组件被挂载到页面的时候会执行componentDidMount挂载的声明周期函数,每一秒执行一次getTime()</span>
<span class="hljs-comment">//Clock组件会通过setState方法更新,React通过重新调用render函数,渲染出新的数据</span>
<span class="hljs-comment">//在页面卸载是的时候执行componentWillUnmount卸载的声明周期函数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">如何修改state</h3>
<p>需要使用this.setState来修改,不可以直接使用this.state来修改</p>
<p>构造函数是唯一可以给 this.state 赋值的地方</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;<span class="hljs-attr">date</span>:<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()&#125;;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">State 的更新可能是异步的</h3>
<p>setState()接收一个函数而不是对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">state, props</span>) =></span> (&#123;
  <span class="hljs-attr">counter</span>: state.counter + props.increment
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">State 的更新会被合并</h3>
<p>当state中包含多个独立的变量的时候,可以单独的对变量进行更新</p></div>  
</div>
            