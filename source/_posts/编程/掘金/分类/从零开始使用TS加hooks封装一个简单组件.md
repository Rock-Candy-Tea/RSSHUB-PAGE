
---
title: '从零开始使用TS加hooks封装一个简单组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4ce1594d92148e5bcf560659526ce8e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 04:50:01 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4ce1594d92148e5bcf560659526ce8e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言：最近工作刚刚接手React项目，封装一个组件是学习React中最基础的一个部分，那么让我们动手来写一个简单的React组件吧！</h3>
<h3 data-id="heading-1">1.interface接口定义</h3>
<p>首先来看我们要实现的组件效果，如图所示，这是一个简单的展示视频速率的小组件：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4ce1594d92148e5bcf560659526ce8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
你可以给它设置各种各样的样式，比如经典的深色模式或浅色模式等。
那么它都有哪些属性呢？让我们来看一下 <strong>interface.ts</strong> 文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; TextStyle, ViewStyle &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;

<span class="hljs-keyword">export</span> interface VideoBitProps &#123;
  <span class="hljs-comment">// 容器样式</span>
  <span class="hljs-attr">containerStyle</span>: ViewStyle;
  <span class="hljs-comment">// 文字背景样式</span>
  bitTxtBoxStyle: ViewStyle;
  <span class="hljs-comment">// 速率单位样式</span>
  unitStyle: TextStyle;
  <span class="hljs-comment">// 速率样式</span>
  valueStyle: TextStyle;
  <span class="hljs-comment">// 速率(自定义)</span>
  bitValue: string | <span class="hljs-literal">undefined</span>;
  <span class="hljs-comment">// 速率单位</span>
  unit: string;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要定义了组件的如下属性：</p>















































<table><thead><tr><th>字段</th><th>说明</th><th>类型</th><th>默认值</th></tr></thead><tbody><tr><td>unit</td><td>速率单位</td><td>string</td><td>kb/s</td></tr><tr><td>bitValue</td><td>速率(自定义)</td><td>string</td><td>undefined</td></tr><tr><td>valueStyle</td><td>速率样式</td><td>TextStyle</td><td>&#123;&#125;</td></tr><tr><td>unitStyle</td><td>速率单位样式</td><td>TextStyle</td><td>&#123;&#125;</td></tr><tr><td>bitTxtBoxStyle</td><td>文字背景样式</td><td>ViewStyle</td><td>&#123;&#125;</td></tr><tr><td>containerStyle</td><td>容器样式</td><td>ViewStyle</td><td>&#123;&#125;</td></tr></tbody></table>
<h3 data-id="heading-2">2.组件实现部分</h3>
<p>先来看下整体的代码模块：
<strong>index.tsx文件</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> _ <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>;
<span class="hljs-keyword">import</span> &#123; View, Text &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;
<span class="hljs-keyword">import</span> Styles <span class="hljs-keyword">from</span> <span class="hljs-string">'./style'</span>;
<span class="hljs-keyword">import</span> TYIpcPlayerManager <span class="hljs-keyword">from</span> <span class="hljs-string">'../ty-ipc-native'</span>;
<span class="hljs-keyword">import</span> &#123; VideoBitProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./interface'</span>

<span class="hljs-keyword">const</span> VideoBit: React.FC<VideoBitProps> & &#123;
  <span class="hljs-attr">defaultProps</span>: Partial<VideoBitProps>;
&#125; = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-keyword">const</span> [bitRateValue, setBitRateValue] = useState(<span class="hljs-string">''</span>);
  <span class="hljs-keyword">const</span> &#123; containerStyle, bitTxtBoxStyle, valueStyle, unitStyle, bitValue, unit &#125; = props;
  <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
  useEffect(<span class="hljs-function">() =></span> &#123;
    convertBitRate();
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">clearInterval</span>(timer);
    &#125;;
  &#125;, []);
  <span class="hljs-keyword">const</span> convertBitRate = <span class="hljs-function">() =></span> &#123;
    getBitValue();
    timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      getBitValue();
    &#125;, <span class="hljs-number">3000</span>);
  &#125;;
  
  <span class="hljs-keyword">const</span> getBitValue = <span class="hljs-function">() =></span> &#123;
    TYIpcPlayerManager.getVideoBitRateKBPS()
      .then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (data) &#123;
          <span class="hljs-keyword">const</span> realBit = (+data).toFixed(<span class="hljs-number">0</span>);
          setBitRateValue(realBit);
        &#125;
      &#125;)
      .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">clearInterval</span>(timer);
      &#125;);
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;[Styles.videoBitContainer,</span> <span class="hljs-attr">containerStyle</span>]&#125;></span>
      &#123;(bitRateValue !== undefined) || (bitValue !== undefined )  ? (
        <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;[Styles.bitTxtBox,</span> <span class="hljs-attr">bitTxtBoxStyle</span>]&#125;></span>
          <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;[Styles.fontContainer,</span> <span class="hljs-attr">valueStyle</span>]&#125;></span>
            &#123;bitRateValue || bitValue&#125;&#123;` `&#125;
            <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;[Styles.fontContainer,</span> <span class="hljs-attr">unitStyle</span>]&#125;></span>&#123;unit&#125;<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      ) : null&#125;
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  );
&#125;;

