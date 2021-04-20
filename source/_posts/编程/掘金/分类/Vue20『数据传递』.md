
---
title: 'Vue2.0『数据传递』'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4837'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 09:13:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=4837'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>总结:</p>
<p>1.子组件$emit抛出 父组件响应</p>
<pre><code class="hljs language-js copyable" lang="js">   给子组件绑定自定义事件：
   <father @fn=fn :data=数据> </father>
   <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params">data</span>)</span> &#123;
       <span class="hljs-built_in">this</span>.data = data
   &#125;
   子组件内部触发自定义事件：
   poper：&#123;
       value：number
   &#125;
   <span class="hljs-built_in">this</span>.emit(<span class="hljs-string">'fn'</span>, 数据)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.父组件v-model响应 子组件抛出input事件 接收value参数 可以通过model参数配置响应事件与接收参数</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-number">1.</span> <father v-model = value > </father>
   poper：&#123;
       value：number
   &#125;
   子组件内部触发自定义事件：<span class="hljs-built_in">this</span>.emit(<span class="hljs-string">'input'</span>, 数据)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.父组件xx.sync="xx"也是双向绑定 子组件$emit('update:xx')抛出</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-number">1.</span> <father :updata:value = <span class="hljs-function"><span class="hljs-params">value</span> =></span> <span class="hljs-built_in">this</span>.data = value :data=数据> </father>
   poper：&#123;
       data：number
   &#125;
   子组件内部触发自定义事件：<span class="hljs-built_in">this</span>.emit(<span class="hljs-string">'updata:value'</span>, 数据)
   <span class="hljs-number">2.</span> <father :value.sync = 数据 :data=数据 > </father> 同步设置data
   poper：&#123;
       data：number
   &#125;
   子组件内部触发自定义事件：<span class="hljs-built_in">this</span>.emit(<span class="hljs-string">'updata:value'</span>, 数据)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.可以通过扩展函数在原型上绑定广播/派发这个是在1.0中有的，但是2.0去除了，原理就是通过<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>c</mi><mi>h</mi><mi>i</mi><mi>l</mi><mi>d</mi><mi>r</mi><mi>e</mi><mi>n</mi></mrow><annotation encoding="application/x-tex">children </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">d</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span></span></span></span></span>parent循环emit事件</p>
<pre><code class="hljs language-js copyable" lang="js">   $parent：父组件内容
   $children[<span class="hljs-number">0</span>]：第一个子组件内容
   <span class="hljs-built_in">this</span>.$parent.$emit(<span class="hljs-string">'自定义事件'</span>, 数据)
   <span class="hljs-built_in">this</span>.$children.$emit(<span class="hljs-string">'自定义事件'</span>, 数据)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.重新创建一个实例实现eventBus事件总线 原理为在新的实例上通过<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>o</mi><mi>n</mi></mrow><annotation encoding="application/x-tex">on </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span></span></span></span></span>emit传递与响应</p>
<pre><code class="hljs language-js copyable" lang="js">    实例化组件：vue.prototypr.$enentBus = <span class="hljs-keyword">new</span> Vue()
    实例化组件绑定事件：<span class="hljs-built_in">this</span>.$eventBus.$on(<span class="hljs-string">'绑定的事件'</span>, （）=> &#123;&#125;)
    触发实例化组件事件：<span class="hljs-built_in">this</span>.$eventBus.$emit(<span class="hljs-string">'绑定的事件'</span>, 数据)
    注意：
        <span class="hljs-number">1.</span>事件触发不能早于事件绑定
        <span class="hljs-number">2.</span>可以用$nextTick解决
        <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.$eventBus.$emit(<span class="hljs-string">'绑定的事件'</span>, 数据)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.传递参数时可以用v-bind/<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mtext>传递传递函数可以用</mtext><mi>v</mi><mo>−</mo><mi>o</mi><mi>n</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">attrs传递 传递函数可以用v-on/</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">传</span><span class="mord cjk_fallback">递</span><span class="mord cjk_fallback">传</span><span class="mord cjk_fallback">递</span><span class="mord cjk_fallback">函</span><span class="mord cjk_fallback">数</span><span class="mord cjk_fallback">可</span><span class="mord cjk_fallback">以</span><span class="mord cjk_fallback">用</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord">/</span></span></span></span></span>listeners</p>
<pre><code class="hljs language-js copyable" lang="js">    $attrs：组件的数据
    $listeners：组件的方法
    <father v-bind = $attrs v-on=$listeners> </father>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7.通过provide inject传递函数与参数</p>
<pre><code class="hljs language-js copyable" lang="js">    父组件注入
    <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params"></span>)</span> &#123;
     <span class="hljs-keyword">return</span> &#123;
         grandpa：<span class="hljs-built_in">this</span>
     &#125;
    &#125;
    子组件消费
    <span class="hljs-attr">inject</span>:[
        <span class="hljs-string">'geandpa'</span>
    ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8.通过ref来获取组件实例，ref不能再template上使用，compute也不能用</p>
<pre><code class="hljs language-js copyable" lang="js">     ref dom元素 dom对象
     ref 组件 组件实例
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不建议用<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">parent/</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord">/</span></span></span></span></span>children 以及组件派发/广播，dispatch1.0是有得，2.0就没有了，因为这样结构不清晰</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            