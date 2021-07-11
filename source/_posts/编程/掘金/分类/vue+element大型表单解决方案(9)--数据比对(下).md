
---
title: 'vue+element大型表单解决方案(9)--数据比对(下)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0027d5bcd2dc4333a238075489a9c8f9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 23:53:40 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0027d5bcd2dc4333a238075489a9c8f9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>先跟大家道个歉，距离上一篇写完居然隔了一个月。这一个月实在太多事情了，身体状态也不太好，每到周末都想着总该写一篇了吧，转念又想反正没人看，干嘛逼着这么累...直到前几天，看到有小伙伴留言催更，我才意识到既然写的是系列文章，就没有半途而废的道理，唯有一鼓作气写完。其实我也只是写技术文章的新手，上来就写系列文章，确实不是好的选择；好在本系列快完结了，后面几篇都是一些真实场景的演示，可以作为vue表单实践的一些参考。</p>
</blockquote>
<p>代码地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fwyh-19%2Fsuper-form-solution.git" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/wyh-19/super-form-solution.git" ref="nofollow noopener noreferrer">gitee.com/wyh-19/supe…</a><br>
上篇代码分支：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fwyh-19%2Fsuper-form-solution%2Ftree%2Fessay-8" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/wyh-19/super-form-solution/tree/essay-8" ref="nofollow noopener noreferrer">essay-8</a><br>
本篇代码分支：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fwyh-19%2Fsuper-form-solution%2Ftree%2Fessay-9" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/wyh-19/super-form-solution/tree/essay-9" ref="nofollow noopener noreferrer">essay-9</a></p>
<p>系列文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6964330851173662757" target="_blank" title="https://juejin.cn/post/6964330851173662757">vue+element大型表单解决方案(1)--概览</a></li>
<li><a href="https://juejin.cn/post/6964677053006217247" target="_blank" title="https://juejin.cn/post/6964677053006217247">vue+element大型表单解决方案(2)--表单拆分</a></li>
<li><a href="https://juejin.cn/post/6965323570738102303" target="_blank" title="https://juejin.cn/post/6965323570738102303">vue+element大型表单解决方案(3)--锚点组件(上)</a></li>
<li><a href="https://juejin.cn/post/6965785753456476168" target="_blank" title="https://juejin.cn/post/6965785753456476168">vue+element大型表单解决方案(4)--锚点组件(下)</a></li>
<li><a href="https://juejin.cn/post/6966944473280413709" target="_blank" title="https://juejin.cn/post/6966944473280413709">vue+element大型表单解决方案(5)--校验标识</a></li>
<li><a href="https://juejin.cn/post/6968070822653067295" target="_blank" title="https://juejin.cn/post/6968070822653067295">vue+element大型表单解决方案(6)--自动标识</a></li>
<li><a href="https://juejin.cn/post/6969221097380118565" target="_blank" title="https://juejin.cn/post/6969221097380118565">vue+element大型表单解决方案(7)--表单形态</a></li>
<li><a href="https://juejin.cn/post/6971056138431234056" target="_blank" title="https://juejin.cn/post/6971056138431234056">vue+element大型表单解决方案(8)--数据比对(上)</a></li>
</ul>
<h2 data-id="heading-0">前言</h2>
<p>上一篇实现了基本的数据比对，只是场景比较简单，比对的都是文本类控件的数据。这一篇将补充一些复杂控件的数据比对，比如select、radio、checkbox等，他们都有一个共同的特点，即value并不适宜直接展示，需要转换成相应的文字后才有比对价值。</p>
<h2 data-id="heading-1">准备工作</h2>
<p>找到form1.vue文件，添加一些常见的复杂控件，代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"学历"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"field-wrapper"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-select</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"formData.education"</span> <span class="hljs-attr">v-compare:education</span>=<span class="hljs-string">"oldFormData"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-option</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in educationList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.value"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"item.value"</span>
               <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.label"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-option</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-select</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
<span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"性别"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"field-wrapper"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-radio-group</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"formData.gender"</span> <span class="hljs-attr">v-compare:gender</span>=<span class="hljs-string">"oldFormData"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"1"</span>></span>女<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"2"</span>></span>男<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-radio-group</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
<span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"爱好"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"field-wrapper"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-checkbox-group</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"formData.hobby"</span> <span class="hljs-attr">v-compare:hobby</span>=<span class="hljs-string">"oldFormData"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-checkbox</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in hobbyList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.value"</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.value"</span>></span>
      &#123;&#123; item.label &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">el-checkbox</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-checkbox-group</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相应的data中加上需要的响应式数据：</p>
