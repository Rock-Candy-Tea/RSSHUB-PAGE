
---
title: '《巧用provide和inject完成精巧的tab组件》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d02e1a138f24094a45dbe7d1e0bb36b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 04:27:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d02e1a138f24094a45dbe7d1e0bb36b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">目标：</h4>
<p>希望用户如下使用代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><m-tabs>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">m-tabs-nav</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab1"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-item</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab2"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-item</span>></span>
<span class="hljs-tag"></<span class="hljs-name">m-tabs-nav</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">m-tabs-content</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-pane</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab1"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-pane</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-pane</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab2"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-pane</span>></span>
<span class="hljs-tag"></<span class="hljs-name">m-tabs-content</span>></span></span>
</m-tabs>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们就来创建5个组件</p>
<h1 data-id="heading-1">思路分析：</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d02e1a138f24094a45dbe7d1e0bb36b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>爷爷组件tabs 有数据 selectedTag, 然后会向head和Body传值，然后，head会向自己的三个孩子传值，body会向自己的三个孩子传值</p>
<p>这里我们可以用到provide和inject</p>
<p>provide 选项允许我们指定我们想要提供给后代组件的数据/方法</p>
<p>然后在任何后代组件里，我们都可以使用 inject 选项来接收指定的我们想要添加在这个实例上的 property.</p>
<p>由于爷爷、爸爸、孙子三者之间的信息传递较为复杂，我们选择用eventbus来减少复杂</p>
<h1 data-id="heading-2">用new Vue()做EventBus</h1>
<p>如果一个对象可以<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi>m</mi><mi>i</mi><mi>t</mi><mo separator="true">,</mo></mrow><annotation encoding="application/x-tex">emit, </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.85396em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal">m</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mpunct">,</span></span></span></span></span>on, $off就是一个eventBus</p>
<pre><code class="hljs language-js copyable" lang="js">Tab.vue
@Component
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Tab</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vue</span> </span>&#123;
  ...
    eventBus = <span class="hljs-keyword">new</span> Vue();

    @Provide(<span class="hljs-string">'eventbus'</span>) eventbus: Vue = <span class="hljs-built_in">this</span>.eventBus;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>爷爷provide, 然后儿子、孙子里inject</p>
