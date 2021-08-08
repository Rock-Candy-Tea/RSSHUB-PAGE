
---
title: 'Element UI Form组件二次封装，使用对象数据快速构建表单应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0862257136624d7e81e64e5034480a84~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 20:15:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0862257136624d7e81e64e5034480a84~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>支持Element ui form大部分类型，并新增了复合型输入框及表单分组功能，基于vue2版本</p>
<h5 data-id="heading-0">行内表单、复合型输入框：</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0862257136624d7e81e64e5034480a84~tplv-k3u1fbpfcp-watermark.image" alt="行内表单、复合型输入框" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-1">表单分组：</h5>
<p>数据的数据为数组
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6752aa34cd1d4f358a92c68cff6c875c~tplv-k3u1fbpfcp-watermark.image" alt="表单分组" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2">表单类型：</h5>
<p>支持的表单类型，允许在对象中设置列宽、隐藏属性
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad5c22fed8de4d1fa6a6832aec8636a9~tplv-k3u1fbpfcp-watermark.image" alt="表单类型" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">下载</h2>
<pre><code class="copyable">npm install el-form-model
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">引用</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> ElFormModel <span class="hljs-keyword">from</span> <span class="hljs-string">'el-form-model'</span>
Vue.use(ElFormModel)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">引用-默认参数(可选)</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.use(ElFormModel, &#123;
  <span class="hljs-attr">global</span>: &#123;
    <span class="hljs-attr">placeholder</span>: &#123;
      <span class="hljs-attr">input</span>: <span class="hljs-string">'请输入'</span>,
      <span class="hljs-attr">select</span>: <span class="hljs-string">'请选择'</span>
    &#125;
  &#125;,
  <span class="hljs-attr">component</span>: &#123;
    <span class="hljs-attr">form</span>: &#123;&#125;,
    <span class="hljs-attr">input</span>: &#123;
      <span class="hljs-attr">clearable</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">autocomplete</span>: &#123;
      <span class="hljs-attr">clearable</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">select</span>: &#123;
      <span class="hljs-attr">clearable</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">cascader</span>: &#123;&#125;,
    <span class="hljs-attr">date</span>: &#123;&#125;,
    <span class="hljs-attr">dates</span>: &#123;&#125;,
    <span class="hljs-attr">datetime</span>: &#123;&#125;,
    <span class="hljs-attr">month</span>: &#123;&#125;,
    <span class="hljs-attr">year</span>: &#123;&#125;,
    <span class="hljs-attr">daterange</span>: &#123;
      <span class="hljs-attr">unlinkPanels</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">rangeSeparator</span>: <span class="hljs-string">'至'</span>,
      <span class="hljs-attr">startPlaceholder</span>: <span class="hljs-string">'开始日期'</span>,
      <span class="hljs-attr">endPlaceholder</span>: <span class="hljs-string">'结束日期'</span>,
      <span class="hljs-attr">defaultTime</span>: [<span class="hljs-string">'00:00:00'</span>, <span class="hljs-string">'23:59:59'</span>]
    &#125;,
    <span class="hljs-attr">datetimerange</span>: &#123;
      <span class="hljs-attr">unlinkPanels</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">rangeSeparator</span>: <span class="hljs-string">'至'</span>,
      <span class="hljs-attr">startPlaceholder</span>: <span class="hljs-string">'开始时间'</span>,
      <span class="hljs-attr">endPlaceholder</span>: <span class="hljs-string">'结束时间'</span>,
      <span class="hljs-attr">defaultTime</span>: [<span class="hljs-string">'00:00:00'</span>, <span class="hljs-string">'23:59:59'</span>]
    &#125;,
    <span class="hljs-attr">monthrange</span>: &#123;
      <span class="hljs-attr">unlinkPanels</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">rangeSeparator</span>: <span class="hljs-string">'至'</span>,
      <span class="hljs-attr">startPlaceholder</span>: <span class="hljs-string">'开始月份'</span>,
      <span class="hljs-attr">endPlaceholder</span>: <span class="hljs-string">'结束月份'</span>,
      <span class="hljs-attr">defaultTime</span>: [<span class="hljs-string">'00:00:00'</span>, <span class="hljs-string">'23:59:59'</span>]
    &#125;,
    <span class="hljs-attr">time</span>: &#123;&#125;,
    <span class="hljs-attr">radio</span>: &#123;&#125;,
    <span class="hljs-attr">checkbox</span>: &#123;&#125;,
    <span class="hljs-attr">count</span>: &#123;&#125;,
    <span class="hljs-attr">switch</span>: &#123;&#125;,
    <span class="hljs-attr">slider</span>: &#123;&#125;,
    <span class="hljs-attr">rate</span>: &#123;&#125;,
    <span class="hljs-attr">color</span>: &#123;&#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">组件</h1>
