
---
title: '深入学习react（二） 写个自己的react-redux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bacc7674f334b419f93776ec5ccd776~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 23:36:08 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bacc7674f334b419f93776ec5ccd776~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bacc7674f334b419f93776ec5ccd776~tplv-k3u1fbpfcp-watermark.image" alt="react.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>hello,大家好今天让我们一起实现下自己react-redux吧！上一篇我们分享了<a href="https://juejin.cn/post/6955004948442513445" target="_blank">redux</a>，不懂的可以直接查看额，本篇文章适合有一定基础的react开发人员，用到了react Context api 不懂的可以先查看下，文本较长，建议收藏，废话不说，直接上干货！！！</p>
<h2 data-id="heading-0">一、从入口文件开始</h2>
<blockquote>
<p>首先我们需要在入门文件index.js文件上做如下修改，引入我们自己的文件，这时候因为我们还没有建立文件，自然就报错了，莫慌往下进行</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'@/pages/home'</span>
<span class="hljs-comment">// 引入我们自己的provider</span>
<span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./myReactRedux/provider'</span>
<span class="hljs-comment">// 引入上期的store</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/store'</span>
ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">store</span> &#125;></span>
      <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二、创建myReactRedux文件夹</h2>
<blockquote>
<p>我们在src目录下创建myReactRedux文件夹，在改文件夹下分别创建bindActionCreators.js  connect.js  createContext.js  provider.js,我们先从最简单的provider.js开始创建</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// provider比较简单就是一个高阶组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Provider</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123;this.props.children&#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="hljs-keyword">export</span> &#123; Provider &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们就可以页面内容了，那么我们的store数据怎么传递呢？</p>
<h2 data-id="heading-2">三、创建createContext.js内容</h2>
<blockquote>
<p>这里我们需要使用react给我们提供的api方法context，让数据可以向下传递</p>
<p>createContext.js代码比较简单我贴出了，就是原封的react api</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// react context</span>
<span class="hljs-keyword">const</span> ValueContext = React.createContext();
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> ValueContext
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们回过头来给provider.js绑定store</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">//引入</span>
<span class="hljs-keyword">import</span> ValueContext <span class="hljs-keyword">from</span> <span class="hljs-string">'./createContext'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Provider</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="hljs-comment">// context属性传递，这里去订阅了store的数据传递给了组件</span>
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ValueContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">this.props.store</span>&#125;></span>
                &#123;this.props.children&#125;
            <span class="hljs-tag"></<span class="hljs-name">ValueContext.Provider</span>></span></span>
        )
    &#125;
&#125;
<span class="hljs-keyword">export</span> &#123; Provider &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们就可以在控制台打印出我们this.props看下了，是不是很简答哇！</p>
<h2 data-id="heading-3">四、创建connect.js内容</h2>
<blockquote>
<p>先分析下结构，connect是一个函数，接收了两个参数并且传递给了组件，代码如下</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// 接收参数，组件，直接将组件返回</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> connect = <span class="hljs-function">(<span class="hljs-params">
    mapStateToProps,
    mapDispatchToProps
</span>) =></span> <span class="hljs-function"><span class="hljs-params">WrappedComponent</span> =></span> &#123; 
    <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;         
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> /></span></span>;
        &#125;
    &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">五、connect函数订阅数据传递给组件</h2>
<blockquote>
<p>我们的store数据使用了contect向下传递，我们首先引入创建的context获取上下文，和store数据</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ValueContext <span class="hljs-keyword">from</span> <span class="hljs-string">'./createContext'</span>
<span class="hljs-comment">// 接收参数和组件，直接将组件返回</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> connect = <span class="hljs-function">(<span class="hljs-params">
    mapStateToProps,
    mapDispatchToProps
</span>) =></span> <span class="hljs-function"><span class="hljs-params">WrappedComponent</span> =></span> &#123; 
    <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123; 
        <span class="hljs-comment">// 挂载contextType属性</span>
        <span class="hljs-keyword">static</span> contextType = ValueContext
        
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;

            <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> /></span></span>;
        &#125;
    &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时context就被我们挂载到了this上</p>
<h2 data-id="heading-5">六、mapStateToProps</h2>
<blockquote>
<p>state在我们传递过来的mapStateToProps上，他是一个函数，我们直接返回就好了，我们在mount阶段去处理数据，将值传递给组件就可以了</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ValueContext <span class="hljs-keyword">from</span> <span class="hljs-string">'./createContext'</span>
<span class="hljs-comment">// 接收参数和组件，直接将组件返回</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> connect = <span class="hljs-function">(<span class="hljs-params">
    mapStateToProps,
    mapDispatchToProps
