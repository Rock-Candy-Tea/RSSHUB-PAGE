
---
title: 'Hooks中的useEffect'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3236093972d44ea1ae8c4de4fc05fa24~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 02 May 2021 21:02:43 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3236093972d44ea1ae8c4de4fc05fa24~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">useEffect</h1>
<p><strong>副作用</strong> ：对环境的改变即为副作用，如修改document.title,useEffect是在render后运行。
<strong>用途</strong> ：</p>
<ul>
<li><strong>作为componentDidMount使用,[ ]作为第二个参数</strong></li>
<li><strong>作为componentDidUpdate使用，可指定依赖</strong></li>
<li><strong>作为componentWillUnmount使用，通过return</strong></li>
</ul>
<p>以上三种用途可以同时存在</p>
<h2 data-id="heading-1">模拟componentDidMount</h2>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react";
import ReactDOM from "react-dom";

function App() &#123;
  const [n, setN] = useState(0);
  const onClick = () => &#123;
    setN((i) => i + 1);
  &#125;;
  useEffect(() => &#123;
    console.log("第一次渲染时执行");
  &#125;, []);
  return (
    <div>
      n: &#123;n&#125;
      <button onClick=&#123;onClick&#125;>+1</button>
    </div>
  );
&#125;

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个参数为[ ]代表只在第一次渲染时才执行,结果如下:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3236093972d44ea1ae8c4de4fc05fa24~tplv-k3u1fbpfcp-watermark.image" alt="react2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">模拟componentDidUpdate</h2>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react";
import ReactDOM from "react-dom";

function App() &#123;
 const [n, setN] = useState(0);
 const onClick = () => &#123;
   setN((i) => i + 1);
 &#125;;
 useEffect(() => &#123;
   console.log("n变化时执行");
 &#125;, [n]);
 return (
   <div>
     n: &#123;n&#125;
     <button onClick=&#123;onClick&#125;>+1</button>
   </div>
 );
&#125;

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>n变化时执行，结果如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66e1468290104861ba5b43ec44ce11af~tplv-k3u1fbpfcp-watermark.image" alt="react2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不接受任何参数时，代表任何一个state变化时都执行</p>
<pre><code class="copyable"> useEffect(() => &#123;
   console.log('任何一个state变化时都执行')
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">模拟componentWillUnmount</h2>
<p>useEffect模拟componentWillUnmount,用return就好了，例子如下:</p>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react";
import ReactDOM from "react-dom";

const App = props => &#123;
  const [childVisible,setChildVisible] = useState(true)
  const hide = () => &#123;
    setChildVisible(false)
  &#125;
  const show = () => &#123;
    setChildVisible(true)
  &#125;
  return (
    <div>
      &#123;childVisible ? <button onClick=&#123;hide&#125;>hide</button> : <button onClick=&#123;show&#125;>show</button>&#125;
      &#123;childVisible ? <Child/> : null&#125;
    </div>
  )
&#125;
  const Child = (props) => &#123;
    useEffect(() => &#123;
      console.log('渲染或者变化了')
      return ()=>&#123;
        console.log('child销毁了')
      &#125;
    &#125;)
    return (
      <div>
        Child
      </div>
    )
  &#125;

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当child从页面消失代表被销毁，结果如下:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34bd3a4b16634ec294e5eadbbbaed39a~tplv-k3u1fbpfcp-watermark.image" alt="react2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">useEffect总结</h2>
<pre><code class="copyable">//第一次渲染时才执行:
useEffect(()=>&#123;
  console.log('第一次渲染后执行这句话')
&#125;,[])

// n或m变化时执行
useEffect(()=>&#123;
  console.log('n变化了,值为'+n)
  console.log('m变化了,值为'+m)
&#125;,[n,m])

// 不传参代表任何state变化时都执行
useEffect(()=>&#123;
  console.log('n变化了,值为'+n)
  console.log('m变化了,值为'+m)
&#125;)

//组件要销毁时用return
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            