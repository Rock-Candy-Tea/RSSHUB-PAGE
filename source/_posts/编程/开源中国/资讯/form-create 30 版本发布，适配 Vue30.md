
---
title: 'form-create 3.0 版本发布，适配 Vue3.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9e2078374be1b5e69756e8a779627b296b9.png'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 15:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9e2078374be1b5e69756e8a779627b296b9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">form-create 是一个可以通过 JSON 生成具有动态渲染、数据收集、验证和提交功能的表单生成组件。支持3个UI框架，并且支持生成任何 Vue 组件。内置20种常用表单组件和自定义组件，再复杂的表单都可以轻松搞定。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv3%2F%3Ffrom%3Dosn" target="_blank">文档</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxaboy%2Fform-create" target="_blank">GitHub</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>3.0.0 版本主要更新了以下内容:</strong></p> 
<div style="text-align:left"> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li> <p style="margin-left:0; margin-right:0">适配 vue3</p> </li> 
  <li> <p style="margin-left:0; margin-right:0">适配 element-plus 和 ant-design-vue3.0</p> </li> 
  <li> <p style="margin-left:0; margin-right:0">功能于 2.5.12 版本一致</p> </li> 
 </ul> 
</div> 
<p style="margin-left:0.5em; margin-right:0px; text-align:start"><strong>移除配置项</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>attrs</li> 
 <li>scopedSlots</li> 
 <li>domProps</li> 
 <li>hook</li> 
 <li>nativeOn</li> 
 <li>nativeEmit</li> 
</ul> 
<p style="margin-left:0.5em; margin-right:0px; text-align:start"><strong>功能调整</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修改<span> </span><code>validate</code>,<span> </span><code>validateField</code>,<span> </span><code>submit</code><span> </span>返回值, 返回<code>Promise</code></li> 
 <li>修改<span> </span><code>v-model</code><span> </span>为<span> </span><code>v-model:api</code></li> 
 <li>修改<span> </span><code>value.sync</code><span> </span>为<span> </span><code>v-model</code></li> 
</ul> 
<p style="margin-left:0.5em; margin-right:0px; text-align:start"><strong>不兼容项</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>不支持 iview</li> 
 <li>移除<span> </span><code>template</code><span> </span>模板方式生成组件</li> 
 <li>移除<span> </span><code>formCreate.init</code><span> </span>方法</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">支持 UI</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>element-plus</li> 
 <li>ant-design-vue</li> 
</ul> 
<h2 style="margin-left:.5em; margin-right:0; text-align:start">功能</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>支持 Vue3 版本</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>支持2个 UI 框架</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>通过 JSON 生成表单</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>自定义组件</strong></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>可生成任何Vue组件</li> 
   <li>自带数据验证</li> 
   <li>可快速扩展</li> 
   <li>轻松转换为表单组件</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>全局配置</strong></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>可以设置表单配置</li> 
   <li>可以设置指定组件全局配置</li> 
   <li>可以设置所有组件公共的全局配置</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>自定义配置项扩展，快速根据业务逻辑扩展</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>支持组件设置前后缀</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>支持规则之前联动更新</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>强大的API，可快速操作表单</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>双向数据绑定</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>事件扩展，事件注入</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>局部视图更新</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>数据验证</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>栅格布局</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>嵌套对象，数组组件</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>内置组件</strong></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>hidden</li> 
   <li>input</li> 
   <li>inputNumber</li> 
   <li>checkbox</li> 
   <li>radio</li> 
   <li>switch</li> 
   <li>select</li> 
   <li>autoComplete</li> 
   <li>cascader</li> 
   <li>colorPicker</li> 
   <li>datePicker</li> 
   <li>timePicker</li> 
   <li>rate</li> 
   <li>slider</li> 
   <li>upload</li> 
   <li>tree</li> 
   <li>frame</li> 
   <li>group</li> 
   <li>subForm/object</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:.5em; margin-right:0; text-align:start">图例</h3> 
<p><img height="1239" src="https://oscimg.oschina.net/oscnet/up-9e2078374be1b5e69756e8a779627b296b9.png" width="1030" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装</h2> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">根据自己使用的 UI 安装对应的版本</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>element-plus</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">i</span></span></span> @<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">form</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">create</span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">element</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">ui@next</span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>ant-design-vue@3.0</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">i</span></span></span> @<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">form</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">create</span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">ant</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">design</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">vue@next</span></span></span></code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">快速上手</h2> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">本文以<code>element-ui</code>为例</p> 
</blockquote> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>在 main.js 中写入以下内容：</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#0077aa">import</span> ElementUI <span style="color:#0077aa">from</span> <span style="color:#669900">'element-plus/es/index'</span>
<span style="color:#0077aa">import</span> <span style="color:#669900">'element-plus/dist/index.css'</span>
<span style="color:#0077aa">import</span> formCreate <span style="color:#0077aa">from</span> <span style="color:#669900">'@form-create/element-ui'</span>

app<span style="color:#999999">.</span><span style="color:#dd4a68">use</span><span style="color:#999999">(</span>ElementUI<span style="color:#999999">)</span>
app<span style="color:#999999">.</span><span style="color:#dd4a68">use</span><span style="color:#999999">(</span>FormCreate<span style="color:#999999">)</span></code></pre> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>生成表单</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fdemo.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-html"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">template</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
  <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">div</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">id</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"app1"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
      <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">form-create</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">v-model:api</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"fApi"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">:rule</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"rule"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">:option</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"option"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">v-model</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"value"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">form-create</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
  <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">div</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">template</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></code></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">export</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">default</span></span></span> &#123;
    <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">data</span></span></span>() &#123;
        <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">return</span></span></span> &#123;
            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">//实例对象</span></span></span>
            <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">fApi</span></span></span>: &#123;&#125;,
            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">//表单数据</span></span></span>
            <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">value</span></span></span>: &#123;&#125;,
            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">//表单生成规则</span></span></span>
            <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">rule</span></span></span>: [
                &#123;
                    <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">type</span></span></span>: <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'input'</span></span></span>,
                    <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">field</span></span></span>: <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'goods_name'</span></span></span>,
                    <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">title</span></span></span>: <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'商品名称'</span></span></span>
                &#125;,
                &#123;
                    <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">type</span></span></span>: <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'datePicker'</span></span></span>,
                    <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">field</span></span></span>: <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'created_at'</span></span></span>,
                    <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">title</span></span></span>: <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'创建时间'</span></span></span>
                &#125;
            ],
            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">//组件参数配置</span></span></span>
            <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">option</span></span></span>: &#123;
                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">//表单提交事件</span></span></span>
                <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">onSubmit</span></span></span>: function (formData) &#123;
                    alert(JSON.stringify(formData))
                &#125;
            &#125;
        &#125;
    &#125;
&#125;</code></pre>
                                        </div>
                                      
</div>
            