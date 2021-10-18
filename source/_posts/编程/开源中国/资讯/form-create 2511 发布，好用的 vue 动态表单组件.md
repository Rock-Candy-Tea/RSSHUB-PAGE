
---
title: 'form-create 2.5.11 发布，好用的 vue 动态表单组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3219'
author: 开源中国
comments: false
date: Mon, 18 Oct 2021 10:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3219'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">form-create 是一个可以通过 JSON 生成具有动态渲染、数据收集、验证和提交功能的表单生成组件。支持3个UI框架，并且支持生成任何 Vue 组件。内置20种常用表单组件和自定义组件，再复杂的表单都可以轻松搞定。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2F%3Ffrom%3Dosn" target="_blank">文档</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxaboy%2Fform-create" target="_blank">GitHub</a> | <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fdemo.html%3Ffrom%3Dosn" target="_blank">示例</a> | <span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fdesigner%3Ffrom%3Dosn" target="_blank">可视化表单设计器</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">支持 UI</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>element-ui</li> 
 <li>iview/view-design</li> 
 <li>ant-design-vue</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2.5.11主要更新了以下内容:</strong></p> 
<div style="text-align:left"> 
 <ul> 
  <li> <p>新增<span> </span><code>deep</code><span> </span>配置项</p> </li> 
  <li> <p>优化 允许<span> </span><code>field</code><span> </span>重复</p> </li> 
  <li> <p>优化<span> </span><code>frame</code>,<code>upload</code>组件, 允许禁用时预览</p> </li> 
  <li> <p>优化<span> </span><code>json</code><span> </span>解析</p> </li> 
  <li> <p>优化<span> </span><code>value</code>同步</p> </li> 
  <li> <p>修复<span> </span><code>control</code><span> </span>首次可能不生效问题</p> </li> 
  <li> <p>删除<span> </span><code>helper</code> 助手方法</p> </li> 
 </ul> 
</div> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fupdate.html%3Ffrom%3Dosn" target="_blank">更新记录</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装</h2> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">根据自己使用的 UI 安装对应的版本</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>element-ui</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">i</span></span></span> @<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">form</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">create</span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">element</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">ui</span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>iview@2.x|3.x</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">i</span></span></span> @<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">form</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">create</span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">iview</span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>iview/view-design@4.x</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">i</span></span></span> @<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">form</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">create</span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">iview4</span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>ant-design-vue@1.5+</code> 版本</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sh"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">npm</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">i</span></span></span> @<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">form</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">create</span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">ant</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">design</span></span></span>-<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">vue</span></span></span></code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">快速上手</h2> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">本文以<code>element-ui</code>为例</p> 
</blockquote> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>在 main.js 中写入以下内容：</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-js"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">import</span></span></span> Vue <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">from</span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'vue'</span></span></span>
<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">import</span></span></span> ELEMENT <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">from</span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'element-ui'</span></span></span>
<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">import</span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'element-ui/lib/theme-chalk/index.css'</span></span></span>

<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">import</span></span></span> formCreate <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">from</span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'@form-create/element-ui'</span></span></span>

Vue.use(ELEMENT)
Vue.use(formCreate)</code></pre> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>生成表单</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv2%2Fguide%2Fdemo.html%3Ffrom%3Dosn" target="_blank">在线示例</a></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-html"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">template</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
  <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">div</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">id</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"app1"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
      <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">form-create</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">v-model</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"fApi"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">:rule</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"rule"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">:option</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"option"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">:value.sync</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"value"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">form-create</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
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
            