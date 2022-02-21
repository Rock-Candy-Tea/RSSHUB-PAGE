
---
title: 'form-create 3.1 发布，动态表单组件_适配 4 个 UI 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4cb85c62c93dc986075a5ffee95d42b511c.png'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 10:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4cb85c62c93dc986075a5ffee95d42b511c.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">form-create 是一个可以通过 JSON 生成具有动态渲染、数据收集、验证和提交功能的表单生成组件。支持4个UI框架，并且支持生成任何 Vue 组件。内置20种常用表单组件和自定义组件，再复杂的表单都可以轻松搞定。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fform-create.com%2Fv3%2F%3Ffrom%3Dosn" target="_blank">文档</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxaboy%2Fform-create" target="_blank">源码</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>3.1 版本主要更新了以下内容:</strong></p> 
<div style="text-align:left"> 
 <ul style="margin-left:0; margin-right:0"> 
  <li>新增 按需加载组件</li> 
  <li>新增 适配 naive-ui</li> 
  <li>新增 适配 arco-design</li> 
  <li>新增 适配 element-plus2.0</li> 
  <li>重构 element-plus<span> </span><code>radio</code>,<code>checkbox</code>组件</li> 
  <li>新增<span> </span><code>html</code><span> </span>组件</li> 
  <li>新增<span> </span><code>options</code>,<span> </span><code>children</code><span> </span>字段支持异步加载</li> 
  <li>新增<span> </span><code>getApi</code>方法</li> 
 </ul> 
 <p style="color:rgba(0, 0, 0, 0.85); margin-left:0; margin-right:0; text-align:start"><strong>不兼容项</strong></p> 
 <ul style="margin-left:0; margin-right:0"> 
  <li>重构 element-plus<span> </span><code>upload</code><span> </span>组件, 部分配置项失效</li> 
  <li>重新实现<span> </span><code>formCreateInect</code>, 改为通过<span> </span><code>props</code><span> </span>接收</li> 
 </ul> 
 <p><strong>支持 UI</strong></p> 
 <ul> 
  <li>element-plus</li> 
  <li>ant-design-vue</li> 
  <li>naive-ui</li> 
  <li>arco-design</li> 
 </ul> 
 <p><strong>按需导入</strong></p> 
</div> 
<p>如果不需要导入UI框架的全部组件,可以通过 auto-import.js 一次导入 form-create 需要的组件. 以 element-ui 为例</p> 
<pre><code class="language-javascript">import formCreate from '@form-create/element-ui'
import install from '@form-create/element-ui/auto-import'
formCreate.use(install)
app.use(formCreate)</code></pre> 
<h2 style="text-align:start">安装</h2> 
<blockquote> 
 <p>根据自己使用的 UI 安装对应的版本</p> 
</blockquote> 
<p style="color:#24292f; text-align:start">element-plus^2.0</p> 
<div style="text-align:start"> 
 <pre>npm install @form-create/element-ui@next</pre> 
</div> 
<p style="color:#24292f; text-align:start">ant-design-vue^3.0</p> 
<div style="text-align:start"> 
 <pre>npm install @form-create/ant-design-vue@next</pre> 
</div> 
<p style="color:#24292f; text-align:start">arco-design^2.0</p> 
<div style="text-align:start"> 
 <pre>npm install @form-create/arco-design@next</pre> 
</div> 
<p style="color:#24292f; text-align:start">naive-ui^2.0</p> 
<div style="text-align:start"> 
 <pre>npm install @form-create/naive-ui@next
</pre> 
</div> 
<h2 style="margin-left:.5em; margin-right:0; text-align:start">引入 form-create</h2> 
<h4 style="margin-left:.5em; margin-right:0; text-align:start">浏览器</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#708090"><!-- import Vue --></span>
<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>script</span> <span style="color:#669900">src</span><span style="color:#0077aa"><span style="color:#999999">=</span><span style="color:#999999">"</span>https://cdn.jsdelivr.net/npm/vue@3.2.22/dist/vue.min.js<span style="color:#999999">"</span></span><span style="color:#999999">></span></span><span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>script</span><span style="color:#999999">></span></span>

