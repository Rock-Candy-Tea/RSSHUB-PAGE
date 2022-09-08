
---
title: 'XRender - 开源之路'
categories: 
 - 编程
 - 掘金
 - 专栏
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b63e3568b5304bd58a022804cd3fae6c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Wed, 16 Mar 2022 19:42:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b63e3568b5304bd58a022804cd3fae6c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2Fx-render" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/x-render" ref="nofollow noopener noreferrer">XRender</a> 是由阿里飞猪内部孵化出的开源产品，目前在GitHub上有 4.2k star；本篇文章不会对XRender的用法进行赘述；我们的目的在于让更多人了解到XRender在这一年内发生了哪些变化，并让XRender能够帮助更多的前端开发者。</p>
</blockquote>
<blockquote>
<p>Github：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2Fx-render" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/x-render" ref="nofollow noopener noreferrer">github.com/alibaba/x-r…</a>
官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fx-render.gitee.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://x-render.gitee.io/" ref="nofollow noopener noreferrer">x-render.gitee.io/</a></p>
</blockquote>
<h2 data-id="heading-0">一、前言</h2>
<h3 data-id="heading-1">1.什么是XRender</h3>
<p>XRender 是一套基于 React.js 框架的，<strong>轻量、易用、易上手</strong>的中后台「<strong>表单 / 表格 / 图表</strong>」解决方案，目前已经在阿里飞猪内部服务了3年，未来也将持续服务 XRender 的用户。</p>
<h3 data-id="heading-2">2.为什么需要XRender</h3>
<p>对于中后台业务来说，表单+表格可以覆盖90%的业务场景，而大部分业务的表单、表格场景<strong>重复度高</strong>。开发人员没必要将时间花费在表单、表格的切图上，因此像 XRender 这样的提效工具必不可少。</p>
<h2 data-id="heading-3">二、XRender 的自我革新</h2>
<p>三年前，FormRender 孵化于阿里飞猪，作为表单解决方案于 GitHub 上正式开源，成为 XRender 家族的第一位成员。</p>
<p>面对日渐复杂的业务场景，FormRender 0.x 陈旧的技术方案遇到了挑战，内部决定对 <strong>FormRender</strong> 进行升级，同时<strong>新增更多的Render方案</strong>，为内部的前端开发者提效。</p>
<p>现在的 XRender 除了 <strong>FormRender</strong> 之外，还拥有「<strong>FRGenetator、TableRender、ChartRender</strong>」四个常见的组件渲染方案，这4个方案合起来称为 <strong>XRender</strong>。</p>
<h3 data-id="heading-4">1.「<a href="https://link.juejin.cn/?target=https%3A%2F%2Fx-render.gitee.io%2Fform-render" target="_blank" rel="nofollow noopener noreferrer" title="https://x-render.gitee.io/form-render" ref="nofollow noopener noreferrer">FormRender</a>」 - 协议驱动的表单解决方案</h3>
<h4 data-id="heading-5">话不多说，先上代码</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Button</span>, <span class="hljs-title class_">PageHeader</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">FormRender</span>, &#123; useForm &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'form-render'</span>;

<span class="hljs-keyword">const</span> schema = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'object'</span>,
  <span class="hljs-attr">properties</span>: &#123;
    <span class="hljs-attr">input</span>: &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'简单输入框'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>,
      <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'昵称'</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
    &#125;,
    <span class="hljs-attr">textarea</span>: &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'简单文本编辑框'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'textarea'</span>,
    &#125;,
    <span class="hljs-attr">color</span>: &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'颜色选择'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'color'</span>,
    &#125;,
    <span class="hljs-attr">image</span>: &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'图片展示'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'image'</span>,
    &#125;,
    <span class="hljs-attr">uploader</span>: &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'上传文件'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'upload'</span>,
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">action</span>: <span class="hljs-string">'https://www.mocky.io/v2/5cc8019d300000980a055e76'</span>,
      &#125;,
    &#125;,
  &#125;,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">Form</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> form = <span class="hljs-title function_">useForm</span>();

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">onFinish</span> = (<span class="hljs-params">formData: <span class="hljs-built_in">any</span>, errors: <span class="hljs-built_in">any</span></span>) => &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'formData:'</span>, formData, <span class="hljs-string">'校验信息:'</span>, errors);
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">PageHeader</span>
      <span class="hljs-attr">ghost</span>=<span class="hljs-string">&#123;false&#125;</span>
      <span class="hljs-attr">onBack</span>=<span class="hljs-string">&#123;()</span> =></span> history.go(-1)&#125;
      title="创建活动报名"
      subTitle=""
      extra=&#123;[
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;form.submit&#125;</span>></span>
          提交
        <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>,
      ]&#125;
    >
      <span class="hljs-tag"><<span class="hljs-name">FormRender</span> <span class="hljs-attr">form</span>=<span class="hljs-string">&#123;form&#125;</span> <span class="hljs-attr">schema</span>=<span class="hljs-string">&#123;schema&#125;</span> <span class="hljs-attr">onFinish</span>=<span class="hljs-string">&#123;onFinish&#125;</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">PageHeader</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">渲染结果</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b63e3568b5304bd58a022804cd3fae6c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码渲染结果如上图，可以看到 <strong>FormRender</strong> 的核心没有改变，依然遵循：「<strong>协议驱动渲染</strong>」。</p>
