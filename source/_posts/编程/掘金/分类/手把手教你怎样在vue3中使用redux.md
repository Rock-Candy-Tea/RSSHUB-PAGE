
---
title: '手把手教你怎样在vue3中使用redux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c32ddcbe4de442c9aba1cd127662525~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 23:39:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c32ddcbe4de442c9aba1cd127662525~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>前言</strong></p>
<p>现在的web应用基本上都走上了数据驱动的道路，而数据状态的管理则理所当然成为了项目开发的核心，所以理论上只要统一状态层，view渲染可以随意更换框架和模式。</p>
<p>而我们在做项目的时候大部分都是vue用vuex。react用redux。以至于很多同学都以为所有的状态管理容器是和页面渲染框架一一绑定的，所以突然想实验一下用redux做状态管理，而vue只做一个简简单单的页面渲染器
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c32ddcbe4de442c9aba1cd127662525~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>思路</strong></p>
<p>我们知道redux的state 只是一个普通的js对象，是无法感知视图的。redux的整套流程和vue的渲染驱动机制其实是相互独立的。不像vuex本身就是一个vue实例，state属性本身就是reactive的，声明在template里，属性的set的方法会自动收集依赖，也就是vue本身的那套双绑模式。所以vuex不需要做任何操作天然的支持vue，或者说vuex就是一个实现了flux思想的全局vue。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da6a1c7f726d4dd8b9000cd4495c0079~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
所以就像官网说的，我们需要做一些简单绑定让redux接入到vue的数据渲染模式中，</p>
<p>然而这个网址已经失效。。。。￣□￣｜｜</p>
<p>不过redux官网也有通用的ui驱动方案
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e283d6299e734fe28c4e35bf7864f325~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大致思路就是在我们dispatch action 之后的回调中对ui层进行更新。不过如果每次state发生变化都对vue进行$forceUpdate不免太僵硬且浪费性能了。</p>
<p>参照react-redux将当前组件需要的参数从redux的state中接管为react组件的状态（props），让组件本身的数据代为驱动ui的更新。</p>
<p>而且vue本身的data就是reactive的，所以只需要将redux中的state注入到vue的data中，在redux的subscribe回调中根据state对data进行修改就可以顺利的驱动vue进行页面渲染。
所以只需要在vue组件挂载之前将state注入到data中即可，如果是vue2，我们只能用mixin将数据混入进组件，不过在vue3中我们则可以用composition component 在setup中进行注入</p>
<p><strong>示例</strong>
描述：做一个简单的小功能进行测试，点击sider内页面标签将页面名分发到state中，再驱动header页面更新。</p>
<p>效果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da4b54f139264fd181e9459e1046731b~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>步骤：</p>
<p>1 构建redux store</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createSlice, PayloadAction &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@reduxjs/toolkit'</span>
<span class="hljs-keyword">export</span> interface GlobalState &#123;
    <span class="hljs-attr">currentRoute</span>: string,
&#125;
<span class="hljs-comment">// 初始化state</span>
<span class="hljs-keyword">const</span> initialState: GlobalState =&#123;
    <span class="hljs-attr">currentRoute</span>: <span class="hljs-string">'应用程序管理'</span>,
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> globalSlice = createSlice(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'global'</span>,
  initialState,
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-attr">updata</span>: <span class="hljs-function">(<span class="hljs-params">state, action: PayloadAction<string></span>) =></span> &#123;
      state.currentRoute = action.payload
    &#125;,
  &#125;,
&#125;)

<span class="hljs-comment">// Action creators are generated for each case reducer function</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123; updata &#125; = globalSlice.actions

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> globalSlice.reducer




<span class="hljs-keyword">import</span> &#123; configureStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@reduxjs/toolkit'</span>
<span class="hljs-keyword">import</span> <span class="hljs-built_in">global</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducers/globalSlice'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> store = configureStore(&#123;
    <span class="hljs-attr">reducer</span>: &#123;
        <span class="hljs-attr">global</span>:<span class="hljs-built_in">global</span>
    &#125;,
  &#125;)
  store.subscribe(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'subscribe'</span>)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时已经生成的state，以及对应的action
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16b7e61c3bae4a32b9d2f1875628413d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2 建立redux与vue的连接组件reduxConnect</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;  reactive,onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> &#123; store &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../config/store/store.ts'</span>;
<span class="hljs-comment">/* 
mapStateToData:state描述集合，示例：[&#123;global:['currentRoute']&#125;]
*/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (mapStateToData:<span class="hljs-built_in">Array</span><any>)=>&#123;
    interface ObjType &#123;
        [propName: string]: any;
    &#125;
    <span class="hljs-keyword">const</span> state:ObjType = reactive(&#123;&#125;) 
    <span class="hljs-comment">// 通过redux state 生成 vue data</span>
    <span class="hljs-keyword">const</span> generate = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">if</span>(!mapStateToData.length)<span class="hljs-keyword">return</span>
        <span class="hljs-keyword">const</span> _state = store.getState() 
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> map <span class="hljs-keyword">of</span> mapStateToData)&#123;
            <span class="hljs-keyword">const</span> k = <span class="hljs-built_in">Object</span>.keys(map)[<span class="hljs-number">0</span>]
            <span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = map[k]
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> v <span class="hljs-keyword">of</span> <span class="hljs-built_in">module</span>)&#123;
                <span class="hljs-comment">// 浅比较替换</span>
                <span class="hljs-keyword">if</span>(!state[v]||state[v]!=_state[k][v])state[v] = _state[k][v]
            &#125;
        &#125;
    &#125;
    generate()
    onMounted(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// 在state完成更新的回调中更新vue data 驱动页面更新</span>
        store.subscribe(<span class="hljs-function">(<span class="hljs-params">v:any</span>)=></span>&#123;
            generate()
        &#125;)
    &#125;)
    <span class="hljs-keyword">return</span> &#123;state&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3 在header组件中根据state的描述规则连接vue和redux</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;...reduxConnect([&#123;<span class="hljs-attr">global</span>:[<span class="hljs-string">'currentRoute'</span>]&#125;])&#125;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时state已经注入进了vue组件（其实不如说是根据state生成新的vue data属性更贴切）
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e3c8ee7c768443e936056c77318de71~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
4 在sider组件内dispatch action 对state进行更新，同时驱动页面更新</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.store.dispatch(updata(params.label))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>后记</strong>
这次的一次小实验主要是验证一些自己的小猜想，顺便巩固一下相关的知识和理解。无论是vuex还是redux都是很优秀的框架。关于状态容器，用法也有很多种。有的同学从来不用只用组件内本身的状态进行管理，有的全局挂一个对象进行管理，有的则所有的状态都托付于容器进行管理。不能说谁对谁错，项目环境千差万别没有最好的用法，只有最适合的用法</p></div>  
</div>
            