<span style="color:#708090"><!-- import element-ui --></span>
<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>link</span> <span style="color:#669900">rel</span><span style="color:#0077aa"><span style="color:#999999">=</span><span style="color:#999999">"</span>stylesheet<span style="color:#999999">"</span></span> <span style="color:#669900">href</span><span style="color:#0077aa"><span style="color:#999999">=</span><span style="color:#999999">"</span>https://cdn.jsdelivr.net/npm/element-plus@2.0.0/dist/index.css<span style="color:#999999">"</span></span><span style="color:#999999">></span></span>
<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>script</span> <span style="color:#669900">src</span><span style="color:#0077aa"><span style="color:#999999">=</span><span style="color:#999999">"</span>https://cdn.jsdelivr.net/npm/element-plus@2.0.0/dist/index.full.min.js<span style="color:#999999">"</span></span><span style="color:#999999">></span></span><span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>script</span><span style="color:#999999">></span></span>

<span style="color:#708090"><!-- import formCreate --></span>
<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>script</span> <span style="color:#669900">src</span><span style="color:#0077aa"><span style="color:#999999">=</span><span style="color:#999999">"</span>https://cdn.jsdelivr.net/npm/@form-create/element-ui@next/dist/form-create.min.js<span style="color:#999999">"</span></span><span style="color:#999999">></span></span><span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>script</span><span style="color:#999999">></span></span>
</code></pre> 
</div> 
<h4 style="margin-left:.5em; margin-right:0; text-align:start">NodeJs</h4> 
<p style="color:rgba(0, 0, 0, 0.85); margin-left:0; margin-right:0; text-align:start">在 main.js 中写入以下内容：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#0077aa">import</span> ElementUI <span style="color:#0077aa">from</span> <span style="color:#669900">'element-plus/es/index'</span>
<span style="color:#0077aa">import</span> <span style="color:#669900">'element-plus/dist/index.css'</span>
<span style="color:#0077aa">import</span> formCreate <span style="color:#0077aa">from</span> <span style="color:#669900">'@form-create/element-ui'</span>

app<span style="color:#999999">.</span><span style="color:#dd4a68">use</span><span style="color:#999999">(</span>ElementUI<span style="color:#999999">)</span>
app<span style="color:#999999">.</span><span style="color:#dd4a68">use</span><span style="color:#999999">(</span>FormCreate<span style="color:#999999">)</span>
</code></pre> 
</div> 
<h1 style="margin-left:.5em; margin-right:0; text-align:start">生成表单</h1> 
<p><img height="534" src="https://oscimg.oschina.net/oscnet/up-4cb85c62c93dc986075a5ffee95d42b511c.png" width="2208" referrerpolicy="no-referrer"></p> 
<p style="color:rgba(0, 0, 0, 0.85); margin-left:0; margin-right:0; text-align:start">使用<span> </span><code><form-create></form-create></code><span> </span>标签创建表单</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>template</span><span style="color:#999999">></span></span>
    <span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>form-create</span> <span style="color:#669900">:rule</span><span style="color:#0077aa"><span style="color:#999999">=</span><span style="color:#999999">"</span>rule<span style="color:#999999">"</span></span> <span style="color:#669900"><span style="color:#e2777a">v-model:</span>api</span><span style="color:#0077aa"><span style="color:#999999">=</span><span style="color:#999999">"</span>fApi<span style="color:#999999">"</span></span> <span style="color:#669900">:option</span><span style="color:#0077aa"><span style="color:#999999">=</span><span style="color:#999999">"</span>options<span style="color:#999999">"</span></span><span style="color:#999999">/></span></span>
<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>template</span><span style="color:#999999">></span></span>

