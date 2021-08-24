
---
title: 'Vue3的7种和Vue2的12种组件通信，值得收藏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2f14ac26fad4d2b8fdba288865c2916~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 11:38:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2f14ac26fad4d2b8fdba288865c2916~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第24天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>如有不对的或者遗漏的，欢迎指正，你的一赞一评都是我前行最大的动力，感谢</p>
<p>Vue2.x组件通信12种方式写在后面了，先来 Vue3 的</p>
<p>奥力给！</p>
<h2 data-id="heading-0">Vue3 组件通信方式</h2>
<ul>
<li>props</li>
<li>$emit</li>
<li>expose / ref</li>
<li>$attrs</li>
<li>v-model</li>
<li>provide / inject</li>
<li>Vuex</li>
</ul>
<h2 data-id="heading-1">Vue3 通信使用写法</h2>
<h3 data-id="heading-2">props</h3>
<p>用 props 传数据给子组件有两种方法，如下</p>
<p>方法一，混合写法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parenv.vue 传送</span>
<child :msg1=<span class="hljs-string">"msg1"</span> :msg2=<span class="hljs-string">"msg2"</span>></child>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> child <span class="hljs-keyword">from</span> <span class="hljs-string">"./child.vue"</span>
<span class="hljs-keyword">import</span> &#123; ref, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">msg1</span>:<span class="hljs-string">"这是传级子组件的信息1"</span>
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 创建一个响应式数据</span>
        
        <span class="hljs-comment">// 写法一 适用于基础类型  ref 还有其他用处，下面章节有介绍</span>
        <span class="hljs-keyword">const</span> msg2 = ref(<span class="hljs-string">"这是传级子组件的信息2"</span>)
        
        <span class="hljs-comment">// 写法二 适用于复杂类型，如数组、对象</span>
        <span class="hljs-keyword">const</span> msg2 = reactive([<span class="hljs-string">"这是传级子组件的信息2"</span>])
        
        <span class="hljs-keyword">return</span> &#123;
            msg2
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="hljs-comment">// Child.vue 接收</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">"msg1"</span>, <span class="hljs-string">"msg2"</span>],<span class="hljs-comment">// 如果这行不写，下面就接收不到</span>
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(props) <span class="hljs-comment">// &#123; msg1:"这是传给子组件的信息1", msg2:"这是传给子组件的信息2" &#125;</span>
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法二，纯 Vue3 写法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent.vue 传送</span>
<child :msg2=<span class="hljs-string">"msg2"</span>></child>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">sutep</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> child <span class="hljs-keyword">from</span> <span class="hljs-string">"./child.vue"</span>
    <span class="hljs-keyword">import</span> &#123; ref, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    <span class="hljs-keyword">const</span> msg2 = ref(<span class="hljs-string">"这是传给子组件的信息2"</span>)
    <span class="hljs-comment">// 或者复杂类型</span>
    <span class="hljs-keyword">const</span> msg2 = reactive([<span class="hljs-string">"这是传级子组件的信息2"</span>])
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="hljs-comment">// Child.vue 接收</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">sutep</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; defineProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    <span class="hljs-keyword">const</span> props = defineProps(&#123;
        <span class="hljs-comment">// 写法一</span>
        <span class="hljs-attr">msg2</span>: <span class="hljs-built_in">String</span>
        <span class="hljs-comment">// 写法二</span>
        <span class="hljs-attr">msg2</span>:&#123;
            <span class="hljs-attr">type</span>:<span class="hljs-built_in">String</span>,
            <span class="hljs-attr">default</span>:<span class="hljs-string">""</span>
        &#125;
    &#125;)
    <span class="hljs-built_in">console</span>.log(props) <span class="hljs-comment">// &#123; msg2:"这是传级子组件的信息2" &#125;</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：</p>
