
---
title: 'vue3实现一个Toast组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c61995623daa48ec8da7f403ffb58e07~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 01:35:00 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c61995623daa48ec8da7f403ffb58e07~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在实现组件之前我们需要了解如下知识点：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.cn.vuejs.org%2Fguide%2Frender-function.html%23h-%25E5%258F%2582%25E6%2595%25B0" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.cn.vuejs.org/guide/render-function.html#h-%E5%8F%82%E6%95%B0" ref="nofollow noopener noreferrer">createVNode的用法</a></li>
<li>render（查阅源码发现的方法，api未体现）</li>
</ul>
<p>接下来开始写代码</p>
<p>在 src/components下创建toast文件夹，并依此创建index.vue和index.ts</p>
<h2 data-id="heading-0">创建模版index.vue</h2>
<p><strong>编写index.vue创建模版</strong></p>
<p>一般toast会有如下功能：</p>
<ul>
<li>背景色</li>
<li>字体颜色</li>
<li>文本</li>
<li>停留时间</li>
</ul>
<p>...
那么自然可以写出如下代码：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
<div class="toast-box" >
    <p class="toast-value" :style="&#123;background: background, color: color&#125;">
        &#123;&#123; value &#125;&#125;
    </p> 
</div>
</template>    
<script lang="ts">
    import &#123; defineComponent &#125; from 'vue'
    export default defineComponent(&#123;
        name: 'Toast',
        props: &#123;
            value: &#123;
                type: String,
                default: ''
            &#125;,
            duration: &#123;
                type: Number,
                default: 3000
            &#125;,
            background: &#123;
                type: String,
                default: '#000'
            &#125;,
            color: &#123;
                type: String,
                default: '#fff'
            &#125;
        &#125;
    &#125;)
</script>

<style>
.toast-box  &#123;
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
&#125;
    .toast-value &#123;
        max-width: 100px;
        background: rgb(8, 8, 8);
        padding: 8px 10px;
        border-radius: 4px;
        text-align: center;
        display: inline-block;
        animation: anim 0.5s;
    &#125;
    @keyframes anim &#123; 
            0% &#123;opacity: 0;&#125;
            100%&#123;opacity:1;
        &#125;
    &#125;
    .toast-value.reomve &#123;
        animation: reomve 0.5s;
    &#125;
     @keyframes reomve &#123; 
            0% &#123;opacity: 1;&#125;
            100%&#123;opacity:0;
        &#125;
    &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">导出Toast方法</h2>
<p>思路</p>
<ul>
<li>创建时
<ul>
<li>首先使用<code>createVNode</code>方法创建一个<code>vNode</code>独享</li>
<li>使用<code>render</code>方法转换成真实<code>dom</code></li>
<li>添加到<code>body</code>上</li>
</ul>
</li>
<li>销毁时
<ul>
<li>首先添加一个淡入淡出效果</li>
<li>使用<code>render</code>将真实设置为<code>null</code></li>
<li>移除创建的dom</li>
</ul>
</li>
</ul>
<p>具体代码实现如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createVNode, render &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> toastTemplate <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> IProps &#123;
    value?: <span class="hljs-built_in">string</span>;
    duration?: <span class="hljs-built_in">number</span>;
    background?: <span class="hljs-built_in">string</span>;
    color?: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">const</span> defaultOpt = &#123; <span class="hljs-comment">// 创建默认参数</span>
    <span class="hljs-attr">duration</span>: <span class="hljs-number">3000</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> ResultParams &#123;
    destory?: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>;
&#125;
<span class="hljs-comment">// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types</span>
<span class="hljs-keyword">const</span> Toast = (options: IProps):<span class="hljs-function"><span class="hljs-params">ResultParams</span> =></span> &#123;
    <span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
    <span class="hljs-keyword">const</span> opt = &#123;...defaultOpt,...options&#125;
    <span class="hljs-keyword">const</span> vm = createVNode(toastTemplate, opt) <span class="hljs-comment">// 创建vNode</span>
    render(vm, container)
    <span class="hljs-built_in">document</span>.body.appendChild(container)       <span class="hljs-comment">// 添加到body上</span>
    <span class="hljs-keyword">const</span> destory =  <span class="hljs-function">()=></span> &#123;
        <span class="hljs-keyword">const</span> dom = vm.el <span class="hljs-keyword">as</span> HTMLDivElement
        <span class="hljs-keyword">if</span>(dom.querySelector(<span class="hljs-string">'.toast-value'</span>)) &#123;
            dom.querySelector(<span class="hljs-string">'.toast-value'</span>)?.classList.add(<span class="hljs-string">'reomve'</span>) <span class="hljs-comment">// 销毁时添加淡入淡出效果</span>
            <span class="hljs-keyword">const</span> t = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;             <span class="hljs-comment">// 淡入淡出效果之后删除dom节点</span>
                render(<span class="hljs-literal">null</span>, container)
                <span class="hljs-built_in">document</span>.body.removeChild(container)
                <span class="hljs-built_in">clearTimeout</span>(t)
            &#125;,<span class="hljs-number">500</span>);
        &#125; 
    &#125;
    <span class="hljs-keyword">if</span>(opt.duration) &#123;                            <span class="hljs-comment">// 如果传入的值为0可以持续保留在页面，需要手动销毁</span>
        <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
            destory()
            <span class="hljs-built_in">clearTimeout</span>(timer)
        &#125;, opt.duration)
    &#125;
    <span class="hljs-keyword">return</span> &#123;
        destory
    &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Toast
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">测试</h2>
<p>在任意vue页面引入刚完成的<code>Toast</code>方法,进行调用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="home">
   测试toast
  </div>
</template>

<script lang="ts">
import &#123; defineComponent, onMounted &#125; from 'vue';
import Toast from '@/components/toast'; // @ is an alias to /src

export default defineComponent(&#123;
  name: 'Home',
  setup() &#123;
    onMounted(()=> &#123;
      const toast = Toast(&#123;
        value: 'toast',
        duration: 0, // 如果大于0则不必使用destory方法
        background: '#000',
        color: '#fff'
      &#125;)
      setTimeout(() => &#123;
        toast.destory && toast.destory()
      &#125;, 3000);
     
    &#125;)
    
  &#125;
&#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c61995623daa48ec8da7f403ffb58e07~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
销毁
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8facd7e6563f4c7cba85c80737cb7199~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">写在最后</h2>
<p>相比较vue2的实现方式，整体思路差不多主要是api的变化</p></div>  
</div>
            