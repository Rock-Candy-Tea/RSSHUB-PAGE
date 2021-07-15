
---
title: 'React 中 refs 的常见用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4103'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 19:51:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=4103'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>默认情况下，不能在函数组件上使用 ref 属性，因为它们没有实例：</p>
</blockquote>
<h3 data-id="heading-0">一、<del>String 类型的 Refs</del></h3>
<p>不建议使用，因为 string 类型的 refs 存在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fpull%2F8333%23issuecomment-271648615" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/pull/8333#issuecomment-271648615" ref="nofollow noopener noreferrer">一些问题</a>。它已过时并可能会在未来的版本被移除。</p>
<pre><code class="copyable">import React from "react";
// 父组件
export default class StringRef extends React.PureComponent &#123;
  componentDidMount() &#123;
    console.log("stringRefDom:", this.refs.stringRefDom);
    console.log("stringRefComp:", this.refs.stringRefComp);
  &#125;
  render() &#123;
    return (
      <div>
        &#123;/*原生组件使用方式*/&#125;
        <div ref=&#123;"stringRefDom"&#125;>stringRefDom</div>
        &#123;/*类组件使用方式*/&#125;
        <StringRefComp ref=&#123;"stringRefComp"&#125; />
      </div>
    );
  &#125;
&#125;
//类组件
class StringRefComp extends React.PureComponent &#123;
  render() &#123;
    return <div>StringRefComp</div>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">二、回调 Refs</h3>
<ul>
<li>如果 ref 回调函数是以内联函数的方式定义的，在更新过程中它会被执行两次</li>
<li>第一次传入参数 null，然后第二次会传入参数 DOM 元素</li>
<li>这是因为在每次渲染时会创建一个新的函数实例，所以 React 清空旧的 ref 并且设置新的</li>
<li>通过将 ref 的回调函数定义成 class 的绑定函数的方式可以避免上述问题</li>
<li>但是大多数情况下它是无关紧要的</li>
</ul>
<pre><code class="copyable">import React from "react";
// 父组件
export default class CallbackRef extends React.PureComponent &#123;
  constructor(props) &#123;
    super(props);
    this.callbackRefDom = null;
    this.callbackRefComp = null;
  &#125;
  componentDidMount() &#123;
    console.log("callbackRefDom:", this.callbackRefDom);
    console.log("callbackRefComp:", this.callbackRefComp);
  &#125;
  //回调函数
  setCallbackRefDom = (ref) => &#123;
    this.callbackRefDom = ref;
  &#125;;
  setCallbackRefComp = (ref) => &#123;
    this.callbackRefComp = ref;
  &#125;;
  //回调函数
  render() &#123;
    return (
      <div>
        <div ref=&#123;this.setCallbackRefDom&#125;>callbackRefDom</div>
        <CallbackRefComp ref=&#123;this.setCallbackRefComp&#125; />
      </div>
    );
  &#125;
&#125;

//类组件
class CallbackRefComp extends React.PureComponent &#123;
  render() &#123;
    return <div>callbackRefComp</div>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">三、React.createRef()</h3>
<ul>
<li>React 16.3 版本引入</li>
<li>较早版本的 React，推荐使用回调形式的 refs</li>
</ul>
<pre><code class="copyable">import React from "react";
// 父组件
export default class CreateRef extends React.PureComponent &#123;
  constructor(props) &#123;
    super(props);
    this.createRefDom = React.createRef();
    this.createRefComp = React.createRef();
  &#125;
  componentDidMount() &#123;
    console.log("createRefDom:", this.createRefDom.current);
    console.log("createRefComp:", this.createRefComp.current);
  &#125;
  render() &#123;
    return (
      <div>
        <div ref=&#123;this.createRefDom&#125;>createRefDom</div>
        <CreateRefComp ref=&#123;this.createRefComp&#125; />
      </div>
    );
  &#125;
&#125;
//类组件
class CreateRefComp extends React.PureComponent &#123;
  render() &#123;
    return <div>CreateRefComp</div>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">四、useRef</h3>
<ul>
<li>Hook 是 React 16.8 的新增特性</li>
</ul>
<pre><code class="copyable">import React, &#123; useEffect &#125; from "react";
// 父组件
const UseRef = React.memo(() => &#123;
  // // 同样可以用
  // const createRefDom = React.createRef();
  // const createRefComp = React.createRef();
  const createRefDom = React.useRef();
  const createRefComp = React.useRef();
  useEffect(() => &#123;
    console.log("useRefDom:", createRefDom.current);
    console.log("useRefComp:", createRefComp.current);
  &#125;, []);
  return (
    <div>
      <div ref=&#123;createRefDom&#125;>useRefDom</div>
      <UseRefComp ref=&#123;createRefComp&#125; />
    </div>
  );
&#125;);

export default UseRef;

//类组件
class UseRefComp extends React.PureComponent &#123;
  render() &#123;
    return <div>useRefComp</div>;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">五、Refs 与函数组件</h3>
<ul>
<li>默认情况下，你不能在函数组件上使用 ref 属性，因为它们没有实例</li>
<li>如果要在函数组件中使用 ref，你可以使用 forwardRef（可与 useImperativeHandle 结合使用）</li>
<li>或者将该组件转化为 class 组件。</li>
</ul>
<pre><code class="copyable">import React, &#123; useEffect, useImperativeHandle &#125; from "react";

// 父组件
const ForwardRef = React.memo(() => &#123;
  const createRefComp = React.useRef();
  const createRefCompMethod = React.useRef();

  useEffect(() => &#123;
    console.log("useRefComp:", createRefComp.current);
    console.log("createRefCompMethod:", createRefCompMethod.current);
    createRefComp.current.reload();
  &#125;, []);
  return (
    <div>
      <ForwardRefFunc ref=&#123;createRefComp&#125; />
    </div>
  );
&#125;);

export default ForwardRef;

const RefFunc = React.forwardRef((props, ref) => &#123;
  const [name, setName] = React.useState(null);
  const reload = () => &#123;
    console.log("reload");
    setTimeout(() => &#123;
      setName("ForwardRefFunc");
    &#125;, 3000);
  &#125;;
  //useImperativeHandle 可以让你在使用 ref 时自定义暴露给父组件的实例值
  useImperativeHandle(ref, () => &#123;
    return &#123;
      reload: reload,
    &#125;;
  &#125;);
  return <div ref=&#123;ref&#125;>ForwardRefFunc &#123;name&#125;</div>;
&#125;);
const ForwardRefFunc = React.memo(RefFunc);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>forwardRef 和 useImperativeHandle 最终目的是设法给 ref 提供一个可调用的对象！</strong></p>
<hr>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2Fdocs%2Frefs-and-the-dom.html" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/docs/refs-and-the-dom.html" ref="nofollow noopener noreferrer">Refs and the DOM</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2Fdocs%2Fforwarding-refs.html" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/docs/forwarding-refs.html" ref="nofollow noopener noreferrer">forwardRef</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2Fdocs%2Fhooks-reference.html%23useimperativehandle" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/docs/hooks-reference.html#useimperativehandle" ref="nofollow noopener noreferrer">useimperativehandle</a></li>
</ul></div>  
</div>
            