VideoBit.defaultProps = &#123;
  <span class="hljs-attr">containerStyle</span>: &#123;&#125;,
  <span class="hljs-attr">bitTxtBoxStyle</span>: &#123;&#125;,
  <span class="hljs-attr">valueStyle</span>: &#123;&#125;,
  <span class="hljs-attr">unitStyle</span>: &#123;&#125;,
  <span class="hljs-attr">unit</span>: <span class="hljs-string">'kb/s'</span>,
  <span class="hljs-attr">bitValue</span>: <span class="hljs-literal">undefined</span>,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> VideoBit;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3.组件使用实例</h3>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> NormalTopRight = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">VideoBit</span>
        <span class="hljs-attr">bitValue</span>=<span class="hljs-string">"20"</span>
        <span class="hljs-attr">unit</span>=<span class="hljs-string">"m/s"</span>
        <span class="hljs-attr">unitStyle</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> '<span class="hljs-attr">black</span>' &#125;&#125;
        <span class="hljs-attr">containerStyle</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">position:</span> '<span class="hljs-attr">absolute</span>', <span class="hljs-attr">left:</span> <span class="hljs-attr">20</span>, <span class="hljs-attr">top:</span> <span class="hljs-attr">50</span> &#125;&#125;
      /></span></span>
    );
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4.单元测试</h3>
<p>VideoBit.test.ts 文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; shallow &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'enzyme'</span>;
<span class="hljs-keyword">import</span> VideoBit <span class="hljs-keyword">from</span> <span class="hljs-string">'../index'</span>;

describe(<span class="hljs-string">'VideoBit components'</span>, <span class="hljs-function">() =></span> &#123;
  it(<span class="hljs-string">'basic render'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> wrapper = shallow(
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">VideoBit</span> <span class="hljs-attr">containerStyle</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">position:</span> '<span class="hljs-attr">absolute</span>', <span class="hljs-attr">right:</span> <span class="hljs-attr">0</span>, <span class="hljs-attr">top:</span> <span class="hljs-attr">30</span> &#125;&#125; /></span></span>
    );
    expect(wrapper).toMatchSnapshot();
  &#125;);
  it(<span class="hljs-string">'container render'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> wrapper = shallow(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">VideoBit</span> <span class="hljs-attr">valueStyle</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> '<span class="hljs-attr">red</span>', <span class="hljs-attr">fontSize:</span> <span class="hljs-attr">24</span> &#125;&#125; /></span></span>);
    expect(wrapper).toMatchSnapshot();
  &#125;);
  it(<span class="hljs-string">'bitTxtBox render'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> wrapper = shallow(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">VideoBit</span> <span class="hljs-attr">bitTxtBoxStyle</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">100</span>, <span class="hljs-attr">height:</span> <span class="hljs-attr">30</span> &#125;&#125; /></span></span>);
    expect(wrapper).toMatchSnapshot();
  &#125;);
  it(<span class="hljs-string">'unit render'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> wrapper = shallow(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">VideoBit</span> <span class="hljs-attr">unitStyle</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> '<span class="hljs-attr">black</span>' &#125;&#125; /></span></span>);
    expect(wrapper).toMatchSnapshot();
  &#125;);
  it(<span class="hljs-string">'bit data'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> wrapper = shallow(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">VideoBit</span> <span class="hljs-attr">bitValue</span>=<span class="hljs-string">&#123;30&#125;</span> /></span></span>);
    expect(wrapper).toMatchSnapshot();
  &#125;);
  it(<span class="hljs-string">'unit data'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> wrapper = shallow(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">VideoBit</span> <span class="hljs-attr">unit</span>=<span class="hljs-string">"m/s"</span> /></span></span>);
    expect(wrapper).toMatchSnapshot();
  &#125;);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            