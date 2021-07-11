
---
title: '使用antd-form-render配置各类表单'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846740cc9ee5404c8a319002809f467c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 05:36:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846740cc9ee5404c8a319002809f467c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>基于react,antd v4 搭配antd-form-render可以轻松实现各类表单</p>
<p>尝试地址： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fleonwgc%2Fantd-form-render-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/leonwgc/antd-form-render-demo" ref="nofollow noopener noreferrer">github.com/leonwgc/ant…</a></p>
<ol>
<li>一行一列布局</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846740cc9ee5404c8a319002809f467c~tplv-k3u1fbpfcp-watermark.image" alt="demo1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>;
<span class="hljs-keyword">import</span> &#123; Form, Button, Space, Input, message &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> FormRender <span class="hljs-keyword">from</span> <span class="hljs-string">'antd-form-render'</span>;

<span class="hljs-keyword">const</span> StyledOneRow = styled.div<span class="hljs-string">`
  width: 400px;
`</span>;

<span class="hljs-keyword">const</span> OneCol = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [form] = Form.useForm();

  <span class="hljs-keyword">const</span> oneRowLayout = [
    &#123;
      <span class="hljs-attr">type</span>: Input,
      <span class="hljs-attr">label</span>: <span class="hljs-string">'手机号'</span>,
      <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'请输入'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'tel'</span>,
      <span class="hljs-attr">elProps</span>: &#123;
        <span class="hljs-attr">maxLength</span>: <span class="hljs-number">11</span>,
      &#125;,
      <span class="hljs-attr">itemProps</span>: &#123;
        <span class="hljs-attr">rules</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入'</span> &#125;,
          &#123; <span class="hljs-attr">pattern</span>: <span class="hljs-regexp">/^1\d&#123;10&#125;$/</span>, message: <span class="hljs-string">'手机号必须为11位数字'</span> &#125;,
        ],
      &#125;,
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: Input.Password,
      <span class="hljs-attr">label</span>: <span class="hljs-string">'密码'</span>,
      <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'请输入'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'pwd'</span>,
      <span class="hljs-attr">itemProps</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入'</span> &#125;],
      &#125;,
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: Input.Password,
      <span class="hljs-attr">label</span>: <span class="hljs-string">'确认密码'</span>,
      <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'请输入'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'confirmPwd'</span>,
      <span class="hljs-attr">itemProps</span>: &#123;
        <span class="hljs-attr">rules</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入'</span> &#125;,
          <span class="hljs-function">(<span class="hljs-params">&#123; getFieldValue &#125;</span>) =></span> (&#123;
            <span class="hljs-function"><span class="hljs-title">validator</span>(<span class="hljs-params">_, value</span>)</span> &#123;
              <span class="hljs-keyword">if</span> (!value || getFieldValue(<span class="hljs-string">'pwd'</span>) === value) &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve();
              &#125;
              <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'两次密码不一致'</span>));
            &#125;,
          &#125;),
        ],
      &#125;,
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: Input.TextArea,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'desc'</span>,
      <span class="hljs-attr">label</span>: <span class="hljs-string">'简介'</span>,
      <span class="hljs-attr">elProps</span>: &#123;
        <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'个人简介'</span>,
        <span class="hljs-attr">rows</span>: <span class="hljs-number">4</span>,
      &#125;,
    &#125;,
    &#123;
      <span class="hljs-comment">// 自定义render</span>
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Form.Item</span> <span class="hljs-attr">wrapperCol</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">offset:</span> <span class="hljs-attr">6</span> &#125;&#125;></span>
            <span class="hljs-tag"><<span class="hljs-name">Space</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">htmlType</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>
                确定
              <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">htmlType</span>=<span class="hljs-string">"reset"</span>></span>重置<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">Space</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span></span>
        );
      &#125;,
    &#125;,
  ];

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">StyledOneRow</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Form</span>
        <span class="hljs-attr">form</span>=<span class="hljs-string">&#123;form&#125;</span>
        <span class="hljs-attr">labelCol</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">span:</span> <span class="hljs-attr">6</span> &#125;&#125;
        <span class="hljs-attr">onFinish</span>=<span class="hljs-string">&#123;(v)</span> =></span> &#123;
          message.success(JSON.stringify(v));
        &#125;&#125;
      >
        <span class="hljs-tag"><<span class="hljs-name">FormRender</span> <span class="hljs-attr">layoutData</span>=<span class="hljs-string">&#123;oneRowLayout&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">FormRender</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Form</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">StyledOneRow</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> OneCol;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>一行多列布局</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b2b039808964cd28f9a7baf70ae21a5~tplv-k3u1fbpfcp-watermark.image" alt="demo2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>;
<span class="hljs-keyword">import</span> &#123; Input, Radio, Form &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> FormRender <span class="hljs-keyword">from</span> <span class="hljs-string">'antd-form-render'</span>;

<span class="hljs-keyword">const</span> StyledOneRow = styled.div<span class="hljs-string">`
  width: 800px;
`</span>;

