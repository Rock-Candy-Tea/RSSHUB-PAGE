
---
title: form-create 2.5.1 发布，强大的动态表单组件
categories: 
    - 编程
    - 开源中国 - 资讯
author: 开源中国 - 资讯
comments: false
date: Fri, 19 Mar 2021 16:41:00 GMT
thumbnail: https://oscimg.oschina.net/oscnet/up-621b6c6bd380a2a7abc9e8dcded63f44c13.png
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">form-create 是一个可以通过 JSON 生成具有动态渲染、数据收集、验证和提交功能的表单生成组件。支持3个UI框架，并且支持生成任何 Vue 组件。内置20种常用表单组件和自定义组件，再复杂的表单都可以轻松搞定。</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2F%3Ffrom%3Dosn" target="_blank">文档</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxaboy%2Fform-create" target="_blank">GitHub</a> | <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fdemo.html%3Ffrom%3Dosn" target="_blank">示例</a></p> 
<h2 style="text-align:left">支持 UI</h2> 
<ul> 
 <li>element-ui</li> 
 <li>iview/view-design</li> 
 <li>ant-design-vue</li> 
</ul> 
<p style="text-align:left"><strong>2.5.1主要更新了一下内容:</strong></p> 
<ul> 
 <li style="text-align:left">新增 parent 和 children 属性</li> 
 <li style="text-align:left"><strong>新增 sync 配置项, 支持 props 同步</strong></li> 
 <li style="text-align:left">修复 page 失效问题</li> 
 <li style="text-align:left">修复 control 可能报错问题</li> 
 <li style="text-align:left">修复 全局配置 col 无效问题</li> 
 <li style="text-align:left">优化 内置组件插槽配置</li> 
 <li style="text-align:left">优化 frame, group, sub-form, select 组件功能优化</li> 
 <li style="text-align:left"><strong>优化 value 同步机制</strong></li> 
 <li style="text-align:left">优化 reload 机制</li> 
 <li style="text-align:left">优化 validate, validateField 方法</li> 
 <li style="text-align:left">优化 表单销毁机制</li> 
 <li style="text-align:left">优化 参数注入</li> 
 <li style="text-align:left">优化 typescript</li> 
</ul> 
<p style="text-align:left"> </p> 
<h2 style="text-align:left">安装</h2> 
<blockquote> 
 <p>根据自己使用的 UI 安装对应的版本</p> 
</blockquote> 
<p style="text-align:left"><code>element-ui</code> 版本</p> 
<pre style="text-align:left"><code class="language-sh"><span style="color:#d73a49">npm</span> <span style="color:#d73a49">i</span> @<span style="color:#d73a49">form</span>-<span style="color:#d73a49">create</span>/<span style="color:#d73a49">element</span>-<span style="color:#d73a49">ui</span></code></pre> 
<p style="text-align:left"><code>iview@2.x|3.x</code> 版本</p> 
<pre style="text-align:left"><code class="language-sh"><span style="color:#d73a49">npm</span> <span style="color:#d73a49">i</span> @<span style="color:#d73a49">form</span>-<span style="color:#d73a49">create</span>/<span style="color:#d73a49">iview</span></code></pre> 
<p style="text-align:left"><code>iview/view-design@4.x</code> 版本</p> 
<pre style="text-align:left"><code class="language-sh"><span style="color:#d73a49">npm</span> <span style="color:#d73a49">i</span> @<span style="color:#d73a49">form</span>-<span style="color:#d73a49">create</span>/<span style="color:#d73a49">iview4</span></code></pre> 
<p style="text-align:left"><code>ant-design-vue@1.5+</code> 版本</p> 
<pre style="text-align:left"><code class="language-sh"><span style="color:#d73a49">npm</span> <span style="color:#d73a49">i</span> @<span style="color:#d73a49">form</span>-<span style="color:#d73a49">create</span>/<span style="color:#d73a49">ant</span>-<span style="color:#d73a49">design</span>-<span style="color:#d73a49">vue</span></code></pre> 
<h2 style="text-align:left">快速上手</h2> 
<blockquote> 
 <p>本文以<code>element-ui</code>为例</p> 
</blockquote> 
<ol> 
 <li>在 main.js 中写入以下内容：</li> 
</ol> 
<pre style="text-align:left"><code class="language-js"><span style="color:#d73a49">import</span> Vue <span style="color:#d73a49">from</span> <span style="color:#032f62">'vue'</span>
<span style="color:#d73a49">import</span> ELEMENT <span style="color:#d73a49">from</span> <span style="color:#032f62">'element-ui'</span>
<span style="color:#d73a49">import</span> <span style="color:#032f62">'element-ui/lib/theme-chalk/index.css'</span>

