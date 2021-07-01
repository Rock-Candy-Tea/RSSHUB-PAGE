
---
title: 'React函数组件详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5242'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 02:30:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=5242'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、创建一个函数组件</h1>
<pre><code class="copyable">const Hello = (props) => &#123;
    return <div>&#123;props.message&#125;</div>
&#125;
// 或者这样写
const Hello = props => <div>&#123;props.message&#125;</div>
// 常用自写法
function Hello(props)&#123;
    return <div>&#123;props.message&#125;</div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">函数组件代替类组件</h2>
<p>函数组件可以代替类组件，因为函数组件语法更加简单易懂，但是也面临以下两个问题</p>
<ul>
<li>没有state</li>
<li>没有生命周期</li>
</ul>
<h1 data-id="heading-2">二、没有state的解决方法</h1>
<p>React v16.8.0推出Hooks API，其中的 <code>useState</code> 可以解决这个问题</p>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react"

const App = props =>&#123;//消除了this
    const [n, setN] = React.useState(0)//数组前面是读，后面是写，叫法无所谓
    const onClick = () => &#123;
        setN(n+1)
    &#125;
    return &#123;
        <div>
        &#123;n&#125;,
        <button onClick = &#123;onClick&#125;>+1</button>
        </div>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">三、没有生命周期的解决方法</h1>
<p>React v16.8.0推出Hooks API，其中的 <code>useEffect</code> 可以解决这个问题</p>
<p>默认每次渲染都会调用</p>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react"

useEffect(()=>&#123; console.log('数据更新了') &#125;,)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useEffect</code> 接受一个函数作为参数，第二个参数表示什么时候调用它</p>
<h2 data-id="heading-4">模拟 <code>componentDidMount</code></h2>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react"

useEffect(()=>&#123; console.log('第一次渲染') &#125;,[])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个参数的空数组表示只在第一次调用，结果是之后点击按钮更新UI都不会打印，以此模拟componentDidMount</p>
<h2 data-id="heading-5">模拟 <code>componentDidUpdate</code></h2>
<pre><code class="copyable">React.useEffect(()=>&#123;
    console.log('n变了')
&#125;,[n])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想让哪个数据更新之后，执行代码，就把那个数据放到数组里。只有n变了，才会触发。如果m变了，就不会执行。</p>
<pre><code class="copyable">React.useEffect(()=>&#123;
    console.log('n,m变了')
&#125;,[n,m])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数组里也可以接受多个数据</p>
<pre><code class="copyable">React.useEffect(()=>&#123;
    console.log('state变了')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果state里有多个数据，想做到不管哪个数据变化，都执行这个函数，就<strong>不写第二个参数</strong>。比如有n和m，此时不管是n+1，还是m+1，都会打印</p>
<p>但是 <code>useEffect</code> 在第一次渲染时也会触发。我们在类组件里第一次渲染是不会触发的，只有数据变化了才会执行。</p>
<h2 data-id="heading-6">模拟 <code>componentWillUnmount</code></h2>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react"

useEffect(()=>&#123;
  console.log('第一次渲染')
  return ()=>&#123;
  console.log('组件要死了')
   &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>return的函数会在销毁时执行，因此需要把组件死之前要做的事情放在return后边</p>
<pre><code class="copyable">const App=(props)=>&#123;
    const [childVisible,setChildVisible]=React.useState(true)
    //数组前面是读，后面是写，叫法无所谓
    const hide=()=>&#123;
        setChildVisible(false)
    &#125;
    const show=()=>&#123;
        setChildVisible(true)
    &#125;
    return (
        <div>
            &#123;childVisible? <Child /> : null&#125;
            &#123;childVisible? <button onClick=&#123;hide&#125;>hide</button> : <button onClick=&#123;show&#125;>show</button>&#125;
        </div>
    )
&#125;
const Child=()=>&#123;
    React.useEffect(()=>&#123;
        return ()=>&#123;
            console.log('child死了');
        &#125;
    &#125;)
    return <div>Child</div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当点击hide按钮时，Child消失了，有打印。
如果同时存在多个 <code>useEffect</code>，会按照出现的顺序执行。</p>
<h2 data-id="heading-7">自定义Hook</h2>
<p><code>React.useEffect()</code> 当使用它模拟更新后执行函数时，比如n更新后就做什么事情，它会把第一次渲染也算上。有没有什么方法能让它不算第一次渲染的，只在n真正变化时才执行。</p>
<p>可以自定义一个hook函数,这个函数<strong>必须是use开头的</strong></p>
<pre><code class="copyable">import React, &#123; useState, useEffect &#125; from "react"

const useUpdate  = (fn, dep) =>&#123;
    const [count, setCount] = useState(0)
    useEffect(()=>&#123;
      setCount(x=> x + 1)  
    &#125;, [dep]);//这里的dep就相当于n
    
    useEffect(()=>&#123;
    if(count > 1)&#123;
        fn()
      &#125;
    &#125;, [count, fn]); 
&#125;

  useUpdate(()=>&#123;
    console.log('变了')
  &#125;，n)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">四. useLayoutEffect</h1>
<ul>
<li><code>useEffect</code> 会在浏览器对真实的DOM节点渲染完成后，执行。</li>
<li><code>useLayoutEffect</code>会在把虚拟DOM=>真实DOM后，浏览器绘制之前执行。</li>
<li>这两个是有时间差的，<code>useLayoutEffect</code> 总是会比 <code>useEffect</code> 先执行</li>
<li>不过我们都优先使用 <code>useEffect</code>。有什么事先让浏览器渲染出来再说，不然影响用户体验。</li>
</ul></div>  
</div>
            