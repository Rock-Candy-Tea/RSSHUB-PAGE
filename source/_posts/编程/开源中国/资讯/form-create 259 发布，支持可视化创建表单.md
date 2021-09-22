
---
title: 'form-create 2.5.9 发布，支持可视化创建表单'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-621b6c6bd380a2a7abc9e8dcded63f44c13.png'
author: 开源中国
comments: false
date: Wed, 22 Sep 2021 09:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-621b6c6bd380a2a7abc9e8dcded63f44c13.png'
---

<div>   
<div class="content">
                                                                                            <p>form-create 是一个可以通过 JSON 生成具有动态渲染、数据收集、验证和提交功能的表单生成组件。支持3个UI框架，并且支持生成任何 Vue 组件。内置20种常用表单组件和自定义组件，再复杂的表单都可以轻松搞定。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2F%3Ffrom%3Dosn" target="_blank">文档</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxaboy%2Fform-create" target="_blank">GitHub</a> | <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fdemo.html%3Ffrom%3Dosn" target="_blank">示例</a> |  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fdesigner%3Ffrom%3Dosn" target="_blank">可视化表单设计器</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">支持 UI</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>element-ui</li> 
 <li>iview/view-design</li> 
 <li>ant-design-vue</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2.5.9主要更新了以下内容:</strong></p> 
<div> 
 <ul> 
  <li><strong>新增<span> </span><code>fetch</code><span> </span>功能,  加载异步数据</strong></li> 
  <li>新增<span> </span><code>subForm</code><span> </span>组件新增<span> </span><code>syncDisabled</code><span> </span>配置项</li> 
 </ul> 
</div> 
<div> 
 <ul> 
  <li> <p>新增<span> </span><strong><code>factory</code><span> </span>方法, 创建一个全新的<span> </span><code>formCreate</code><span> </span>对象</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fglobal-api.html%23factory" target="_blank">(说明)</a></p> </li> 
  <li> <p>新增 自定义属性新增<code>load</code>事件,调整<span> </span><code>init</code>事件触发时机</p> </li> 
  <li> <p>新增<span> </span><code>repeat</code><span> </span>事件, 当组件字段重复时触发</p> </li> 
  <li> <p>优化<span> </span><strong><code>formData</code><span> </span>数据, 支持增量返回额外字段</strong></p> </li> 
  <li> <p>优化 支持<code>element-ui</code>表单的<code>label-suffix</code>配置项 #402</p> </li> 
  <li> <p>优化<span> </span><code>remove</code>事件触发时机</p> </li> 
  <li> <p>优化 增强<code>json</code>解析功能</p> </li> 
  <li> <p>修复 移除规则时可能意外报错问题</p> </li> 
 </ul> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装</h2> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">根据自己使用的 UI 安装对应的版本</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>element-ui</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span> <span style="color:#d73a49"><span style="color:#d73a49">i</span></span> @<span style="color:#d73a49"><span style="color:#d73a49">form</span></span>-<span style="color:#d73a49"><span style="color:#d73a49">create</span></span>/<span style="color:#d73a49"><span style="color:#d73a49">element</span></span>-<span style="color:#d73a49"><span style="color:#d73a49">ui</span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>iview@2.x|3.x</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span> <span style="color:#d73a49"><span style="color:#d73a49">i</span></span> @<span style="color:#d73a49"><span style="color:#d73a49">form</span></span>-<span style="color:#d73a49"><span style="color:#d73a49">create</span></span>/<span style="color:#d73a49"><span style="color:#d73a49">iview</span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>iview/view-design@4.x</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span> <span style="color:#d73a49"><span style="color:#d73a49">i</span></span> @<span style="color:#d73a49"><span style="color:#d73a49">form</span></span>-<span style="color:#d73a49"><span style="color:#d73a49">create</span></span>/<span style="color:#d73a49"><span style="color:#d73a49">iview4</span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>ant-design-vue@1.5+</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span> <span style="color:#d73a49"><span style="color:#d73a49">i</span></span> @<span style="color:#d73a49"><span style="color:#d73a49">form</span></span>-<span style="color:#d73a49"><span style="color:#d73a49">create</span></span>/<span style="color:#d73a49"><span style="color:#d73a49">ant</span></span>-<span style="color:#d73a49"><span style="color:#d73a49">design</span></span>-<span style="color:#d73a49"><span style="color:#d73a49">vue</span></span></code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">快速上手</h2> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">本文以<code>element-ui</code>为例</p> 
</blockquote> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>在 main.js 中写入以下内容：</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">import</span></span> Vue <span style="color:#d73a49"><span style="color:#d73a49">from</span></span> <span style="color:#032f62"><span style="color:#032f62">'vue'</span></span>
<span style="color:#d73a49"><span style="color:#d73a49">import</span></span> ELEMENT <span style="color:#d73a49"><span style="color:#d73a49">from</span></span> <span style="color:#032f62"><span style="color:#032f62">'element-ui'</span></span>
<span style="color:#d73a49"><span style="color:#d73a49">import</span></span> <span style="color:#032f62"><span style="color:#032f62">'element-ui/lib/theme-chalk/index.css'</span></span>