</span>) =></span> <span class="hljs-function"><span class="hljs-params">WrappedComponent</span> =></span> &#123; 
    <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123; 
        <span class="hljs-comment">// 挂载contextType属性</span>
        <span class="hljs-keyword">static</span> contextType = ValueContext
        <span class="hljs-comment">//为了修改props让组件更新变化，需要调用setState，所以这里重新创建下</span>
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
            <span class="hljs-built_in">super</span>(props);
            <span class="hljs-built_in">this</span>.state = &#123;
                <span class="hljs-attr">props</span>: &#123;&#125;
            &#125;;
        &#125;
        <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123; 
            <span class="hljs-built_in">this</span>.update();
            <span class="hljs-comment">//我们在mount阶段去获取一下context中的值</span>
            <span class="hljs-keyword">const</span> &#123; subscribe, getState &#125; = <span class="hljs-built_in">this</span>.context
            subscribe(<span class="hljs-function">() =></span> &#123; 
                <span class="hljs-built_in">this</span>.update();
            &#125;)
        &#125;
        update = <span class="hljs-function">() =></span> &#123; 
            <span class="hljs-keyword">const</span> &#123; getState, dispatch &#125; = <span class="hljs-built_in">this</span>.context;
            <span class="hljs-comment">//查看一下传递过来的类型</span>
            <span class="hljs-comment">// console.log(mapStateToProps, mapDispatchToProps);</span>
            <span class="hljs-comment">//直接返回state的值</span>
            <span class="hljs-keyword">const</span> stateProps = mapStateToProps(getState())
            
            <span class="hljs-keyword">let</span> dispatchProps;
            
            <span class="hljs-built_in">this</span>.setState(&#123;
                <span class="hljs-attr">props</span>: &#123;
                    ...stateProps,
                    ...dispatchProps
                &#125;
            &#125;);
        &#125;
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;

            <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> &#123;<span class="hljs-attr">...this.props</span>&#125; &#123;<span class="hljs-attr">...this.state.props</span>&#125;/></span></span>;
        &#125;
    &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">七、mapDispatchToProps</h2>
<blockquote>
<p>我们知道mapDispatchToProps可以接受一个对象或者函数，只不过函数需要使用bindActionCreators绑定下dispatch，所以这里要对他们分别进行处理，我们先给出bindActionCreators函数</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindActionCreator</span>(<span class="hljs-params">creator, dispatch</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> dispatch(creator(...args));
&#125;
<span class="hljs-comment">// 循环绑定包裹dispatch</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindActionCreators</span>(<span class="hljs-params">creators,dispatch</span>) </span>&#123;
    <span class="hljs-keyword">const</span> obj = &#123;&#125;;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> creators) &#123;
        obj[key] = bindActionCreator(creators[key],dispatch);
    &#125;
    <span class="hljs-keyword">return</span> obj;
&#125;
<span class="hljs-keyword">export</span> &#123; bindActionCreators &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以实现我们的mapDispatchToPropsle</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ValueContext <span class="hljs-keyword">from</span> <span class="hljs-string">'./createContext'</span>
<span class="hljs-keyword">import</span> &#123; bindActionCreators &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./bindActionCreators'</span>
<span class="hljs-comment">// 接收参数和组件，直接将组件返回</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> connect = <span class="hljs-function">(<span class="hljs-params">
    mapStateToProps,
    mapDispatchToProps
</span>) =></span> <span class="hljs-function"><span class="hljs-params">WrappedComponent</span> =></span> &#123; 
    <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123; 
        <span class="hljs-comment">// 挂载contextType属性</span>
        <span class="hljs-keyword">static</span> contextType = ValueContext
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
            <span class="hljs-built_in">super</span>(props);
            <span class="hljs-built_in">this</span>.state = &#123;
                <span class="hljs-attr">props</span>: &#123;&#125;
            &#125;;
        &#125;
        <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123; 
            <span class="hljs-built_in">this</span>.update();
            <span class="hljs-comment">//我们在mount阶段去获取一下context中的值</span>
            <span class="hljs-comment">//看下context中有什么吧</span>
            <span class="hljs-comment">// console.log(this.context)</span>
            <span class="hljs-keyword">const</span> &#123; subscribe, getState &#125; = <span class="hljs-built_in">this</span>.context
            <span class="hljs-comment">//这里已经可以看到我们的值了</span>
            <span class="hljs-comment">// console.log(getState())</span>
            subscribe(<span class="hljs-function">() =></span> &#123; 
                <span class="hljs-built_in">this</span>.update();
            &#125;)
        &#125;
        update = <span class="hljs-function">() =></span> &#123; 
            <span class="hljs-keyword">const</span> &#123; getState, dispatch &#125; = <span class="hljs-built_in">this</span>.context;
            <span class="hljs-comment">//查看一下传递过来的类型</span>
            <span class="hljs-comment">// console.log(mapStateToProps, mapDispatchToProps);</span>
            <span class="hljs-comment">//直接返回state的值</span>
            <span class="hljs-keyword">const</span> stateProps = mapStateToProps(getState())
            
            <span class="hljs-keyword">let</span> dispatchProps;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> mapDispatchToProps === <span class="hljs-string">"object"</span>) &#123;
                <span class="hljs-comment">// 办理object，分别绑定dispath方法</span>
                dispatchProps = bindActionCreators(mapDispatchToProps,dispatch);
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> mapDispatchToProps === <span class="hljs-string">"function"</span>) &#123;
                <span class="hljs-comment">// 绑定dispath方法</span>
                dispatchProps = mapDispatchToProps(dispatch, <span class="hljs-built_in">this</span>.props);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 直接绑定</span>
                dispatchProps = &#123; dispatch &#125;;
            &#125;
            <span class="hljs-built_in">this</span>.setState(&#123;
                <span class="hljs-attr">props</span>: &#123;
                    ...stateProps,
                    ...dispatchProps
                &#125;
            &#125;);
        &#125;
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;

            <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> &#123;<span class="hljs-attr">...this.props</span>&#125; &#123;<span class="hljs-attr">...this.state.props</span>&#125;/></span></span>;
        &#125;
    &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok，你学会了吗?快来试试新技能吧！</p></div>  
</div>
            