<span style="color:#d73a49">import</span> formCreate <span style="color:#d73a49">from</span> <span style="color:#032f62">'@form-create/element-ui'</span>

Vue.use(ELEMENT)
Vue.use(formCreate)</code></pre> 
<ol> 
 <li>生成表单</li> 
</ol> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fdemo.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
<pre style="text-align:left"><code class="language-html"><span style="color:#333333"><<span style="color:#22863a">template</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">div</span> <span style="color:#6f42c1">id</span>=<span style="color:#032f62">"app1"</span>></span>
      <span style="color:#333333"><<span style="color:#22863a">form-create</span> <span style="color:#6f42c1">v-model</span>=<span style="color:#032f62">"fApi"</span> <span style="color:#6f42c1">:rule</span>=<span style="color:#032f62">"rule"</span> <span style="color:#6f42c1">:option</span>=<span style="color:#032f62">"option"</span> <span style="color:#6f42c1">:value.sync</span>=<span style="color:#032f62">"value"</span>></span><span style="color:#333333"></<span style="color:#22863a">form-create</span>></span>
  <span style="color:#333333"></<span style="color:#22863a">div</span>></span>
<span style="color:#333333"></<span style="color:#22863a">template</span>></span></code></pre> 
<pre style="text-align:left"><code class="language-js"><span style="color:#d73a49">export</span> <span style="color:#d73a49">default</span> {
    <span style="color:#d73a49">data</span>() {
        <span style="color:#d73a49">return</span> {
            <span style="color:#6a737d">//实例对象</span>
            <span style="color:#005cc5">fApi</span>: {},
            <span style="color:#6a737d">//表单数据</span>
            <span style="color:#005cc5">value</span>: {},
            <span style="color:#6a737d">//表单生成规则</span>
            <span style="color:#005cc5">rule</span>: [
                {
                    <span style="color:#005cc5">type</span>: <span style="color:#032f62">'input'</span>,
                    <span style="color:#005cc5">field</span>: <span style="color:#032f62">'goods_name'</span>,
                    <span style="color:#005cc5">title</span>: <span style="color:#032f62">'商品名称'</span>
                },
                {
                    <span style="color:#005cc5">type</span>: <span style="color:#032f62">'datePicker'</span>,
                    <span style="color:#005cc5">field</span>: <span style="color:#032f62">'created_at'</span>,
                    <span style="color:#005cc5">title</span>: <span style="color:#032f62">'创建时间'</span>
                }
            ],
            <span style="color:#6a737d">//组件参数配置</span>
            <span style="color:#005cc5">option</span>: {
                <span style="color:#6a737d">//表单提交事件</span>
                <span style="color:#005cc5">onSubmit</span>: function (formData) {
                    alert(JSON.stringify(formData))
                }
            }
        }
    }
}
</code></pre> 
<div style="text-align:left"> 
 <h2>规则介绍</h2> 
 <p><img alt="https://oscimg.oschina.net/oscnet/up-621b6c6bd380a2a7abc9e8dcded63f44c13.png" src="https://oscimg.oschina.net/oscnet/up-621b6c6bd380a2a7abc9e8dcded63f44c13.png" referrerpolicy="no-referrer"></p> 
 <h3><strong>type</strong></h3> 
 <ul> 
  <li>​<strong>类型</strong>: <code>String</code></li> 
  <li><strong>说明</strong>: 设置生成组件的名称</li> 
 </ul> 
 <h3><strong>field</strong></h3> 
 <ul> 
  <li>​<strong>类型</strong>: <code>String</code></li> 
  <li><strong>说明</strong>: 设置<strong>表单组件</strong>的字段名称,<strong>自定义组件可以不配置</strong></li> 
 </ul> 
 <h3><strong>title</strong></h3> 
 <ul> 
  <li>​<strong>类型</strong>: <code>String|Object</code></li> 
  <li><strong>说明</strong>: 组件的名称</li> 
 </ul> 
 <h3><strong>value</strong></h3> 
 <ul> 
  <li>​<strong>类型</strong>: <code>any</code></li> 
  <li><strong>说明</strong>: 表单组件的字段值,自定义组件可以不用设置</li> 
 </ul> 
 <h3><strong>props</strong></h3> 
 <ul> 
  <li>​<strong>参数</strong>: <code>Object</code></li> 
  <li><strong>说明</strong>: 设置组件的<code>props</code></li> 
 </ul> 
 <h3><strong>info</strong></h3> 
 <ul> 
  <li>​<strong>类型</strong>: <code>String|Object</code></li> 
  <li><strong>说明</strong>: 设置组件的提示信息</li> 
 </ul> 
 <h3><strong>hidden</strong></h3> 
 <ul> 
  <li>​<strong>类型</strong>: <code>Bool</code></li> 
  <li><strong>说明</strong>: 设置组件是否渲染</li> 
 </ul> 
 <h3><strong>prefix</strong></h3> 
 <ul> 
  <li>​<strong>类型</strong>: <code>string|Object</code></li> 
  <li><strong>说明</strong>: 设置组件的前缀</li> 
 </ul> 
 <h3><strong>suffix</strong></h3> 
 <ul> 
  <li>​<strong>类型</strong>: <code>string|Object</code></li> 
  <li><strong>说明</strong>: 设置组件的后缀</li> 
 </ul> 
 <h3><strong>validate</strong></h3> 
 <ul> 
  <li><strong>类型</strong>: <code>Array</code></li> 
  <li><strong>说明</strong>: 设置表单组件的验证规则</li> 
 </ul> 
 <h3><strong>options</strong></h3> 
 <ul> 
  <li><strong>类型</strong>: <code>Array</code></li> 
  <li><strong>说明</strong>: 设置<code>radio</code>,<code>select</code>,<code>checkbox</code>等组件<code>option</code>选择项</li> 
 </ul> 
 <h3><strong>col</strong></h3> 
 <ul> 
  <li><strong>类型</strong>: <code>Object</code></li> 
  <li><strong>说明</strong>: 设置组件的布局规则</li> 
 </ul> 
 <h3><strong>control</strong></h3> 
 <ul> 
  <li><strong>类型</strong>: <code>Object</code></li> 
  <li><strong>说明</strong>: 控制其他组件显示</li> 
 </ul> 
 <h3><strong>children</strong></h3> 
 <ul> 
  <li> <p><strong>类型</strong>: <code>Array<rule|string|maker></code></p> </li> 
  <li> <p><strong>说明</strong>: 设置父级组件的插槽,默认为<code>default</code>.可配合 <code>slot</code> 配置项使用</p> 
   <ul> 
    <li>示例1</li> 
   </ul> <pre><code class="language-js"><span style="color:#d73a49">formCreate</span><span style="color:#6f42c1">.maker</span><span style="color:#6f42c1">.create</span>(<span style="color:#032f62">'button'</span>)<span style="color:#6f42c1">.children</span>([
   <span style="color:#032f62">'按钮内容'</span> 
])</code></pre> 
   <ul> 
    <li>示例2</li> 
   </ul> <pre><code class="language-js"><span style="color:#d73a49">maker</span><span style="color:#6f42c1">.input</span>(<span style="color:#032f62">'text'</span>,<span style="color:#032f62">'text'</span>,<span style="color:#032f62">'text'</span>)<span style="color:#6f42c1">.children</span>([
    maker.create(<span style="color:#032f62">'span'</span>).children([<span style="color:#032f62">'append'</span>]).slot(<span style="color:#032f62">'append'</span>)
])</code></pre> 
   <ul> 
    <li>示例3</li> 
   </ul> <pre><code class="language-js">formCreate.maker.create(<span style="color:#032f62">'i-row'</span>).children([
  formCreate.maker.create(<span style="color:#032f62">'i-col'</span>).props(<span style="color:#032f62">'span'</span>,12).children([
    formCreate.maker.template(<span style="color:#032f62">'<span>自定义组件</span>'</span>,() => <span style="color:#d73a49">new</span> Vue)
  ]),
])</code></pre> </li> 
 </ul> 
 <div> 
  <h2>功能介绍</h2> 
  <h3>1. 自定义组件</h3> 
  <p><strong>form-create 支持的在表单内部生成任何 vue 组件</strong></p> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fcustom-component.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
  <p>例如生成一个<code>el-button</code>组件:</p> 
  <pre><code class="language-js">{
<span style="color:#6a737d">//type 可以是内置组件名称,也可以是vue组件名称或者 html 标签</span>
<span style="color:#005cc5">type</span>: <span style="color:#032f62">'el-button'</span>,
   <span style="color:#6a737d">//...</span>
<span style="color:#005cc5">children</span>: [<span style="color:#032f62">'按钮内容'</span>]
}</code></pre> 
  <p>生成一个 html 标签</p> 
  <pre><code class="language-js">{
<span style="color:#6a737d">//type 可以是内置组件名称,也可以是vue组件名称或者 html 标签</span>
<span style="color:#005cc5">type</span>: <span style="color:#032f62">'span'</span>,
   <span style="color:#6a737d">//...</span>
<span style="color:#005cc5">children</span>: [<span style="color:#032f62">'span内容'</span>]
}</code></pre> 
  <p><strong>注意! 生成的组件必须挂载到全局或者通过 form-create 挂载</strong></p> 
  <p>通过 Vue 挂载</p> 
  <pre><code class="language-js"><span style="color:#d73a49">Vue</span><span style="color:#6f42c1">.component</span>(<span style="color:#d73a49">component</span><span style="color:#6f42c1">.name</span>, <span style="color:#d73a49">component</span>);</code></pre> 
  <p>通过 form-create 挂载</p> 
  <pre><code class="language-js"><span style="color:#d73a49">formCreate</span><span style="color:#6f42c1">.component</span>(<span style="color:#d73a49">component</span><span style="color:#6f42c1">.name</span>, <span style="color:#d73a49">component</span>);</code></pre> 
  <h3>2. 自定义布局</h3> 
  <p><strong>通过设置配置项<code>col</code>或者栅格组件可以实现对组件的布局</strong></p> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Flayout.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
  <p>通过配置项<code>col</code>设置组件布局,设置一行显示两个组件</p> 
  <pre><code class="language-js"><span style="color:#6f42c1">[</span>
<span style="color:#6f42c1">{</span>
        <span style="color:#6f42c1">type</span>:<span style="color:#032f62">'input',</span>
        <span style="color:#6f42c1">field</span>:<span style="color:#032f62">'input1',</span>
        <span style="color:#6f42c1">title</span>:<span style="color:#032f62">'input1',</span>
        <span style="color:#6f42c1">col</span>:<span style="color:#032f62">{span:12}</span>
<span style="color:#6f42c1">},{</span>
        <span style="color:#6f42c1">type</span>:<span style="color:#032f62">'input',</span>
        <span style="color:#6f42c1">field</span>:<span style="color:#032f62">'input2',</span>
        <span style="color:#6f42c1">title</span>:<span style="color:#032f62">'input2',</span>
        <span style="color:#6f42c1">col</span>:<span style="color:#032f62">{span:12}</span>
<span style="color:#6f42c1">},</span>
<span style="color:#6f42c1">]</span></code></pre> 
  <p>通过栅格组件设置一行显示三个组件</p> 
  <pre><code class="language-js">{
<span style="color:#005cc5">type</span>:<span style="color:#032f62">'el-row'</span>,
   <span style="color:#005cc5">children</span>: [
    {
        <span style="color:#005cc5">type</span>:<span style="color:#032f62">'el-col'</span>,
        <span style="color:#005cc5">props</span>:{
            <span style="color:#005cc5">span</span>:8
        },
        <span style="color:#005cc5">children</span>: [{<span style="color:#005cc5">type</span>:<span style="color:#032f62">'input'</span>,<span style="color:#005cc5">field</span>:<span style="color:#032f62">'input1'</span>,<span style="color:#005cc5">title</span>:<span style="color:#032f62">'input1'</span>}]
        },
    {
        <span style="color:#005cc5">type</span>:<span style="color:#032f62">'el-col'</span>,
        <span style="color:#005cc5">props</span>:{
            <span style="color:#005cc5">span</span>:8
        },
        <span style="color:#005cc5">children</span>: [{<span style="color:#005cc5">type</span>:<span style="color:#032f62">'input'</span>,<span style="color:#005cc5">field</span>:<span style="color:#032f62">'input1'</span>,<span style="color:#005cc5">title</span>:<span style="color:#032f62">'input1'</span>}]
        },
    {
        <span style="color:#005cc5">type</span>:<span style="color:#032f62">'el-col'</span>,
        <span style="color:#005cc5">props</span>:{
            <span style="color:#005cc5">span</span>:8
        },
        <span style="color:#005cc5">children</span>: [{<span style="color:#005cc5">type</span>:<span style="color:#032f62">'input'</span>,<span style="color:#005cc5">field</span>:<span style="color:#032f62">'input1'</span>,<span style="color:#005cc5">title</span>:<span style="color:#032f62">'input1'</span>}]
        }
    ]
}</code></pre> 
  <h3>3. 组件前后缀</h3> 
  <p><strong>通过生成规则的prefix属性配置组件的前缀,suffix属性配置组件的后缀</strong></p> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fside.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
  <pre><code class="language-js">{
    <span style="color:#005cc5">type</span>:<span style="color:#032f62">'input'</span>,
    <span style="color:#005cc5">field</span>:<span style="color:#032f62">'text'</span>,
    <span style="color:#005cc5">title</span>:<span style="color:#032f62">'text'</span>,
    <span style="color:#005cc5">prefix</span>:<span style="color:#032f62">'prefix'</span>,
    <span style="color:#005cc5">suffix</span>:<span style="color:#032f62">'suffix'</span>,
}</code></pre> 
  <p>设置前后缀为自定义组件</p> 
  <pre><code class="language-js">{
    <span style="color:#005cc5">type</span>:<span style="color:#032f62">'input'</span>,
    <span style="color:#005cc5">field</span>:<span style="color:#032f62">'text'</span>,
    <span style="color:#005cc5">title</span>:<span style="color:#032f62">'text'</span>,
    <span style="color:#005cc5">value</span>:<span style="color:#032f62">'default'</span>,
    <span style="color:#005cc5">prefix</span>:{
        <span style="color:#005cc5">type</span>:<span style="color:#032f62">'ElButton'</span>, <span style="color:#005cc5">children</span>:[<span style="color:#032f62">'prefix'</span>]
    },
    <span style="color:#005cc5">suffix</span>:{
        <span style="color:#005cc5">type</span>:<span style="color:#032f62">'ElButton'</span>, <span style="color:#005cc5">children</span>:[<span style="color:#032f62">'suffix'</span>]
    },
}</code></pre> 
  <div> 
   <div> 
    <h3>4.组件联动</h3> 
    <p><strong>可以通过control配置项实现通过组件的值控制其他组件是否显示</strong></p> 
    <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fcontrol.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
    <p>例如当评价小于3星时输入差评原因</p> 
    <pre><code class="language-js"><span style="color:#6f42c1">{</span>
    <span style="color:#6f42c1">type</span>:<span style="color:#032f62">'rate',</span>
    <span style="color:#6f42c1">field</span>: <span style="color:#032f62">'star',</span>
    <span style="color:#6f42c1">title</span>:<span style="color:#032f62">'评分',</span>
    <span style="color:#6f42c1">value</span>:<span style="color:#032f62">5,</span>
    <span style="color:#6f42c1">control</span>:<span style="color:#032f62">[</span>
        <span style="color:#6f42c1">{</span>
            <span style="color:#6f42c1">handle(val){</span>
                <span style="color:#6f42c1">return</span> <span style="color:#032f62">val < 3</span>
            <span style="color:#6f42c1">},</span>
            <span style="color:#6f42c1">rule</span>:<span style="color:#032f62">[</span>
                <span style="color:#6f42c1">{</span>
                    <span style="color:#6f42c1">type</span>:<span style="color:#032f62">'input',</span>
                    <span style="color:#6f42c1">field</span>:<span style="color:#032f62">'info',</span>
                    <span style="color:#6f42c1">title</span>:<span style="color:#032f62">'差评原因',</span>
                    <span style="color:#6f42c1">value</span>:<span style="color:#032f62">'default info', </span>
                <span style="color:#6a737d">}</span> 
            <span style="color:#6a737d">]</span>   
        <span style="color:#6a737d">}</span>                                              
    <span style="color:#6f42c1">]</span>
<span style="color:#6f42c1">}</span></code></pre> 
    <table cellspacing="0" style="width:776px"> 
     <thead> 
      <tr> 
       <th>参数</th> 
       <th>说明</th> 
       <th>类型</th> 
      </tr> 
     </thead> 
     <tbody> 
      <tr> 
       <td style="border-color:#dddddd">value</td> 
       <td style="border-color:#dddddd">当组件的值和<code>value</code>全等时显示<code>rule</code>中的组件</td> 
       <td style="border-color:#dddddd">string|Number|Bool</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">handle</td> 
       <td style="border-color:#dddddd">当<code>handle</code>方法返回<code>true</code>时显示<code>rule</code>中的组件</td> 
       <td style="border-color:#dddddd">Function</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">rule</td> 
       <td style="border-color:#dddddd">该组件控制显示的组件</td> 
       <td style="border-color:#dddddd">Array</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">append</td> 
       <td style="border-color:#dddddd">设置<code>rule</code>中的规则追加的位置</td> 
       <td style="border-color:#dddddd">string</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">prepend</td> 
       <td style="border-color:#dddddd">设置<code>rule</code>中的规则前置插入的位置</td> 
       <td style="border-color:#dddddd">string</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">child</td> 
       <td style="border-color:#dddddd">设置<code>rule</code>是否插入到指定位置的children中,默认添加到当前规则的 children 中</td> 
       <td style="border-color:#dddddd">Boolean</td> 
      </tr> 
     </tbody> 
    </table> 
    <p><strong>注意! <code>handle</code>优先级大于<code>value</code>,所有符合条件的<code>control</code>都会生效</strong></p> 
    <h3>5. 表单验证</h3> 
    <p><strong>可以通过 validate 配置项设置组件的验证规则,自定义的表单组件也支持校验</strong></p> 
    <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fother%2Fvalidation-rules.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
    <p>例如设置input 组件必填</p> 
    <pre><code class="language-js">{
<span style="color:#005cc5">type</span>:<span style="color:#032f62">'input'</span>,
<span style="color:#6a737d">//...</span>
<span style="color:#005cc5">validate</span>:[{<span style="color:#005cc5">required</span>:true, <span style="color:#005cc5">type</span>:<span style="color:#032f62">'string'</span>, <span style="color:#005cc5">message</span>:<span style="color:#032f62">'请个输入内容'</span>}]
}</code></pre> 
    <table cellspacing="0" style="width:776px"> 
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
       <td style="border-color:#dddddd">enum</td> 
       <td style="border-color:#dddddd">枚举类型</td> 
       <td style="border-color:#dddddd">string</td> 
       <td style="border-color:#dddddd">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">len</td> 
       <td style="border-color:#dddddd">字段长度</td> 
       <td style="border-color:#dddddd">number</td> 
       <td style="border-color:#dddddd">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">max</td> 
       <td style="border-color:#dddddd">最大长度</td> 
       <td style="border-color:#dddddd">number</td> 
       <td style="border-color:#dddddd">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">message</td> 
       <td style="border-color:#dddddd">校验文案</td> 
       <td style="border-color:#dddddd">string</td> 
       <td style="border-color:#dddddd">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">min</td> 
       <td style="border-color:#dddddd">最小长度</td> 
       <td style="border-color:#dddddd">number</td> 
       <td style="border-color:#dddddd">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">pattern</td> 
       <td style="border-color:#dddddd">正则表达式校验</td> 
       <td style="border-color:#dddddd">RegExp</td> 
       <td style="border-color:#dddddd">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">required</td> 
       <td style="border-color:#dddddd">是否必选</td> 
       <td style="border-color:#dddddd">boolean</td> 
       <td style="border-color:#dddddd"><code>false</code></td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">transform</td> 
       <td style="border-color:#dddddd">校验前转换字段值</td> 
       <td style="border-color:#dddddd">function(value) => transformedValue:any</td> 
       <td style="border-color:#dddddd">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">type</td> 
       <td style="border-color:#dddddd">内建校验类型，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyiminghe%2Fasync-validator%23type" target="_blank">可选项</a></td> 
       <td style="border-color:#dddddd">string</td> 
       <td style="border-color:#dddddd">'string'</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">validator</td> 
       <td style="border-color:#dddddd">自定义校验</td> 
       <td style="border-color:#dddddd">function(rule, value, callback)</td> 
       <td style="border-color:#dddddd">-</td> 
      </tr> 
      <tr> 
       <td style="border-color:#dddddd">whitespace</td> 
       <td style="border-color:#dddddd">必选时，空格是否会被视为错误</td> 
       <td style="border-color:#dddddd">boolean</td> 
       <td style="border-color:#dddddd"><code>false</code></td> 
      </tr> 
     </tbody> 
    </table> 
    <p>注意!<code>type</code>需要根据组件的<code>value</code>类型定</p> 
    <div> 
     <h2>APi 介绍</h2> 
     <p><strong>下列是常用的方法</strong></p> 
     <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Finstance.html%3Ffrom%3Dosn" target="_blank">完整的Api介绍</a></p> 
     <h3>设置表单值</h3> 
     <p>覆盖方式,未定义的字段会设置为 <code>null</code></p> 
     <pre><code class="language-typescript"><span style="color:#d73a49">type</span> coverValue = (formData:{[field:string]:any}) => void</code></pre> 
     <ul> 
      <li>用法：</li> 
     </ul> 
     <pre><code class="language-js"><span style="color:#d73a49">fApi</span><span style="color:#6f42c1">.coverValue</span>({<span style="color:#005cc5">goods_name</span>:<span style="color:#032f62">'HuaWei'</span>})</code></pre> 
     <p>合并方式,未定义的字段不做修改</p> 
     <pre><code class="language-typescript"><span style="color:#d73a49">interface</span> setValue {
    (formData:{[field:string]:any}): void
    (field:string, value:any): void
}</code></pre> 
     <ul> 
      <li>用法：</li> 
     </ul> 
     <pre><code class="language-js"><span style="color:#d73a49">fApi</span><span style="color:#6f42c1">.setValue</span>({<span style="color:#005cc5">goods_name</span>:<span style="color:#032f62">'HuaWei'</span>})</code></pre> 
     <p>别名方法<code>changeValue</code>, <code>changeField</code></p> 
     <h3>隐藏字段</h3> 
     <pre><code class="language-typescript"><span style="color:#d73a49">interface</span> hidden {
    <span style="color:#6a737d">//隐藏全部组件</span>
    (status:Boolean):void
    <span style="color:#6a737d">//隐藏指定组件</span>
    (status:Boolean, field:string):void
    <span style="color:#6a737d">//隐藏部分组件</span>
    (status:Boolean, field:string[]):void 
}</code></pre> 
     <ul> 
      <li>用法：</li> 
     </ul> 
     <pre><code class="language-js">fApi.hidden(<span style="color:#005cc5">true</span>, <span style="color:#005cc5">'goods_name</span>')</code></pre> 
     <p><strong>获取组件隐藏状态</strong></p> 
     <pre><code class="language-typescript"><span style="color:#d73a49">type</span> hiddenStatus = (field:string)=>Boolean</code></pre> 
     <ul> 
      <li>用法：</li> 
     </ul> 
     <pre><code class="language-js"><span style="color:#d73a49">const</span> status = fApi.hiddenStatus(<span style="color:#005cc5">'goods_name</span>')</code></pre> 
     <h3>获取规则</h3> 
     <pre><code class="language-typescript"><span style="color:#d73a49">interface</span> getRule {
    (field:string):Rule
    (field:string, origin: <span style="color:#005cc5">true</span>): FormRule
}</code></pre> 
     <ul> 
      <li>用法：</li> 
     </ul> 
     <pre><code class="language-js"><span style="color:#d73a49">const</span> rule = fApi.getRule(<span style="color:#005cc5">'goods_name</span>')</code></pre> 
     <h3>插入规则</h3> 
     <p><strong>前置插入</strong></p> 
     <pre><code class="language-typescript"><span style="color:#d73a49">interface</span> prepend {
    <span style="color:#6a737d">//插入到第一个</span>
    (rule:FormRule):void 
    <span style="color:#6a737d">//插入指定字段前面</span>
    (rule:FormRule, field:string):void
    <span style="color:#6a737d">//插入到指定字段 children 中</span>
    (rule:FormRule, field:string, child:<span style="color:#005cc5">true</span>):void
}</code></pre> 
     <ul> 
      <li>用法：</li> 
     </ul> 
     <pre><code class="language-js"><span style="color:#d73a49">fApi</span><span style="color:#6f42c1">.prepend</span>({
     <span style="color:#005cc5">type</span>:<span style="color:#032f62">"input"</span>,
     <span style="color:#005cc5">title</span>:<span style="color:#032f62">"商品简介"</span>,
     <span style="color:#005cc5">field</span>:<span style="color:#032f62">"goods_info"</span>,
     <span style="color:#005cc5">value</span>:<span style="color:#032f62">""</span>,
     <span style="color:#005cc5">props</span>: {
         <span style="color:#032f62">"type"</span>: <span style="color:#032f62">"text"</span>,
         <span style="color:#032f62">"placeholder"</span>: <span style="color:#032f62">"请输入商品简介"</span>,
     },
     <span style="color:#005cc5">validate</span>:[
         { <span style="color:#005cc5">required</span>: true, <span style="color:#005cc5">message</span>: <span style="color:#032f62">'请输入商品简介'</span>, <span style="color:#005cc5">trigger</span>: <span style="color:#032f62">'blur'</span> },
     ],
}, <span style="color:#032f62">'goods-name'</span>)</code></pre> 
     <p><strong>后置追加</strong></p> 
     <pre><code class="language-typescript"><span style="color:#d73a49">interface</span> append {
    <span style="color:#6a737d">//插入到最后一个</span>
    (rule:FormRule):void 
    <span style="color:#6a737d">//插入指定字段后面</span>
    (rule:FormRule, field:string):void
    <span style="color:#6a737d">//插入到指定字段 children 中</span>
    (rule:FormRule, field:string, child:<span style="color:#005cc5">true</span>):void
}</code></pre> 
     <ul> 
      <li>用法：</li> 
     </ul> 
     <pre><code class="language-js"><span style="color:#d73a49">fApi</span><span style="color:#6f42c1">.append</span>({
     <span style="color:#005cc5">type</span>:<span style="color:#032f62">"input"</span>,
     <span style="color:#005cc5">title</span>:<span style="color:#032f62">"商品简介"</span>,
     <span style="color:#005cc5">field</span>:<span style="color:#032f62">"goods_info"</span>,
     <span style="color:#005cc5">value</span>:<span style="color:#032f62">""</span>,
     <span style="color:#005cc5">props</span>: {
         <span style="color:#032f62">"type"</span>: <span style="color:#032f62">"text"</span>,
         <span style="color:#032f62">"placeholder"</span>: <span style="color:#032f62">"请输入商品简介"</span>,
     },
     <span style="color:#005cc5">validate</span>:[
         { <span style="color:#005cc5">required</span>: true, <span style="color:#005cc5">message</span>: <span style="color:#032f62">'请输入商品简介'</span>, <span style="color:#005cc5">trigger</span>: <span style="color:#032f62">'blur'</span> },
     ],
}, <span style="color:#032f62">'goods-name'</span>)</code></pre> 
     <div> 
      <div> 
       <h3>删除指定规则</h3> 
       <pre><code class="language-typescript">type removeRule = (rule:FormRule) => FormRule</code></pre> 
       <ul> 
        <li>用法：</li> 
       </ul> 
       <pre><code class="language-js"><span style="color:#d73a49">const</span> rule = {<span style="color:#d73a49">type</span>:<span style="color:#032f62">'input'</span>, <span style="color:#6a737d">/** ... **/</span>}