<span style="color:#d73a49"><span style="color:#d73a49">import</span></span> formCreate <span style="color:#d73a49"><span style="color:#d73a49">from</span></span> <span style="color:#032f62"><span style="color:#032f62">'@form-create/element-ui'</span></span>

Vue.use(ELEMENT)
Vue.use(formCreate)</code></pre> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>生成表单</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fdemo.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-html"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">template</span></span></span><span style="color:#333333">></span></span>
  <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">div</span></span></span><span style="color:#333333"> </span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">id</span></span></span><span style="color:#333333">=</span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"app1"</span></span></span><span style="color:#333333">></span></span>
      <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">form-create</span></span></span><span style="color:#333333"> </span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">v-model</span></span></span><span style="color:#333333">=</span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"fApi"</span></span></span><span style="color:#333333"> </span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">:rule</span></span></span><span style="color:#333333">=</span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"rule"</span></span></span><span style="color:#333333"> </span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">:option</span></span></span><span style="color:#333333">=</span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"option"</span></span></span><span style="color:#333333"> </span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">:value.sync</span></span></span><span style="color:#333333">=</span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"value"</span></span></span><span style="color:#333333">></span></span><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">form-create</span></span></span><span style="color:#333333">></span></span>
  <span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">div</span></span></span><span style="color:#333333">></span></span>
<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">template</span></span></span><span style="color:#333333">></span></span></code></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">export</span></span> <span style="color:#d73a49"><span style="color:#d73a49">default</span></span> &#123;
    <span style="color:#d73a49"><span style="color:#d73a49">data</span></span>() &#123;
        <span style="color:#d73a49"><span style="color:#d73a49">return</span></span> &#123;
            <span style="color:#6a737d"><span style="color:#6a737d">//实例对象</span></span>
            <span style="color:#005cc5"><span style="color:#005cc5">fApi</span></span>: &#123;&#125;,
            <span style="color:#6a737d"><span style="color:#6a737d">//表单数据</span></span>
            <span style="color:#005cc5"><span style="color:#005cc5">value</span></span>: &#123;&#125;,
            <span style="color:#6a737d"><span style="color:#6a737d">//表单生成规则</span></span>
            <span style="color:#005cc5"><span style="color:#005cc5">rule</span></span>: [
                &#123;
                    <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>: <span style="color:#032f62"><span style="color:#032f62">'input'</span></span>,
                    <span style="color:#005cc5"><span style="color:#005cc5">field</span></span>: <span style="color:#032f62"><span style="color:#032f62">'goods_name'</span></span>,
                    <span style="color:#005cc5"><span style="color:#005cc5">title</span></span>: <span style="color:#032f62"><span style="color:#032f62">'商品名称'</span></span>
                &#125;,
                &#123;
                    <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>: <span style="color:#032f62"><span style="color:#032f62">'datePicker'</span></span>,
                    <span style="color:#005cc5"><span style="color:#005cc5">field</span></span>: <span style="color:#032f62"><span style="color:#032f62">'created_at'</span></span>,
                    <span style="color:#005cc5"><span style="color:#005cc5">title</span></span>: <span style="color:#032f62"><span style="color:#032f62">'创建时间'</span></span>
                &#125;
            ],
            <span style="color:#6a737d"><span style="color:#6a737d">//组件参数配置</span></span>
            <span style="color:#005cc5"><span style="color:#005cc5">option</span></span>: &#123;
                <span style="color:#6a737d"><span style="color:#6a737d">//表单提交事件</span></span>
                <span style="color:#005cc5"><span style="color:#005cc5">onSubmit</span></span>: function (formData) &#123;
                    alert(JSON.stringify(formData))
                &#125;
            &#125;
        &#125;
    &#125;