<p>如果父组件是混合写法，子组件纯 Vue3 写法的话，是接收不到父组件里 data 的属性，只能接收到父组件里 setup 函数里传的属性</p>
<p>如果父组件是纯 Vue3 写法，子组件混合写法，可以通过 props 接收到 data 和 setup 函数里的属性，但是子组件要是在 setup 里接收，同样只能接收到父组件中 setup 函数里的属性，接收不到 data 里的属性</p>
<p>官方也说了，既然用了 3，就不要写 2 了，所以不推荐混合写法。下面的例子，一律只用纯 Vue3 的写法，就不写混合写法了</p>
<h3 data-id="heading-3">$emit</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Child.vue 派发</span>
<template>
    <span class="hljs-comment">// 写法一</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"emit('myClick')"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">buttom</span>></span></span>
    <span class="hljs-comment">// 写法二</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleClick"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">buttom</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; defineEmit, useContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    
    <span class="hljs-comment">// 方法一 使用 defineEmit</span>
    <span class="hljs-comment">// 对应写法一</span>
    <span class="hljs-keyword">const</span> emit = defineEmit([<span class="hljs-string">"myClick"</span>,<span class="hljs-string">"myClick2"</span>])
    <span class="hljs-comment">// 对应写法二</span>
    <span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">()=></span>&#123;
        emit(<span class="hljs-string">"myClick"</span>, <span class="hljs-string">"这是发送给父组件的信息"</span>)
    &#125;
    
    <span class="hljs-comment">// 方法二 使用上下文 useContext </span>
    <span class="hljs-keyword">const</span> ctx = useContext()
    <span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">()=></span>&#123;
        ctx.emit(<span class="hljs-string">"myClick"</span>, <span class="hljs-string">"这是发送给父组件的信息"</span>)
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="hljs-comment">// Parent.vue 响应</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">child</span> @<span class="hljs-attr">myClick</span>=<span class="hljs-string">"onMyClick"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">sutep</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> onMyClick = <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(msg) <span class="hljs-comment">// 这是父组件收到的信息</span>
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">expose / ref</h3>
<p>父组件获取子组件的属性或者调用子组件方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Child.vue</span>
<script setup>
    <span class="hljs-keyword">import</span> &#123; useContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    <span class="hljs-keyword">const</span> ctx = useContext()
    <span class="hljs-comment">// 对外暴露属性方法等都可以</span>
    ctx.expose(&#123;
        <span class="hljs-attr">childName</span>: <span class="hljs-string">"这是子组件的属性"</span>,
        <span class="hljs-function"><span class="hljs-title">someMethod</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"这是子组件的方法"</span>)
        &#125;
    &#125;）
</script>

<span class="hljs-comment">// Parent.vue  注意 ref="comp"</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"comp"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> child <span class="hljs-keyword">from</span> <span class="hljs-string">"./child.vue"</span>
    <span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    <span class="hljs-keyword">const</span> comp = ref(<span class="hljs-literal">null</span>)
    <span class="hljs-built_in">console</span>.log(comp.value.childName) <span class="hljs-comment">// 获取子组件对外暴露的属性</span>
    comp.value.someMethod() <span class="hljs-comment">// 调用子组件对外暴露的方法</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">attrs</h3>
