
---
title: '【react】事件绑定与传参'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9148'
author: 掘金
comments: false
date: Wed, 26 May 2021 23:55:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=9148'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>class中的方法默认不会绑定this，所以如果事件处理函数中使用到了this，必须手动绑定this。官方介绍了四种方法：</p>
<h4 data-id="heading-0">第一种 在构造函数中绑定</h4>
<ul>
<li>优点：性能较好，只生成一个方法实例，</li>
<li>缺点：不能携带参数，需要增加额外的代码</li>
</ul>
<pre><code class="copyable">class LoggingButton extends React.Component &#123;
  constructor(props)&#123;
    super(props)
    this.state=&#123;&#125;
  
    this.handleClick=this.handleClick.bind(this)
  &#125;
  handleClick ()&#123;
    ...
  &#125;

  render() &#123;
    return (
      <button onClick=&#123;this.handleClick&#125;>
        Click me
      </button>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">第二种 调用时绑定</h4>
<ul>
<li>优点：可携带参数，无需额外代码，</li>
<li>缺点：每次调用都会生成一个新的方法实例，性能不好</li>
</ul>
<pre><code class="copyable">class LoggingButton extends React.Component &#123;
  constructor(props)&#123;
    super(props)
    this.state=&#123;&#125;
  &#125;
  handleClick (val)&#123;
    ...
  &#125;

  render() &#123;
    return (
      <button onClick=&#123;this.handleClick.bind(this,'a')&#125;>
        Click me
      </button>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">第三种 用箭头函数调用（箭头函数的this指向定义该函数时所在的作用域指向的对象）</h3>
<ul>
<li>优缺点同第二种方式</li>
</ul>
<pre><code class="copyable">class LoggingButton extends React.Component &#123;
  constructor(props)&#123;
    super(props)
    this.state=&#123;&#125;
  &#125;
  handleClick (val,e)&#123;
    ...
  &#125;

  render() &#123;
    return (
      <button onClick=&#123;(e)=>this.handleClick('a',e)&#125;>
        Click me
      </button>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">第四种 方法用箭头函数声明</h3>
<ul>
<li>优点：性能好，无需额外代码，只生成一个实例</li>
<li>缺点：不能携带额外参数</li>
</ul>
<pre><code class="copyable">class LoggingButton extends React.Component &#123;
  constructor(props)&#123;
    super(props)
    this.state=&#123;&#125;
  &#125;
  handleClick= (val) => &#123;
    ...
  &#125;

  render() &#123;
    return (
      <button onClick=&#123;this.handleClick&#125;>
        Click me
      </button>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">说明1</h3>
<p>若要携带event外的参数，只能使用第二种和第三种方式</p>
<h3 data-id="heading-5">说明2</h3>
<p>若未绑定this，直接onClick=&#123;this.test()&#125;这样使用，则该事件只会在初始渲染时触发，点击不会触发。完整代码如下：</p>
<pre><code class="copyable">class LoggingButton extends React.Component &#123;
  handleClick ()&#123;
    ...
  &#125;

  render() &#123;
    return (
      <button onClick=&#123;this.handleClick()&#125;>
        Click me
      </button>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            