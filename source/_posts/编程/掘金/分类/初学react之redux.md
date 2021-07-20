
---
title: '初学react之redux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5707'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 05:21:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=5707'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一、状态管理一直是我们绕不开的一个点，之前出了一期vue的状态管理vuex的用法，这期出一个react的状态管理redux。首先需要了解两个点，第一个是actions，第二个是reducers,
actions的用处就是管理redux的一些方法，reducer是管理不同actios的触发条件，写处理逻辑的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//actions,定义一个action: setUserInfo</span>
<span class="hljs-keyword">const</span> setUserInfo = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">type</span>: actionTypes.SET_USERINFO,
        data
    &#125;
&#125;;
<span class="hljs-keyword">export</span> &#123;setUserInfo&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再定义一个reducer</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//action指明了type，reducer根据action的类型来匹配对应的逻辑</span>
<span class="hljs-keyword">const</span> userInfo = <span class="hljs-function">(<span class="hljs-params">state = &#123;&#125;, action</span>) =></span> &#123;
<span class="hljs-keyword">switch</span> (action.type) &#123;
<span class="hljs-keyword">case</span> actionTypes.SET_USERINFO:
<span class="hljs-keyword">return</span> action.data;
<span class="hljs-keyword">default</span>:
<span class="hljs-keyword">return</span> state;
&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件中使用</p>
<pre><code class="hljs language-js copyable" lang="js">首先我们需要处理的是把reducer关联到组件中
<span class="hljs-comment">/**
 * 1、provider包裹在最外层，使得所有组件都能获取redux的state值
 * 2、Router是路由出口
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> (
<span class="hljs-comment">//</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Router</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在业务组件中使用</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function"><span class="hljs-params">state</span> =></span> state;

<span class="hljs-keyword">const</span> mapDispatchToProps = <span class="hljs-function"><span class="hljs-params">dispatch</span> =></span> (&#123;
<span class="hljs-attr">setUserInfo</span>: <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
        <span class="hljs-comment">//分发reducer</span>
dispatch(setUserInfo(data));
&#125;
&#125;);
<span class="hljs-comment">//将reducer中的state映射到组件的props中</span>
<span class="hljs-comment">//将redux中的actions映射到组件的props中</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(
mapStateToProps,
mapDispatchToProps
)(Form.create()(Login));

<span class="hljs-comment">//触发reducer，利用props来调用reducers中的方法</span>
<span class="hljs-built_in">this</span>.props.setUserInfo(<span class="hljs-built_in">Object</span>.assign(&#123;&#125;, values, &#123; <span class="hljs-attr">role</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'超级管理员'</span> &#125; &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然我还没有在项目中使用过，但是在学习一些开源项目中我总结了它的用法，虽然不太完美，但是可以让自己日后更好翻阅。</p></div>  
</div>
            