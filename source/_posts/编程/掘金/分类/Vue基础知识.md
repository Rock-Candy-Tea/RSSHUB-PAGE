
---
title: 'Vue基础知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=667'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 05:57:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=667'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">组件传值之子传父</h1>
<p>子组件向父组件传递值需要用到$emit这个属性，意思为发出一个东西。参数1：发射的事件名称 ，参数2：事件传递的参数</p>
<pre><code class="hljs language-js copyable" lang="js">    <div id=<span class="hljs-string">"app"</span>>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>父-->&#123;&#123;father&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">son</span> @<span class="hljs-attr">fire</span>=<span class="hljs-string">'shou'</span>></span><span class="hljs-tag"></<span class="hljs-name">son</span>></span></span>
    </div>
 Vue.component(<span class="hljs-string">'son'</span>, &#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">`<h1 @click='fire'>子-->我是子组件</h1>`</span>,
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">sonmse</span>: <span class="hljs-string">'你好啊'</span>
                &#125;
            &#125;,
            <span class="hljs-attr">methods</span>: &#123;
                <span class="hljs-function"><span class="hljs-title">fire</span>(<span class="hljs-params">value</span>)</span> &#123;
                    <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'fire'</span>, <span class="hljs-built_in">this</span>.sonmse)
                &#125;
            &#125;,
        &#125;)
         <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">father</span>: <span class="hljs-string">'我是父组件信息'</span>
            &#125;,
            <span class="hljs-attr">methods</span>: &#123;
                <span class="hljs-function"><span class="hljs-title">shou</span>(<span class="hljs-params">value</span>)</span> &#123;
                    <span class="hljs-built_in">this</span>.father = value
                &#125;
            &#125;
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">非父子传值</h1>
<p>我们有时候会遇到不是父子组件传值，也就是兄弟传值，这是我们需要定义一个空的Vue实例，来委托这个空的Vue实例来帮我们发出要传递的信息，其中$emit中的参数与子传父参数一样。</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">first</span>></span><span class="hljs-tag"></<span class="hljs-name">first</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">second</span>></span><span class="hljs-tag"></<span class="hljs-name">second</span>></span></span>
    </div>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-comment">//定义一个空的Vue实例对象 </span>
        <span class="hljs-keyword">let</span> kVue = <span class="hljs-keyword">new</span> Vue()
        Vue.component(<span class="hljs-string">'first'</span>, &#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">`<h1 @click='pass'>我是first</h1>`</span>,
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">firstMse</span>: <span class="hljs-string">'我是first的信息'</span>
                &#125;
            &#125;,
            <span class="hljs-attr">methods</span>: &#123;
                <span class="hljs-function"><span class="hljs-title">pass</span>(<span class="hljs-params"></span>)</span> &#123;
                    kVue.$emit(<span class="hljs-string">'fire'</span>, <span class="hljs-built_in">this</span>.firstMse)
                &#125;
            &#125;,

        &#125;)
        Vue.component(<span class="hljs-string">'second'</span>, &#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">`<h1>我是second &#123;&#123;mes&#125;&#125;</h1>`</span>,
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">mes</span>: <span class="hljs-string">''</span>
                &#125;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
                kVue.$on(<span class="hljs-string">'fire'</span>, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
                    <span class="hljs-built_in">this</span>.mes = value
                &#125;)
            &#125;,
        &#125;)
          </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>  
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">插槽</h1>
<p>slot 插槽作用：将组件之间的所有内容插入到指定的位置
我们在定义组件之后，组件之间就不可以写数据，如果想要写数据，就需要插槽，就相当于将这个信息插到这个组件之中。<br>
具名插槽，就是给插槽起一个名字，为了让不同组件的信息保持独有，我们可以个插槽起一个名字，然后将这个具名插槽写在你想要的位置。</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">first</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"A"</span>></span>今天天气不错<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">'B'</span>></span>我看看你今天乖不乖<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>ahil1<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">first</span>></span></span>
    </div>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"first"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>1 <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">'A'</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>2 <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">'B'</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>3 <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">'A'</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
        Vue.component(<span class="hljs-string">'first'</span>, &#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">'#first'</span>
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">Vue生命周期钩子函数</h1>
<p>Vue2.0官网显示的Vue生命周期钩子函数有11个。<br></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在实例初始化之后，数据观测 (data observer) 和 event/watcher 事件配置之前被调用。在组件创建之前调用'</span>);
            &#125;,
            <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'实例创建完成之后立即被调用 但这时 el 还不可以使用'</span>);
                <span class="hljs-comment">// console.log(this.$el);</span>
            &#125;,
            <span class="hljs-function"><span class="hljs-title">beforeMount</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在挂载开始之前被调用：相关的 render 函数首次被调用'</span>);
                <span class="hljs-comment">// console.log(this.$rednder);</span>
            &#125;,
            <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在内容挂载之后调用，这是el已经被挂载 也是最常用的周期函数'</span>)
                <span class="hljs-comment">// console.log(this.$el);</span>
            &#125;,
            <span class="hljs-function"><span class="hljs-title">beforeUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'数据更新时调用'</span>);
            &#125;,
            <span class="hljs-function"><span class="hljs-title">updated</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'组件DOM已经更新完成之后调用'</span>);
            &#125;,
            <span class="hljs-function"><span class="hljs-title">beforeDestroy</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'实例销毁之前调用。在这一步，实例仍然完全可用。'</span>);
            &#125;,
            <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'实例销毁后调用。该钩子被调用后，对应 Vue 实例的所有指令都被解绑，所有的事件监听器被移除，所有的子实例也都被销毁'</span>);
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">自定义指令</h1>
<p>除了Vue官方给我们提供的一些指令之外，我们也可以自定义指令，自定义资指令分为全局指令和局部指令
全局指令使用Vue.directive（） 第一个是指令名称，第二个是一个对象 ，里面包含inserted属性</p>
<pre><code class="hljs language-js copyable" lang="js">      Vue.directive(<span class="hljs-string">'bg'</span>, &#123;
            <span class="hljs-comment">// inserted 插入  指令的生命周期 在指令刚调用的时候 就会执行   相当于 monuted</span>
            <span class="hljs-comment">// 参数1：指令所挂载的标签</span>
            <span class="hljs-comment">// 参数2：数据对象</span>
            <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el, data</span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(el);
                <span class="hljs-built_in">console</span>.log(data);
                <span class="hljs-built_in">console</span>.log(data.value);
                el.style.background = data.value
            &#125;
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>局部指令写在Vue实例中</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>: &#123;&#125;,
            <span class="hljs-attr">directives</span>: &#123;
                <span class="hljs-attr">color</span>: &#123;
                    <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el, data</span>)</span> &#123;
                        el.style.color = data.value
                    &#125;
                &#125;
            &#125;
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">混入</h1>
<p>我们在写组件时，可能会遇到很多组件都有同一样的功能，这是用混入来定义这个相同的功能，可以减少大量的重复代码。</p>
<pre><code class="hljs language-js copyable" lang="js">  <div id=<span class="hljs-string">"app"</span>>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">first</span>></span><span class="hljs-tag"></<span class="hljs-name">first</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">second</span>></span><span class="hljs-tag"></<span class="hljs-name">second</span>></span></span>
    </div>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"first"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">'myClick'</span>></span>点我获取最新时间<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">'clickDown'</span>></span>点我<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
    <script>
        <span class="hljs-keyword">let</span> time = &#123;
            <span class="hljs-attr">methods</span>: &#123;
                <span class="hljs-function"><span class="hljs-title">myClick</span>(<span class="hljs-params"></span>)</span> &#123;
                    alert(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>())
                &#125;
            &#125;,
        &#125;
        <span class="hljs-keyword">let</span> lifeCircle = &#123;
            <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'组件被创建了'</span>)
            &#125;,
        &#125;
        Vue.component(<span class="hljs-string">'first'</span>, &#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">'#first'</span>,
            <span class="hljs-attr">mixins</span>: [time, lifeCircle],
            <span class="hljs-attr">methods</span>: &#123;
                <span class="hljs-function"><span class="hljs-title">clickDown</span>(<span class="hljs-params"></span>)</span> &#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'年后破'</span>)
                &#125;,
                <span class="hljs-function"><span class="hljs-title">myClick</span>(<span class="hljs-params"></span>)</span> &#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'aaa'</span>)
                &#125;
            &#125;,

        &#125;)
        Vue.component(<span class="hljs-string">'second'</span>, &#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">`<h1 @click='myClick'>点我啊</h1>`</span>,
            <span class="hljs-attr">mixins</span>: [time]

        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">验证传值，父传子</h1>
<p>在进行父向子通信时，我们使用props属性来接父组件传过来的信息，抱枕之前我们会使用数组来接收，但是Vue官方推荐我们使用对象的形式，我们可以为组件的 prop 指定验证要求，例如你知道的这些类型。如果有一个需求没有被满足，则 Vue 会在浏览器控制台中警告你。这在开发一个会被别人用到的组件时尤其有帮助。</p>
<pre><code class="hljs language-js copyable" lang="js"> props: &#123;
                <span class="hljs-attr">mes</span>: &#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>
                &#125;,
                <span class="hljs-attr">age</span>: &#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>
                &#125;,
                <span class="hljs-attr">font</span>: &#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
                    <span class="hljs-attr">default</span>: <span class="hljs-string">'一直嗨皮'</span>
                &#125;
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">元素查找</h1>
<p>我们在Vue不需要直接操作DOM树，在我们绑定ref之后我们可以直接使用$refs来获取这个属性。</p>
<pre><code class="hljs language-js copyable" lang="js"> <div id=<span class="hljs-string">"app"</span>>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">'bg'</span>></span>你好<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">'color'</span>></span>我们学习<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"a"</span>></span>ss<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    </div>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>: &#123;&#125;,
            <span class="hljs-attr">methods</span>: &#123;&#125;,
            <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">this</span>.$refs.bg.style.color = <span class="hljs-string">'red'</span>
                <span class="hljs-built_in">this</span>.$refs.color.style.background = <span class="hljs-string">'orange'</span>
                <span class="hljs-built_in">this</span>.$refs.a.style.color = <span class="hljs-string">'green'</span>
            &#125;,
        &#125;);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            