<span style="color:#990055"><span style="color:#990055"><span style="color:#999999"><</span>script</span><span style="color:#999999">></span></span><span><span>
    <span style="color:#0077aa">export</span> <span style="color:#0077aa">default</span> <span style="color:#999999">&#123;</span>
        <span style="color:#dd4a68">data</span><span style="color:#999999">(</span><span style="color:#999999">)</span><span style="color:#999999">&#123;</span>
            <span style="color:#0077aa">return</span> <span style="color:#999999">&#123;</span>
                fApi<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#999999">&#123;</span><span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                options<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#999999">&#123;</span>
                    <span style="color:#dd4a68">onSubmit</span><span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#999999">(</span><span>formData</span><span style="color:#999999">)</span><span style="background-color:rgba(255, 255, 255, 0.5)">=></span><span style="color:#999999">&#123;</span>
                        <span style="color:#dd4a68">alert</span><span style="color:#999999">(</span><span style="color:#990055">JSON</span><span style="color:#999999">.</span><span style="color:#dd4a68">stringify</span><span style="color:#999999">(</span>formData<span style="color:#999999">)</span><span style="color:#999999">)</span>
                    <span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                    resetBtn<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#990055">true</span>
                <span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                rule<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#999999">[</span>
                    <span style="color:#999999">&#123;</span>
                        type<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'input'</span><span style="color:#999999">,</span>
                        field<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'goods_name'</span><span style="color:#999999">,</span>
                        title<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'商品名称'</span><span style="color:#999999">,</span>
                        value<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'form-create'</span>
                    <span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                    <span style="color:#999999">&#123;</span>
                        type<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'checkbox'</span><span style="color:#999999">,</span>
                        field<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'label'</span><span style="color:#999999">,</span>
                        title<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'标签'</span><span style="color:#999999">,</span>
                        value<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#999999">[</span><span style="color:#990055">0</span><span style="color:#999999">,</span><span style="color:#990055">1</span><span style="color:#999999">,</span><span style="color:#990055">2</span><span style="color:#999999">,</span><span style="color:#990055">3</span><span style="color:#999999">]</span><span style="color:#999999">,</span>
                        options<span style="background-color:rgba(255, 255, 255, 0.5)">:</span> <span style="color:#999999">[</span>
                            <span style="color:#999999">&#123;</span>label<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'好用'</span><span style="color:#999999">,</span>value<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#990055">0</span><span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                            <span style="color:#999999">&#123;</span>label<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'快速'</span><span style="color:#999999">,</span>value<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#990055">1</span><span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                            <span style="color:#999999">&#123;</span>label<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'高效'</span><span style="color:#999999">,</span>value<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#990055">2</span><span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                            <span style="color:#999999">&#123;</span>label<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'全能'</span><span style="color:#999999">,</span>value<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#990055">3</span><span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                        <span style="color:#999999">]</span>
                    <span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                  <span style="color:#999999">&#123;</span>
                    type<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'a-button'</span><span style="color:#999999">,</span>
                    title<span style="background-color:rgba(255, 255, 255, 0.5)">:</span><span style="color:#669900">'自定义按钮'</span><span style="color:#999999">,</span>
                    native<span style="background-color:rgba(255, 255, 255, 0.5)">:</span> <span style="color:#990055">false</span><span style="color:#999999">,</span>
                    on<span style="background-color:rgba(255, 255, 255, 0.5)">:</span> <span style="color:#999999">&#123;</span>
                      <span style="color:#dd4a68">click</span><span style="color:#999999">(</span><span style="color:#999999">)</span><span style="color:#999999">&#123;</span>
                        <span style="color:#dd4a68">alert</span><span style="color:#999999">(</span><span style="color:#669900">'点击了按钮'</span><span style="color:#999999">)</span>
                      <span style="color:#999999">&#125;</span>
                    <span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                    children<span style="background-color:rgba(255, 255, 255, 0.5)">:</span> <span style="color:#999999">[</span><span style="color:#669900">'按钮'</span><span style="color:#999999">]</span>
                  <span style="color:#999999">&#125;</span><span style="color:#999999">,</span>
                <span style="color:#999999">]</span>
            <span style="color:#999999">&#125;</span>
            
        <span style="color:#999999">&#125;</span>
    <span style="color:#999999">&#125;</span>
</span></span><span style="color:#990055"><span style="color:#990055"><span style="color:#999999"></</span>script</span><span style="color:#999999">></span></span></code></pre> 
</div>
                                        </div>
                                      
</div>
            