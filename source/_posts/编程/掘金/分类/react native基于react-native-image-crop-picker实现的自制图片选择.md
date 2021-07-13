
---
title: 'react native基于react-native-image-crop-picker实现的自制图片选择'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29ec5d6ddfff42ecb7c47e2dcbb70a10~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 01:45:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29ec5d6ddfff42ecb7c47e2dcbb70a10~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">参考</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmarlti7%2Freact-native-image-crop-picker" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/marlti7/react-native-image-crop-picker" ref="nofollow noopener noreferrer">react-native-image-crop-picker 官方参考</a></li>
</ul>
<h1 data-id="heading-1">效果展示</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29ec5d6ddfff42ecb7c47e2dcbb70a10~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5d760af654b421a8bf6f5b210e9bac4~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">前言</h1>
<ul>
<li>使用这个react-native-image-crop-picker组件是因为这个组件功能更加强大。自带了图片剪切，IOS端视频压缩。</li>
<li>当前的实现仅能选择一张图片，通过回调的方式返回图片的信息对象。</li>
<li>返回结果实例：</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;height: <span class="hljs-number">388</span>,
mime: <span class="hljs-string">"image/png"</span>,
modificationDate: <span class="hljs-string">"1626168615000"</span>,
path: <span class="hljs-string">"file:///data/user/0/com.idance_app/cache/react-native-image-crop-picker/333.png"</span>,
size: <span class="hljs-number">399743</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">源码</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 选择图片、视频
 * 2021-7-13
 */</span>

<span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; View, TouchableOpacity, Image &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;
<span class="hljs-keyword">import</span> &#123; pxToDp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../utils/stylesKits'</span>;
<span class="hljs-keyword">import</span> Icon <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-vector-icons/FontAwesome5'</span>;
<span class="hljs-keyword">import</span> ImagePicker <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native-image-crop-picker'</span>;

interface Props &#123;
  <span class="hljs-attr">callBackImage</span>: any;
  style: any;
&#125;

<span class="hljs-keyword">const</span> Index = <span class="hljs-function">(<span class="hljs-params">props: Props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [image, setImage] = useState(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">''</span> &#125;);
  <span class="hljs-keyword">const</span> [isShow, setIsShow] = useState(<span class="hljs-literal">false</span>);

  <span class="hljs-comment">/**
   * 选择图片
   */</span>
  <span class="hljs-keyword">const</span> pickImage = <span class="hljs-function">() =></span> &#123;
    ImagePicker.openPicker(&#123;
      <span class="hljs-attr">width</span>: pxToDp(<span class="hljs-number">96</span>),
      <span class="hljs-attr">height</span>: pxToDp(<span class="hljs-number">96</span>),
      <span class="hljs-attr">mediaType</span>: <span class="hljs-string">'photo'</span>
    &#125;).then(<span class="hljs-function">(<span class="hljs-params">image</span>) =></span> &#123;
      setImage(image);
      setIsShow(<span class="hljs-literal">true</span>);
      props.callBackImage(image);
    &#125;);
  &#125;;

  <span class="hljs-keyword">const</span> pickView = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">TouchableOpacity</span>
        <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
          <span class="hljs-attr">borderStyle:</span> '<span class="hljs-attr">dashed</span>',
          <span class="hljs-attr">borderColor:</span> '<span class="hljs-attr">black</span>',
          <span class="hljs-attr">width:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">96</span>),
          <span class="hljs-attr">height:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">96</span>),
          <span class="hljs-attr">borderWidth:</span> <span class="hljs-attr">1</span>,
          <span class="hljs-attr">justifyContent:</span> '<span class="hljs-attr">center</span>',
          <span class="hljs-attr">alignItems:</span> '<span class="hljs-attr">center</span>',
          <span class="hljs-attr">borderRadius:</span> <span class="hljs-attr">0.1</span>
        &#125;&#125;
        <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;pickImage&#125;</span>
      ></span>
        <span class="hljs-tag"><<span class="hljs-name">Icon</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"plus"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">&#123;30&#125;</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"#E8E8E8"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">TouchableOpacity</span>></span></span>
    );
  &#125;;

  <span class="hljs-comment">/**
   * 缩略图展示
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-keyword">const</span> thumbnailView = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Image</span>
          <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">96</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">96</span>), <span class="hljs-attr">borderRadius:</span> <span class="hljs-attr">10</span> &#125;&#125;
          <span class="hljs-attr">source</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">uri:</span> <span class="hljs-attr">image.path</span> &#125;&#125;
        /></span>
        <span class="hljs-tag"><<span class="hljs-name">TouchableOpacity</span>
          <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">20</span>), <span class="hljs-attr">position:</span> '<span class="hljs-attr">absolute</span>', <span class="hljs-attr">top:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">-10</span>), <span class="hljs-attr">left:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">86</span>) &#125;&#125;
          <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
            setIsShow(!isShow);
            props.callBackImage(null);
          &#125;&#125;
        >
          <span class="hljs-tag"><<span class="hljs-name">Image</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">20</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">20</span>) &#125;&#125;
            <span class="hljs-attr">source</span>=<span class="hljs-string">&#123;require(</span>'@/<span class="hljs-attr">res</span>/<span class="hljs-attr">images</span>/<span class="hljs-attr">x.png</span>')&#125;
          /></span>
        <span class="hljs-tag"></<span class="hljs-name">TouchableOpacity</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    );
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;[props.style,</span> &#123; <span class="hljs-attr">width:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">110</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">110</span>) &#125;]&#125;></span>
      &#123;isShow ? thumbnailView() : pickView()&#125;
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  );
&#125;;

Index.defaultProps = &#123;
  <span class="hljs-attr">callBackImage</span>: <span class="hljs-function">() =></span> &#123;&#125;,
  <span class="hljs-attr">style</span>: &#123;&#125;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Index;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">使用实例</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//回调的方法</span>
  pickImage = <span class="hljs-function">(<span class="hljs-params">image: any</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(image);
  &#125;;

<span class="hljs-comment">//组件的使用</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Pick</span>
<span class="hljs-attr">callBackImage</span>=<span class="hljs-string">&#123;this.pickImage&#125;</span>
<span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginTop:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">20</span>), <span class="hljs-attr">marginLeft:</span> <span class="hljs-attr">pxToDp</span>(<span class="hljs-attr">15</span>) &#125;&#125;
/></span></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            