<pre><code class="hljs language-js copyable" lang="js"> @Component
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TabHead</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vue</span> </span>&#123;
    @Inject() eventbus!: Vue;
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'爷爷给爸爸的eventBus'</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.eventbus)
&#125;

  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">@Component
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TabItem</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vue</span> </span>&#123;
    @Inject() eventbus!: Vue;
    @Prop(<span class="hljs-built_in">String</span>) name: string | <span class="hljs-literal">undefined</span>;

    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"爷爷给tab item的eventbus"</span>)
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.eventBus)
      <span class="hljs-built_in">this</span>.eventbus.$on(<span class="hljs-string">'update:selected'</span>, <span class="hljs-function">(<span class="hljs-params">name: string</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(name);
      &#125;);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">到底是谁在触发，谁在监听？</h1>
<p>this.$emit 是当前实例在触发</p>
<p>this.eventBus.$emit 是eventBus这个对象本身在触发，注意两者的区别</p>
<p>在vue中，事件并不会冒泡，我们需要关注是在哪个对象上触发的事件</p>
<h2 data-id="heading-4">问题一：</h2>
<pre><code class="hljs language-js copyable" lang="js"><m-tabs @update:selected=<span class="hljs-string">"yyy"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">m-tabs-nav</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab1"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-item</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab2"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-item</span>></span>
<span class="hljs-tag"></<span class="hljs-name">m-tabs-nav</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">m-tabs-content</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-pane</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab1"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-pane</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-pane</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab2"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-pane</span>></span>
<span class="hljs-tag"></<span class="hljs-name">m-tabs-content</span>></span></span>
</m-tabs>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件之间用eventBus触发和监听事件，那么爷爷上的@update:selected="yyy"事件会被触发吗？</p>
<p>答案是不会！因为eventBus触发的事件和这个组件没有关系</p>
<h2 data-id="heading-5">问题二：</h2>
<pre><code class="hljs language-js copyable" lang="js"><m-tabs @update:selected=<span class="hljs-string">"yyy"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">m-tabs-nav</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab1"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-item</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab2"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-item</span>></span>
<span class="hljs-tag"></<span class="hljs-name">m-tabs-nav</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">m-tabs-content</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-pane</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab1"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-pane</span>></span>
<span class="hljs-tag"><<span class="hljs-name">m-tabs-pane</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"tab2"</span>></span><span class="hljs-tag"></<span class="hljs-name">m-tabs-pane</span>></span>
<span class="hljs-tag"></<span class="hljs-name">m-tabs-content</span>></span></span>
</m-tabs>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在上触发同名事件@update:selected，请问爷爷组件上的@update:selected事件会被触发吗？</p>
<p>答案是不会，在vue里事件是不会冒泡的</p>
<h2 data-id="heading-6">小结：</h2>
<ol>
<li>在哪个对象触发事件，就在那个对象上监听</li>
<li>vue里事件不会冒泡</li>
</ol>
<h1 data-id="heading-7">Props传值还是Data传值？</h1>
<p>props: 需要用户传值</p>
<p>data不需要用户传值，自身维护</p>
<p>我们这里用data来传值</p>
<h1 data-id="heading-8">切换tag</h1>
<p>实现切换tag功能有两步</p>
<h2 data-id="heading-9">第一步是从外界取值</h2>
<p>点击一个tag后，爷爷组件会广而告之所有人，XXX被选中了，然后他的孙子们通过eventBus就能知道了！</p>
<p>然后我们根据传进来的变量，计算出css class， 然后更新样式</p>
<pre><code class="hljs language-js copyable" lang="js">Tab组件(爷爷组件)

    @Provide(<span class="hljs-string">'eventbus'</span>) eventbus: Vue = <span class="hljs-built_in">this</span>.eventBus;

    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.eventbus.$emit(<span class="hljs-string">'update:selected'</span>, <span class="hljs-built_in">this</span>.selected);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">TabPanel 和 TabItem

<span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.eventbus.$on(<span class="hljs-string">'update:selected'</span>, <span class="hljs-function">(<span class="hljs-params">name: string</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.active = name === <span class="hljs-built_in">this</span>.name;
      &#125;);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>孙子组件在created阶段就开始监听'update:selected'事件，然后判断被选中的是不是自己</p>
<h2 data-id="heading-10">第二步是用点击事件从内部更新</h2>
<p>因为vue里事件不会冒泡，所以我们监听点击元素：tab-item, 设置onClick事件</p>
<pre><code class="hljs language-js copyable" lang="js">TabItem

<template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tab-item"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"xxx"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"classes"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
  <span class="hljs-keyword">import</span> &#123;Component, Inject, Prop&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-property-decorator'</span>;

  @Component
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TabItem</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vue</span> </span>&#123;
    @Inject() eventbus!: Vue;
    @Prop(<span class="hljs-built_in">String</span>) name: string | <span class="hljs-literal">undefined</span>;
    @Prop(<span class="hljs-built_in">Boolean</span>) disabled = <span class="hljs-literal">false</span>;
    active = <span class="hljs-literal">false</span>;

    <span class="hljs-keyword">get</span> <span class="hljs-title">classes</span>() &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">active</span>: <span class="hljs-built_in">this</span>.active
      &#125;;
    &#125;

    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.eventbus.$on(<span class="hljs-string">'update:selected'</span>, <span class="hljs-function">(<span class="hljs-params">name: string</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.active = name === <span class="hljs-built_in">this</span>.name;
      &#125;);
    &#125;

    <span class="hljs-function"><span class="hljs-title">xxx</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.eventbus.$emit(<span class="hljs-string">'update:selected'</span>, <span class="hljs-built_in">this</span>.name, <span class="hljs-built_in">this</span>)
    &#125;
  &#125;
</span></span><span class="copy-code-btn">复制代码</span></code></pre>
<p>每次点击，就往事件中心广播 是哪个Name被点击了</p>
<p><em>本文为fjl的原创文章，著作权归本人和饥人谷所有，转载务必注明来源</em></p></div>  
</div>
            