<span class="hljs-keyword">const</span> MultipleCols = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> layout = [];
  <span class="hljs-keyword">const</span> [cols, setCols] = useState(<span class="hljs-number">4</span>);

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">11</span>; i++) &#123;
    layout.push(&#123;
      <span class="hljs-attr">type</span>: Input,
      <span class="hljs-attr">label</span>: <span class="hljs-string">`输入框<span class="hljs-subst">$&#123;i + <span class="hljs-number">1</span>&#125;</span>`</span>,
      <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'请输入'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">`name<span class="hljs-subst">$&#123;i&#125;</span>`</span>,
    &#125;);
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">StyledOneRow</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Form</span> <span class="hljs-attr">layout</span>=<span class="hljs-string">"vertical"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">margin:</span> '<span class="hljs-attr">16px</span> <span class="hljs-attr">0</span>' &#125;&#125;></span>
          <span class="hljs-tag"><<span class="hljs-name">Radio.Group</span>
            <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> setCols(Number(e.target.value))&#125;
            optionType="button"
            value=&#123;cols&#125;
          >
            <span class="hljs-tag"><<span class="hljs-name">Radio</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;1&#125;</span>></span>1行1列<span class="hljs-tag"></<span class="hljs-name">Radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Radio</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;2&#125;</span>></span>1行2列<span class="hljs-tag"></<span class="hljs-name">Radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Radio</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;3&#125;</span>></span>1行3列<span class="hljs-tag"></<span class="hljs-name">Radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Radio</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;4&#125;</span>></span>1行4列<span class="hljs-tag"></<span class="hljs-name">Radio</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">Radio.Group</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">FormRender</span> <span class="hljs-attr">layoutData</span>=<span class="hljs-string">&#123;layout&#125;</span> <span class="hljs-attr">cols</span>=<span class="hljs-string">&#123;cols&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">FormRender</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Form</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">FormRender</span> <span class="hljs-attr">layoutData</span>=<span class="hljs-string">&#123;layout&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">FormRender</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">StyledOneRow</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> MultipleCols;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>等间距排列 (常用于列表页面的搜索等)</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45f46855cad44c968f5bde33999cb0b2~tplv-k3u1fbpfcp-watermark.image" alt="demo3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>;
<span class="hljs-keyword">import</span> &#123; Input, Radio, Form &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> &#123; FormSpaceRender &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd-form-render'</span>;

<span class="hljs-keyword">const</span> StyledOneRow = styled.div<span class="hljs-string">`
  width: 1000px;
`</span>;

<span class="hljs-keyword">const</span> SpaceLayout = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> layout = [];
  <span class="hljs-keyword">const</span> [space, setSpace] = useState(<span class="hljs-number">8</span>);

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++) &#123;
    layout.push(&#123;
      <span class="hljs-attr">type</span>: Input,
      <span class="hljs-attr">label</span>: <span class="hljs-string">`输入框<span class="hljs-subst">$&#123;i + <span class="hljs-number">1</span>&#125;</span>`</span>,
      <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'请输入'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">`name<span class="hljs-subst">$&#123;i&#125;</span>`</span>,
    &#125;);
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">StyledOneRow</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Form</span> <span class="hljs-attr">layout</span>=<span class="hljs-string">"horizontal"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">margin:</span> '<span class="hljs-attr">16px</span> <span class="hljs-attr">0</span>' &#125;&#125;></span>
          <span class="hljs-tag"><<span class="hljs-name">Radio.Group</span>
            <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> setSpace(Number(e.target.value))&#125;
            optionType="button"
            value=&#123;space&#125;
          >
            <span class="hljs-tag"><<span class="hljs-name">Radio</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;8&#125;</span>></span>8px<span class="hljs-tag"></<span class="hljs-name">Radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Radio</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;16&#125;</span>></span>16px<span class="hljs-tag"></<span class="hljs-name">Radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Radio</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;24&#125;</span>></span>24px<span class="hljs-tag"></<span class="hljs-name">Radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Radio</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;32&#125;</span>></span>32px<span class="hljs-tag"></<span class="hljs-name">Radio</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">Radio.Group</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">FormSpaceRender</span> <span class="hljs-attr">layoutData</span>=<span class="hljs-string">&#123;layout&#125;</span> <span class="hljs-attr">size</span>=<span class="hljs-string">&#123;space&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">FormSpaceRender</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Form</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">StyledOneRow</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> SpaceLayout;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.表单联动</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb820b0216ca42d597f7898e404bb465~tplv-k3u1fbpfcp-watermark.image" alt="demo4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>;
<span class="hljs-keyword">import</span> &#123; Form, Button, Radio, message &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> FormRender <span class="hljs-keyword">from</span> <span class="hljs-string">'antd-form-render'</span>;

<span class="hljs-keyword">const</span> StyledOneRow = styled.div<span class="hljs-string">`
  width: 600px;
`</span>;

<span class="hljs-keyword">const</span> StyledP = styled.p<span class="hljs-string">`
  padding: 10px;
`</span>;

<span class="hljs-keyword">const</span> OneColWithDynamicControl = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [form] = Form.useForm();

  <span class="hljs-keyword">const</span> [form1] = Form.useForm();

  <span class="hljs-comment">// 用于同步表单状态</span>
  <span class="hljs-keyword">const</span> [data, setData] = useState(&#123;&#125;);

  <span class="hljs-keyword">const</span> layout = [
    &#123;
      <span class="hljs-attr">type</span>: Radio.Group,
      <span class="hljs-attr">label</span>: <span class="hljs-string">'性别'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'gender'</span>,
      <span class="hljs-attr">elProps</span>: &#123;
        <span class="hljs-attr">options</span>: [
          &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'男'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'男生'</span> &#125;,
          &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'女'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'女生'</span> &#125;,
        ],
      &#125;,
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'div'</span>,
      <span class="hljs-attr">label</span>: <span class="hljs-string">'你是'</span>,
      <span class="hljs-attr">elProps</span>: &#123;
        <span class="hljs-attr">children</span>: data.gender || <span class="hljs-string">'未选择'</span>,
      &#125;,
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: Button,
      <span class="hljs-attr">elProps</span>: &#123;
        <span class="hljs-attr">htmlType</span>: <span class="hljs-string">'submit'</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'primary'</span>,
        <span class="hljs-attr">children</span>: <span class="hljs-string">'确定'</span>,
      &#125;,
      <span class="hljs-attr">itemProps</span>: &#123;
        <span class="hljs-attr">wrapperCol</span>: &#123; <span class="hljs-attr">offset</span>: <span class="hljs-number">6</span> &#125;,
      &#125;,
    &#125;,
  ];

  <span class="hljs-comment">// 基于antd , dependency 实现表单联动</span>
  <span class="hljs-keyword">const</span> layout1 = [
    &#123;
      <span class="hljs-attr">type</span>: Radio.Group,
      <span class="hljs-attr">label</span>: <span class="hljs-string">'性别'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'gender'</span>,
      <span class="hljs-attr">elProps</span>: &#123;
        <span class="hljs-attr">options</span>: [
          &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'男'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'男生'</span> &#125;,
          &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'女'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'女生'</span> &#125;,
        ],
      &#125;,
    &#125;,
    &#123;
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Form.Item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"你是"</span> <span class="hljs-attr">dependencies</span>=<span class="hljs-string">&#123;[</span>'<span class="hljs-attr">gender</span>']&#125;></span>
            &#123;() => &#123;
              const gender = form1.getFieldValue('gender');
              return gender || '未选择';
            &#125;&#125;
          <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span></span>
        );
      &#125;,
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: Button,
      <span class="hljs-attr">elProps</span>: &#123;
        <span class="hljs-attr">htmlType</span>: <span class="hljs-string">'submit'</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'primary'</span>,
        <span class="hljs-attr">children</span>: <span class="hljs-string">'确定'</span>,
      &#125;,
      <span class="hljs-attr">itemProps</span>: &#123;
        <span class="hljs-attr">wrapperCol</span>: &#123; <span class="hljs-attr">offset</span>: <span class="hljs-number">6</span> &#125;,
      &#125;,
    &#125;,
  ];

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">StyledOneRow</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">StyledP</span>></span>1.定义onValuesChange 同步状态到state , 触发重新渲染实现表单联动<span class="hljs-tag"></<span class="hljs-name">StyledP</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Form</span>
        <span class="hljs-attr">form</span>=<span class="hljs-string">&#123;form&#125;</span>
        <span class="hljs-attr">onValuesChange</span>=<span class="hljs-string">&#123;(v)</span> =></span> &#123;
          setData((p) => (&#123; ...p, ...v &#125;));
        &#125;&#125;
        labelCol=&#123;&#123; span: 6 &#125;&#125;
        onFinish=&#123;(v) => &#123;
          message.success(JSON.stringify(v));
        &#125;&#125;
      >
        <span class="hljs-tag"><<span class="hljs-name">FormRender</span> <span class="hljs-attr">layoutData</span>=<span class="hljs-string">&#123;layout&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">FormRender</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Form</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">StyledP</span>></span>2.利用Form.Item dependencies 和自定义render 实现表单联动<span class="hljs-tag"></<span class="hljs-name">StyledP</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Form</span>
        <span class="hljs-attr">form</span>=<span class="hljs-string">&#123;form1&#125;</span>
        <span class="hljs-attr">labelCol</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">span:</span> <span class="hljs-attr">6</span> &#125;&#125;
        <span class="hljs-attr">onFinish</span>=<span class="hljs-string">&#123;(v)</span> =></span> &#123;
          message.success(JSON.stringify(v));
        &#125;&#125;
      >
        <span class="hljs-tag"><<span class="hljs-name">FormRender</span> <span class="hljs-attr">layoutData</span>=<span class="hljs-string">&#123;layout1&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">FormRender</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Form</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">StyledOneRow</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> OneColWithDynamicControl;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            