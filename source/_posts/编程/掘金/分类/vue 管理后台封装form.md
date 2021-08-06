
---
title: 'vue 管理后台封装form'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec732f9e03574c9f8cb137ff2707d31c~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 04:20:52 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec732f9e03574c9f8cb137ff2707d31c~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<p>在上一篇<a href="https://juejin.cn/post/6992493380815028232" target="_blank" title="https://juejin.cn/post/6992493380815028232">vue 管理后台table封装</a>中，讲解了如何封装table,这一篇写如何封装form。封装form说难也难，说简单也简单，毕竟你封装一个也是封装，把好多东西全搞进入也是封装。我这个项目刚开始，我也就简单的介绍下，暂时只封装下input，其实思路都是一样的。</p>
<h1 data-id="heading-0">问题分析</h1>
<p>看下图：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec732f9e03574c9f8cb137ff2707d31c~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们封装的只有这两个input。</p>
<h2 data-id="heading-1">组件分析</h2>
<pre><code class="hljs language-js copyable" lang="js"><el-form ref=<span class="hljs-string">"form"</span> :model=<span class="hljs-string">"listQuery"</span> label-width=<span class="hljs-string">"80px"</span>>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"店铺名称"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width:300px;float:left;"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"listQuery.name"</span> /></span>
   <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span></span>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"店铺手机号"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width:300px;float:left;"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"listQuery.phone"</span> /></span>
   <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span></span>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-left: 20px;"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"getStoreList"</span>></span>查询<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span></span>
