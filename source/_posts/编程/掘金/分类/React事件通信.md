
---
title: 'React事件通信'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6651'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 19:40:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=6651'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">写在前面</h2>
<p>React组件之间的通信一般分为下面几种情况：</p>
<ul>
<li>父子组件之间的通信</li>
<li>非嵌套组件之间的通信</li>
</ul>
<h2 data-id="heading-1">父子组件之间的通信</h2>
<p>这是最简单也是最常用的一种通信方式：父组件通过向子组件传递 props，子组件得到 props 后进行相应的处理。下面贴两段代码:</p>
<p>父组件 FatherComp.js：</p>
<pre><code class="copyable">import React from "react";
import Son from "./SonComp";

export default function FatherComp() &#123;
  return (
    <div>
      <Son title="我就是高阶领主" />
    </div>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件 SonComp.js：</p>
<pre><code class="copyable">import React from "react";

const Son = (props) => &#123;
  return <h1>&#123;props.title&#125;</h1>;
&#125;;

export default Son;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个也没啥好说的，最简单的透传，下面主要介绍非嵌套的组件之间的通信。</p>
<h2 data-id="heading-2">非嵌套组件之间的通信</h2>
<p>简单来说就是组件之间没有什么关联，需要通信就需要有个媒介，这里我们采用自定义事件的方式来进行通信：
首先需要安装一个event包</p>
<pre><code class="copyable">npm install events --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建一个 event.js，引入 events 包，并向外提供一个事件对象，供通信时使用：</p>
<pre><code class="copyable">import &#123; EventEmitter &#125; from "events";
export default new EventEmitter();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>App.js</p>
<pre><code class="copyable">import React from "react";
import "./styles.css";

import Comp1 from "./Comp1";
import Comp2 from "./Comp2";
import FatherComp from "./FatherComp";

export default function App() &#123;
  return (
    <div>
      <FatherComp />
      <Comp1 />
      <Comp2 />
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Comp1.js</p>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react";
import emitter from "./event";

export default function Comp1() &#123;
  const [msg, setMsg] = useState(null);
  useEffect(() => &#123;
    // 声明一个自定义事件
    // 在组件装载完成以后
    this.eventEmitter = emitter.addListener("clickMe", (msg) => &#123;
      setMsg(msg);
    &#125;);
    // 组件销毁前移除事件监听
    return () => &#123;
      emitter.removeListener(this.eventEmitter);
    &#125;;
  &#125;, []);

  return (
    <div>
      &#123;msg&#125;
      组件1
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Comp2.js</p>
<pre><code class="copyable">import React from "react";
import emitter from "./event";

export default function Comp2() &#123;
  const cb = () => &#123;
    return () => &#123;
      // 触发自定义事件
      emitter.emit("clickMe", "Hello");
    &#125;;
  &#125;;
  return (
    <div>
      组件2<button onClick=&#123;cb()&#125;>点击我</button>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我们写一个简单的事件demo来深入了解一下：</p>
<pre><code class="copyable">    var eventPool = &#123;
      map: &#123;&#125;,
      // 事件订阅
      on: (name, cb) => &#123;
        eventPool.map[name] = cb;
      &#125;,
      // 事件发射
      emit: (name, ...args) => &#123;
        const cb = eventPool.map[name];
        cb && cb(...args);
      &#125;
    &#125;;
    // xxx为事件名，有两个参数
    eventPool.on("xxx", (p1, p2) => console.log(p1, p2));
    // 发射完直接打印了这两个参数
    eventPool.emit("xxx", 1, 2);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结</h2>
<p>自定义事件在组件之间没有直接联系的情况下使用还是很方便的，总之就是香~
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fcomp-interaction-demo-8ov47" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/comp-interaction-demo-8ov47" ref="nofollow noopener noreferrer">这里</a>是本篇文章涉及的代码，项目地址在
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhangzheyi1.com%2F2021%2F07%2F30%2FReact%25E4%25BA%258B%25E4%25BB%25B6%25E9%2580%259A%25E4%25BF%25A1%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhangzheyi1.com/2021/07/30/React%E4%BA%8B%E4%BB%B6%E9%80%9A%E4%BF%A1/" ref="nofollow noopener noreferrer">www.zhangzheyi1.com/2021/07/30/…</a></p></div>  
</div>
            