&#125;
</code></pre> 
<div style="text-align:left"> 
 <h2 style="margin-left:0; margin-right:0">规则介绍</h2> 
 <p style="margin-left:0; margin-right:0"><img alt="https://oscimg.oschina.net/oscnet/up-621b6c6bd380a2a7abc9e8dcded63f44c13.png" src="https://oscimg.oschina.net/oscnet/up-621b6c6bd380a2a7abc9e8dcded63f44c13.png" referrerpolicy="no-referrer"></p> 
 <h3 style="margin-left:0; margin-right:0"><strong>type</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>类型</strong>: <code>String</code></li> 
  <li><strong>说明</strong>: 设置生成组件的名称</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>field</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>类型</strong>: <code>String</code></li> 
  <li><strong>说明</strong>: 设置<strong>表单组件</strong>的字段名称,<strong>自定义组件可以不配置</strong></li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>title</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>类型</strong>: <code>String|Object</code></li> 
  <li><strong>说明</strong>: 组件的名称</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>value</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>类型</strong>: <code>any</code></li> 
  <li><strong>说明</strong>: 表单组件的字段值,自定义组件可以不用设置</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>props</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>参数</strong>: <code>Object</code></li> 
  <li><strong>说明</strong>: 设置组件的<code>props</code></li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>info</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>类型</strong>: <code>String|Object</code></li> 
  <li><strong>说明</strong>: 设置组件的提示信息</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>hidden</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>类型</strong>: <code>Bool</code></li> 
  <li><strong>说明</strong>: 设置组件是否渲染</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>prefix</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>类型</strong>: <code>string|Object</code></li> 
  <li><strong>说明</strong>: 设置组件的前缀</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>suffix</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>​<strong>类型</strong>: <code>string|Object</code></li> 
  <li><strong>说明</strong>: 设置组件的后缀</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>validate</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><strong>类型</strong>: <code>Array</code></li> 
  <li><strong>说明</strong>: 设置表单组件的验证规则</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>options</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><strong>类型</strong>: <code>Array</code></li> 
  <li><strong>说明</strong>: 设置<code>radio</code>,<code>select</code>,<code>checkbox</code>等组件<code>option</code>选择项</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>col</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><strong>类型</strong>: <code>Object</code></li> 
  <li><strong>说明</strong>: 设置组件的布局规则</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>control</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><strong>类型</strong>: <code>Object</code></li> 
  <li><strong>说明</strong>: 控制其他组件显示</li> 
 </ul> 
 <h3 style="margin-left:0; margin-right:0"><strong>children</strong></h3> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li> <p style="margin-left:0; margin-right:0"><strong>类型</strong>: <code>Array<rule|string|maker></code></p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>说明</strong>: 设置父级组件的插槽,默认为<code>default</code>.可配合 <code>slot</code> 配置项使用</p> 
   <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
    <li>示例1</li> 
   </ul> <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">formCreate</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.maker</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.create</span></span>(<span style="color:#032f62"><span style="color:#032f62">'button'</span></span>)<span style="color:#6f42c1"><span style="color:#6f42c1">.children</span></span>([
   <span style="color:#032f62"><span style="color:#032f62">'按钮内容'</span></span> 
])</code></pre> 
   <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
    <li>示例2</li> 
   </ul> <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">maker</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.input</span></span>(<span style="color:#032f62"><span style="color:#032f62">'text'</span></span>,<span style="color:#032f62"><span style="color:#032f62">'text'</span></span>,<span style="color:#032f62"><span style="color:#032f62">'text'</span></span>)<span style="color:#6f42c1"><span style="color:#6f42c1">.children</span></span>([
    maker.create(<span style="color:#032f62"><span style="color:#032f62">'span'</span></span>).children([<span style="color:#032f62"><span style="color:#032f62">'append'</span></span>]).slot(<span style="color:#032f62"><span style="color:#032f62">'append'</span></span>)
])</code></pre> 
   <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
    <li>示例3</li> 
   </ul> <pre style="margin-left:0; margin-right:0"><code class="language-js">formCreate.maker.create(<span style="color:#032f62"><span style="color:#032f62">'i-row'</span></span>).children([
  formCreate.maker.create(<span style="color:#032f62"><span style="color:#032f62">'i-col'</span></span>).props(<span style="color:#032f62"><span style="color:#032f62">'span'</span></span>,<span>12</span>).children([
    formCreate.maker.template(<span style="color:#032f62"><span style="color:#032f62">'<span>自定义组件</span>'</span></span>,<span><span>()</span> =></span> <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> Vue)
  ]),
])</code></pre> </li> 
 </ul> 
 <div> 
  <h2 style="margin-left:0; margin-right:0">功能介绍</h2> 
  <h3 style="margin-left:0; margin-right:0">1. 自定义组件</h3> 
  <p style="margin-left:0; margin-right:0"><strong>form-create 支持的在表单内部生成任何 vue 组件</strong></p> 
  <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fcustom-component.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
  <p style="margin-left:0; margin-right:0">例如生成一个<code>el-button</code>组件:</p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-js">&#123;
<span style="color:#6a737d"><span style="color:#6a737d">//type 可以是内置组件名称,也可以是vue组件名称或者 html 标签</span></span>
<span style="color:#005cc5"><span style="color:#005cc5">type</span></span>: <span style="color:#032f62"><span style="color:#032f62">'el-button'</span></span>,
   <span style="color:#6a737d"><span style="color:#6a737d">//...</span></span>
<span style="color:#005cc5"><span style="color:#005cc5">children</span></span>: [<span style="color:#032f62"><span style="color:#032f62">'按钮内容'</span></span>]
&#125;</code></pre> 
  <p style="margin-left:0; margin-right:0">生成一个 html 标签</p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-js">&#123;
<span style="color:#6a737d"><span style="color:#6a737d">//type 可以是内置组件名称,也可以是vue组件名称或者 html 标签</span></span>
<span style="color:#005cc5"><span style="color:#005cc5">type</span></span>: <span style="color:#032f62"><span style="color:#032f62">'span'</span></span>,
   <span style="color:#6a737d"><span style="color:#6a737d">//...</span></span>
