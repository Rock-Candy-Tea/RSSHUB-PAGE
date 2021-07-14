
---
title: '最熟悉的陌生人rc-form'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 15:07:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 107 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzoo.team%2Farticle%2Frc-from" target="_blank" rel="nofollow noopener noreferrer" title="https://zoo.team/article/rc-from" ref="nofollow noopener noreferrer">最熟悉的陌生人rc-form</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d418387923574e8fb301751f707be871~tplv-k3u1fbpfcp-watermark.image" alt="清风.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">rc-form 是谁?</h3>
<p>我们也许会经常使用例如 Ant Design、Element UI、Vant 等第三方组件库来快速在项目中完成页面的布局效果和简单的交互功能。</p>
<p>但是我们可能会忽略掉在这些优秀的第三方库中的某些组件可能也依赖于其他优秀的库!正如我们使用频率很高的 Ant Design 中的 Form 组件(这里我说的是 React 版本的)。</p>
<p>其实这些优秀的开源库内部使用了优秀的第三方库rc-form; 正如我们经常使用的 getFieldDecorator、getFieldsValue、setFieldsValue、validateFields 等这些 Api，其实这些都是 rc-form 暴露出来的方法。</p>
<h3 data-id="heading-1">为什么要使用 rc-form?</h3>
<blockquote>
<p>我们都知道 React 框架设计模式和 Vue 不同，Vue 中作者已经帮我们实现了数据的双向绑定，数据驱动视图，视图驱动数据的改变，但是 React 中需要我们手动调用 setState 实现数据驱动视图的改变，请看下面的代码。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">value1</span>: <span class="hljs-string">"peter"</span>,
    <span class="hljs-attr">value2</span>: <span class="hljs-string">"123"</span>,
    <span class="hljs-attr">value3</span>: <span class="hljs-string">"23"</span>,
  &#125;;

  onChange1 = <span class="hljs-function">(<span class="hljs-params">&#123; target: &#123; value &#125; &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">value1</span>: value &#125;);
  &#125;;

  onChange2 = <span class="hljs-function">(<span class="hljs-params">&#123; target: &#123; value &#125; &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">value2</span>: value &#125;);
  &#125;;
  
  onChange3 = <span class="hljs-function">(<span class="hljs-params">&#123; target: &#123; value &#125; &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">value3</span>: value &#125;);
  &#125;;
  
submit = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> &#123; value1, value2, value3 &#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-keyword">const</span> obj = &#123;
      value1,
      value2,
      value3,
    &#125;;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> axios(<span class="hljs-string">"url"</span>, obj)
  &#125;;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; value1, value2, value3 &#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">""</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">""</span>></span>用户名: <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value1&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;this.onChange1&#125;</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">""</span>></span>密码: <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value2&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;this.onChange2&#125;</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">""</span>></span>年龄: <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value3&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;this.onChange3&#125;</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.submit&#125;</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>上面是一个表单登录的简单功能! 要想实现表单数据的实时更新需要在表单 onChange 的时候手动更新 state 状态;</p>
</li>
<li>
<p>从上面代码中可以看出，这样写功能也能实现，但是当我们的表单多的时候，难道页面要写十几个 onChange 事件去实现页面的数据驱动视图的更新吗？这样考虑一下其实是不妥的;</p>
</li>
<li>
<p>这个时候 rc-form 就应运而生了，rc-form 创建一个数据集中管理仓库，这个仓库负责统一收集表单数据验证、重置、设置、获取值等逻辑操作，这样我们就把重复无用功交给 rc-form 来处理了，以达到代码的高度可复用性!</p>
</li>
</ul>
<h3 data-id="heading-2">主要 Api 简要说明</h3>


















































<table><thead><tr><th align="left">Api名称</th><th>说明</th><th>类型</th></tr></thead><tbody><tr><td align="left">getFieldDecorator</td><td>用于和表单进行双向绑定，</td><td>Function(name)</td></tr><tr><td align="left">getFieldsValue</td><td>获取一组字段名对应的值，会按照对应结构返回。默认返回现存字段值，当调用  <code>getFieldsValue(true)</code>  时返回所有值</td><td>(nameList?: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fant.design%2Fcomponents%2Fform-cn%2F%23NamePath" target="_blank" rel="nofollow noopener noreferrer" title="https://ant.design/components/form-cn/#NamePath" ref="nofollow noopener noreferrer">NamePath</a>[], filterFunc?: (meta: &#123; touched: boolean, validating: boolean &#125;) => boolean) => any</td></tr><tr><td align="left">getFieldValue</td><td>获取对应字段名的值</td><td>(name: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fant.design%2Fcomponents%2Fform-cn%2F%23NamePath" target="_blank" rel="nofollow noopener noreferrer" title="https://ant.design/components/form-cn/#NamePath" ref="nofollow noopener noreferrer">NamePath</a>) => any</td></tr><tr><td align="left">setFieldsValue</td><td>设置一组表单的值</td><td>(values) => void</td></tr><tr><td align="left">setFields</td><td>设置一组字段状态</td><td>(fields: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fant.design%2Fcomponents%2Fform-cn%2F%23FieldData" target="_blank" rel="nofollow noopener noreferrer" title="https://ant.design/components/form-cn/#FieldData" ref="nofollow noopener noreferrer">FieldData</a>[]) => void</td></tr><tr><td align="left">validateFields</td><td>触发表单验证</td><td>(nameList?: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fant.design%2Fcomponents%2Fform-cn%2F%23NamePath" target="_blank" rel="nofollow noopener noreferrer" title="https://ant.design/components/form-cn/#NamePath" ref="nofollow noopener noreferrer">NamePath</a>[]) => Promise</td></tr><tr><td align="left">isFieldValidating</td><td>检查一组字段是否正在校验</td><td>(name: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fant.design%2Fcomponents%2Fform-cn%2F%23NamePath" target="_blank" rel="nofollow noopener noreferrer" title="https://ant.design/components/form-cn/#NamePath" ref="nofollow noopener noreferrer">NamePath</a>) => boolean</td></tr><tr><td align="left">getFieldProps</td><td>获取对应字段名的属性</td><td>(name: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fant.design%2Fcomponents%2Fform-cn%2F%23NamePath" target="_blank" rel="nofollow noopener noreferrer" title="https://ant.design/components/form-cn/#NamePath" ref="nofollow noopener noreferrer">NamePath</a>) => any</td></tr></tbody></table>
<h3 data-id="heading-3">使用 rc-form</h3>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> &#123; createForm &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../../rc-form"</span>;
<span class="hljs-comment">// import ReactClass from './ReactClass'</span>

<span class="hljs-keyword">const</span> RcForm = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123;
    <span class="hljs-attr">form</span>: &#123; getFieldDecorator, validateFields &#125;,
  &#125; = props;

  <span class="hljs-keyword">const</span> handleSubmit = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    e && e.stopPropagation();
    validateFields(<span class="hljs-function">(<span class="hljs-params">err, value</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (!err) &#123;
        <span class="hljs-built_in">console</span>.log(value);
      &#125;
    &#125;);
  &#125;;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">padding:</span> <span class="hljs-attr">20</span>, <span class="hljs-attr">background:</span> "#<span class="hljs-attr">fff</span>" &#125;&#125; ></span>
      <span class="hljs-tag"><<span class="hljs-name">form</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span>></span>姓名:<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        &#123;getFieldDecorator("username", &#123;
          rules: [&#123; required: true, message: "请输入用户名!" &#125;],
          initialValue:'initialValue',
        &#125;)(<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> /></span>)&#125;
        <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span>></span>密码:<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        &#123;getFieldDecorator("password", &#123;
          rules: [
            &#123; required: true, message: "请输入密码!" &#125;, 
            &#123; pattern: /^[a-z0-9_-]&#123;6,18&#125;$/, message:'只允许数字!' &#125;
          ],
        &#125;)(<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginTop:</span> "<span class="hljs-attr">15px</span>" &#125;&#125; /></span> )&#125;
        <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleSubmit&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginTop:</span> "<span class="hljs-attr">15px</span>" &#125;&#125;></span>
          提交
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createForm()(RcForm);

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意: 经过 createForm 方法处理的组件(就是 Ant Design 中 Form 的 create() 方法)，会自动向组件没注入 form 对象，组件本身也就拥有了这些 Api 。</p>
</blockquote>
<ul>
<li>
<p>Demo 只是简单的基于 rc-form 实现了表单的装饰、表单验证、数据收集等功能。那么如何实现更加具有针对性的，适用多种业务场景的表单组件呢?</p>
</li>
<li>
<p>绕开优秀的开源的组件库不说，如果哪一天这些优秀的开源作品不再开源了，那我们怎么办？</p>
</li>
<li>
<p>为了避免这种情况发生，或者如果仅是为了我们自己的职业生涯规划，使自己更上一层楼的话也是有必要的去学习一下优秀的三方库的设计理念。就算看一下别人的代码风格也是有必要的。其实还是需要我们自己了解 rc-form 的设计思路的；只有了解了这些优秀开源作品的精髓,我们即使不用开源库，也可以封装自己的代码库以及类似Ant Design中Form这些优秀的组件的。</p>
</li>
</ul>
<h3 data-id="heading-4">从 createForm 开始</h3>
<p>都知道我们平时编写业务组件一般只要用到表单都会用到 createForm 或者 Form.create() 这些方法对自己的组件进行包装，那么我们就从这里开始我们的故事。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> createBaseForm <span class="hljs-keyword">from</span> <span class="hljs-string">'./createBaseForm'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createForm</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createBaseForm(options, [mixin]);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createForm;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到其实 createForm 只是做了一层封装，真正的调用函数是 createBaseForm，那么着重看一下 createBaseForm 函数内部实现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/808dfbb739c54bf1b0fff1ccd8fc70de~tplv-k3u1fbpfcp-zoom-1.image" alt="createBaseForm" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的图片中可以看出这个函数利用闭包特性返回一个新函数，这个函数的参数其实就是你的业务组件对象，经过 createBaseForm 内部加工之后返回给你的是一个注入了 form 对象的组件.也就是我们常说的这个  createBaseForm 是一个高阶组件。</p>
<p>那么也就清楚了 Ant Design 的 <code>Form.create()</code> 方法就是 <code>rc-form</code> 中的 <code>createBaseForm</code> 方法的替代! 经过  <code>createBaseForm</code> 包装的组件将会注入 form 对象， 而 <code>form</code> 属性中提供的 getFieldDecorator 以及 fieldsStore 实例则是实现数据自动收集的关键。</p>
<h3 data-id="heading-5">浅析内部实现</h3>
<p>我们就先从最初的的渲染表单的逻辑开始，我们业务场景中用到的表单组件都会使用 getFieldDecorator 包装一下。当然，我说的是Ant Design 4.0以前的版本， 那么我们就先从这里开始看起。</p>
<p>这里首先说明一下，此篇文章我只是浅析一下整个表单数据双向绑定的简单过程，因为这个是 rc-form 的核心，精力有限具体的细节处理留待以后慢慢研究。那么我们就来看一下  <code>getFieldDecorator</code> 方法做了些什么？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getFieldDecorator</span>(<span class="hljs-params">name, fieldOption</span>)</span> &#123;
  <span class="hljs-keyword">const</span> props = <span class="hljs-built_in">this</span>.getFieldProps(name, fieldOption);
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-params">fieldElem</span> =></span> &#123;
    <span class="hljs-comment">// We should put field in record if it is rendered</span>
    <span class="hljs-built_in">this</span>.renderFields[name] = <span class="hljs-literal">true</span>;

    <span class="hljs-keyword">const</span> fieldMeta = <span class="hljs-built_in">this</span>.fieldsStore.getFieldMeta(name);
    <span class="hljs-keyword">const</span> originalProps = fieldElem.props;
    fieldMeta.originalProps = originalProps;
    fieldMeta.ref = fieldElem.ref;
    <span class="hljs-keyword">const</span> decoratedFieldElem = React.cloneElement(fieldElem, &#123;
      ...props,
      ...this.fieldsStore.getFieldValuePropValue(fieldMeta),
    &#125;);
    <span class="hljs-keyword">return</span> supportRef(fieldElem) ? (
      decoratedFieldElem
    ) : (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">FieldElemWrapper</span> <span class="hljs-attr">name</span>=<span class="hljs-string">&#123;name&#125;</span> <span class="hljs-attr">form</span>=<span class="hljs-string">&#123;this&#125;</span>></span>
      &#123;decoratedFieldElem&#125;
  <span class="hljs-tag"></<span class="hljs-name">FieldElemWrapper</span>></span></span>
  );
&#125;;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处我删除了一些无关紧要的代码，因为这样看起来更加清晰明了。 首先对传入的表单组件调用 getFieldProps 方法进行了 props 的构建处理，接着返回一个函数，这个函数参数就是我们使用 getFieldDecorator 传入的表单组件，调用 fieldsStore 中的 getFieldMeta 获取表单组件的配置数据，兼容原有组件的配置属性以及对不支持 ref组件的处理，最终返回一个克隆后的挂载处理后的一些配置对象的组件!</p>
<h4 data-id="heading-6">fieldsStore</h4>
<p>既然用到了 fieldsStore，那么这里要说一下 fieldsStore， fieldsStore 中包含了当前 form 的主要信息和一些处理表单数据的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FieldsStore</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">fields</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.fields = internalFlattenFields(fields);
    <span class="hljs-built_in">this</span>.fieldsMeta = &#123;&#125;;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fieldMeta 可以看成是一个表单项的描述，以传入的name为索引key，支持嵌套、存储表单数据， 即配置信息不涉及值的问题，主要包括：</p>
<ul>
<li>name 字段的名称</li>
<li>originalProps 被 getFieldDecorator() 装饰的组件的原始 props</li>
<li>rules 校验的规则</li>
<li>trigger 触发数据收集的时机 默认 <code>onChange</code></li>
<li>validate 校验规则和触发事件</li>
<li>valuePropName 子节点的值的属性，例如 checkbox 应该设为 <code>checked</code></li>
<li>getValueFromEvent 如何从 event 中获取组件的值</li>
<li>hidden 为 true 时，校验或者收集数据时会忽略这个字段</li>
</ul>
<p>fields 主要用于记录每个表单的实时属性，主要包括：</p>
<ul>
<li>
<p>dirty 数据是否已经改变，但未校验</p>
</li>
<li>
<p>errors 校验文案</p>
</li>
<li>
<p>name 字段名称</p>
</li>
<li>
<p>touched 数据是否更新过</p>
</li>
<li>
<p>value 字段的值</p>
</li>
<li>
<p>validating 校验状态</p>
</li>
</ul>
<p>那么接下来还是要看一下 getFieldProps 方法内部是如何实现props构建的?</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">getFieldProps</span>(<span class="hljs-params">name, usersFieldOption = &#123;&#125;</span>)</span> &#123;
  <span class="hljs-comment">// 重新组装props</span>
  <span class="hljs-keyword">const</span> fieldOption = &#123;
    name,
    <span class="hljs-attr">trigger</span>: DEFAULT_TRIGGER,
    <span class="hljs-attr">valuePropName</span>: <span class="hljs-string">'value'</span>,
    <span class="hljs-attr">validate</span>: [],
    ...usersFieldOption,
  &#125;;
  <span class="hljs-keyword">const</span> &#123;
    rules,
    trigger,
    validateTrigger = trigger,
    validate,
  &#125; = fieldOption;
  <span class="hljs-keyword">const</span> fieldMeta = <span class="hljs-built_in">this</span>.fieldsStore.getFieldMeta(name);
  <span class="hljs-comment">// 初始值处理</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-string">'initialValue'</span> <span class="hljs-keyword">in</span> fieldOption) &#123;
    fieldMeta.initialValue = fieldOption.initialValue;
  &#125;
<span class="hljs-comment">// 组装inputProps</span>
  <span class="hljs-keyword">const</span> inputProps = &#123;
    ...this.fieldsStore.getFieldValuePropValue(fieldOption),
    <span class="hljs-attr">ref</span>: <span class="hljs-built_in">this</span>.getCacheBind(name, <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>__ref`</span>, <span class="hljs-built_in">this</span>.saveRef),
  &#125;;
  <span class="hljs-keyword">if</span> (fieldNameProp) &#123;
    inputProps[fieldNameProp] = formName ? <span class="hljs-string">`<span class="hljs-subst">$&#123;formName&#125;</span>_<span class="hljs-subst">$&#123;name&#125;</span>`</span> : name;
  &#125;

  <span class="hljs-comment">// 收集验证规则</span>
  <span class="hljs-keyword">const</span> validateRules = normalizeValidateRules(validate, rules, validateTrigger);
  <span class="hljs-keyword">const</span> validateTriggers = getValidateTriggers(validateRules);
  validateTriggers.forEach(<span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (inputProps[action]) <span class="hljs-keyword">return</span>;
    inputProps[action] = <span class="hljs-built_in">this</span>.getCacheBind(name, action, <span class="hljs-built_in">this</span>.onCollectValidate);
  &#125;);

  <span class="hljs-comment">// 不走效验的组件使用onCollect收集组件的值</span>
  <span class="hljs-keyword">if</span> (trigger && validateTriggers.indexOf(trigger) === -<span class="hljs-number">1</span>) &#123;
    inputProps[trigger] = <span class="hljs-built_in">this</span>.getCacheBind(name, trigger, <span class="hljs-built_in">this</span>.onCollect);
  &#125;

  <span class="hljs-keyword">return</span> inputProps;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除了一些细节代码, 先来看看getFieldProps 首先进行了默认值的处理，如果用户没有设置  <code>trigger</code> 和<code>valuePropName     </code> 则使用默认值，随后调用 <code>fieldsStore</code> 中的<code>getFieldMeta</code> 方法， <code>fieldsStore</code> 实例对象在整个过程中尤为关键，它的作用是作为一个数据中心，让我们免除了手动去维护 <code>form</code> 中绑定的各个值。那么我们看一下 <code>fieldsStore.getFieldMeta</code> 做了那些工作？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-title">getFieldMeta</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.fieldsMeta[name] = <span class="hljs-built_in">this</span>.fieldsMeta[name] || &#123;&#125;;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.fieldsMeta[name];
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此函数作用在于根据组件传递的 name 属性获取数据中心的 fieldMeta，如果没有则默认空对象，也就是首次渲染返回初始值。 重要的是 inputProps 的组装环节，第一步调用 <code>getFieldValuePropValue</code> 方法获取当前 props，然后加入 ref 属性，接下来是效验规则的收集。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> validateRules = normalizeValidateRules(validate, rules, validateTrigger);
<span class="hljs-keyword">const</span> validateTriggers = getValidateTriggers(validateRules);
validateTriggers.forEach(<span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (inputProps[action]) <span class="hljs-keyword">return</span>;
    inputProps[action] = <span class="hljs-built_in">this</span>.getCacheBind(name, action, <span class="hljs-built_in">this</span>.onCollectValidate);
&#125;);

<span class="hljs-keyword">if</span> (trigger && validateTriggers.indexOf(trigger) === -<span class="hljs-number">1</span>) &#123;
    inputProps[trigger] = <span class="hljs-built_in">this</span>.getCacheBind(name, trigger, <span class="hljs-built_in">this</span>.onCollect);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>validateRules </code>  即是所有的表单组件效验规则，<code>validateTriggers</code> 即所有效验规则触发的事件名， 那么我们就看一下  <code>nomalizeValidateRules</code>  以及  <code>getValidateTriggers </code> 方法是如何收集验证规则的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">normalizeValidateRules</span>(<span class="hljs-params">validate, rules, validateTrigger</span>) </span>&#123;
  <span class="hljs-keyword">const</span> validateRules = validate.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> newItem = &#123;
      ...item,
      <span class="hljs-attr">trigger</span>: item.trigger || [],
    &#125;;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> newItem.trigger === <span class="hljs-string">'string'</span>) &#123;
      newItem.trigger = [newItem.trigger];
    &#125;
    <span class="hljs-keyword">return</span> newItem;
  &#125;);
  <span class="hljs-keyword">if</span> (rules) &#123;
    validateRules.push(&#123;
      <span class="hljs-attr">trigger</span>: validateTrigger
      ? [].concat(validateTrigger)
      : [],
      rules,
    &#125;);
  &#125;
  <span class="hljs-keyword">return</span> validateRules;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getValidateTriggers</span>(<span class="hljs-params">validateRules</span>) </span>&#123;
  <span class="hljs-keyword">return</span> validateRules
    .filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !!item.rules && item.rules.length)
    .map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.trigger)
    .reduce(<span class="hljs-function">(<span class="hljs-params">pre, curr</span>) =></span> pre.concat(curr), []);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其会将  <code>validate</code>、  <code>rules</code> 组合，返回一个数组，其内部的元素为一个个规则对象，并且每个元素都存在一个可以为空的 <code>trigger</code> 数组，并且将  <code>validateTrigger</code> 作为 <code>rule</code> 的 <code>triggers</code> 推入 <code>validateRules</code> 中，我们回回头看一下 <code>validateTrigger</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fieldOption = &#123;
     name,
     <span class="hljs-attr">trigger</span>: DEFAULT_TRIGGER,
     <span class="hljs-attr">valuePropName</span>: <span class="hljs-string">'value'</span>,
     <span class="hljs-attr">validate</span>: [],
     ...usersFieldOption,
 &#125;;

<span class="hljs-keyword">const</span> &#123;
    rules,
    trigger,
    validateTrigger = trigger,
    validate,
&#125; = fieldOption;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看出如果用户配置了触发验证方法时默认使用配置的 <code>trigger</code>，如果用户没有设置 <code>trigger</code> 则默认使用默认 <code>onChange</code>。</p>
<p><code>getValidateTriggers</code> 则是将所有触发事件统一收集至一个数组，随后通过 forEach 循环将所有 <code>validateTriggers  </code> 中的事件都绑定上同一个处理函数getCacheBind上。</p>
<pre><code class="hljs language-js copyable" lang="js"> validateTriggers.forEach(<span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
 <span class="hljs-keyword">if</span> (inputProps[action]) <span class="hljs-keyword">return</span>;
 inputProps[action] = <span class="hljs-built_in">this</span>.getCacheBind(
    name, 
    action, 
    <span class="hljs-built_in">this</span>.onCollectValidate
  );
 &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面再来看一下触发验证规则绑定事件 action 的 getCacheBind 函数做了哪些操作?</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getCacheBind</span>(<span class="hljs-params">name, action, fn</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.cachedBind[name]) &#123;
    <span class="hljs-built_in">this</span>.cachedBind[name] = &#123;&#125;;
  &#125;
  <span class="hljs-keyword">const</span> cache = <span class="hljs-built_in">this</span>.cachedBind[name];
  <span class="hljs-keyword">if</span> (
    !cache[action] ||
    cache[action].oriFn !== fn 
  ) &#123;
    cache[action] = &#123;
      <span class="hljs-attr">fn</span>: fn.bind(<span class="hljs-built_in">this</span>, name, action),
      <span class="hljs-attr">oriFn</span>: fn,
    &#125;;
  &#125;
  <span class="hljs-keyword">return</span> cache[action].fn;
&#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p>暂且忽略 cachedBind 方法，这里可以看到 getCacheBind 方法主要对传入的 fn 做了一个改变 this 指向的逻辑处理，真正的处理函数则是  <code>onCollectValidate</code>，那我们来看一下  <code>onCollectValidate </code> 做了什么？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">onCollectValidate</span>(<span class="hljs-params">name_, action, ...args</span>)</span> &#123;
  <span class="hljs-keyword">const</span> &#123; field, fieldMeta &#125; = <span class="hljs-built_in">this</span>.onCollectCommon(name_, action, args);
  <span class="hljs-keyword">const</span> newField = &#123;
    ...field,
    <span class="hljs-attr">dirty</span>: <span class="hljs-literal">true</span>,
  &#125;;
  <span class="hljs-built_in">this</span>.fieldsStore.setFieldsAsDirty();
  
  <span class="hljs-built_in">this</span>.validateFieldsInternal([newField], &#123;
    action,
    <span class="hljs-attr">options</span>: &#123;<span class="hljs-attr">firstFields</span>: !!fieldMeta.validateFirst,&#125;,
  &#125;);
&#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 <code>onCollectValidate    </code> 被调用，也就是数据校验函数被触发时，首先调用了 onCollectCommon 方法，那么这个函数是干什么的？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">onCollectCommon</span>(<span class="hljs-params">name, action, args</span>)</span> &#123;
  <span class="hljs-keyword">const</span> fieldMeta = <span class="hljs-built_in">this</span>.fieldsStore.getFieldMeta(name);
  <span class="hljs-keyword">if</span> (fieldMeta[action]) &#123;
    fieldMeta[action](...args);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (fieldMeta.originalProps && fieldMeta.originalProps[action]) &#123;
    fieldMeta.originalProps[action](...args);
  &#125;
  <span class="hljs-keyword">const</span> value = fieldMeta.getValueFromEvent ?
        fieldMeta.getValueFromEvent(...args) :
  getValueFromEvent(...args);
  <span class="hljs-keyword">if</span> (onValuesChange && value !== <span class="hljs-built_in">this</span>.fieldsStore.getFieldValue(name)) &#123;
    <span class="hljs-keyword">const</span> valuesAll = <span class="hljs-built_in">this</span>.fieldsStore.getAllValues();
    <span class="hljs-keyword">const</span> valuesAllSet = &#123;&#125;;
    valuesAll[name] = value;
    <span class="hljs-built_in">Object</span>.keys(valuesAll).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> set(valuesAllSet, key, valuesAll[key]));
    onValuesChange(&#123;
      [formPropName]: <span class="hljs-built_in">this</span>.getForm(),
      ...this.props
    &#125;, set(&#123;&#125;, name, value), valuesAllSet);
  &#125;
  <span class="hljs-keyword">const</span> field = <span class="hljs-built_in">this</span>.fieldsStore.getField(name);
  <span class="hljs-keyword">return</span> (&#123; name, <span class="hljs-attr">field</span>: &#123; ...field, value, <span class="hljs-attr">touched</span>: <span class="hljs-literal">true</span> &#125;, fieldMeta &#125;);
&#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>onCollectCommon </code> 主要是获取了包装组件最新的值，随后将其包装在对象中返回，返回后将其组装为一个新的名为  <code>newField </code> 的对象。</p>
<p>而 <code>fieldsStore.setFieldsAsDirty</code>  则是标记包装组件的校验状态，暂且略过，随后执行  <code>validateFieldsInternal</code>， 我们看一下 validateFieldsInternal 函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">validateFieldsInternal</span>(<span class="hljs-params"> 
  fields,
  &#123; fieldNames, action, options = &#123;&#125; &#125;,
  callback,
</span>)</span> &#123;
  <span class="hljs-keyword">const</span> allRules = &#123;&#125;;
  <span class="hljs-keyword">const</span> allValues = &#123;&#125;;
  <span class="hljs-keyword">const</span> allFields = &#123;&#125;;
  <span class="hljs-keyword">const</span> alreadyErrors = &#123;&#125;;
  fields.forEach(<span class="hljs-function"><span class="hljs-params">field</span> =></span> &#123;
    <span class="hljs-keyword">const</span> name = field.name;
    <span class="hljs-keyword">if</span> (options.force !== <span class="hljs-literal">true</span> && field.dirty === <span class="hljs-literal">false</span>) &#123;
      <span class="hljs-keyword">if</span> (field.errors) &#123;
        set(alreadyErrors, name, &#123; <span class="hljs-attr">errors</span>: field.errors &#125;);
      &#125;
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">const</span> fieldMeta = <span class="hljs-built_in">this</span>.fieldsStore.getFieldMeta(name);
    <span class="hljs-keyword">const</span> newField = &#123;
      ...field,
    &#125;;
    newField.errors = <span class="hljs-literal">undefined</span>;
    newField.validating = <span class="hljs-literal">true</span>;
    newField.dirty = <span class="hljs-literal">true</span>;
    allRules[name] = <span class="hljs-built_in">this</span>.getRules(fieldMeta, action);
    allValues[name] = newField.value;
    allFields[name] = newField;
  &#125;);
  <span class="hljs-built_in">this</span>.setFields(allFields);
  <span class="hljs-comment">// in case normalize</span>
  <span class="hljs-built_in">Object</span>.keys(allValues).forEach(<span class="hljs-function"><span class="hljs-params">f</span> =></span> &#123;
    allValues[f] = <span class="hljs-built_in">this</span>.fieldsStore.getFieldValue(f);
  &#125;);
  <span class="hljs-keyword">if</span> (callback && isEmptyObject(allFields)) &#123;
    callback(
      isEmptyObject(alreadyErrors) ? <span class="hljs-literal">null</span> : alreadyErrors,
      <span class="hljs-built_in">this</span>.fieldsStore.getFieldsValue(fieldNames),
    );
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-comment">// console.log(allRules);</span>
  <span class="hljs-keyword">const</span> validator = <span class="hljs-keyword">new</span> AsyncValidator(allRules);
  <span class="hljs-keyword">if</span> (validateMessages) &#123;
    <span class="hljs-comment">// console.log(validateMessages);</span>
    validator.messages(validateMessages);
  &#125;
  validator.validate(allValues, options, <span class="hljs-function"><span class="hljs-params">errors</span> =></span> &#123;
    <span class="hljs-keyword">const</span> errorsGroup = &#123;
      ...alreadyErrors,
    &#125;;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">const</span> expired = [];
    <span class="hljs-keyword">const</span> nowAllFields = &#123;&#125;;
    <span class="hljs-built_in">Object</span>.keys(allRules).forEach(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
      <span class="hljs-keyword">const</span> fieldErrors = get(errorsGroup, name);
      <span class="hljs-keyword">const</span> nowField = <span class="hljs-built_in">this</span>.fieldsStore.getField(name);
      <span class="hljs-comment">// avoid concurrency problems</span>
      <span class="hljs-keyword">if</span> (!eq(nowField.value, allValues[name])) &#123;
        expired.push(&#123;
          name,
        &#125;);
      &#125; <span class="hljs-keyword">else</span> &#123;
        nowField.errors = fieldErrors && fieldErrors.errors;
        nowField.value = allValues[name];
        nowField.validating = <span class="hljs-literal">false</span>;
        nowField.dirty = <span class="hljs-literal">false</span>;
        nowAllFields[name] = nowField;
      &#125;
    &#125;);
    <span class="hljs-built_in">this</span>.setFields(nowAllFields);
    <span class="hljs-comment">// ...</span>
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 <code>validateFieldsInternal</code> 主要逻辑都是在调用 <code>AsyncValidator</code>  进行异步校验以及对特殊场景的处理，我们暂时略过只看数据收集部分，我们看到在最后调用了  <code>this.setFields(allFields);</code> 并传入了新的值，接下来就看一下  <code>setFields</code> 方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setFields</span>(<span class="hljs-params">maybeNestedFields, callback</span>)</span> &#123;
  <span class="hljs-keyword">const</span> fields = <span class="hljs-built_in">this</span>.fieldsStore.flattenRegisteredFields(maybeNestedFields);
  <span class="hljs-built_in">this</span>.fieldsStore.setFields(fields);
  <span class="hljs-keyword">if</span> (onFieldsChange) &#123;
    <span class="hljs-keyword">const</span> changedFields = <span class="hljs-built_in">Object</span>.keys(fields)
    .reduce(<span class="hljs-function">(<span class="hljs-params">acc, name</span>) =></span> set(acc, name, <span class="hljs-built_in">this</span>.fieldsStore.getField(name)), &#123;&#125;);
    onFieldsChange(&#123;
      [formPropName]: <span class="hljs-built_in">this</span>.getForm(),
      ...this.props
    &#125;, changedFields, <span class="hljs-built_in">this</span>.fieldsStore.getNestedAllFields());
  &#125;
  <span class="hljs-built_in">this</span>.forceUpdate(callback);
&#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到， <code>setFields</code> 首先对传入的值进行与初始化相似的验证，随后调用 fieldsStore 实例中的 setFields 方法将值存入  <code>fieldsStore</code>， 暂时忽略  <code>onFieldsChange</code>，之后调用 <code>forceUpdate</code> 更新视图。到此，我们简单的描述了整个流程。</p>
<h4 data-id="heading-7">表单数据双向绑定</h4>
<p>表单数据更新大致流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13b00035e0a84410a16da28a15075b9c~tplv-k3u1fbpfcp-zoom-1.image" alt="forceUpdate" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>总结:</strong></p>
<ul>
<li>
<p>用户输入或者选择表单组件的行为都会触发 getFieldDecorator(HOC) 高阶组件，进而调用 getFieldProps 组装组件 props，这个方法中如果表单组件中配置了 validateRules 以及 validateTriggers 的话(也就是 rules 对象) 就调用 onCollectValidate 方法收集效验规则。然后就是设置表单组件的最新的值到 fieldsStore 中， 并调用 this.forceUpdate() 更新 UI 视图!</p>
</li>
<li>
<p>如果我们没有配置 validateRules 以及 validateTriggers 等规则，那就使用 onCollect 方法收集最新的数据并更新到 fieldsStore 中。不对表单进行单独验证,，从而在设置最新值 setFields 方法中调用 this.forceUpdate() 更新UI视图!</p>
</li>
</ul>
<h4 data-id="heading-8">整体设计思路</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a599dadab0c4afc94b6ec5c49bd2b7e~tplv-k3u1fbpfcp-zoom-1.image" alt="fremework" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>总结:</strong></p>
<ul>
<li>总之 rc-form 内部有自己的状态管理，fieldsStore 记录着所有表单项的信息，通过 getFieldDecorator 和表单进行双向绑定；</li>
<li>真正的区别在于用不用表单规则验证，不用就 onCollect，否则使用 onCollectValidate，但是必然都会使用 onCollectCommon；</li>
<li>onCollectCommon 方法内部展示了 onCollect 取值的细节，forceUpdate 在更新组件后，触发 render 方法，接着又回到一开始 getFieldDecorator 中获取 fieldStore 内的值，返回被修改后的组件。</li>
</ul>
<blockquote>
<p>想一下假如当我改变输入框的值得时候是不是会引起表单的重新渲染的问题。 所以这也就导致了渲染性能的问题! 那么必然会有优化的方法，有兴趣的可以看看 rc-field-form。</p>
</blockquote>
<p>文章只是整体浅析实现思路，如有不同意见，欢迎联系我交流</p>
<h2 data-id="heading-9">推荐阅读</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzoo.team%2Farticle%2Fabout-vite" target="_blank" rel="nofollow noopener noreferrer" title="https://zoo.team/article/about-vite" ref="nofollow noopener noreferrer">Vite 特性和部分源码解析</a></p>
<p><a href="https://juejin.cn/post/6974184935804534815" target="_blank" title="https://juejin.cn/post/6974184935804534815">我在工作中是如何使用 git 的</a></p>
<p><a href="https://juejin.cn/post/6981921291980767269" target="_blank" title="https://juejin.cn/post/6981921291980767269">Serverless Custom (Container) Runtime</a></p>
<h2 data-id="heading-10">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zoo.team%2Fopenweekly%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zoo.team/openweekly/" ref="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-11">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d3aa3d1f8646a8bcda8cfd9e335a4b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            