<pre><code class="hljs language-js copyable" lang="js">educationList: [
    &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'研究生'</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>
    &#125;,
    &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'本科'</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-number">2</span>
    &#125;,
    &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'大专'</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>
    &#125;
  ],
  <span class="hljs-attr">hobbyList</span>: [
    &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'看书'</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>
    &#125;,
    &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'打游戏'</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-number">2</span>
    &#125;,
    &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'运动'</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>
    &#125;
  ],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到demo.js文件，增加测试数据返回，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajaxGetData</span>(<span class="hljs-params"></span>) </span>&#123;
...省略
resolve(
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'wyh'</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">30</span>,
      <span class="hljs-attr">education</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">gender</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">hobby</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">3</span>],
      <span class="hljs-attr">company</span>: <span class="hljs-string">'aaa'</span>
    &#125;
  )
...省略
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajaxGetOldData</span>(<span class="hljs-params"></span>) </span>&#123;
...省略
resolve(
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'wyh19'</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">30</span>,
      <span class="hljs-attr">education</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">gender</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">hobby</span>: [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
      <span class="hljs-attr">company</span>: <span class="hljs-string">'bbb'</span>
    &#125;
  )
...省略
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表单组装文件index.vue中，找到<code>resolveDataToMap</code>方法，增加字段处理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">resolveDataToMap</span>(<span class="hljs-params">data</span>)</span> &#123;
  <span class="hljs-keyword">const</span> form1 = &#123;
    <span class="hljs-attr">name</span>: data.name,
    <span class="hljs-attr">age</span>: data.age,
    <span class="hljs-attr">education</span>: data.education,
    <span class="hljs-attr">gender</span>: data.gender,
    <span class="hljs-attr">hobby</span>: data.hobby
  &#125;
  ...省略
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此准备工作完毕，进入比对页面，效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0027d5bcd2dc4333a238075489a9c8f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
显然，这些value型的数据比对结果无法让人满意，这正是本篇要解决的问题，下面正式开始。</p>
<h2 data-id="heading-2">实现思路</h2>
<p>通过新旧value的比较，可以区分出数据是否有变化，但是又不能像文本类的字段那样直接显示文本内容，需要根据value反推出文本，因此指令中需要增加文本解析的功能。之前<code>v-compare:字段名="oldFormData"</code>的信息已经不够了，需要扩展下增加额外信息，比如这种形式<code>v-compare:字段名.比对方式="&#123;oldFormData,其他信息&#125;"</code>。由于涉及到指令内部，因此一些字段需要固定成规范，比如当前例子中，select、radio都是需要将value映射成label进行显示，这里比对方式使用map这个单词，其他信息的字段也采用map作为字段名，形式为<code>v-compare:字段名.map="&#123;oldFormData,map:&#123;...&#125;&#125;"</code>。</p>
<h2 data-id="heading-3">具体实现</h2>
<h3 data-id="heading-4">radio的实现</h3>
<p>radio相对来说是最简单的，先从这里入手实现上面的思路。修改性别这个字段的比对指令使用代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">el-radio-group</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"formData.gender"</span>
                <span class="hljs-attr">v-compare:gender.map</span>=<span class="hljs-string">"&#123;oldFormData,map:&#123;1:'女',2:'男'&#125;&#125;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"1"</span>></span>女<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"2"</span>></span>男<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-radio-group</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时进入v-compare.js文件中，增加对map类型的处理。由于指令的使用形式和之前的不一样，我又不想改变原有的写法，因此需要在指令内部做了隔离，保留原来的逻辑不变。从binding参数中取出modifiers，根据其内容判断采用哪套逻辑，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">componentUpdated</span>(<span class="hljs-params">el, binding, vnode</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; value, oldValue, arg, modifiers &#125; = binding
    <span class="hljs-keyword">if</span> (modifiers.map) &#123;
      <span class="hljs-comment">// map类型的逻辑在此实现</span>

    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// ===原来文本类型比对逻辑保持写法用法不变====</span>
      <span class="hljs-comment">// oldFormData从无数据到有数据时，才进行比对</span>
      <span class="hljs-comment">// 避免数据更新过多无效的比对</span>
      <span class="hljs-keyword">if</span> (!oldValue && value) &#123;
        <span class="hljs-comment">// 进入此if判断时才真正有比对功能</span>
        <span class="hljs-comment">// 最新的数据，即v-model里现在绑定的值</span>
        <span class="hljs-keyword">const</span> lastModel = vnode.data.model.value
        <span class="hljs-comment">// 之前的数据，即oldFormData[arg]</span>
        <span class="hljs-keyword">const</span> beforeModel = value[arg]
        <span class="hljs-comment">// 如果两个数据不相同，这里没有使用!==</span>
        <span class="hljs-keyword">if</span> (lastModel !== beforeModel) &#123;
          <span class="hljs-comment">// 打上标记</span>
          markDiffrent(el, beforeModel)
        &#125;
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在map的判断体内写上类似的比对逻辑代码，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (modifiers.map) &#123;
    <span class="hljs-comment">// map类型的逻辑在此实现</span>
    <span class="hljs-comment">// 拿到指令更新前后两次的oldFormData</span>
    <span class="hljs-keyword">const</span> oldV = oldValue.oldFormData
    <span class="hljs-keyword">const</span> v = value.oldFormData
    <span class="hljs-comment">// 拿到map信息</span>
    <span class="hljs-keyword">const</span> map = value.map
    <span class="hljs-comment">// 比较两次oldFormData，当从无到有时才比对，避免多余的无效比对</span>
    <span class="hljs-keyword">if</span> (!oldV && v) &#123;
    <span class="hljs-keyword">const</span> lastModel = vnode.data.model.value
    <span class="hljs-keyword">const</span> beforeModel = v[arg]
        <span class="hljs-keyword">if</span> (lastModel !== beforeModel) &#123;
          <span class="hljs-comment">// 直接从map中映射成相应的文本</span>
          markDiffrent(el, map[beforeModel])
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时看到radio已经实现了比对效果，如下图(样式问题不在此讨论，可自行根据需要调整)：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1775439ee144276a5730630f3124c03~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">select的实现</h3>
<p>在这个例子中，本质上radio和select是一样的，唯一的区别是radio的选项是枚举出来的，而select的选项是遍历出来的，因此这里主要工作是如何得到map信息。在super-form-mixin.js文件中，写一个公共方法，专门处理转换工作，代码如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 转换select选项为比对指令需要的map类型
 * 例如: [&#123;value:1,label:'a'&#125;] ===> &#123;1:a&#125;
 */</span>
<span class="hljs-function"><span class="hljs-title">composeOptions</span>(<span class="hljs-params">options = [], value = <span class="hljs-string">'value'</span>, label = <span class="hljs-string">'label'</span></span>)</span> &#123;
  <span class="hljs-keyword">const</span> map = &#123;&#125;
  options.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    map[item[value]] = item[label]
  &#125;)
  <span class="hljs-keyword">return</span> map
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时修改select的比对指令为<code> v-compare:education.map="&#123;oldFormData,map:composeOptions(educationList)&#125;"</code>
此时比对结果如下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2508e78c6e1498fb8038d8ec5f54b45~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">checkbox的实现</h3>
<p>与之前不同，checkbox不是单一值的映射，而是数组类型值的映射，因此在逻辑上有些区别，修饰符命名为arrayMap，map信息依然采用composeOptions函数转换，checkbox的比对指令使用代码为<code>v-compare:hobby.arrayMap="&#123;oldFormData,map:composeOptions(hobbyList)&#125;</code>
在modifiers.map判断后面增加新的判断分支，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (modifiers.arrayMap) &#123;
  <span class="hljs-comment">// arrayMap类型的逻辑在此实现</span>
  <span class="hljs-comment">// 拿到指令更新前后两次的oldFormData</span>
  <span class="hljs-keyword">const</span> oldV = oldValue.oldFormData
  <span class="hljs-keyword">const</span> v = value.oldFormData
  <span class="hljs-comment">// 拿到map信息</span>
  <span class="hljs-keyword">const</span> map = value.map
  <span class="hljs-comment">// 比较两次oldFormData，当从无到有时才比对，避免多余的无效比对</span>
  <span class="hljs-keyword">if</span> (!oldV && v) &#123;
    <span class="hljs-keyword">const</span> lastModel = vnode.data.model.value
    <span class="hljs-keyword">const</span> beforeModel = v[arg]
    <span class="hljs-keyword">if</span> (!compareEasyArray(lastModel, beforeModel)) &#123;
      <span class="hljs-comment">// 直接从map中映射成相应的文本</span>
      markDiffrent(el, getArrayMapResult(beforeModel, map))
    &#125;
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我为了书写方便，没有优化代码，大家可以根据自己习惯采用switch分支方式扩展以及优化掉重复的代码。
和前面的比对不同的地方在于:</p>
<ol>
<li>不是简单的使用<code>lastModel !== beforeModel</code>比对两个值是否不同，而是使用了<code>compareEasyArray</code>方法，这里的需求是判断数组不同不在于其顺序，而在于是否存在不同的项。</li>
<li>不是简单的<code>map[beforeModel]</code>得到文本，而是使用了<code>getArrayMapResult</code>方法</li>
</ol>
<p>下面实现这两个方法:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compareEasyArray</span>(<span class="hljs-params">arr1, arr2</span>) </span>&#123;
  <span class="hljs-comment">// 数组的每一项都是简单类型，且不比较顺序</span>
  <span class="hljs-keyword">const</span> arr1ToString = arr1.sort().join(<span class="hljs-string">','</span>)
  <span class="hljs-keyword">const</span> arr2ToString = arr2.sort().join(<span class="hljs-string">','</span>)
  <span class="hljs-keyword">return</span> arr1ToString === arr2ToString
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getArrayMapResult</span>(<span class="hljs-params">arr, map</span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = arr.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> map[item])
  <span class="hljs-keyword">return</span> result.join(<span class="hljs-string">','</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/331649e634d54abf86fdcaa290ecfe8b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时已基本实现我们的目标，如果想做的更完美些，只需要沿用当前思路加上自己的奇思妙想了。</p>
<h2 data-id="heading-7">拓展补充</h2>
<p>实践中，远不止这些比对类型，下面的代码都不在demo中演示了，只是简单的记录一下，便于以后需要时快速查找。</p>
<ol>
<li>value型的字段，但是后端直接返回了相应的label，或者前端自己查出了laebl，不想在指令内部map，那么可以增加label比对方式<code>v-compare:字段名.label="&#123;oldFormData,label:xxLabel&#125;"</code></li>
</ol>
<p>对应的指令解析办法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (modifiers.label) &#123;
  <span class="hljs-keyword">const</span> oldV = oldValue.oldFormData
  <span class="hljs-keyword">const</span> v = value.oldFormData
  <span class="hljs-keyword">const</span> label = value.label
  <span class="hljs-keyword">if</span> (!oldV && v) &#123;
    <span class="hljs-keyword">const</span> lastModel = vnode.data.model.value
    <span class="hljs-keyword">const</span> beforeModel = v[arg]
    <span class="hljs-keyword">if</span> (lastModel !== beforeModel) &#123;
      markDiffrent(el, label)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>select-tree型控件数据，需要递归查找tree中的节点</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">v-tree-select</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"formData.respUnitId"</span>
               <span class="hljs-attr">v-compare:respUnitId.tree</span>=<span class="hljs-string">"&#123;oldFormData,tree:&#123;options:$store.state.base.unitUserTreeData,id:'id',label:'name',children:'childList'&#125;&#125;"</span>
               <span class="hljs-attr">:options</span>=<span class="hljs-string">"$store.state.base.unitUserTreeData"</span>
               <span class="hljs-attr">no-results-text</span>=<span class="hljs-string">"不存在该部门"</span>
               <span class="hljs-attr">:normalizer</span>=<span class="hljs-string">"(node)=>(&#123;id:node.id,label:node.name,children:node.childList&#125;)"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应指令解析代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (modifiers.tree) &#123;
  <span class="hljs-keyword">const</span> oldV = oldValue.oldFormData
  <span class="hljs-keyword">const</span> v = value.oldFormData
  <span class="hljs-keyword">const</span> tree = value.tree
  <span class="hljs-keyword">if</span> (!oldV && v) &#123;
    <span class="hljs-keyword">const</span> lastModel = vnode.data.model.value
    <span class="hljs-keyword">const</span> beforeModel = v[arg]
    <span class="hljs-keyword">if</span> (lastModel !== beforeModel) &#123;
      <span class="hljs-keyword">const</span> &#123; options, id, label, children &#125; = tree
      <span class="hljs-keyword">const</span> beforeLabel = getLabelFromTree(beforeModel, options, id, label, children)
      markDiffrent(el, beforeLabel)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过递归实现getLabelFromTree方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getLabelFromTree</span>(<span class="hljs-params">value, tree, idKey, labelKey, childrenKey</span>) </span>&#123;
  <span class="hljs-keyword">let</span> result = <span class="hljs-string">''</span>
  <span class="hljs-keyword">if</span> (!value || !tree || !tree.length) &#123;
    <span class="hljs-keyword">return</span> result
  &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < tree.length; i++) &#123;
    <span class="hljs-keyword">if</span> (tree[i][idKey] === value) &#123;
      result = tree[i][labelKey]
    &#125; <span class="hljs-keyword">else</span> &#123;
      result = getLabelFromTree(value, tree[i][childrenKey], idKey, labelKey, childrenKey)
    &#125;
    <span class="hljs-keyword">if</span> (result) &#123;
      <span class="hljs-keyword">break</span>
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面例子，我想说明任何复杂的value型控件都能转换成可以显示的比对结果，如果遇到实在不好解决的情况，可以在外层主动获取label，通过label的形式传入显示。</p>
<p>到这里，普通表单的字段比对的功能已全部实现。后面将演示一些复杂类型的表单如何实现，以及跨表单之间如何联动通信。<em>谢谢您的阅读，欢迎提出指正意见！</em></p></div>  
</div>
            