<span style="color:#005cc5"><span style="color:#005cc5">children</span></span>: [<span style="color:#032f62"><span style="color:#032f62">'span内容'</span></span>]
&#125;</code></pre> 
  <p style="margin-left:0; margin-right:0"><strong>注意! 生成的组件必须挂载到全局或者通过 form-create 挂载</strong></p> 
  <p style="margin-left:0; margin-right:0">通过 Vue 挂载</p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">Vue</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.component</span></span>(<span style="color:#d73a49"><span style="color:#d73a49">component</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.name</span></span>, <span style="color:#d73a49"><span style="color:#d73a49">component</span></span>);</code></pre> 
  <p style="margin-left:0; margin-right:0">通过 form-create 挂载</p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">formCreate</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.component</span></span>(<span style="color:#d73a49"><span style="color:#d73a49">component</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.name</span></span>, <span style="color:#d73a49"><span style="color:#d73a49">component</span></span>);</code></pre> 
  <h3 style="margin-left:0; margin-right:0">2. 自定义布局</h3> 
  <p style="margin-left:0; margin-right:0"><strong>通过设置配置项<code>col</code>或者栅格组件可以实现对组件的布局</strong></p> 
  <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Flayout.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
  <p style="margin-left:0; margin-right:0">通过配置项<code>col</code>设置组件布局,设置一行显示两个组件</p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#6f42c1"><span style="color:#6f42c1">[</span></span>
<span style="color:#6f42c1"><span style="color:#6f42c1">&#123;</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input',</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input1',</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input1',</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">col</span></span>:<span style="color:#032f62"><span style="color:#032f62">&#123;span:12&#125;</span></span>
<span style="color:#6f42c1"><span style="color:#6f42c1">&#125;,&#123;</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input',</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input2',</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input2',</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">col</span></span>:<span style="color:#032f62"><span style="color:#032f62">&#123;span:12&#125;</span></span>
<span style="color:#6f42c1"><span style="color:#6f42c1">&#125;,</span></span>
<span style="color:#6f42c1"><span style="color:#6f42c1">]</span></span></code></pre> 
  <p style="margin-left:0; margin-right:0">通过栅格组件设置一行显示三个组件</p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-js">&#123;