</el-form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是我所使用的组件的代码，在封装的时候，我们可以直接看el-form的组件给到的属性，</p>
<h2 data-id="heading-2">数据类型</h2>
<p>我们要确定好我们需要的数据，例如label ,type, prop, Function等等，在思考后，得到如下数据结构</p>
<p><strong>form</strong></p>
<pre><code class="hljs language-js copyable" lang="js">formName: <span class="hljs-built_in">String</span>
<span class="hljs-attr">formType</span>: <span class="hljs-built_in">String</span>
<span class="hljs-attr">formData</span>: <span class="hljs-built_in">Object</span>
<span class="hljs-keyword">const</span> formArr: <span class="hljs-built_in">Array</span> = [
  &#123;
    <span class="hljs-attr">label</span>: <span class="hljs-built_in">Array</span>,
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">prop</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">size</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">labelWidth</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">placeholder</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">handle</span>: <span class="hljs-built_in">Function</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>btn</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> btnArr: <span class="hljs-built_in">Array</span> =  [
  &#123;
    <span class="hljs-attr">label</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">handle</span>: <span class="hljs-built_in">Function</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们确定完数据结构，我们就可以敲代码了，结合element组件。</p>
<h1 data-id="heading-3">封装form</h1>
<h2 data-id="heading-4">全局组件</h2>
<p>这里我们还是先创建我们的组件，我的组件名称为FrForm.vue，之后导入到index.js中，同时把它添加到组件列表中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> FrForm <span class="hljs-keyword">from</span> <span class="hljs-string">'./FrForm/index'</span>
<span class="hljs-keyword">const</span> components = [FrForm]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">组件的编写</h2>
<h3 data-id="heading-6">组件分析</h3>
<p>在这个组件里我们其实封装有两种，一种是表单，一种是按钮，两种我们一一叙述。</p>
<h4 data-id="heading-7">表单封装</h4>
<p>我们已经定义好了数据格式，那么我们就需要通过for循环遍历出来，同时我们给了type类型，这是为了后期的扩展。
这里说下一个参数<strong>formType</strong>，这个参数分为form和select，form是指弹窗，select就是我们查询，当然我是这么搞的，大家有其他的想法随意发挥。</p>
<pre><code class="hljs language-js copyable" lang="js"><el-form :ref=<span class="hljs-string">"formName"</span> :model=<span class="hljs-string">"formData"</span>>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in formArr"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>
          <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>
          <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.label"</span>
          <span class="hljs-attr">:label-width</span>=<span class="hljs-string">"item.labelWidth"</span>
          <span class="hljs-attr">:prop</span>=<span class="hljs-string">"item.prop"</span>
          <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;
            marginLeft: item.marginLeft,
            float: formType === 'select' ? 'left' : 'none'
          &#125;"</span>
        ></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span>
            <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.type === 'input'"</span>
            <span class="hljs-attr">v-model.trim.lazy</span>=<span class="hljs-string">"formData[item.prop]"</span>
            @<span class="hljs-attr">keyup.enter.native</span>=<span class="hljs-string">"item.handle()"</span>
          /></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
</el-form>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">btn组件</h4>
<p>这个组件其实没有什么可说的，就是label，type，Function等，后期扩展在再说</p>
<pre><code class="hljs language-js copyable" lang="js"><template v-<span class="hljs-keyword">for</span>=<span class="hljs-string">"(item, index) in btnArr"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-button</span>
   <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>
   <span class="hljs-attr">:type</span>=<span class="hljs-string">"item.type"</span>
   <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"item.disabled"</span>
   <span class="hljs-attr">:size</span>=<span class="hljs-string">"item.size || size"</span>
   <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-left: 20px;"</span>
   @<span class="hljs-attr">click</span>=<span class="hljs-string">"item.handle()"</span>
  ></span>
    &#123;&#123; item.label &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实还是一个原则，就是尽量多考虑，最好是组件上有的参数，你都加上，有备无患。</p>
<h3 data-id="heading-9">prop定义</h3>
<p>根据上边的内容，我们就可以直接定义我们从父组件传到全局组件的参数了</p>
<pre><code class="hljs language-js copyable" lang="js">formName: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
      &#125;
    &#125;,
    <span class="hljs-attr">formType</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'select'</span>
      &#125;
    &#125;,
    <span class="hljs-attr">formData</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
      &#125;
    &#125;,
    <span class="hljs-attr">formArr</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> []
      &#125;
    &#125;,
    <span class="hljs-attr">btnArr</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> []
      &#125;
    &#125;,
    <span class="hljs-attr">size</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'small'</span>
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上边的编写我们的组件已经可以正常使用了，剩下的就是在页面调用这个组件</p>
<h1 data-id="heading-10">组件的调用</h1>
<p>因为是全局组件，我们也不需要去注册，直接使用就可以了，代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><FrForm
  ref=<span class="hljs-string">"formData"</span>
  :form-name=<span class="hljs-string">"'formData'"</span>
  :form-data=<span class="hljs-string">"formData"</span>
  :form-arr=<span class="hljs-string">"formArr"</span>
  :btn-arr=<span class="hljs-string">"btnArr"</span>
  :inline=<span class="hljs-string">"true"</span>
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们按需写好自己的参数就可以正常使用了。以上就是form的封装，提一句的是，我们可以把表单的所有内容都封装进入，这个我们就搞了一个大而全的内容，剩下的就写数据就好了。后期我还会把其他内容一点点添加进去的，后边继续分享。</p>
<p>以上就是今天的分享了，有不足之处，还请多多留言知道！！！感谢感谢</p>
<h1 data-id="heading-11">相关文章</h1>
<h3 data-id="heading-12">vue 管理后台table封装 <a href="https://juejin.cn/post/6992493380815028232" target="_blank" title="https://juejin.cn/post/6992493380815028232">juejin.cn/post/699249…</a></h3>
<h3 data-id="heading-13">lerna，开发与发布流程 <a href="https://juejin.cn/post/6992213605869420552" target="_blank" title="https://juejin.cn/post/6992213605869420552">juejin.cn/post/699221…</a></h3>
<h3 data-id="heading-14">Promise复习 <a href="https://juejin.cn/post/6991839839687540773" target="_blank" title="https://juejin.cn/post/6991839839687540773">juejin.cn/post/699183…</a></h3>
<h3 data-id="heading-15">let,const复习 <a href="https://juejin.cn/post/6991475477550628901" target="_blank" title="https://juejin.cn/post/6991475477550628901">juejin.cn/post/699147…</a></h3>
<h3 data-id="heading-16">初学koa搭建项目  <a href="https://juejin.cn/post/6987566845867851812" target="_blank" title="https://juejin.cn/post/6987566845867851812">juejin.cn/post/698756…</a></h3>
<h3 data-id="heading-17">正则表达式总结 <a href="https://juejin.cn/post/6986156162701852679" target="_blank" title="https://juejin.cn/post/6986156162701852679">juejin.cn/post/698615…</a></h3>
<h3 data-id="heading-18">flex布局总结 <a href="https://juejin.cn/post/6984970083923656718" target="_blank" title="https://juejin.cn/post/6984970083923656718">juejin.cn/post/698497…</a></h3>
<h3 data-id="heading-19">mongodb基础用法 <a href="https://juejin.cn/post/6983647396441931789" target="_blank" title="https://juejin.cn/post/6983647396441931789">juejin.cn/post/698364…</a></h3>
<h3 data-id="heading-20">vue3搭建管理后台-项目搭建 <a href="https://juejin.cn/post/6968028312111153189" target="_blank" title="https://juejin.cn/post/6968028312111153189">juejin.cn/post/696802…</a></h3>
<h3 data-id="heading-21">工厂模式，构造器模式和原型模式  <a href="https://juejin.cn/post/6957940016785915918" target="_blank" title="https://juejin.cn/post/6957940016785915918">juejin.cn/post/695794…</a></h3></div>  
</div>
            