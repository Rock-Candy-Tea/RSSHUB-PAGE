
---
title: 'Vue-实用插件  vee-validate插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6244'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 18:28:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=6244'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">vee-validate插件</h2>
<p>这个插件可以用来在未使用组件库,没有自带好的校验规则时使用,进行表单校验</p>
<p>1.安装</p>
<pre><code class="hljs language-js copyable" lang="js">npm i vee-validate@<span class="hljs-number">4.0</span><span class="hljs-number">.3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.导入</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Form, Field &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vee-validate'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.定义校验规则(最好是在utils文件夹中单独封装js文件导出)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建js文件进行导出</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// 校验项account</span>
  account (value) &#123;
    <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-string">'不能为空'</span><span class="hljs-comment">// 条件判断,</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span> <span class="hljs-comment">// 最后全部通过必须return true</span>
  &#125;,
  password (value) &#123;
    <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-string">'请输入密码'</span>
    <span class="hljs-keyword">if</span> (!<span class="hljs-regexp">/^\w&#123;6,24&#125;$/</span>.test(value)) <span class="hljs-keyword">return</span> <span class="hljs-string">'密码是6-24个字符'</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;,
  mobile (value) &#123;
    <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-string">'请输入手机号'</span>
    <span class="hljs-keyword">if</span> (!<span class="hljs-regexp">/^1[3-9]\d&#123;9&#125;$/</span>.test(value)) <span class="hljs-keyword">return</span> <span class="hljs-string">'手机号格式错误'</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;,
  code (value) &#123;
    <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-string">'请输入验证码'</span>
    <span class="hljs-keyword">if</span> (!<span class="hljs-regexp">/^\d&#123;6&#125;$/</span>.test(value)) <span class="hljs-keyword">return</span> <span class="hljs-string">'验证码是6个数字'</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;,
  isAgree (value) &#123;
    <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-string">'请勾选同意用户协议'</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.使用<code>Form</code>组件配置校验规则和错误对象 (form 和 Field都是从插件中按需导出)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// validation-schema="mySchema"  配置校验规则</span>
<span class="hljs-comment">// v-slot：导出错误对象</span>
<Form
  :validation-schema=<span class="hljs-string">"mySchema"</span>
  v-slot=<span class="hljs-string">"&#123; errors &#125;"</span>
>
 <!-- 表单元素 -->
</Form>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> schema <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/vee-validate-schema'</span>
  setup () &#123;
    <span class="hljs-comment">// 表单对象数据</span>
    <span class="hljs-keyword">const</span> form = reactive(&#123;
      <span class="hljs-attr">account</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 账号</span>
      <span class="hljs-attr">password</span>: <span class="hljs-literal">null</span> <span class="hljs-comment">// 密码</span>
    &#125;)
    <span class="hljs-comment">// 校验规则对象</span>
    <span class="hljs-keyword">const</span> mySchema = &#123;
      <span class="hljs-attr">account</span>: schema.account,
      <span class="hljs-attr">password</span>: schema.password
    &#125;
    <span class="hljs-keyword">return</span> &#123; form, mySchema &#125;
 &#125; 
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.使用 <code>Field</code> 组件，添加表单项目校验</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//1. 把input改成 `Field` 组件，默认解析成input</span>
<span class="hljs-comment">//2. `Field` 添加name属性，作用是指定使用schema中哪个校验规则</span>
<span class="hljs-comment">//3. `Field`添加v-model，作用是提供表单数据的双向绑定</span>
<span class="hljs-comment">//4. 发生表单校验错误，显示错误类名`error`，提示红色边框</span>

<Field
      v-model=<span class="hljs-string">"form.account"</span>
      name=<span class="hljs-string">"account"</span> 
      type=<span class="hljs-string">"text"</span>
      placeholder=<span class="hljs-string">"请输入用户名"</span>
      :<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"&#123; error: errors.account &#125;"</span> <span class="hljs-comment">// 如果返回错误信息,为true 显示类error</span>
    />
    <!-- <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入用户名"</span> /></span></span> -->
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.补充表单数据和验证规则数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 表单绑定的数据</span>
<span class="hljs-keyword">const</span> form = reactive(&#123;
  <span class="hljs-attr">account</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 账号</span>
  <span class="hljs-attr">password</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 密码</span>
  <span class="hljs-attr">isAgree</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 是否选中</span>
&#125;)

<span class="hljs-comment">// 声明当前表单需要的校验数据规则</span>
<span class="hljs-keyword">const</span> curSchema = reactive(&#123;
  <span class="hljs-attr">account</span>: schema.account, <span class="hljs-comment">// 账号</span>
  <span class="hljs-attr">password</span>: schema.password, <span class="hljs-comment">// 密码</span>
  <span class="hljs-attr">isAgree</span>: schema.isAgree <span class="hljs-comment">// 是否选中</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            