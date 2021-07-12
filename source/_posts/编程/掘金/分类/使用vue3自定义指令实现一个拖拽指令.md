
---
title: '使用vue3自定义指令实现一个拖拽指令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b794270fed42489caf72011c1beb29ea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 19:40:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b794270fed42489caf72011c1beb29ea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">自定义指令-拖拽</h1>
<h2 data-id="heading-1">前言</h2>
<p>vue3正式版已经发布大半年了,咱也得紧跟时代潮流,vue3带来的很多改变,使用ts重写代码,在兼容vue2语法的基础上,增加了很多新语法,比如新增了组合api,也移除了一些旧语法</p>
<h2 data-id="heading-2">什么是自定义指令</h2>
<p>vue提供了很多内置的指令例如 v-model,v-show,v-for 等,这些指令极大的帮助我们提示开发效率,除了这些内置指令,vue也允许我们自定义自己的指令,vue3升级后,为了更好的与组件生命周期保持一致,指令的钩子函数被重命名了</p>
<h2 data-id="heading-3">2.x语法</h2>
<ul>
<li>bind - 指令绑定到元素后发生。只发生一次。</li>
<li>inserted - 元素插入父 DOM 后发生。</li>
<li>update - 当元素更新，但子元素尚未更新时，将调用此钩子。</li>
<li>componentUpdated - 一旦组件和子级被更新，就会调用这个钩子。</li>
<li>unbind - 一旦指令被移除，就会调用这个钩子。也只调用一次。</li>
</ul>
<h2 data-id="heading-4">3.x语法</h2>
<ul>
<li>created - 新的！在元素的 attribute 或事件侦听器应用之前调用。</li>
<li>bind → beforeMount</li>
<li>inserted → mounted</li>
<li>beforeUpdate：新的！这是在元素本身更新之前调用的，很像组件生命周期钩子。</li>
<li>update → 移除！有太多的相似之处要更新，所以这是多余的，请改用 updated。</li>
<li>componentUpdated → updated</li>
<li>beforeUnmount：新的！与组件生命周期钩子类似，它将在卸载元素之前调用。</li>
<li>unbind -> unmounted</li>
</ul>
<h2 data-id="heading-5">实现一个拖拽指令</h2>
<p>先创建一个vue项目,根据自己喜好配置项目,我选择的是ts</p>
<pre><code class="hljs language-js copyable" lang="js">npm install -g @vue/cli
vue create my-project
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">先创建一个需要拖拽的小方块</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./style.scss"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Drag"</span>,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"rect"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
  &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">样式scss</h3>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.rect</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background-color</span>:peru;
  <span class="hljs-attribute">position</span>: absolute;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b794270fed42489caf72011c1beb29ea~tplv-k3u1fbpfcp-watermark.image" alt="1625743340(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">clientX,clientY,offsetLeft,offsetTop</h3>
<p>实现拖拽需要用到以下属性</p>
<ul>
<li>clientX和clientY是一个只读属性,可以获取当前鼠标在客户端的水平坐标 (与页面坐标不同),如点击页面左上角为0,无论是否出现滚动条</li>
<li>offsetLeft.offsetTop 只读属性,返回当前元素相对于  HTMLElement.offsetParent 节点的左边界偏移的像素值</li>
</ul>
<h3 data-id="heading-9">自定义指令局部注册</h3>
<p>可以在当前实例上添加directives属性来实现自定义指令,先初始化一个drag指令,这样我们就可以在vue里使用v-drag</p>
<pre><code class="hljs language-js copyable" lang="js">  name: <span class="hljs-string">"Drag"</span>,
  <span class="hljs-attr">directives</span>: &#123;
    <span class="hljs-attr">drag</span>: &#123;
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为需要操作dom实例,所以我们使用mounted这个钩子函数,并给当前el添加鼠标按下事件,并记录当前鼠标按下坐标mouseXStart,mouseYStart和当前滑块距离当前父节点的偏移量rectLeft,rectTop,再按下后,我们给document添加鼠标移动事件,每次移动记录当前鼠标坐标,滑块移动的距离就是mouseXEnd - mouseXStart + rectLeft和mouseYEnd - mouseYStart + rectTop,在鼠标抬起后,将move事件清空,不然会一直移动(这里要注意的是我给document添加监听事件,是因为如果给滑块添加事件,当鼠标移动过快,鼠标移出el会出现计算错误)</p>
<pre><code class="copyable">export default defineComponent(&#123;
  name: "Drag",
  directives: &#123;
    drag: &#123;
      mounted(el: HTMLDivElement) &#123;
        el.onmousedown = (ev) => &#123;
          console.log(ev);
          // 鼠标按下的位置
          const mouseXStart = ev.clientX;
          const mouseYStart = ev.clientY;
          console.log("按下开始", mouseXStart, mouseYStart);
          // 当前滑块位置
          const rectLeft = el.offsetLeft;
          const ,rectTop = el.offsetTop;
          document.onmousemove = (e) => &#123;
            // 鼠标移动的位置
            const mouseXEnd = e.clientX;
            const mouseYEnd = e.clientY;
            const moveX = mouseXEnd - mouseXStart + rectLeft;
            const moveY = mouseYEnd - mouseYStart + rectTop;
            console.log(rectLeft, rectTop);
            el.style["top"] = moveY + "px";
            el.style["left"] = moveX + "px";
          &#125;;
          document.onmouseup = () => &#123;
            console.log("鼠标抬起");
            // 取消事件
            document.onmousemove = null;
          &#125;;
        &#125;;
      &#125;,
    &#125;,
  &#125;,
  render() &#123;
    return <div class="rect" v-drag></div>;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">这样就实现了一个简单的拖拽指令</h3>
<p>第一次写文章,大佬们轻点喷</p></div>  
</div>
            