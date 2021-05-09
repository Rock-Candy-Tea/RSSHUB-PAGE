
---
title: 'React 基础总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2489'
author: 掘金
comments: false
date: Sat, 08 May 2021 23:02:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=2489'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">基本使用</h3>
<h4 data-id="heading-1">React事件和Dom事件的区别</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、event 是SyntheticEvent，模拟出来Dom事件所有能力
<span class="hljs-number">2</span>、event.nativeEvent是原生事件对象
<span class="hljs-number">3</span>、所有的事件都被挂载到<span class="hljs-built_in">document</span>上
<span class="hljs-number">4</span>、和Dom事件不一样，和Vue事件也不一样
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：React 16 绑定到document、React 17 事件绑定到root组件</p>
<p>有利于多个React版本并存。例如微前端</p>
<h4 data-id="heading-2">表单</h4>
<p>受控组件：实现v-model，由state控制表单的值</p>
<h4 data-id="heading-3">组件使用</h4>
<pre><code class="hljs language-js copyable" lang="js">props传递数据
props传递函数
props类型检查
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">setState</h4>
<p>1、不可变值：不能直接去操作state</p>
<p>2、可能是异步更新</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、直接使用时异步的，可使用setState的第二个参数，回调函数
<span class="hljs-number">2</span>、<span class="hljs-built_in">setTimeout</span> 中setState是同步的
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
    &#125;)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count)
&#125;, <span class="hljs-number">0</span>)
<span class="hljs-number">3</span>、自定义DOM事件是同步的
<span class="hljs-built_in">document</span>.body.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
    &#125;)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、可能会被合并</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、传入对象，会被合并，执行结果只一次 + <span class="hljs-number">1</span>（类似<span class="hljs-built_in">Object</span>.assign）
<span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
&#125;)
<span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
&#125;)
<span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
&#125;)
<span class="hljs-number">2</span>、传入函数，不会被合并，执行结果 + <span class="hljs-number">3</span>
<span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">pervState, props</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">count</span>: prevState.count + <span class="hljs-number">1</span>
    &#125;
&#125;)
<span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">pervState, props</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">count</span>: prevState.count + <span class="hljs-number">1</span>
    &#125;
&#125;)
<span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">pervState, props</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">count</span>: prevState.count + <span class="hljs-number">1</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">组件生命周期</h4>
<p>1、挂载时</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title">constructor</span>
<span class="hljs-title">componentWillMount</span>
<span class="hljs-title">componentDidMount</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、更新时</p>
<pre><code class="hljs language-js copyable" lang="js">shouldCompontntUpdate
componentDidUpdate
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、卸载时</p>
<pre><code class="hljs language-js copyable" lang="js">componentWillUnmount
componentDidUnmount
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">高级特性</h3>
<h4 data-id="heading-7">函数组件</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、纯函数，输入props，输出JSX
<span class="hljs-number">2</span>、没有实例，没有生命周期，没有state
<span class="hljs-number">3</span>、不能扩展其他方法
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">非受控组件</h4>
<p>只赋值默认值，使用时通过ref获取最终的值</p>
<pre><code class="hljs language-js copyable" lang="js">ref
defaultValue defaultChecked
手动操作DOM元素
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用场景</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、必须手动操作DOM，setState实现不了
<span class="hljs-number">2</span>、文件上传
<span class="hljs-number">3</span>、某些富文本编辑器，需要传入DOM元素
<span class="copy-code-btn">复制代码</span></code></pre>
<p>受控组件和非受控组件的选择</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、优先使用受控组件，符合React设计原则（数据驱动视图）
<span class="hljs-number">2</span>、必须操作DOM时，再使用非受控组件
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">Portals</h4>
<p>组件默认会按照既定层次嵌套渲染, Portals让组件渲染到父组件以外</p>
<pre><code class="hljs language-js copyable" lang="js">ReactDom.createPortal(<span class="xml"><span class="hljs-tag"><></span><span class="hljs-tag"></></span></span>, <span class="hljs-built_in">document</span>.body<span class="hljs-comment">/*(DOM节点)*/</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用场景</p>
<pre><code class="hljs language-js copyable" lang="js">overflow:hidden
父组件z-index值太小
fixed定位需要放单body第一层
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">context</h4>
<pre><code class="hljs language-js copyable" lang="js">React.createContext().Provider
React.createContext().Consumer
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">异步组件</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span>()
React.lazy
React.Suspense
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> demo = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'XXX'</span>))
<React.Suspense fallback=&#123;<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>&#125;>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">demo</span> /></span></span>
</React.Suspense>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">性能优化</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、shouldComponentUpdate：通过前后state的对比，控制是否渲染
React shouldComponentUpdate 默认返回<span class="hljs-literal">true</span>，父组件有更新，子组件则无条件更新
深度比较比较耗性能、shouldComponentUpdate一定要配合不可变值，否则通过前后对比优化渲染时会出现问题
所有，根据具体的需求，可以使用shouldComponentUpdate优化渲染
<span class="hljs-number">2</span>、PureComponent和React.memo
通过SCU的浅层比较优化
<span class="hljs-number">3</span>、不可变值 immutable.js
基于共享数据（不是深拷贝），速度好
有一定的学习和迁移成本，按需使用
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">高阶组件HOC</h4>
<p>reduc connect是高阶组件，传入一个组件，得到一个新的组件</p>
<h4 data-id="heading-14">Render Props</h4>
<p>通过一个函数将class组件的state作为props传递给纯函数组件</p>
<h4 data-id="heading-15">HOC vs Render Props</h4>
<p>HOC 模式简单，但会增加组件层级</p>
<p>Render Props 代码简洁</p>
<h3 data-id="heading-16">Redux</h3>
<pre><code class="hljs language-js copyable" lang="js">基本概念
store state action reducer
单项数据流
<span class="hljs-number">1</span>、dispatch（action）
<span class="hljs-number">2</span>、reducer -> newState
<span class="hljs-number">3</span>、subscribe 触发通知
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">react-redux</h4>
<pre><code class="hljs language-js copyable" lang="js"><Provider>connect
异步action
redux-thunk
redux-promise
redux-saga
中间件
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            