<p><code>attrs</code>：包含父作用域里除 class 和 style 除外的非 props <strong>属性集合</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent.vue 传送</span>
<child :msg1=<span class="hljs-string">"msg1"</span> :msg2=<span class="hljs-string">"msg2"</span> title=<span class="hljs-string">"3333"</span>></child>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> child <span class="hljs-keyword">from</span> <span class="hljs-string">"./child.vue"</span>
    <span class="hljs-keyword">import</span> &#123; ref, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    <span class="hljs-keyword">const</span> msg1 = ref(<span class="hljs-string">"1111"</span>)
    <span class="hljs-keyword">const</span> msg2 = ref(<span class="hljs-string">"2222"</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="hljs-comment">// Child.vue 接收</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; defineProps, useContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    <span class="hljs-keyword">const</span> props = defineProps(&#123;
        <span class="hljs-attr">msg1</span>: <span class="hljs-built_in">String</span>
    &#125;)
    <span class="hljs-keyword">const</span> ctx = useContext()
    
    <span class="hljs-comment">// 如果没有用 props 接收 msg1 的话就是 &#123; msg1: "1111", msg2:"2222", title: "3333" &#125;</span>
    <span class="hljs-built_in">console</span>.log(ctx.attrs) <span class="hljs-comment">//&#123; msg2:"2222", title: "3333" &#125;</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">v-model</h3>
<p>可以支持多个数据双向绑定</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent.vue</span>
<child v-model:key=<span class="hljs-string">"key"</span> v-model:value=<span class="hljs-string">"value"</span>></child>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> child <span class="hljs-keyword">from</span> <span class="hljs-string">"./child.vue"</span>
    <span class="hljs-keyword">import</span> &#123; ref, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    <span class="hljs-keyword">const</span> key = ref(<span class="hljs-string">"1111"</span>)
    <span class="hljs-keyword">const</span> value = ref(<span class="hljs-string">"2222"</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="hljs-comment">// Child.vue</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handlerClick"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; defineEmit, useContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    
    <span class="hljs-keyword">const</span> &#123; emit &#125; = useContext()
    
    <span class="hljs-keyword">const</span> handlerClick = <span class="hljs-function">() =></span> &#123;
        emit(<span class="hljs-string">"update:key"</span>, <span class="hljs-string">"新的key"</span>)
        emit(<span class="hljs-string">"update:value"</span>, <span class="hljs-string">"新的value"</span>)
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">provide / inject</h3>
<p>provide / inject 为依赖注入</p>
<p><code>provide</code>：可以让我们指定想要提供给后代组件的数据或</p>
<p><code>inject</code>：在任何后代组件中接收想要添加在这个组件上的数据，不管组件嵌套多深都可以直接拿来用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent.vue</span>
<script setup>
    <span class="hljs-keyword">import</span> &#123; provide &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    provide(<span class="hljs-string">"name"</span>, <span class="hljs-string">"沐华"</span>)
</script>

<span class="hljs-comment">// Child.vue</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; inject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    <span class="hljs-keyword">const</span> name = inject(<span class="hljs-string">"name"</span>)
    <span class="hljs-built_in">console</span>.log(name) <span class="hljs-comment">// 沐华</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Vuex</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store/index.js</span>
<span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(&#123;
    <span class="hljs-attr">state</span>:&#123; <span class="hljs-attr">count</span>: <span class="hljs-number">1</span> &#125;,
    <span class="hljs-attr">getters</span>:&#123;
        <span class="hljs-attr">getCount</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count
    &#125;,
    <span class="hljs-attr">mutations</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">state</span>)</span>&#123;
            state.count++
        &#125;
    &#125;
&#125;)

<span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"./store"</span>
createApp(App).use(store).mount(<span class="hljs-string">"#app"</span>)

<span class="hljs-comment">// Page.vue</span>
<span class="hljs-comment">// 方法一 直接使用</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123; $store.state.count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$store.commit('add')"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</template>

<span class="hljs-comment">// 方法二 获取</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; useStore, computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>
    <span class="hljs-keyword">const</span> store = useStore()
    <span class="hljs-built_in">console</span>.log(store.state.count) <span class="hljs-comment">// 1</span>

    <span class="hljs-keyword">const</span> count = computed(<span class="hljs-function">()=></span>store.state.count) <span class="hljs-comment">// 响应式，会随着vuex数据改变而改变</span>
    <span class="hljs-built_in">console</span>.log(count) <span class="hljs-comment">// 1 </span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">Vue2.x 组件通信方式</h2>
<p>Vue2.x 组件通信共有12种</p>
<ol>
<li>props</li>
<li>$emit / v-on</li>
<li>.sync</li>
<li>v-model</li>
<li>ref</li>
<li>$children / $parent</li>
<li>$attrs / $listeners</li>
<li>provide / inject</li>
<li>EventBus</li>
<li>Vuex</li>
<li>$root</li>
<li>slot</li>
</ol>
<p>父子组件通信可以用：</p>
<ul>
<li>props</li>
<li>$emit / v-on</li>
<li>$attrs / $listeners</li>
<li>ref</li>
<li>.sync</li>
<li>v-model</li>
<li>$children / $parent</li>
</ul>
<p>兄弟组件通信可以用：</p>
<ul>
<li>EventBus</li>
<li>Vuex</li>
<li>$parent</li>
</ul>
<p>跨层级组件通信可以用：</p>
<ul>
<li>provide/inject</li>
<li>EventBus</li>
<li>Vuex</li>
<li>$attrs / $listeners</li>
<li>$root</li>
</ul>
<h2 data-id="heading-10">Vue2.x 通信使用写法</h2>
<p>下面把每一种组件通信方式的写法一一列出</p>
<h3 data-id="heading-11">1. props</h3>
<p>父组件向子组件传送数据，这应该是最常用的方式了</p>
<p>子组件接收到数据之后，<strong>不能直接修改</strong>父组件的数据。会报错，所以当父组件重新渲染时，数据会被覆盖。如果子组件内要修改的话推荐使用 computed</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parenv.vue 传送</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">:msg</span>=<span class="hljs-string">"msg"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span></span>
</template>

<span class="hljs-comment">// Child.vue 接收</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// 写法一 用数组接收</span>
  <span class="hljs-attr">props</span>:[<span class="hljs-string">'msg'</span>],
  <span class="hljs-comment">// 写法二 用对象接收，可以限定接收的数据类型、设置默认值、验证等</span>
  <span class="hljs-attr">props</span>:&#123;
      <span class="hljs-attr">msg</span>:&#123;
          <span class="hljs-attr">type</span>:<span class="hljs-built_in">String</span>,
          <span class="hljs-attr">default</span>:<span class="hljs-string">'这是默认数据'</span>
      &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.msg)
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2. .sync</h3>
<p>可以帮我们实现父组件向子组件传递的数据 的双向绑定，所以子组件接收到数据后<strong>可以直接修改</strong>，并且会同时修改父组件的数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">:page</span>=<span class="hljs-string">"page"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">page</span>:<span class="hljs-number">1</span>
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// Child.vue</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>:[<span class="hljs-string">"page"</span>],
    <span class="hljs-function"><span class="hljs-title">computed</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 当我们在子组件里修改 currentPage 时，父组件的 page 也会随之改变</span>
        currentPage &#123;
            <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.page
            &#125;,
            <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span>&#123;
                <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"update:page"</span>, newVal)
            &#125;
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">3. v-model</h3>
<p>和 .sync 类似，可以实现将父组件传给子组件的数据为双向绑定，子组件通过 $emit 修改父组件的数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">value</span>:<span class="hljs-number">1</span>
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// Child.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"value"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"handlerChange"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>:[<span class="hljs-string">"value"</span>],
    <span class="hljs-comment">// 可以修改事件名，默认为 input</span>
    <span class="hljs-attr">model</span>:&#123;
        <span class="hljs-attr">event</span>:<span class="hljs-string">"updateValue"</span>
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">handlerChange</span>(<span class="hljs-params">e</span>)</span>&#123;
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"input"</span>, e.target.value)
            <span class="hljs-comment">// 如果有上面的重命名就是这样</span>
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"updateValue"</span>, e.target.value)
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">4. ref</h3>
<p>ref 如果在普通的DOM元素上，引用指向的就是该DOM元素;</p>
<p>如果在子组件上，引用的指向就是子组件实例，然后父组件就可以通过 ref 主动获取子组件的属性或者调用子组件的方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Child.vue</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">name</span>:<span class="hljs-string">"沐华"</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">someMethod</span>(<span class="hljs-params">msg</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(msg)
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// Parent.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"child"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> child = <span class="hljs-built_in">this</span>.$refs.child
        <span class="hljs-built_in">console</span>.log(child.name) <span class="hljs-comment">// 沐华</span>
        child.someMethod(<span class="hljs-string">"调用了子组件的方法"</span>)
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">5. $emit / v-on</h3>
<p>子组件通过派发事件的方式给父组件数据，或者触发父组件更新等操作</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Child.vue 派发</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">msg</span>: <span class="hljs-string">"这是发给父组件的信息"</span> &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"sendMsg"</span>,<span class="hljs-built_in">this</span>.msg)
      &#125;
  &#125;,
&#125;
<span class="hljs-comment">// Parenv.vue 响应</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">v-on:sendMsg</span>=<span class="hljs-string">"getChildMsg"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span></span>
    <span class="hljs-comment">// 或 简写</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">:sendMsg</span>=<span class="hljs-string">"getChildMsg"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span></span>
</template>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">getChildMsg</span>(<span class="hljs-params">msg</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(msg) <span class="hljs-comment">// 这是父组件接收到的消息</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">6. $attrs / $listeners</h3>
<p>多层嵌套组件传递数据时，如果只是传递数据，而不做中间处理的话就可以用这个，比如父组件向孙子组件传递数据时</p>
<p><code>$attrs</code>：包含父作用域里除 class 和 style 除外的非 props <strong>属性集合</strong>。通过 this.$attrs 获取父作用域中所有符合条件的属性集合，然后还要继续传给子组件内部的其他组件，就可以通过 v-bind="$attrs"</p>
<p><code>$listeners</code>：包含父作用域里 .native 除外的监听<strong>事件集合</strong>。如果还要继续传给子组件内部的其他组件，就可以通过 v-on="$linteners"</p>
<p>使用方式是相同的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"1111"</span> ></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span></span>
</template
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">name</span>:<span class="hljs-string">"沐华"</span>
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// Child.vue</span>
<template>
    <span class="hljs-comment">// 继续传给孙子组件</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">sun-child</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"$attrs"</span>></span><span class="hljs-tag"></<span class="hljs-name">sun-child</span>></span></span>
</template>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">props</span>:[<span class="hljs-string">"name"</span>], <span class="hljs-comment">// 这里可以接收，也可以不接收</span>
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 如果props接收了name 就是 &#123; title:1111 &#125;，否则就是&#123; name:"沐华", title:1111 &#125;</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$attrs)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">7. $children / $parent</h3>
<p><code>$children</code>：获取到一个包含所有子组件(不包含孙子组件)的 VueComponent 对象数组，可以直接拿到子组件中所有数据和方法等</p>
<p><code>$parent</code>：获取到一个父节点的 VueComponent 对象，同样包含父节点中所有数据和方法等</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent.vue</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$children[<span class="hljs-number">0</span>].someMethod() <span class="hljs-comment">// 调用第一个子组件的方法</span>
        <span class="hljs-built_in">this</span>.$children[<span class="hljs-number">0</span>].name <span class="hljs-comment">// 获取第一个子组件中的属性</span>
    &#125;
&#125;

<span class="hljs-comment">// Child.vue</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$parent.someMethod() <span class="hljs-comment">// 调用父组件的方法</span>
        <span class="hljs-built_in">this</span>.$parent.name <span class="hljs-comment">// 获取父组件中的属性</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">8. provide / inject</h3>
<p>provide / inject 为依赖注入，说是不推荐直接用于应用程序代码中，但是在一些插件或组件库里却是被常用，所以我觉得用也没啥，还挺好用的</p>
<p><code>provide</code>：可以让我们指定想要提供给后代组件的数据或方法</p>
<p><code>inject</code>：在任何后代组件中接收想要添加在这个组件上的数据或方法，不管组件嵌套多深都可以直接拿来用</p>
<p>要注意的是 provide 和 inject 传递的数据不是响应式的，也就是说用 inject 接收来数据后，provide 里的数据改变了，后代组件中的数据不会改变，除非传入的就是一个可监听的对象</p>
<p>所以建议还是传递一些常量或者方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-comment">// 方法一 不能获取 methods 中的方法</span>
    <span class="hljs-attr">provide</span>:&#123;
        <span class="hljs-attr">name</span>:<span class="hljs-string">"沐华"</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-built_in">this</span>.data中的属性
    &#125;,
    <span class="hljs-comment">// 方法二 不能获取 data 中的属性</span>
    <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">name</span>:<span class="hljs-string">"沐华"</span>,
            <span class="hljs-attr">someMethod</span>:<span class="hljs-built_in">this</span>.someMethod <span class="hljs-comment">// methods 中的方法</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">someMethod</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"这是注入的方法"</span>)
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 后代组件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">inject</span>:[<span class="hljs-string">"name"</span>,<span class="hljs-string">"someMethod"</span>],
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
        <span class="hljs-built_in">this</span>.someMethod()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">9. EventBus</h3>
<p>EventBus 是中央事件总线，不管是父子组件，兄弟组件，跨层级组件等都可以使用它完成通信操作</p>
<p>定义方式有三种</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 方法一</span>
<span class="hljs-comment">// 抽离成一个单独的 js 文件 Bus.js ，然后在需要的地方引入</span>
<span class="hljs-comment">// Bus.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vue()

<span class="hljs-comment">// 方法二 直接挂载到全局</span>
<span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
Vue.prototype.$bus = <span class="hljs-keyword">new</span> Vue()

<span class="hljs-comment">// 方法三 注入到 Vue 根对象上</span>
<span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">Bus</span>: <span class="hljs-keyword">new</span> Vue()
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用如下，以方法一按需引入为例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在需要向外部发送自定义事件的组件内</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handlerClick"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</template>
<span class="hljs-keyword">import</span> Bus <span class="hljs-keyword">from</span> <span class="hljs-string">"./Bus.js"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">handlerClick</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-comment">// 自定义事件名 sendMsg</span>
            Bus.$emit(<span class="hljs-string">"sendMsg"</span>, <span class="hljs-string">"这是要向外部发送的数据"</span>)
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 在需要接收外部事件的组件内</span>
<span class="hljs-keyword">import</span> Bus <span class="hljs-keyword">from</span> <span class="hljs-string">"./Bus.js"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 监听事件的触发</span>
        Bus.$on(<span class="hljs-string">"sendMsg"</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"这是接收到的数据："</span>, data)
        &#125;)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">beforeDestroy</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 取消监听</span>
        Bus.$off(<span class="hljs-string">"sendMsg"</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">10. Vuex</h3>
<p>Vuex 是状态管理器，集中式存储管理所有组件的状态。这一块内容过长，如果基础不熟的话可以看这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuex.vuejs.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuex.vuejs.org/zh/" ref="nofollow noopener noreferrer">Vuex</a>，然后大致用法如下</p>
<p>比如创建这样的文件结构</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2f14ac26fad4d2b8fdba288865c2916~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210824003500.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>index.js 里内容如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> getters <span class="hljs-keyword">from</span> <span class="hljs-string">'./getters'</span>
<span class="hljs-keyword">import</span> actions <span class="hljs-keyword">from</span> <span class="hljs-string">'./actions'</span>
<span class="hljs-keyword">import</span> mutations <span class="hljs-keyword">from</span> <span class="hljs-string">'./mutations'</span>
<span class="hljs-keyword">import</span> state <span class="hljs-keyword">from</span> <span class="hljs-string">'./state'</span>
<span class="hljs-keyword">import</span> user <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules/user'</span>

Vue.use(Vuex)

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">modules</span>: &#123;
    user
  &#125;,
  getters,
  actions,
  mutations,
  state
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 main.js 引入</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"./store"</span>
<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
    store,
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在需要的使用组件里</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapGetters, mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">computed</span>:&#123;
        <span class="hljs-comment">// 方式一 然后通过 this.属性名就可以用了</span>
        ...mapGetters([<span class="hljs-string">"引入getters.js里属性1"</span>,<span class="hljs-string">"属性2"</span>])
        <span class="hljs-comment">// 方式二</span>
        ...mapGetters(<span class="hljs-string">"user"</span>, [<span class="hljs-string">"user模块里的属性1"</span>,<span class="hljs-string">"属性2"</span>])
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-comment">// 方式一 然后通过 this.属性名就可以用了</span>
        ...mapMutations([<span class="hljs-string">"引入mutations.js里的方法1"</span>,<span class="hljs-string">"方法2"</span>])
        <span class="hljs-comment">// 方式二</span>
        ...mapMutations(<span class="hljs-string">"user"</span>,[<span class="hljs-string">"引入user模块里的方法1"</span>,<span class="hljs-string">"方法2"</span>])
    &#125;
&#125;

<span class="hljs-comment">// 或者也可以这样获取</span>
<span class="hljs-built_in">this</span>.$store.state.xxx
<span class="hljs-built_in">this</span>.$store.state.user.xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">11. $root</h3>
<p><code>$root</code> 可以拿到 App.vue 里的数据和方法</p>
<h3 data-id="heading-22">12. slot</h3>
<p>就是把子组件的数据通过插槽的方式传给父组件使用，然后再插回来</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Child.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">:user</span>=<span class="hljs-string">"user"</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">user</span>:&#123; <span class="hljs-attr">name</span>:<span class="hljs-string">"沐华"</span> &#125;
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// Parent.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"slotProps"</span>></span>
            &#123;&#123; slotProps.user.name &#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">child</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">结语</h2>
<p>写作不易，你的一赞一评，就是我前行的最大动力。</p></div>  
</div>
            