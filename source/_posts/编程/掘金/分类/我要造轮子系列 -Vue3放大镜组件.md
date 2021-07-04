
---
title: '我要造轮子系列 -Vue3放大镜组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d1811c4c13a41ef93939b753f401cfd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 07:41:09 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d1811c4c13a41ef93939b753f401cfd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>系列前几个组件都是用vue2编写的，这次用最新的vue3编写, vue3也出了一段时间，公司也不会牟然换版本，所以很少实践的机会，那就只能够自己写一个组件实践下，看了一下vue3的文档，最大变化，就是setup函数和Composition Api这块，这次我主要也是说说这部分的使用过程。</p>
<p>另外组件也是常用的组件，一般用在电商类网站产品详情页，鼠标移到图片位置放大图片，具体怎实现就不详说 如图:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d1811c4c13a41ef93939b753f401cfd~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-07-03 下午10.25.38.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">说说Vue3 Composition Api</h2>
<p>vue2中,我们会在methods，computed，watch，data中等等定义属性和方法，共同处理页面逻辑，我们称这种方式为Options API。相信用过的都知道，方便是挺方便，不过缺点也很明显，当项目越来越大，很可能一个methods下就有二三十个方法， 还得确切地知道方法中可以访问哪些属性以及this关键字的行为，维护起来就十分麻烦了。Composition API（组合API）就是解决这个问题而生的。另外vue3是向下兼容的，也就是说允许我们用vue2的写法在vue3写，但既然是个新东西，我们就要尝试体验，看看有什么改变给自己带来什么便利。</p>
<p>Composition API它类似 react hooks写法。这次我直接用 setup 的语法糖编写这个组件。</p>
<h2 data-id="heading-2">setup 语法糖</h2>
<p>什么是setup 语法糖？想要使用 <code>setup</code> 模式只要在 <code>script</code> 标签上面加个 <code>setup</code> 属性就可以了。这个模式下不需要 <code>return</code> 和 <code>export</code> 就可以在模板中使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><script setup>
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">编写组件</h2>
<p>先上组件完整代码</p>
<pre><code class="hljs language-js copyable" lang="js">
<script setup>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"imgBox"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"imgbox"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask"</span>
             <span class="hljs-attr">v-show</span>=<span class="hljs-string">"state.isShow"</span>
             <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;
                 left:state.maskX + 'px',
             top :state.maskY +'px'&#125;"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fade"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"zoomBox"</span>
         <span class="hljs-attr">v-show</span>=<span class="hljs-string">"state.isShow"</span>
         <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;left :state.boxX +'px',top: state.boxY +'px',&#125;"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"state.imgSrc"</span>
             <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;
                width:state.zoomImgWidth + 'px',
                height: state.zoomImgHeight + 'px',
                marginLeft :-state.bImgX + 'px',
                marginTop : -state.bImgY + 'px'
               &#125;"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123;defineProps, onMounted, onUnmounted, reactive, ref&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
    <span class="hljs-keyword">const</span> maskWidth = <span class="hljs-number">50</span>,
    maskHeight = <span class="hljs-number">50</span>
    <span class="hljs-keyword">const</span> imgbox = ref(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> props = defineProps(&#123;<span class="hljs-attr">mode</span>: <span class="hljs-built_in">String</span>&#125;)
    <span class="hljs-keyword">const</span> state = reactive(&#123;
        <span class="hljs-attr">zoomImgWidth</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">zoomImgHeight</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">boxX</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">boxY</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">maskX</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">maskY</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">bImgX</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">bImgY</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">imgSrc</span>: <span class="hljs-string">''</span>
    &#125;)
    <span class="hljs-keyword">const</span> zommIn = <span class="hljs-function">(<span class="hljs-params">ev</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> img = ev.currentTarget.getElementsByTagName(<span class="hljs-string">'img'</span>)[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">const</span> &#123;offsetWidth, offsetTop, offsetHeight&#125; = imgbox.value
        state.zoomImgWidth = offsetWidth * <span class="hljs-number">3</span>
        state.zoomImgHeight = offsetHeight * <span class="hljs-number">3</span>
        state.imgSrc = img.src
        state.boxX = offsetWidth
        state.boxY = offsetTop
        state.isShow = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-keyword">const</span> zoomMove = <span class="hljs-function">(<span class="hljs-params">ev</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> &#123;clientX, clientY&#125; = ev
        <span class="hljs-keyword">const</span> &#123;offsetTop, offsetLeft&#125; = ev.currentTarget
        <span class="hljs-keyword">const</span> &#123;offsetWidth, offsetHeight&#125; = imgbox.value
        <span class="hljs-keyword">let</span> mx = clientX - offsetLeft - (maskWidth / <span class="hljs-number">2</span>),
            my = clientY - offsetTop - (maskHeight / <span class="hljs-number">2</span>)
        mx = mx < <span class="hljs-number">0</span> ? <span class="hljs-number">0</span> : mx
        my = my < <span class="hljs-number">0</span> ? <span class="hljs-number">0</span> : my
        <span class="hljs-keyword">if</span> (mx > offsetWidth - maskWidth / <span class="hljs-number">2</span>) &#123;
            mx = offsetWidth - maskWidth / <span class="hljs-number">2</span>
        &#125;
        <span class="hljs-keyword">if</span> (my > offsetHeight - maskHeight / <span class="hljs-number">2</span>) &#123;
            my = offsetHeight - maskHeight / <span class="hljs-number">2</span>
        &#125;
        state.maskX = mx
        state.maskY = my

        state.bImgX = mx * (state.zoomImgWidth - offsetWidth) / (offsetWidth - maskWidth)
        state.bImgY = my * (state.zoomImgWidth - offsetWidth) / (offsetWidth - maskWidth)
    &#125;
    <span class="hljs-keyword">const</span> zommOut = <span class="hljs-function">() =></span> &#123;
        state.isShow = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-comment">//绑定方法</span>
    onMounted(<span class="hljs-function">() =></span> &#123;
        imgbox.value.addEventListener(<span class="hljs-string">'mouseover'</span>, zommIn)
        imgbox.value.addEventListener(<span class="hljs-string">'mousemove'</span>, zoomMove)
        imgbox.value.addEventListener(<span class="hljs-string">'mouseout'</span>, zommOut)
    &#125;)
    onUnmounted(<span class="hljs-function">() =></span> &#123;
        imgbox.value.removeEventListener(<span class="hljs-string">'mouseover'</span>, <span class="hljs-function">()=></span>&#123;&#125;)
        imgbox.value.removeEventListener(<span class="hljs-string">'mousemove'</span>, <span class="hljs-function">()=></span>&#123;&#125;)
        imgbox.value.removeEventListener(<span class="hljs-string">'mouseout'</span>, <span class="hljs-function">()=></span>&#123;&#125;)
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
    <span class="hljs-selector-class">.mask</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">opacity</span>: .<span class="hljs-number">6</span>;
        <span class="hljs-attribute">cursor</span>: crosshair;
        <span class="hljs-attribute">position</span>: absolute;
    &#125;

    <span class="hljs-selector-class">.imgBox</span> &#123;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">overflow</span>: hidden;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
    &#125;

    <span class="hljs-selector-class">.zoomBox</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#eee</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">overflow</span>: hidden;
    &#125;
    <span class="hljs-selector-class">.fade-enter-active</span>, <span class="hljs-selector-class">.fade-leave-active</span> &#123;
        <span class="hljs-attribute">transition</span>: opacity .<span class="hljs-number">5s</span>
    &#125;
    <span class="hljs-selector-class">.fade-enter</span>, <span class="hljs-selector-class">.fade-leave-active</span> &#123;
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到这种模式编程，不就是函数式编程吗！！接下来我就说说我是怎样使用这些API</p>
<p>1.依赖注入<code>defineProps</code>, <code>onMounted</code>, <code>onUnmounted</code>, <code>reactive</code>, <code>ref</code>
这些函数都是在这个组件用到的，看到函数的命名，是不是有点似曾相识的感觉呢，没错，除了<code>reactive</code>比较陌生 其他就是你想的！</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">import</span> &#123;defineProps, onMounted, onUnmounted, reactive, ref&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.<code>defineProps</code> 这个相当于props,组件传入的参数,然后通过保存props变量读取</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> props = defineProps(&#123;<span class="hljs-attr">mode</span>: <span class="hljs-built_in">String</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>reactive</code> 这个方式类似于我们设置的data选项， 但绑定到模板上就需要带上<code>state</code> 这个函数目的是为了观察引用数据类型。想直接绑定变量到模板上可以通过<code>toRefs</code>解构模板变量。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">       <span class="hljs-keyword">const</span> state = reactive(&#123;
        <span class="hljs-attr">zoomImgWidth</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">zoomImgHeight</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">boxX</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">boxY</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">maskX</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">maskY</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">bImgX</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">bImgY</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">imgSrc</span>: <span class="hljs-string">''</span>
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.<code>ref</code>这个也是类似设置data的选项, 但它一般是观察原始数据类型,另外还可以类似vue2通过绑定ref获取dom信息，这次的ref我也是用在获取dom信息，当然你也可以用来设置可观察数据</p>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-comment">// 绑定ref</span>
    <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"imgBox"</span> ref=<span class="hljs-string">"imgbox"</span>></div>
    <span class="hljs-comment">//获取dom信息</span>
    <span class="hljs-keyword">const</span> imgbox = ref(<span class="hljs-literal">null</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.<code>onMounted</code> 和 <code>onUnmounted</code> 这两个方法类似 mounted 的钩子函数，
相信熟悉vue的对钩子应该也不会陌生，这里我直接做事件监听</p>
<pre><code class="hljs language-js copyable" lang="js">onMounted(<span class="hljs-function">() =></span> &#123;
        imgbox.value.addEventListener(<span class="hljs-string">'mouseover'</span>, zommIn)
        imgbox.value.addEventListener(<span class="hljs-string">'mousemove'</span>, zoomMove)
        imgbox.value.addEventListener(<span class="hljs-string">'mouseout'</span>, zommOut)
    &#125;)
    onUnmounted(<span class="hljs-function">() =></span> &#123;
        imgbox.value.removeEventListener(<span class="hljs-string">'mouseover'</span>, <span class="hljs-function">()=></span>&#123;&#125;)
        imgbox.value.removeEventListener(<span class="hljs-string">'mousemove'</span>, <span class="hljs-function">()=></span>&#123;&#125;)
        imgbox.value.removeEventListener(<span class="hljs-string">'mouseout'</span>, <span class="hljs-function">()=></span>&#123;&#125;)
    &#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">组件调用</h2>
<p>组件调用也简化了，直接<code>import</code>进来，不用在<code>components</code>注册组件。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">import</span>  zoom  <span class="hljs-keyword">from</span>  <span class="hljs-string">'./components/zoom.vue'</span>
      <zoom>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"Vue logo"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./assets/logo.png"</span>/></span></span>
    </zoom>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">最后</h2>
<p>vue3还提供很多api 在这个组件没用到 ，如emit、watch、computed、provide、inject、还有各生命周期钩子函数，这些都是在vue2 熟悉的东西 ，但在vue3允许你用其他形式来编写，喜欢这种编写方式，就会感觉写得很爽。 对于用react的同学也是可以无缝接入，很快就可以上手，反之在vue3用过Composition Api的同学去学习react hooks 也是很容易上手。</p></div>  
</div>
            