<h3 data-id="heading-7">组件-行内</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"myForm"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"true"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">组件-列宽</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"myForm"</span>
    <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"false"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">组件-继承组件属性(Element Form Attributes)</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"myForm"</span>
    <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"false"</span>
    <span class="hljs-attr">:hide-required-asterisk</span>=<span class="hljs-string">"true"</span>
    <span class="hljs-attr">:show-message</span>=<span class="hljs-string">"true"</span>
    <span class="hljs-attr">:inline-message</span>=<span class="hljs-string">"true"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">组件-继承组件事件(Element Form Events)</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"myForm"</span>
    <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"false"</span>
    @<span class="hljs-attr">validate</span>=<span class="hljs-string">"onValidate"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">组件-执行组件事件(Element Form Methods)</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">methods: &#123;
  <span class="hljs-function"><span class="hljs-title">setForm</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$refs.myForm.onFormMethod(<span class="hljs-string">'validate'</span>, [<span class="hljs-function"><span class="hljs-params">valid</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'validate'</span>, valid)
    &#125;])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">数据</h1>
<h3 data-id="heading-13">数据-默认值、类型</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"myForm"</span>
    <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"false"</span>
    <span class="hljs-attr">:data</span>=<span class="hljs-string">"data"</span>
    <span class="hljs-attr">:items</span>=<span class="hljs-string">"items"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">myInput</span>: <span class="hljs-string">'apple'</span>,
      <span class="hljs-attr">myAutocomplete</span>: <span class="hljs-string">'banana'</span>,
      <span class="hljs-attr">mySelect</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">myCascader</span>: [<span class="hljs-string">'zhinan'</span>, <span class="hljs-string">'shejiyuanze'</span>],
      <span class="hljs-attr">myTime</span>: <span class="hljs-number">1628072756566</span>,
      <span class="hljs-attr">myDate</span>: <span class="hljs-string">'2020-01-01'</span>,
      <span class="hljs-attr">myDates</span>: [<span class="hljs-string">'2020-01-01'</span>, <span class="hljs-string">'2020-01-02'</span>],
      <span class="hljs-attr">myDatetime</span>: <span class="hljs-number">1628072756566</span>,
      <span class="hljs-attr">myMonth</span>: <span class="hljs-string">'2020-01'</span>,
      <span class="hljs-attr">myYear</span>: <span class="hljs-string">'2020'</span>,
      <span class="hljs-attr">myDateRangeStart</span>: <span class="hljs-string">'2020-01-01'</span>,
      <span class="hljs-attr">myDateRangeEnd</span>: <span class="hljs-string">'2020-12-31'</span>,
      <span class="hljs-attr">myDatetimeRangeStart</span>: <span class="hljs-number">1628072756566</span>,
      <span class="hljs-attr">myDatetimeRangeEnd</span>: <span class="hljs-number">1688072756566</span>,
      <span class="hljs-attr">myMonthRangeStart</span>: <span class="hljs-string">'2020-01'</span>,
      <span class="hljs-attr">myMonthRangeEnd</span>: <span class="hljs-string">'2020-12'</span>,
      <span class="hljs-attr">myTextarea</span>: <span class="hljs-string">'orange'</span>,
      <span class="hljs-attr">myRadio</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">myCheckbox</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>],
      <span class="hljs-attr">myCount</span>: <span class="hljs-number">3</span>,
      <span class="hljs-attr">mySwitch</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">mySlider</span>: <span class="hljs-number">56</span>,
      <span class="hljs-attr">myRate</span>: <span class="hljs-number">5</span>
    &#125;,
    <span class="hljs-attr">items</span>: [&#123; 
      <span class="hljs-attr">label</span>: <span class="hljs-string">'输入框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myInput'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>
    &#125;, &#123;
      <span class="hljs-attr">labels</span>: [<span class="hljs-string">'仅行内表单生效'</span>, <span class="hljs-string">'多个输入框'</span>],
      <span class="hljs-attr">props</span>: [<span class="hljs-string">'myInput1'</span>, <span class="hljs-string">'myInput2'</span>],
      <span class="hljs-attr">type</span>: <span class="hljs-string">'inputs'</span>
    &#125;, &#123; 
      <span class="hljs-attr">label</span>: <span class="hljs-string">'自动补全'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myAutocomplete'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'autocomplete'</span>,
      <span class="hljs-attr">fetchSuggestions</span>: <span class="hljs-built_in">this</span>.querySearch
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'下拉框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'mySelect'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'select'</span>,
      <span class="hljs-attr">options</span>: [
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'选项1'</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;,
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'选项2'</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">1</span> &#125;
      ]
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'级联选择器'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myCascader'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'cascader'</span>,
      <span class="hljs-attr">options</span>: [&#123;
        <span class="hljs-attr">value</span>: <span class="hljs-string">'zhinan'</span>,
        <span class="hljs-attr">label</span>: <span class="hljs-string">'指南'</span>,
        <span class="hljs-attr">children</span>: [&#123;
          <span class="hljs-attr">value</span>: <span class="hljs-string">'shejiyuanze'</span>,
          <span class="hljs-attr">label</span>: <span class="hljs-string">'设计原则'</span>
        &#125;]
      &#125;]
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'时间'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myTime'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'time'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'timestamp'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'日期'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myDate'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'date'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'yyyy-MM-dd'</span>
    &#125;,  &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'多个日期'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myDates'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'dates'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'yyyy-MM-dd'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'日期时间'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myDatetime'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'datetime'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'timestamp'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'月份'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myMonth'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'month'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'yyyy-MM'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'年份'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myYear'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'year'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'yyyy'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'日期范围'</span>,
      <span class="hljs-attr">props</span>: [<span class="hljs-string">'myDateRangeStart'</span>, <span class="hljs-string">'myDateRangeEnd'</span>],
      <span class="hljs-attr">type</span>: <span class="hljs-string">'daterange'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'yyyy-MM-dd'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'日期时间范围'</span>,
      <span class="hljs-attr">props</span>: [<span class="hljs-string">'myDatetimeRangeStart'</span>, <span class="hljs-string">'myDatetimeRangeEnd'</span>],
      <span class="hljs-attr">type</span>: <span class="hljs-string">'datetimerange'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'timestamp'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'月份范围'</span>,
      <span class="hljs-attr">props</span>: [<span class="hljs-string">'myMonthRangeStart'</span>, <span class="hljs-string">'myMonthRangeEnd'</span>],
      <span class="hljs-attr">type</span>: <span class="hljs-string">'monthrange'</span>,
      <span class="hljs-attr">valueFormat</span>: <span class="hljs-string">'yyyy-MM'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'长文本框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myTextarea'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'textarea'</span>,
      <span class="hljs-attr">autosize</span>: &#123;
        <span class="hljs-attr">minRows</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">maxRows</span>: <span class="hljs-number">6</span>
      &#125;
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'单选框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myRadio'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'radio'</span>,
      <span class="hljs-attr">options</span>: [
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'选项1'</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;,
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'选项2'</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">1</span> &#125;
      ]
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'多选框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myCheckbox'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'checkbox'</span>,
      <span class="hljs-attr">options</span>: [
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'选项1'</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;,
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'选项2'</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">1</span> &#125;
      ]
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'计数器'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myCount'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'count'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'开关'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'mySwitch'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'switch'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'滑块'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'mySlider'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'slider'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'评分'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myRate'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'rate'</span>
    &#125;, &#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'颜色'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myColor'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'color'</span>
    &#125;]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">数据-修改默认值</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">methods: &#123;
  <span class="hljs-function"><span class="hljs-title">setValue</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.data = &#123;
      ...this.$refs.myForm.form,
      <span class="hljs-attr">myTime</span>: +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">数据-列宽(非行内表单时生效)</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">items</span>: [&#123; 
      <span class="hljs-attr">label</span>: <span class="hljs-string">'输入框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myInput'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">width</span>: <span class="hljs-string">'50%'</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">数据-隐藏</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">items</span>: [&#123; 
      <span class="hljs-attr">label</span>: <span class="hljs-string">'输入框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myInput'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">hidden</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">数据-继承子项属性(Element Form Item Attributes)</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">items</span>: [&#123; 
      <span class="hljs-attr">label</span>: <span class="hljs-string">'输入框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myInput'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">minlength</span>: <span class="hljs-number">6</span>,
      <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'请输入...'</span>,
      <span class="hljs-attr">clearable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">prefixIcon</span>: <span class="hljs-string">'el-icon-edit'</span>,
      <span class="hljs-attr">rules</span>: [
        &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入...'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
      ]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">数据-继承子项事件(Element Form Item Events)</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">items</span>: [&#123; 
      <span class="hljs-attr">label</span>: <span class="hljs-string">'输入框'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myInput'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">events</span>: &#123;
        <span class="hljs-attr">focus</span>: <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'myInput focus'</span>, e)
        &#125;,
        <span class="hljs-attr">blur</span>: <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'myInput blur'</span>, e)
        &#125;,
        <span class="hljs-attr">change</span>: <span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'myInput change'</span>, val)
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">数据-插槽</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"false"</span>
    <span class="hljs-attr">:items</span>=<span class="hljs-string">"items"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:myCustomContent</span>></span>
      自定义内容区域
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-form-model</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">items</span>: [&#123;
      <span class="hljs-attr">label</span>: <span class="hljs-string">'自定义内容'</span>,
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myCustomContent'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'slot'</span>
    &#125;]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">数据-组别</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"myForm"</span>
    <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"false"</span>
    <span class="hljs-attr">:data</span>=<span class="hljs-string">"data"</span>
    <span class="hljs-attr">:items</span>=<span class="hljs-string">"items"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:addButton</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> 
        <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>
        <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-plus"</span>
        @<span class="hljs-attr">click</span>=<span class="hljs-string">"$refs.myForm.onAddGroup('myGroup')"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:delButton</span>=<span class="hljs-string">"&#123; item &#125;"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> 
        <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span>
        <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-minus"</span>
        <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"items.find(item => item.prop === 'myGroup').count <= 1"</span>
        @<span class="hljs-attr">click</span>=<span class="hljs-string">"$refs.myForm.onDelGroup('myGroup', item.index)"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-form-model</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">myGroup</span>: [
        &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'baidu'</span>, <span class="hljs-attr">url</span>: <span class="hljs-string">'http://www.baidu.com'</span> &#125;,
        &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'qq'</span>, <span class="hljs-attr">url</span>: <span class="hljs-string">'http://www.qq.com'</span> &#125;
      ]
    &#125;,
    <span class="hljs-attr">items</span>: [&#123;
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'addButton'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'slot'</span>,
      <span class="hljs-attr">width</span>: <span class="hljs-string">'100%'</span>,
    &#125;, &#123;
      <span class="hljs-attr">prop</span>: <span class="hljs-string">'myGroup'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'group'</span>,
      <span class="hljs-attr">children</span>: [&#123;
        <span class="hljs-attr">label</span>: <span class="hljs-string">'标题'</span>,
        <span class="hljs-attr">prop</span>: <span class="hljs-string">'title'</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-string">'calc(50% - 50px)'</span>
      &#125;, &#123;
        <span class="hljs-attr">label</span>: <span class="hljs-string">'地址'</span>,
        <span class="hljs-attr">prop</span>: <span class="hljs-string">'url'</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-string">'calc(50% - 50px)'</span>
      &#125;, &#123;
        <span class="hljs-attr">prop</span>: <span class="hljs-string">'delButton'</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'slot'</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-string">'100px'</span>
      &#125;]
    &#125;]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-21">按钮</h1>
<h3 data-id="heading-22">按钮-对象(权重：低)</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"false"</span>
    <span class="hljs-attr">:items</span>=<span class="hljs-string">"items"</span>
    <span class="hljs-attr">:buttons</span>=<span class="hljs-string">"buttons"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">buttons</span>: [&#123; 
      <span class="hljs-attr">text</span>: <span class="hljs-string">'提交'</span>,
      <span class="hljs-attr">size</span>: <span class="hljs-string">'small'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'primary'</span>,
      <span class="hljs-attr">submitEvent</span>: <span class="hljs-built_in">this</span>.onSubmit
    &#125;, &#123;
      <span class="hljs-attr">text</span>: <span class="hljs-string">'重置'</span>,
      <span class="hljs-attr">size</span>: <span class="hljs-string">'small'</span>,
      <span class="hljs-attr">resetEvent</span>: <span class="hljs-built_in">this</span>.onReset
    &#125;]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">methods: &#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">onSubmit</span>(<span class="hljs-params">event</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; type, form, valid &#125; = <span class="hljs-keyword">await</span> event()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onSubmit'</span>, type, form, valid)
  &#125;,
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">onReset</span>(<span class="hljs-params">event</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; type, form, valid &#125; = <span class="hljs-keyword">await</span> event()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onReset'</span>, type, form, valid)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">按钮-插槽(权重：高)</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-form-model</span>
    <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">:inline</span>=<span class="hljs-string">"false"</span>
    <span class="hljs-attr">:items</span>=<span class="hljs-string">"items"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:button</span>=<span class="hljs-string">"&#123; submitEvent, resetEvent &#125;"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span>
        <span class="hljs-attr">size</span>=<span class="hljs-string">"medium"</span>
      ></span>
        自定义按钮1
      <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>
        <span class="hljs-attr">size</span>=<span class="hljs-string">"medium"</span>
        @<span class="hljs-attr">click</span>=<span class="hljs-string">"onSubmit(submitEvent)"</span>
      ></span>
        提交
      <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span>
        <span class="hljs-attr">size</span>=<span class="hljs-string">"medium"</span>
        @<span class="hljs-attr">click</span>=<span class="hljs-string">"onReset(resetEvent)"</span>
      ></span>
        重置
      <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span>
        <span class="hljs-attr">size</span>=<span class="hljs-string">"medium"</span>
      ></span>
        自定义按钮2
      <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-form-model</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">methods: &#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">onSubmit</span>(<span class="hljs-params">event</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; type, form, valid &#125; = <span class="hljs-keyword">await</span> event()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onSubmit'</span>, type, form, valid)
  &#125;,
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">onReset</span>(<span class="hljs-params">event</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; type, form, valid &#125; = <span class="hljs-keyword">await</span> event()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onReset'</span>, type, form, valid)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            