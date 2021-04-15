
---
title: '基于vue3.0+TS的自定义表单工具 ✨'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c562537a521439cae664bfdaf3f060e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 18:36:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c562537a521439cae664bfdaf3f060e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><figure><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c562537a521439cae664bfdaf3f060e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></figure>
<p>由于本人最近要做一个动态工作流系统，其中需要用到自定义表单这个功能。但是由于我自己的这个项目是基于vue3.0开发的，目前市面上已有的这些自定义表单都是不支持的。想了想算了，还是自己搞一个，后面可扩展性也比较强。于是参考了目前市面上大部分自定义表单的功能，做了个基于vue3.0 + ts的自定义表单插件。支持 ant-design-vue 和 element-plus这两个UI库。目前刚做好初版，做个简单介绍，大家有需要的可以直接拿去用。</p>
<h1 data-id="heading-0"><span class="prefix"></span><span class="content">vue-form-create</span><span class="suffix"></span></h1>
<p>基于 Vue3.0 + TS 的自定义表单生成器。支持 npm 与 cdn 引入的方式。UI 库支持 ant-design-vue 与 element-plus。</p>
<figure><img alt="预览" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/375eabc0c39240299cc4f28fbe66b53b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<h2 data-id="heading-1"><span class="prefix"></span><span class="content">支持功能</span><span class="suffix"></span></h2>
<ul>
<li>远端数据获取</li><li>图片上传</li><li>富文本编辑器</li><li>栅格布局</li><li>生成JSON</li><li>生成代码</li></ul>
<h3 data-id="heading-2"><span class="prefix"></span><span class="content">演示地址（github）</span><span class="suffix"></span></h3>
<p><a href="https://fuchengwei.github.io/vue-form-create/example/index.html" target="_blank" rel="nofollow noopener noreferrer">fuchengwei.github.io/vue-form-cr…</a></p>
<h3 data-id="heading-3"><span class="prefix"></span><span class="content">演示地址（gitee）</span><span class="suffix"></span></h3>
<p><a href="http://fuchengwei.gitee.io/vue-form-create/example/index.html" target="_blank" rel="nofollow noopener noreferrer">fuchengwei.gitee.io/vue-form-cr…</a></p>
<h3 data-id="heading-4"><span class="prefix"></span><span class="content">github</span><span class="suffix"></span></h3>
<p><a href="https://github.com/fuchengwei/vue-form-create" target="_blank" rel="nofollow noopener noreferrer">github.com/fuchengwei/…</a></p>
<h3 data-id="heading-5"><span class="prefix"></span><span class="content">npm</span><span class="suffix"></span></h3>
<p><a href="https://www.npmjs.com/package/vue-form-create" target="_blank" rel="nofollow noopener noreferrer">www.npmjs.com/package/vue…</a></p>
<h2 data-id="heading-6"><span class="prefix"></span><span class="content">1 安装</span><span class="suffix"></span></h2>
<h3 data-id="heading-7"><span class="prefix"></span><span class="content">使用 npm 或 yarn 安装</span><span class="suffix"></span></h3>
<p><strong>我们推荐使用 npm 或 yarn 的方式进行开发</strong>，不仅可在开发环境轻松调试，也可放心地在生产环境打包部署使用，享受整个生态圈和工具链带来的诸多好处。</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-meta">$</span><span class="bash"> npm install vue-form-create --save</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-meta">$</span><span class="bash"> yarn add vue-form-create</span><br><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8"><span class="prefix"></span><span class="content">浏览器引入</span><span class="suffix"></span></h3>
<p>在浏览器中使用 <code>script</code> 标签直接引入文件，并使用全局变量 <code>formCreate</code>。</p>
<p>我们在 npm 发布包内的 <code>vue-form-create/dist</code>提供了 <code>formCreate.common.js</code>  <code>formCreate.umd.js</code> <code>formCreate.umd.min.js</code>。你可以通过 <a href="https://unpkg.com/vue-form-create/dist/" target="_blank" rel="nofollow noopener noreferrer">UNPKG</a> 进行下载。</p>
<pre class="custom"><span></span><code class="hljs copyable"><script src=<span class="hljs-string">"https://unpkg.com/vue-form-create/dist/formCreate.umd.min.js"</span>><<span class="hljs-regexp">/script><br></span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><span class="prefix"></span><span class="content">注意</span><span class="suffix"></span></h3>
<ol>
<li><p>无论 npm 或者 cdn 引入都需要在全局引入 <a href="https://2x.antdv.com/docs/vue/introduce-cn" target="_blank" rel="nofollow noopener noreferrer">ant-design-vue</a> 或 <a href="https://element-plus.gitee.io/#/zh-CN" target="_blank" rel="nofollow noopener noreferrer">element-plus</a> 。并且项目依赖了 <a href="https://github.com/ajaxorg/ace" target="_blank" rel="nofollow noopener noreferrer">acejs</a> , 需要在全局使用 cdn 的方式引入。</p>
<pre class="custom"><span></span><code class="hljs copyable"><script src=<span class="hljs-string">"https://unpkg.com/ace-builds/src-noconflict/ace.js"</span>><<span class="hljs-regexp">/script><br></span><span class="copy-code-btn">复制代码</span></code></pre>
</li><li><p>cdn 引入 ant-design-vue 需要自行引入 <a href="http://momentjs.com/" target="_blank" rel="nofollow noopener noreferrer">moment</a> 。</p>
</li><li><p>不想在全局安装也可以在组件内直接使用相应的组件。</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">import</span> &#123; AntdDesignForm, ElDesignForm, AntdGenerateForm, ElGenerateForm &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-form-create'</span><br><span class="copy-code-btn">复制代码</span></code></pre>
</li></ol>
<h3 data-id="heading-10"><span class="prefix"></span><span class="content">示例</span><span class="suffix"></span></h3>
<p><strong>npm引入</strong></p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span><br><span class="hljs-keyword">import</span> antd <span class="hljs-keyword">from</span> <span class="hljs-string">'ant-design-vue'</span><br><span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span><br><span class="hljs-keyword">import</span> DesignForm <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-form-create'</span><br><span class="hljs-keyword">import</span> <span class="hljs-string">'ant-design-vue/dist/antd.css'</span><br><br>createApp(App)<br>  .use(antd)<br>  .use(DesignForm)<br>  .mount(<span class="hljs-string">'#app'</span>)<br><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>浏览器引入</strong></p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span><br><span class="hljs-tag"><<span class="hljs-name">html</span>></span><br>  <span class="hljs-tag"><<span class="hljs-name">head</span>></span><br>    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span><br>    <span class="hljs-tag"><<span class="hljs-name">link</span><br>      <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span><br>      <span class="hljs-attr">href</span>=<span class="hljs-string">"https://unpkg.com/ant-design-vue@next/dist/antd.min.css"</span><br>    /></span><br>  <span class="hljs-tag"></<span class="hljs-name">head</span>></span><br>  <span class="hljs-tag"><<span class="hljs-name">body</span>></span><br>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><br>      <span class="hljs-tag"><<span class="hljs-name">antd-design-form</span> /></span><br>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span><br>    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next/dist/vue.global.prod.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span><br>    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue-form-create/dist/formCreate.umd.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span><br>    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/ace-builds/src-noconflict/ace.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span><br>    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/moment/moment.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span><br>    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/ant-design-vue@next/dist/antd.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span><br>    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"><br>      <span class="hljs-keyword">const</span> &#123; createApp, reactive, toRefs &#125; = Vue<br><br>      createApp(&#123;&#125;)<br>        .use(antd)<br>        .use(formCreate)<br>        .mount(<span class="hljs-string">'#app'</span>)<br>    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span><br>  <span class="hljs-tag"></<span class="hljs-name">body</span>></span><br><span class="hljs-tag"></<span class="hljs-name">html</span>></span><br><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11"><span class="prefix"></span><span class="content">2 组件说明</span><span class="suffix"></span></h2>
<h3 data-id="heading-12"><span class="prefix"></span><span class="content">表单设计器（AntdDesignForm）</span><span class="suffix"></span></h3>
<p><strong>示例</strong></p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-tag"><<span class="hljs-name">template</span>></span><br> <span class="hljs-tag"><<span class="hljs-name">AntdDesignForm</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"designForm"</span>  /></span><br><span class="hljs-tag"></<span class="hljs-name">template</span>></span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>API</strong></p>
<h6 data-id="heading-13"><span class="prefix"></span><span class="content">Props</span><span class="suffix"></span></h6>
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
<th>类型</th>
<th>默认值</th>
</tr>
</thead>
<tbody>
<tr>
<td>preview</td>
<td>设计器预览操作按钮</td>
<td>boolean</td>
<td>true</td>
</tr>
<tr>
<td>generateCode</td>
<td>设计器生成代码按钮</td>
<td>boolean</td>
<td>true</td>
</tr>
<tr>
<td>generateJson</td>
<td>设计器生成Json按钮</td>
<td>boolean</td>
<td>true</td>
</tr>
<tr>
<td>uploadJson</td>
<td>设计器导入JSON按钮</td>
<td>boolean</td>
<td>true</td>
</tr>
<tr>
<td>clearable</td>
<td>设计器清空按钮</td>
<td>boolean</td>
<td>true</td>
</tr>
<tr>
<td>basicFields</td>
<td>设计器左侧基础字段配置</td>
<td>array</td>
<td>-</td>
</tr>
<tr>
<td>advanceFields</td>
<td>设计器左侧高级字段配置</td>
<td>array</td>
<td>-</td>
</tr>
<tr>
<td>layoutFields</td>
<td>设计器左侧布局字段配置</td>
<td>array</td>
<td>-</td>
</tr>
</tbody>
</table>
<h6 data-id="heading-14"><span class="prefix"></span><span class="content">方法</span><span class="suffix"></span></h6>
<p>通过 ref 可以获取到实例并调用实例方法</p>
<table>
<thead>
<tr>
<th>方法名</th>
<th>说明</th>
<th>参数</th>
</tr>
</thead>
<tbody>
<tr>
<td>getJson()</td>
<td>获取设计器配置的JSON数据</td>
<td>-</td>
</tr>
<tr>
<td>setJson(value)</td>
<td>设置设计器的配置信息</td>
<td>通过getJson获取的数据</td>
</tr>
<tr>
<td>clear()</td>
<td>清空设计器</td>
<td></td>
</tr>
<tr>
<td>getTemplate(type)</td>
<td>获取设计器生成的可以直接使用的代码</td>
<td>type的类型为 'vue' 或 'html'</td>
</tr>
</tbody>
</table>
<h6 data-id="heading-15"><span class="prefix"></span><span class="content">字段说明</span><span class="suffix"></span></h6>
<p>基础字段（basicFields）</p>
<table>
<thead>
<tr>
<th>type</th>
<th>字段名</th>
</tr>
</thead>
<tbody>
<tr>
<td>input</td>
<td>单行文本</td>
</tr>
<tr>
<td>password</td>
<td>密码框</td>
</tr>
<tr>
<td>textarea</td>
<td>多行文本</td>
</tr>
<tr>
<td>number</td>
<td>计数器</td>
</tr>
<tr>
<td>radio</td>
<td>单选框组</td>
</tr>
<tr>
<td>checkbox</td>
<td>多选框组</td>
</tr>
<tr>
<td>time</td>
<td>时间选择器</td>
</tr>
<tr>
<td>date</td>
<td>日期选择器</td>
</tr>
<tr>
<td>rate</td>
<td>评分</td>
</tr>
<tr>
<td>select</td>
<td>下拉选择框</td>
</tr>
<tr>
<td>switch</td>
<td>开关</td>
</tr>
<tr>
<td>slider</td>
<td>滑块</td>
</tr>
<tr>
<td>text</td>
<td>文字</td>
</tr>
</tbody>
</table>
<p>高级字段（advanceFields）</p>
<table>
<thead>
<tr>
<th>type</th>
<th>字段名</th>
</tr>
</thead>
<tbody>
<tr>
<td>img-upload</td>
<td>图片</td>
</tr>
<tr>
<td>richtext-editor</td>
<td>富文本编辑器</td>
</tr>
<tr>
<td>cascader</td>
<td>级联选择器</td>
</tr>
</tbody>
</table>
<p>布局字段（layoutFields）</p>
<table>
<thead>
<tr>
<th>type</th>
<th>字段名</th>
</tr>
</thead>
<tbody>
<tr>
<td>grid</td>
<td>栅格布局</td>
</tr>
</tbody>
</table>
<h3 data-id="heading-16"><span class="prefix"></span><span class="content">表单生成器（AntdGenerateForm）</span><span class="suffix"></span></h3>
<p><strong>示例</strong></p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-tag"><<span class="hljs-name">template</span>></span><br> <span class="hljs-tag"><<span class="hljs-name">AntdGenerateForm</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"generateForm"</span>  /></span><br><span class="hljs-tag"></<span class="hljs-name">template</span>></span><br><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>API</strong></p>
<h6 data-id="heading-17"><span class="prefix"></span><span class="content">Props</span><span class="suffix"></span></h6>
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
<th>类型</th>
<th>默认值</th>
</tr>
</thead>
<tbody>
<tr>
<td>data</td>
<td>表单json配置数据（从表单设计器获取的json）</td>
<td>object</td>
<td>-</td>
</tr>
<tr>
<td>value</td>
<td>表单数据（从表单生成器获取的value）</td>
<td>object</td>
<td>-</td>
</tr>
</tbody>
</table>
<h6 data-id="heading-18"><span class="prefix"></span><span class="content">方法</span><span class="suffix"></span></h6>
<p>通过 ref 可以获取到实例并调用实例方法</p>
<table>
<thead>
<tr>
<th>方法名</th>
<th>说明</th>
<th>参数</th>
</tr>
</thead>
<tbody>
<tr>
<td>getData()</td>
<td>获取表单数据（返回Promise）</td>
<td>-</td>
</tr>
<tr>
<td>reset()</td>
<td>重置表单数据</td>
<td>通过getJson获取的数据</td>
</tr>
</tbody>
</table>
<h2 data-id="heading-19"><span class="prefix"></span><span class="content">3 功能说明</span><span class="suffix"></span></h2>
<h3 data-id="heading-20"><span class="prefix"></span><span class="content">远端数据</span><span class="suffix"></span></h3>
<p>单选框，多选框，下拉选择框、级联选择器等选择项需要通过数据生成，这时可以配置远端数据。</p>
<p>设置远端方法地址与返回值。</p>
<figure><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a026b55f926d41d48c485170f7bdbb1b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></figure>
<h3 data-id="heading-21"><span class="prefix"></span><span class="content">文件上传</span><span class="suffix"></span></h3>
<p>填写服务器上传地址、参数名等配置信息。</p>
<figure><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc6dc82bbc7b4f21a7fbe859ff380152~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></figure>
<h2 data-id="heading-22"><span class="prefix"></span><span class="content">4 后续规划</span><span class="suffix"></span></h2>
<p>目前是v1.0.0的初版，后面预计支持更多的功能组件与布局组件，以及对移动端的支持。
对于移动端不知道大家对那个UI库用的比较多，可以在下面留言告诉我，后面我会优先考虑支持的。</p>
<p>最后如果大家觉得还不错挺好用的话，麻烦给个 Star 😜😜😜。</p>
</div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            