<span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'el-row'</span></span>,
   <span style="color:#005cc5"><span style="color:#005cc5">children</span></span>: [
    &#123;
        <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'el-col'</span></span>,
        <span style="color:#005cc5"><span style="color:#005cc5">props</span></span>:&#123;
            <span style="color:#005cc5"><span style="color:#005cc5">span</span></span>:<span>8</span>
        &#125;,
        <span style="color:#005cc5"><span style="color:#005cc5">children</span></span>: [&#123;<span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input'</span></span>,<span style="color:#005cc5"><span style="color:#005cc5">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input1'</span></span>,<span style="color:#005cc5"><span style="color:#005cc5">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input1'</span></span>&#125;]
        &#125;,
    &#123;
        <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'el-col'</span></span>,
        <span style="color:#005cc5"><span style="color:#005cc5">props</span></span>:&#123;
            <span style="color:#005cc5"><span style="color:#005cc5">span</span></span>:<span>8</span>
        &#125;,
        <span style="color:#005cc5"><span style="color:#005cc5">children</span></span>: [&#123;<span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input'</span></span>,<span style="color:#005cc5"><span style="color:#005cc5">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input1'</span></span>,<span style="color:#005cc5"><span style="color:#005cc5">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input1'</span></span>&#125;]
        &#125;,
    &#123;
        <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'el-col'</span></span>,
        <span style="color:#005cc5"><span style="color:#005cc5">props</span></span>:&#123;
            <span style="color:#005cc5"><span style="color:#005cc5">span</span></span>:<span>8</span>
        &#125;,
        <span style="color:#005cc5"><span style="color:#005cc5">children</span></span>: [&#123;<span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input'</span></span>,<span style="color:#005cc5"><span style="color:#005cc5">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input1'</span></span>,<span style="color:#005cc5"><span style="color:#005cc5">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input1'</span></span>&#125;]
        &#125;
    ]
&#125;</code></pre> 
  <h3 style="margin-left:0; margin-right:0">3. 组件前后缀</h3> 
  <p style="margin-left:0; margin-right:0"><strong>通过生成规则的prefix属性配置组件的前缀,suffix属性配置组件的后缀</strong></p> 
  <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fside.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-js">&#123;
    <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input'</span></span>,
    <span style="color:#005cc5"><span style="color:#005cc5">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">'text'</span></span>,
    <span style="color:#005cc5"><span style="color:#005cc5">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'text'</span></span>,
    <span style="color:#005cc5"><span style="color:#005cc5">prefix</span></span>:<span style="color:#032f62"><span style="color:#032f62">'prefix'</span></span>,
    <span style="color:#005cc5"><span style="color:#005cc5">suffix</span></span>:<span style="color:#032f62"><span style="color:#032f62">'suffix'</span></span>,
&#125;</code></pre> 
  <p style="margin-left:0; margin-right:0">设置前后缀为自定义组件</p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-js">&#123;
    <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input'</span></span>,
    <span style="color:#005cc5"><span style="color:#005cc5">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">'text'</span></span>,
    <span style="color:#005cc5"><span style="color:#005cc5">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'text'</span></span>,
    <span style="color:#005cc5"><span style="color:#005cc5">value</span></span>:<span style="color:#032f62"><span style="color:#032f62">'default'</span></span>,
    <span style="color:#005cc5"><span style="color:#005cc5">prefix</span></span>:&#123;
        <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'ElButton'</span></span>, <span style="color:#005cc5"><span style="color:#005cc5">children</span></span>:[<span style="color:#032f62"><span style="color:#032f62">'prefix'</span></span>]
    &#125;,
    <span style="color:#005cc5"><span style="color:#005cc5">suffix</span></span>:&#123;
        <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'ElButton'</span></span>, <span style="color:#005cc5"><span style="color:#005cc5">children</span></span>:[<span style="color:#032f62"><span style="color:#032f62">'suffix'</span></span>]
    &#125;,
&#125;</code></pre> 
  <div> 
   <div> 
    <h3 style="margin-left:0; margin-right:0">4.组件联动</h3> 
    <p style="margin-left:0; margin-right:0"><strong>可以通过control配置项实现通过组件的值控制其他组件是否显示</strong></p> 
    <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fcontrol.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
    <p style="margin-left:0; margin-right:0">例如当评价小于3星时输入差评原因</p> 
    <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#6f42c1"><span style="color:#6f42c1">&#123;</span></span>
    <span style="color:#6f42c1"><span style="color:#6f42c1">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'rate',</span></span>
    <span style="color:#6f42c1"><span style="color:#6f42c1">field</span></span>: <span style="color:#032f62"><span style="color:#032f62">'star',</span></span>
    <span style="color:#6f42c1"><span style="color:#6f42c1">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'评分',</span></span>
    <span style="color:#6f42c1"><span style="color:#6f42c1">value</span></span>:<span style="color:#032f62"><span style="color:#032f62">5,</span></span>
    <span style="color:#6f42c1"><span style="color:#6f42c1">control</span></span>:<span style="color:#032f62"><span style="color:#032f62">[</span></span>
        <span style="color:#6f42c1"><span style="color:#6f42c1">&#123;</span></span>
            <span style="color:#6f42c1"><span style="color:#6f42c1">handle(val)&#123;</span></span>
                <span style="color:#6f42c1"><span style="color:#6f42c1">return</span></span> <span style="color:#032f62"><span style="color:#032f62">val < 3</span></span>
            <span style="color:#6f42c1"><span style="color:#6f42c1">&#125;,</span></span>
            <span style="color:#6f42c1"><span style="color:#6f42c1">rule</span></span>:<span style="color:#032f62"><span style="color:#032f62">[</span></span>
                <span style="color:#6f42c1"><span style="color:#6f42c1">&#123;</span></span>
                    <span style="color:#6f42c1"><span style="color:#6f42c1">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input',</span></span>
                    <span style="color:#6f42c1"><span style="color:#6f42c1">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">'info',</span></span>
                    <span style="color:#6f42c1"><span style="color:#6f42c1">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">'差评原因',</span></span>
                    <span style="color:#6f42c1"><span style="color:#6f42c1">value</span></span>:<span style="color:#032f62"><span style="color:#032f62">'default info', </span></span>
                <span style="color:#6a737d"><span style="color:#6a737d">&#125;</span></span> 
            <span style="color:#6a737d"><span style="color:#6a737d">]</span></span>   
        <span style="color:#6a737d"><span style="color:#6a737d">&#125;</span></span>                                              
    <span style="color:#6f42c1"><span style="color:#6f42c1">]</span></span>
<span style="color:#6f42c1"><span style="color:#6f42c1">&#125;</span></span></code></pre> 
    <table cellspacing="0" style="border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-size:14px; line-height:inherit; margin:0px 0px 20px; max-width:100%; overflow:auto; width:776px; word-break:keep-all"> 
     <thead> 
      <tr> 
       <th>参数</th> 
       <th>说明</th> 
       <th>类型</th> 
      </tr> 
     </thead> 
     <tbody> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">value</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">当组件的值和<code>value</code>全等时显示<code>rule</code>中的组件</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">string|Number|Bool</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">handle</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">当<code>handle</code>方法返回<code>true</code>时显示<code>rule</code>中的组件</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">Function</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">rule</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">该组件控制显示的组件</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">Array</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">append</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">设置<code>rule</code>中的规则追加的位置</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">string</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">prepend</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">设置<code>rule</code>中的规则前置插入的位置</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">string</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">child</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">设置<code>rule</code>是否插入到指定位置的children中,默认添加到当前规则的 children 中</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">Boolean</td> 
      </tr> 
     </tbody> 
    </table> 
    <p style="margin-left:0; margin-right:0"><strong>注意! <code>handle</code>优先级大于<code>value</code>,所有符合条件的<code>control</code>都会生效</strong></p> 
    <h3 style="margin-left:0; margin-right:0">5. 表单验证</h3> 
    <p style="margin-left:0; margin-right:0"><strong>可以通过 validate 配置项设置组件的验证规则,自定义的表单组件也支持校验</strong></p> 
    <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fother%2Fvalidation-rules.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
    <p style="margin-left:0; margin-right:0">例如设置input 组件必填</p> 
    <pre style="margin-left:0; margin-right:0"><code class="language-js">&#123;
<span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input'</span></span>,
<span style="color:#6a737d"><span style="color:#6a737d">//...</span></span>
<span style="color:#005cc5"><span style="color:#005cc5">validate</span></span>:[&#123;<span style="color:#005cc5"><span style="color:#005cc5">required</span></span>:true, <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'string'</span></span>, <span style="color:#005cc5"><span style="color:#005cc5">message</span></span>:<span style="color:#032f62"><span style="color:#032f62">'请个输入内容'</span></span>&#125;]
&#125;</code></pre> 
    <table cellspacing="0" style="border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-size:14px; line-height:inherit; margin:0px 0px 20px; max-width:100%; overflow:auto; width:776px; word-break:keep-all"> 
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
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">enum</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">枚举类型</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">string</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">len</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">字段长度</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">number</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">max</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">最大长度</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">number</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">message</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">校验文案</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">string</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">min</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">最小长度</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">number</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">pattern</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">正则表达式校验</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">RegExp</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">required</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">是否必选</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">boolean</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>false</code></td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">transform</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">校验前转换字段值</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">function(value) => transformedValue:any</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">type</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">内建校验类型，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyiminghe%2Fasync-validator%23type" target="_blank">可选项</a></td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">string</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">'string'</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">validator</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">自定义校验</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">function(rule, value, callback)</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">whitespace</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">必选时，空格是否会被视为错误</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px">boolean</td> 
       <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>false</code></td> 
      </tr> 
     </tbody> 
    </table> 
    <p style="margin-left:0; margin-right:0">注意!<code>type</code>需要根据组件的<code>value</code>类型定</p> 
    <div> 
     <h2 style="margin-left:0; margin-right:0">APi 介绍</h2> 
     <p style="margin-left:0; margin-right:0"><strong>下列是常用的方法</strong></p> 
     <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Finstance.html%3Ffrom%3Dosn" target="_blank">完整的Api介绍</a></p> 
     <h3 style="margin-left:0; margin-right:0">设置表单值</h3> 
     <p style="margin-left:0; margin-right:0">覆盖方式,未定义的字段会设置为 <code>null</code></p> 
     <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">type</span></span> coverValue = <span>(<span>formData:&#123;[field:<span>string</span>]:<span>any</span>&#125;</span>) =></span> <span>void</span></code></pre> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>用法：</li> 
     </ul> 
     <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">fApi</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.coverValue</span></span>(&#123;<span style="color:#005cc5"><span style="color:#005cc5">goods_name</span></span>:<span style="color:#032f62"><span style="color:#032f62">'HuaWei'</span></span>&#125;)</code></pre> 
     <p style="margin-left:0; margin-right:0">合并方式,未定义的字段不做修改</p> 
     <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">interface</span></span> setValue &#123;
    (formData:&#123;[field:<span>string</span>]:<span>any</span>&#125;): <span>void</span>
    (field:<span>string</span>, value:<span>any</span>): <span>void</span>
&#125;</code></pre> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>用法：</li> 
     </ul> 
     <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">fApi</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.setValue</span></span>(&#123;<span style="color:#005cc5"><span style="color:#005cc5">goods_name</span></span>:<span style="color:#032f62"><span style="color:#032f62">'HuaWei'</span></span>&#125;)</code></pre> 
     <p style="margin-left:0; margin-right:0">别名方法<code>changeValue</code>, <code>changeField</code></p> 
     <h3 style="margin-left:0; margin-right:0">隐藏字段</h3> 
     <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">interface</span></span> hidden &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">//隐藏全部组件</span></span>
    (status:<span>Boolean</span>):<span>void</span>
    <span style="color:#6a737d"><span style="color:#6a737d">//隐藏指定组件</span></span>
    (status:<span>Boolean</span>, field:<span>string</span>):<span>void</span>
    <span style="color:#6a737d"><span style="color:#6a737d">//隐藏部分组件</span></span>
    (status:<span>Boolean</span>, field:<span>string</span>[]):<span>void</span> 
&#125;</code></pre> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>用法：</li> 
     </ul> 
     <pre style="margin-left:0; margin-right:0"><code class="language-js">fApi.hidden(<span style="color:#005cc5"><span style="color:#005cc5">true</span></span>, <span style="color:#005cc5"><span style="color:#005cc5">'goods_name</span></span>')</code></pre> 
     <p style="margin-left:0; margin-right:0"><strong>获取组件隐藏状态</strong></p> 
     <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">type</span></span> hiddenStatus = <span>(<span>field:<span>string</span></span>)=></span><span>Boolean</span></code></pre> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>用法：</li> 
     </ul> 
     <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">const</span></span> status = fApi.hiddenStatus(<span style="color:#005cc5"><span style="color:#005cc5">'goods_name</span></span>')</code></pre> 
     <h3 style="margin-left:0; margin-right:0">获取规则</h3> 
     <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">interface</span></span> getRule &#123;
    (field:<span>string</span>):Rule
    (field:<span>string</span>, origin: <span style="color:#005cc5"><span style="color:#005cc5">true</span></span>): FormRule
&#125;</code></pre> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>用法：</li> 
     </ul> 
     <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">const</span></span> rule = fApi.getRule(<span style="color:#005cc5"><span style="color:#005cc5">'goods_name</span></span>')</code></pre> 
     <h3 style="margin-left:0; margin-right:0">插入规则</h3> 
     <p style="margin-left:0; margin-right:0"><strong>前置插入</strong></p> 
     <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">interface</span></span> prepend &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">//插入到第一个</span></span>
    (rule:FormRule):<span>void</span> 
    <span style="color:#6a737d"><span style="color:#6a737d">//插入指定字段前面</span></span>
    (rule:FormRule, field:<span>string</span>):<span>void</span>
    <span style="color:#6a737d"><span style="color:#6a737d">//插入到指定字段 children 中</span></span>
    (rule:FormRule, field:<span>string</span>, child:<span style="color:#005cc5"><span style="color:#005cc5">true</span></span>):<span>void</span>
&#125;</code></pre> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>用法：</li> 
     </ul> 
     <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">fApi</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.prepend</span></span>(&#123;
     <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">"input"</span></span>,
     <span style="color:#005cc5"><span style="color:#005cc5">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">"商品简介"</span></span>,
     <span style="color:#005cc5"><span style="color:#005cc5">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">"goods_info"</span></span>,
     <span style="color:#005cc5"><span style="color:#005cc5">value</span></span>:<span style="color:#032f62"><span style="color:#032f62">""</span></span>,
     <span style="color:#005cc5"><span style="color:#005cc5">props</span></span>: &#123;
         <span style="color:#032f62"><span style="color:#032f62">"type"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"text"</span></span>,
         <span style="color:#032f62"><span style="color:#032f62">"placeholder"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"请输入商品简介"</span></span>,
     &#125;,
     <span style="color:#005cc5"><span style="color:#005cc5">validate</span></span>:[
         &#123; <span style="color:#005cc5"><span style="color:#005cc5">required</span></span>: true, <span style="color:#005cc5"><span style="color:#005cc5">message</span></span>: <span style="color:#032f62"><span style="color:#032f62">'请输入商品简介'</span></span>, <span style="color:#005cc5"><span style="color:#005cc5">trigger</span></span>: <span style="color:#032f62"><span style="color:#032f62">'blur'</span></span> &#125;,
     ],
&#125;, <span style="color:#032f62"><span style="color:#032f62">'goods-name'</span></span>)</code></pre> 
     <p style="margin-left:0; margin-right:0"><strong>后置追加</strong></p> 
     <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">interface</span></span> append &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">//插入到最后一个</span></span>
    (rule:FormRule):<span>void</span> 
    <span style="color:#6a737d"><span style="color:#6a737d">//插入指定字段后面</span></span>
    (rule:FormRule, field:<span>string</span>):<span>void</span>
    <span style="color:#6a737d"><span style="color:#6a737d">//插入到指定字段 children 中</span></span>
    (rule:FormRule, field:<span>string</span>, child:<span style="color:#005cc5"><span style="color:#005cc5">true</span></span>):<span>void</span>
&#125;</code></pre> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>用法：</li> 
     </ul> 
     <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">fApi</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.append</span></span>(&#123;
     <span style="color:#005cc5"><span style="color:#005cc5">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">"input"</span></span>,
     <span style="color:#005cc5"><span style="color:#005cc5">title</span></span>:<span style="color:#032f62"><span style="color:#032f62">"商品简介"</span></span>,
     <span style="color:#005cc5"><span style="color:#005cc5">field</span></span>:<span style="color:#032f62"><span style="color:#032f62">"goods_info"</span></span>,
     <span style="color:#005cc5"><span style="color:#005cc5">value</span></span>:<span style="color:#032f62"><span style="color:#032f62">""</span></span>,
     <span style="color:#005cc5"><span style="color:#005cc5">props</span></span>: &#123;
         <span style="color:#032f62"><span style="color:#032f62">"type"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"text"</span></span>,
         <span style="color:#032f62"><span style="color:#032f62">"placeholder"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"请输入商品简介"</span></span>,
     &#125;,
     <span style="color:#005cc5"><span style="color:#005cc5">validate</span></span>:[
         &#123; <span style="color:#005cc5"><span style="color:#005cc5">required</span></span>: true, <span style="color:#005cc5"><span style="color:#005cc5">message</span></span>: <span style="color:#032f62"><span style="color:#032f62">'请输入商品简介'</span></span>, <span style="color:#005cc5"><span style="color:#005cc5">trigger</span></span>: <span style="color:#032f62"><span style="color:#032f62">'blur'</span></span> &#125;,
     ],
&#125;, <span style="color:#032f62"><span style="color:#032f62">'goods-name'</span></span>)</code></pre> 
     <div> 
      <div> 
       <h3 style="margin-left:0; margin-right:0">删除指定规则</h3> 
       <pre style="margin-left:0; margin-right:0"><code class="language-typescript">type removeRule = <span><span>(rule:FormRule)</span> =></span> FormRule</code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li>用法：</li> 
       </ul> 
       <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">const</span></span> rule = &#123;<span style="color:#d73a49"><span style="color:#d73a49">type</span></span>:<span style="color:#032f62"><span style="color:#032f62">'input'</span></span>, <span style="color:#6a737d"><span style="color:#6a737d">/** ... **/</span></span>&#125;
fApi.removeRule(rule)</code></pre> 
       <h3 style="margin-left:0; margin-right:0">验证表单</h3> 
       <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">type</span></span> validate = <span>(<span>callback:(<span>...args:<span>any</span>[]</span>) => <span>void</span></span>)=></span> <span>void</span></code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li>用法：</li> 
       </ul> 
       <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">fApi</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.validate</span></span>((valid, fail) => &#123;
    <span style="color:#d73a49"><span style="color:#d73a49">if</span></span>(valid)&#123;
        <span style="color:#6a737d"><span style="color:#6a737d">//todo 表单验证通过</span></span>
    &#125;else&#123;
        <span style="color:#6a737d"><span style="color:#6a737d">//todo 表单验证未通过</span></span>
    &#125;
&#125;)</code></pre> 
       <h3 style="margin-left:0; margin-right:0">验证指定字段</h3> 
       <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">type</span></span> validateField = <span>(<span>field, callback:(<span>...args:<span>any</span>[]</span>) => <span>void</span></span>)=></span> <span>void</span></code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li>用法：</li> 
       </ul> 
       <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">fApi</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.validateField</span></span>(<span style="color:#032f62"><span style="color:#032f62">'goods_name'</span></span>, (valid, fail) => &#123;
    <span style="color:#d73a49"><span style="color:#d73a49">if</span></span>(valid)&#123;
        <span style="color:#6a737d"><span style="color:#6a737d">//todo 字段验证通过</span></span>
    &#125;else&#123;
        <span style="color:#6a737d"><span style="color:#6a737d">//todo 字段验证未通过</span></span>
    &#125;
&#125;)</code></pre> 
       <h3 style="margin-left:0; margin-right:0">获取表单数据</h3> 
       <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">interface</span></span> formData &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">//获取全部数据</span></span>
    (): &#123;[field:<span>string</span>]:<span>any</span> &#125;
    <span style="color:#6a737d"><span style="color:#6a737d">//获取部分字段的数据</span></span>
    (field:<span>string</span>[]): &#123;[field:<span>string</span>]:<span>any</span> &#125;
&#125;</code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li>用法：</li> 
       </ul> 
       <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#6f42c1"><span style="color:#6f42c1">const</span></span> <span style="color:#032f62"><span style="color:#032f62">formData = fApi.formData()</span></span></code></pre> 
       <h3 style="margin-left:0; margin-right:0">修改提交按钮</h3> 
       <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">type</span></span> submitBtnProps = <span>(<span>props:<span>Object</span></span>) =></span> <span>void</span></code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li>用法：</li> 
       </ul> 
       <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">fApi</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.submitBtnProps</span></span>(&#123;<span style="color:#005cc5"><span style="color:#005cc5">disabled</span></span>:true&#125;)</code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li> <p style="margin-left:0; margin-right:0">快捷操作:</p> 
         <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
          <li><code>fApi.btn.loading(true)</code> 设置提交按钮进入loading状态</li> 
          <li><code>fApi.btn.disabled(true)</code> 设置提交按钮禁用状态</li> 
          <li><code>fApi.btn.show(true)</code> 设置提交按钮显示状态</li> 
         </ul> </li> 
       </ul> 
       <h3 style="margin-left:0; margin-right:0">修改重置按钮</h3> 
       <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">type</span></span> resetBtnProps = <span>(<span> props:<span>Object</span></span>) =></span> <span>void</span></code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li>用法：</li> 
       </ul> 
       <pre style="margin-left:0; margin-right:0"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49">fApi</span></span><span style="color:#6f42c1"><span style="color:#6f42c1">.resetBtnProps</span></span>(&#123;<span style="color:#005cc5"><span style="color:#005cc5">disabled</span></span>:true&#125;)</code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li> <p style="margin-left:0; margin-right:0">快捷操作:</p> 
         <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
          <li><code>fApi.resetBtn.loading(true)</code> 设置重置按钮进入loading状态</li> 
          <li><code>fApi.resetBtn.disabled(true)</code> 设置重置按钮禁用状态</li> 
          <li><code>fApi.resetBtn.show(true)</code> 设置重置按钮显示状态</li> 
         </ul> </li> 
       </ul> 
       <h3 style="margin-left:0; margin-right:0">隐藏表单</h3> 
       <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">type</span></span> hideForm = <span>(<span>hide:<span>Boolean</span></span>)=></span><span>void</span></code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li>用法：</li> 
       </ul> 
       <pre style="margin-left:0; margin-right:0"><code class="language-js">fApi.hideForm(<span style="color:#005cc5"><span style="color:#005cc5">true</span></span>)</code></pre> 
       <h3 style="margin-left:0; margin-right:0">提交表单</h3> 
       <pre style="margin-left:0; margin-right:0"><code class="language-typescript"><span style="color:#d73a49"><span style="color:#d73a49">type</span></span> submit = <span>(<span>success: (<span>formData: FormData, $f: fApi</span>) => <span>void</span>, fail: (<span>$f: fApi</span>) => <span>void</span></span>)=></span> <span>void</span>
</code></pre> 
       <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
        <li>用法：</li> 
       </ul> 
       <pre style="margin-left:0; margin-right:0"><code class="language-js">fApi.submit(<span><span>(formData, fapi)</span> =></span> &#123;
    <span>//</span>todo 提交表单
&#125;,<span><span>()</span>=></span>&#123;
    <span>//</span>todo 表单验证未通过
&#125;</code></pre> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            