<h4 data-id="heading-7">代码重构，面向未来</h4>
<p><strong>FormRender 1.x 对本身的内核进行了非常彻底的重构，全面拥抱了 React Hooks 和 Antd Design 4.x，且增加了 Typescript 的类型定义，写法上相比于 FormRender 0.x 精简了很多</strong>。</p>
<h4 data-id="heading-8">生命周期</h4>
<p><strong>新增 beforeFinish、onFinish</strong> 两个钩子，供开发者进行「表单提交前的校验处理」，「提交表单数据」；<strong>新增 onMount 方法</strong>，类似于 React 的 componentDidMount；</p>
<h4 data-id="heading-9">状态内置</h4>
<p><strong>新增 useForm 方法</strong>，返回 form 实例，对表单的所有操作都依赖于 form 实例提供的方法。方便开发者做对表单、schema 进行操作，比如：异步获取数据后，通过 <strong>form.setSchemaByPath</strong> 动态修改下拉选框的 schema；</p>
<h4 data-id="heading-10">数据监听</h4>
<p><strong>新增了 watch 变量</strong>，用于数据的监听的唤起回调，语法类似于 vue 的 watch。</p>
<h4 data-id="heading-11">内置组件更加丰富</h4>
<p>新增了 <strong>rate、treeSelect</strong> 等组件的内置支持；我们给 <strong>JSON Schema</strong> 新增了 <strong>format</strong> 属性，用来描述输入框的格式，辅助 <strong>type</strong> 一同用于判断使用哪个组件来渲染，以及校验表单数据。</p>
<h4 data-id="heading-12">更好的自定义组件支持</h4>
<p>自定义组件功能使 FormRender 拥有很好扩展性，当FormRender 提供的内置组件无法满足你的需求时，可以考虑写一个自定义组件。</p>
<h3 data-id="heading-13">2.「<a href="https://link.juejin.cn/?target=https%3A%2F%2Fx-render.gitee.io%2Fgenerator" target="_blank" rel="nofollow noopener noreferrer" title="https://x-render.gitee.io/generator" ref="nofollow noopener noreferrer">表单设计器</a>」- 中后台表单可视化搭建生成利器</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c884c7363404d55a1ca41edfeac8814~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">可拖拽、可搭建的表单设计器</h4>
<p><strong>FormRender</strong> 解放了前端开发在写表单上的效率，而基于 <strong>FormRender</strong> 的「表单设计器」，为表单带来了可搭建、可拖拽的能力，并支持导出对应的 <strong>schema</strong> 。</p>
<h3 data-id="heading-15">3.「<a href="https://link.juejin.cn/?target=https%3A%2F%2Fx-render.gitee.io%2Ftable-render" target="_blank" rel="nofollow noopener noreferrer" title="https://x-render.gitee.io/table-render" ref="nofollow noopener noreferrer">TableRender</a>」 - 表格解决方案</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbe8105778ad4457bd1d933440343f21~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">优势</h4>
<p><strong>TableRender</strong> 是 <strong>XRender</strong> 的新成员，它是基于 <strong>FormRender</strong> 的「表格解决方案」，内置了<strong>搜索、重置、分页</strong>的功能，开发者只需要提供「<strong>schema、columns</strong>」即可快速开发一个与服务端交互的查询表格。搜索筛选能力用 FormRender 来提供，以最小成本快速生成上侧搜索面板。</p>
<h4 data-id="heading-17">无缝习惯使用</h4>
<p><strong>TableRender</strong> 就像使用 Antd Table 一样，但是我们扩展了 Antd Table 的 column 属性，提供了<strong>enum、ellipsis、valueType</strong>等特性，可以快速格式化表格数据，例如：<strong>时间格式化、文本省略展示、ToolTips、enum枚举定义</strong>等。</p>
<h4 data-id="heading-18">获取 TableRender Context</h4>
<p>我们提供了 <strong>useTable</strong> ，用于获取 <strong>TableRender</strong> 整体的 <strong>React Context</strong>，其返回的方法可供开发者进行自定义的操作。</p>
<h3 data-id="heading-19">4.「<a href="https://link.juejin.cn/?target=https%3A%2F%2Fx-render.gitee.io%2Fchart-render" target="_blank" rel="nofollow noopener noreferrer" title="https://x-render.gitee.io/chart-render" ref="nofollow noopener noreferrer">ChartRender</a>」 - 图表解决方案</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86ded60ca23c4cb29288299d971409a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>ChartRender</strong> 是基于 <strong>@ant-design/charts</strong> 的图表解决方案，常用于图表展示页快速生成。可用少量代码快速生成一张图表。</p>
<h4 data-id="heading-20">真正的开箱即用</h4>
<p>只需要关心你的数据，传入 meta、data 即可出图。</p>
<h4 data-id="heading-21">开发体验舒适</h4>
<p>使用 TypeScript 开发，提供完整的类型定义文件。</p>
<h4 data-id="heading-22">无缝习惯使用</h4>
<p>图表用 Ant Design Charts 来提供，自定义的样式支持参数透传。</p>
<h2 data-id="heading-23">三、适合场景</h2>
<h4 data-id="heading-24">中后台业务开发</h4>
<p><strong>XRender</strong> 已经全面覆盖飞猪的中后台业务，除此之外，还有阿里云、高德、淘宝、蚂蚁等BU的同学在深入使用。</p>
<h4 data-id="heading-25">面向C端的投放、搭建平台</h4>
<p><strong>如果你的团队正在做面向运营的搭建平台，那么我们非常推荐你基于 XRender 来搞</strong>以下为社区同学给出的优秀案例：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccd0c613a12145019e40d380a044bb9a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="5.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49118f769a314cb0b031d4355bbae63f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-26">谁在使用</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/850d9e84e5874bc08cf5d1a3d4c757ba~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更多可见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2Fform-render%2Fissues%2F94" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/form-render/issues/94" ref="nofollow noopener noreferrer">使用场景</a>，若 XRender 有帮助到你，也很欢迎在评论区补充或者提交PR。</p>
<h2 data-id="heading-27">四、未来规划</h2>
<h4 data-id="heading-28">List、Array类型的内置组件支持自定义</h4>
<p>FormRender内置的List、Array类型的嵌套组件样式单一、暂不不支持自定义，需要开放定制化的口子出来，满足不同的业务需求。</p>
<h4 data-id="heading-29">XRender 2.0</h4>
<p>XRender 1.x 已经稳定运行一年左右的时间了，为了支持更多的组件库和移动端引擎，需要对底层代码进行抽离与重构，具体的Action大致为：抽离 <strong>form-render-core、实现插件机制、移动端渲染引擎。</strong></p>
<h4 data-id="heading-30">拥抱移动端</h4>
<p>XRender 服务了3年的 PC 端业务，在此期间，不管是社区还是内部，对于 XRender 在移动端上的需求从未停止过；最近在 XRender 的开发者周会上，对此进行了认真的讨论与规划，决定在 2022 年中旬完成 <strong>XRender 2.0</strong> 的开发，支持移动端：Rax、Ant Design Mobile v5。</p>
<h2 data-id="heading-31">五、结尾</h2>
<p><strong>为感谢XRender的开发者们，我们特意制作了一个视频，以此向社区中的小伙伴们致敬！</strong>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fintranetproxy.alipay.com%2Fskylark%2Flark%2F0%2F2022%2Fmp4%2F263405%2F1647397030754-ef1c1dcb-51f6-4e6f-b37a-da40194be9e7.mp4" target="_blank" rel="nofollow noopener noreferrer" title="https://intranetproxy.alipay.com/skylark/lark/0/2022/mp4/263405/1647397030754-ef1c1dcb-51f6-4e6f-b37a-da40194be9e7.mp4" ref="nofollow noopener noreferrer">xrender.mp4</a></p>
<p>1.如果你想在项目中尝试使用 <strong>XRender</strong> 来提高日常开发效率，那么可以通过访问我们的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fx-render.gitee.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://x-render.gitee.io/" ref="nofollow noopener noreferrer">文档站点</a> 快速上手；</p>
<p>2.如果你想翻阅源代码或者提交 <strong>Issue</strong>，那么可以前往我们的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2Fx-render" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/x-render" ref="nofollow noopener noreferrer">GitHub 仓库</a>；</p></div>  
</div>
            