fApi.removeRule(rule)</code></pre> 
       <h3>验证表单</h3> 
       <pre><code class="language-typescript"><span style="color:#d73a49">type</span> validate = (callback:(...args:any[]) => void)=> void</code></pre> 
       <ul> 
        <li>用法：</li> 
       </ul> 
       <pre><code class="language-js"><span style="color:#d73a49">fApi</span><span style="color:#6f42c1">.validate</span>((valid, fail) => {
    <span style="color:#d73a49">if</span>(valid){
        <span style="color:#6a737d">//todo 表单验证通过</span>
    }else{
        <span style="color:#6a737d">//todo 表单验证未通过</span>
    }
})</code></pre> 
       <h3>验证指定字段</h3> 
       <pre><code class="language-typescript"><span style="color:#d73a49">type</span> validateField = (field, callback:(...args:any[]) => void)=> void</code></pre> 
       <ul> 
        <li>用法：</li> 
       </ul> 
       <pre><code class="language-js"><span style="color:#d73a49">fApi</span><span style="color:#6f42c1">.validateField</span>(<span style="color:#032f62">'goods_name'</span>, (valid, fail) => {
    <span style="color:#d73a49">if</span>(valid){
        <span style="color:#6a737d">//todo 字段验证通过</span>
    }else{
        <span style="color:#6a737d">//todo 字段验证未通过</span>
    }
})</code></pre> 
       <h3>获取表单数据</h3> 
       <pre><code class="language-typescript"><span style="color:#d73a49">interface</span> formData {
    <span style="color:#6a737d">//获取全部数据</span>
    (): {[field:string]:any }
    <span style="color:#6a737d">//获取部分字段的数据</span>
    (field:string[]): {[field:string]:any }
}</code></pre> 
       <ul> 
        <li>用法：</li> 
       </ul> 
       <pre><code class="language-js"><span style="color:#6f42c1">const</span> <span style="color:#032f62">formData = fApi.formData()</span></code></pre> 
       <h3>修改提交按钮</h3> 
       <pre><code class="language-typescript"><span style="color:#d73a49">type</span> submitBtnProps = (props:Object) => void</code></pre> 
       <ul> 
        <li>用法：</li> 
       </ul> 
       <pre><code class="language-js"><span style="color:#d73a49">fApi</span><span style="color:#6f42c1">.submitBtnProps</span>({<span style="color:#005cc5">disabled</span>:true})</code></pre> 
       <ul> 
        <li> <p>快捷操作:</p> 
         <ul> 
          <li><code>fApi.btn.loading(true)</code> 设置提交按钮进入loading状态</li> 
          <li><code>fApi.btn.disabled(true)</code> 设置提交按钮禁用状态</li> 
          <li><code>fApi.btn.show(true)</code> 设置提交按钮显示状态</li> 
         </ul> </li> 
       </ul> 
       <h3>修改重置按钮</h3> 
       <pre><code class="language-typescript"><span style="color:#d73a49">type</span> resetBtnProps = ( props:Object) => void</code></pre> 
       <ul> 
        <li>用法：</li> 
       </ul> 
       <pre><code class="language-js"><span style="color:#d73a49">fApi</span><span style="color:#6f42c1">.resetBtnProps</span>({<span style="color:#005cc5">disabled</span>:true})</code></pre> 
       <ul> 
        <li> <p>快捷操作:</p> 
         <ul> 
          <li><code>fApi.resetBtn.loading(true)</code> 设置重置按钮进入loading状态</li> 
          <li><code>fApi.resetBtn.disabled(true)</code> 设置重置按钮禁用状态</li> 
          <li><code>fApi.resetBtn.show(true)</code> 设置重置按钮显示状态</li> 
         </ul> </li> 
       </ul> 
       <h3>隐藏表单</h3> 
       <pre><code class="language-typescript"><span style="color:#d73a49">type</span> hideForm = (hide:Boolean)=>void</code></pre> 
       <ul> 
        <li>用法：</li> 
       </ul> 
       <pre><code class="language-js">fApi.hideForm(<span style="color:#005cc5">true</span>)</code></pre> 
       <h3>提交表单</h3> 
       <pre><code class="language-typescript"><span style="color:#d73a49">type</span> submit = (success: (formData: FormData, $f: fApi) => void, fail: ($f: fApi) => void)=> void
</code></pre> 
       <ul> 
        <li>用法：</li> 
       </ul> 
       <pre><code class="language-js">fApi.submit((formData, fapi) => {
    //todo 提交表单
},()=>{
    //todo 表单验证未通过
}</code>
</pre> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            