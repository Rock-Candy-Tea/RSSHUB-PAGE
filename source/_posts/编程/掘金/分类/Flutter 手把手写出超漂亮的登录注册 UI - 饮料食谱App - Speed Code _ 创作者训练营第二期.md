
---
title: 'Flutter 手把手写出超漂亮的登录注册 UI - 饮料食谱App - Speed Code _ 创作者训练营第二期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4945103816a5449fa3b2c725e9cfbffb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 01:42:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4945103816a5449fa3b2c725e9cfbffb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>我是 Zero，今天我们要用 Flutter 敲出上面👆的效果</p>
</blockquote>
<p><strong>粗略一看</strong><br>嗯🤔... 很漂亮... 很笔优特佛（<code>Beautiful</code>）👍<br><strong>再粗略一看</strong><br>🤣小老弟，你唬我呢？不就是个登录注册页面吗？<br><strong>再仔细一看</strong><br>不对😱，居然有下面👇这么多的知识点</p>
<h3 data-id="heading-0">核心知识点</h3>
<ul>
<li><a href="https://api.flutter.dev/flutter/widgets/Container-class.html" target="_blank" rel="nofollow noopener noreferrer">Container</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/Text-class.html" target="_blank" rel="nofollow noopener noreferrer">Text</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/Image-class.html" target="_blank" rel="nofollow noopener noreferrer">Image</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/Column-class.html" target="_blank" rel="nofollow noopener noreferrer">Column</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/Row-class.html" target="_blank" rel="nofollow noopener noreferrer">Row</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/Stack-class.html" target="_blank" rel="nofollow noopener noreferrer">Stack</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/SizedBox-class.html" target="_blank" rel="nofollow noopener noreferrer">SizedBox</a></li>
<li><a href="https://api.flutter.dev/flutter/material/TextField-class.html" target="_blank" rel="nofollow noopener noreferrer">TextField</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/Padding-class.html" target="_blank" rel="nofollow noopener noreferrer">Padding</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/Spacer-class.html" target="_blank" rel="nofollow noopener noreferrer">Spacer</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/Positioned-class.html" target="_blank" rel="nofollow noopener noreferrer">Positioned</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/GestureDetector-class.html" target="_blank" rel="nofollow noopener noreferrer">GestureDetector</a></li>
<li><a href="https://api.flutter.dev/flutter/material/Divider-class.html" target="_blank" rel="nofollow noopener noreferrer">Divider</a></li>
<li><a href="https://api.flutter.dev/flutter/widgets/ClipPath-class.html" target="_blank" rel="nofollow noopener noreferrer">ClipPath</a></li>
<li><a href="https://api.flutter.dev/flutter/dart-ui/Path-class.html" target="_blank" rel="nofollow noopener noreferrer">Path</a></li>
<li><a href="https://www.jasondavies.com/animated-bezier/" target="_blank" rel="nofollow noopener noreferrer">Bezier(贝塞尔曲线)</a></li>
<li>Flutter 组件抽离</li>
</ul>
<p>看完文章，点赞后再点击对应的 Widget 可直接进入 Flutter 官方文档😏，(<code>超级贴心💗</code>)<br></p>
<ul>
<li>先赞后看，更新永不断👏</li>
<li>好的，我们进入正题</li>
</ul>
<h3 data-id="heading-1">📖 项目介绍 📖</h3>
<p>这是我的第 2 个 Speed Code 视频项目文章，通过此文章你可以学习到如上 <code>Widget</code> 的<code>基础</code>或<code>进阶</code>用法，更重要的你可以学习到如何将这些 <code>Widget</code> 灵活的组合，最终实现上面👆的效果。</p>
<blockquote>
<p>如果觉得对你有帮助可以点个赞👍 ，我会更有动力录制分享更多 Flutter 优质内容，谢谢你的赞</p>
</blockquote>
<h2 data-id="heading-2">定义通用主题</h2>
<ul>
<li>大小</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">/// <span class="markdown">theme/app<span class="hljs-emphasis">_size.dart</span></span></span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-comment">// 标题文字大小</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">double</span> kTitleTextSize = <span class="hljs-number">24</span>;
<span class="hljs-comment">// 内容体文字大小</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">double</span> kBodyTextSize = <span class="hljs-number">14</span>;
<span class="hljs-comment">// 按钮文字大小</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">double</span> kBtnTextSize = <span class="hljs-number">18</span>;
<span class="hljs-comment">// 按钮圆角半径</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">double</span> kBtnRadius = <span class="hljs-number">24</span>;
<span class="hljs-comment">// 输入框边框圆角半径</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">double</span> kInputBorderRadius = <span class="hljs-number">5</span>;
<span class="hljs-comment">// icon 大小</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">double</span> kIconSize = <span class="hljs-number">24</span>;
<span class="hljs-comment">// icon 盒子大小</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">double</span> kIconBoxSize = <span class="hljs-number">56</span>;
<span class="hljs-comment">// Light 字重</span>
<span class="hljs-keyword">const</span> FontWeight kLightFontWeight = FontWeight.w300;
<span class="hljs-comment">// Medium 字重</span>
<span class="hljs-keyword">const</span> FontWeight kMediumFontWeight = FontWeight.w500;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>颜色</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">/// <span class="markdown">theme/app<span class="hljs-emphasis">_colors.dart</span></span></span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/widgets.dart'</span>;

<span class="hljs-comment">// 背景颜色</span>
<span class="hljs-keyword">const</span> Color kBgColor = Color(<span class="hljs-number">0xFFFEDCE0</span>);
<span class="hljs-comment">// 文字颜色</span>
<span class="hljs-keyword">const</span> Color kTextColor = Color(<span class="hljs-number">0xFF3D0007</span>);
<span class="hljs-comment">// 按钮开始颜色</span>
<span class="hljs-keyword">const</span> Color kBtnColorStart = Color(<span class="hljs-number">0xFFF89500</span>);
<span class="hljs-comment">// 按钮结束颜色</span>
<span class="hljs-keyword">const</span> Color kBtnColorEnd = Color(<span class="hljs-number">0xFFFA6B74</span>);
<span class="hljs-comment">// 按钮投影颜色</span>
<span class="hljs-keyword">const</span> Color kBtnShadowColor = Color(<span class="hljs-number">0x33D83131</span>);
<span class="hljs-comment">// 输入框边框颜色</span>
<span class="hljs-keyword">const</span> Color kInputBorderColor = Color(<span class="hljs-number">0xFFECECEC</span>);

<span class="hljs-comment">// 按钮渐变背景色</span>
<span class="hljs-keyword">const</span> LinearGradient kBtnLinearGradient = LinearGradient(
  colors: [
    kBtnColorStart,
    kBtnColorEnd,
  ],
);

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>样式</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">/// <span class="markdown">theme/app<span class="hljs-emphasis">_style.dart</span></span></span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/widgets.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'app_colors.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'app_size.dart'</span>;

<span class="hljs-comment">// 按钮投影</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">List</span><BoxShadow> kBtnShadow = [
  BoxShadow(
    color: kBtnShadowColor,
    offset: Offset(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>),
    blurRadius: <span class="hljs-number">20</span>,
  )
];

<span class="hljs-comment">// 按钮文字样式</span>
<span class="hljs-keyword">const</span> TextStyle kBtnTextStyle = TextStyle(
  color: kBtnColorStart,
  fontSize: kBtnTextSize,
  fontWeight: kMediumFontWeight,
);

<span class="hljs-comment">// 标题文字样式</span>
<span class="hljs-keyword">const</span> TextStyle kTitleTextStyle = TextStyle(
  fontSize: kTitleTextSize,
  color: kTextColor,
  fontWeight: kMediumFontWeight,
);

<span class="hljs-comment">// 内容文字样式</span>
<span class="hljs-keyword">const</span> TextStyle kBodyTextStyle = TextStyle(
  fontSize: kBodyTextSize,
  color: kTextColor,
  fontWeight: kLightFontWeight,
);

<span class="hljs-comment">// 输入框边框</span>
OutlineInputBorder kInputBorder = OutlineInputBorder(
  borderRadius: BorderRadius.circular(<span class="hljs-number">5</span>),
  borderSide: BorderSide(
    color: kInputBorderColor,
    width: <span class="hljs-number">1</span>,
  ),
);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">构建欢迎页面</h2>
<h3 data-id="heading-4">绘制头部内容</h3>
<ul>
<li>1、绘制头部背景</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// WelBgHeader</span>
Image.asset(
  <span class="hljs-string">'assets/images/bg_welcome_header.png'</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4945103816a5449fa3b2c725e9cfbffb~tplv-k3u1fbpfcp-zoom-1.image" alt="img_01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>2、绘制 App Icon</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// AppIconWidget</span>
Container(
  width: kIconBoxSize,
  height: kIconBoxSize,
  decoration: BoxDecoration(
    color: Colors.white,
    shape: BoxShape.circle,
  ),
  alignment: Alignment.center,
  child: Image.asset(
    <span class="hljs-string">'assets/icons/app_icon.png'</span>,
    width: <span class="hljs-number">24</span>,
    height: <span class="hljs-number">32</span>,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e62013eee6484ddfa38d9f0d7372dafc~tplv-k3u1fbpfcp-zoom-1.image" alt="img_02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>3、绘制 Icon 下的文字</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">/// <span class="markdown">Icon Text</span></span>
Positioned(
  top: <span class="hljs-number">194</span>,
  left: <span class="hljs-number">40</span>,
  child: Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      AppIconWidget(),
      SizedBox(height: <span class="hljs-number">8</span>),
      Text(
        <span class="hljs-string">'Sour'</span>,
        style: kTitleTextStyle,
      ),
      SizedBox(height: <span class="hljs-number">8</span>),
      Text(
        <span class="hljs-string">'Best drink\nreceipes'</span>,
        style: kBodyTextStyle,
      ),
    ],
  ),
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecd77bb4576c4dfcb8be5d87e927cdbb~tplv-k3u1fbpfcp-zoom-1.image" alt="img_03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4、设置整体背景色</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">/// <span class="markdown">WelcomePage</span></span>
Scaffold(
  backgroundColor: kBgColor,
  body: Column(
    children: [
      WelcomeHeaderWidget(),
    ],
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77e667b727cd46c09db30be0755971fc~tplv-k3u1fbpfcp-zoom-1.image" alt="img_04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">绘制底部内容</h3>
<blockquote>
<p>仔细看注释，很重要</p>
</blockquote>
<ul>
<li>1、绘制按钮渐变色背景</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 按钮渐变背景色</span>
<span class="hljs-keyword">const</span> LinearGradient kBtnLinearGradient = LinearGradient(
  colors: [
    kBtnColorStart,
    kBtnColorEnd,
  ],
);
<span class="hljs-comment">// 按钮投影</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">List</span><BoxShadow> kBtnShadow = [
  BoxShadow(
    color: kBtnShadowColor,
    offset: Offset(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>),
    blurRadius: <span class="hljs-number">20</span>,
  )
];
<span class="hljs-comment">// 渐变色按钮</span>
<span class="hljs-comment">// GradientBtnWidget</span>
SizedBox(
  width: width,
  height: <span class="hljs-number">48</span>,
  child: GestureDetector(
    onTap: onTap,
    child: Container(
      decoration: BoxDecoration(
        <span class="hljs-comment">// 设置渐变色</span>
        gradient: kBtnLinearGradient,
        <span class="hljs-comment">// 设置投影</span>
        boxShadow: kBtnShadow,
    <span class="hljs-comment">// 设置圆角半径</span>
        borderRadius: BorderRadius.circular(kBtnRadius),
      ),
      alignment: Alignment.center,
      child: child,
    ),
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2、绘制文字</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 按钮文字样式</span>
<span class="hljs-keyword">const</span> TextStyle kBtnTextStyle = TextStyle(
  color: kBtnColorStart,
  fontSize: kBtnTextSize,
  fontWeight: kMediumFontWeight,
);
<span class="hljs-comment">// 白色按钮文字</span>
<span class="hljs-comment">// BtnTextWhiteWidget</span>
Text(
  text,
  style: kBtnTextStyle.copyWith(
    color: Colors.white,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3、组合</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// Sign up 按钮</span>
GradientBtnWidget(
  width: <span class="hljs-number">208</span>,
  child: BtnTextWhiteWidget(text: <span class="hljs-string">'Sign up'</span>),
  onTap: () &#123;&#125;,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2c8d78c89dd43f6b40796506c98112a~tplv-k3u1fbpfcp-zoom-1.image" alt="img_05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4、绘制登录按钮</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// LoginBtnWidget</span>
Container(
  height: <span class="hljs-number">48</span>,
  width: <span class="hljs-number">208</span>,
  decoration: BoxDecoration(
    <span class="hljs-comment">// 设置白色</span>
    color: Colors.white,
    <span class="hljs-comment">// 设置圆角半径</span>
    borderRadius: BorderRadius.circular(kBtnRadius),
    <span class="hljs-comment">// 设置投影</span>
    boxShadow: kBtnShadow,
  ),
  alignment: Alignment.center,
  child: Text(
    <span class="hljs-string">'Login'</span>,
    style: kBtnTextStyle,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9946368049e84d1abc04d8632ca88156~tplv-k3u1fbpfcp-zoom-1.image" alt="img_06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>5、添加忘记密码文字</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 忘记密码</span>
Text(
  <span class="hljs-string">'Forgot password?'</span>,
  style: TextStyle(
    fontSize: <span class="hljs-number">18</span>,
    color: kTextColor,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>6、绘制底部社交媒体第三方登录</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">
<span class="hljs-comment">// 登录方式图标</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginTypeIconWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> LoginTypeIconWidget(&#123;
    Key key,
    <span class="hljs-keyword">this</span>.icon,
  &#125;) : <span class="hljs-keyword">super</span>(key: key);
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> icon;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Padding(
      padding: <span class="hljs-keyword">const</span> EdgeInsets.symmetric(horizontal: <span class="hljs-number">10</span>),
      child: Image.asset(
        icon,
        width: <span class="hljs-number">16</span>,
        height: <span class="hljs-number">16</span>,
      ),
    );
  &#125;
&#125;

<span class="hljs-comment">// 横线</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LineWidget</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> LineWidget(&#123;
    Key key,
  &#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> SizedBox(
      child: Divider(color: kTextColor),
      width: <span class="hljs-number">80</span>,
    );
  &#125;
&#125;
<span class="hljs-comment">/// <span class="markdown">组合起来</span></span>
Row(
  children: [
    Spacer(),
    LineWidget(),
    LoginTypeIconWidget(icon: <span class="hljs-string">'assets/icons/logo_ins.png'</span>),
    LoginTypeIconWidget(icon: <span class="hljs-string">'assets/icons/logo_fb.png'</span>),
    LoginTypeIconWidget(icon: <span class="hljs-string">'assets/icons/logo_twitter.png'</span>),
    LineWidget(),
    Spacer(),
  ],
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c07a724253a943e2a23ec41c6019142b~tplv-k3u1fbpfcp-zoom-1.image" alt="img_08.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">登录页面</h2>
<h3 data-id="heading-7">绘制头部区域</h3>
<ul>
<li>1、绘制背景</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">Scaffold(
  <span class="hljs-comment">// 设置背景为白色</span>
  backgroundColor: Colors.white,
  body: Stack(
    children: [
      Image.asset(
        <span class="hljs-string">'assets/images/bg_login_header.png'</span>
      ),
    ],
  ),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2、绘制返回按钮</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// BackIcon</span>
GestureDetector(
  onTap: () &#123;
    <span class="hljs-comment">// 返回</span>
    Navigator.pop(context);
  &#125;,
  child: Container(
    width: <span class="hljs-number">56</span>,
    height: <span class="hljs-number">56</span>,
    decoration: BoxDecoration(
      <span class="hljs-comment">// 白色背景</span>
      color: Colors.white,
      <span class="hljs-comment">// 设置圆形</span>
      shape: BoxShape.circle,
    ),
    <span class="hljs-comment">// 【这里很重要】设置居中</span>
    alignment: Alignment.center,
    child: Image.asset(
      <span class="hljs-string">'assets/icons/icon_back.png'</span>,
      width: <span class="hljs-number">24</span>,
      height: <span class="hljs-number">24</span>,
    ),
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61c5908a731a4158b003e6500f08ee01~tplv-k3u1fbpfcp-zoom-1.image" alt="img_10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">绘制输入区域内容</h3>
<ul>
<li>1、绘制文字</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 登录文字内容，可以看上面全局定义的样式</span>
Text(
  <span class="hljs-string">'Login'</span>,
  style: kTitleTextStyle,
),
SizedBox(height: <span class="hljs-number">20</span>),
Text(
  <span class="hljs-string">'Your Email'</span>,
  style: kBodyTextStyle,
),
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2、绘制输入框</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// LoginInput</span>
TextField(
  decoration: InputDecoration(
    <span class="hljs-comment">// 缺省文字</span>
    hintText: hintText,
    <span class="hljs-comment">// 边框</span>
    border: kInputBorder,
    focusedBorder: kInputBorder,
    enabledBorder: kInputBorder,
    <span class="hljs-comment">// 输入框前面的邮件图标</span>
    prefixIcon: Container(
      width: kIconBoxSize,
      height: kIconBoxSize,
      <span class="hljs-comment">// 【这里很重要，再次强调】不然会拉升</span>
      alignment: Alignment.center,
      child: Image.asset(
        prefixIcon,
        width: kIconSize,
        height: kIconSize,
      ),
    ),
    <span class="hljs-comment">// 设置是否为密码样式</span>
    obscureText: obscureText,
    <span class="hljs-comment">// 设置文字样式</span>
    style: kBodyTextStyle.copyWith(
      fontSize: <span class="hljs-number">18</span>,
    ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3、组合样式</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// LoginBodyWidget - Column</span>
SizedBox(height: <span class="hljs-number">4</span>),
LoginInput(
  hintText: <span class="hljs-string">'Email'</span>,
  prefixIcon: <span class="hljs-string">'assets/icons/icon_email.png'</span>,
),
SizedBox(height: <span class="hljs-number">16</span>),
Text(
  <span class="hljs-string">'Your Password'</span>,
  style: kBodyTextStyle,
),
SizedBox(height: <span class="hljs-number">4</span>),
LoginInput(
  hintText: <span class="hljs-string">'Password'</span>,
  prefixIcon: <span class="hljs-string">'assets/icons/icon_pwd.png'</span>,
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eeecd67a0294375b1e97d9b3957a14e~tplv-k3u1fbpfcp-zoom-1.image" alt="img_11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4、绘制登录按钮</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 登录按钮</span>
Row(
  children: [
    Spacer(),
    <span class="hljs-comment">// 渐变背景组件</span>
    GradientBtnWidget(
      child: Row(
        children: [
          SizedBox(width: <span class="hljs-number">34</span>),
          <span class="hljs-comment">// 白色文字</span>
          BtnTextWhiteWidget(text: <span class="hljs-string">'Login'</span>),
          Spacer(),
          <span class="hljs-comment">// 向右图标</span>
          Image.asset(
            <span class="hljs-string">'assets/icons/icon_arrow_right.png'</span>,
            width: kIconSize,
            height: kIconSize,
          ),
          SizedBox(width: <span class="hljs-number">24</span>),
        ],
      ),
      width: <span class="hljs-number">160</span>,
      onTap: () &#123;
        <span class="hljs-comment">// 点击登录，这里模拟返回了</span>
        Navigator.pop(context);
      &#125;,
    ),
  ],
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d909465dce343d8884b5f0541827beb~tplv-k3u1fbpfcp-zoom-1.image" alt="img_12.png" loading="lazy" referrerpolicy="no-referrer">**</p>
<h3 data-id="heading-9">绘制曲线剪裁</h3>
<p>可以先看看这个曲线设计的整体路径，找出<code>6个控制点</code> 和 <code>4个坐标点</code><br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2d03a53bba949ed80542b6c6976eb7f~tplv-k3u1fbpfcp-zoom-1.image" alt="img_13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>p：坐标点</li>
<li>c：控制点</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 我们是用路径剪裁</span>
ClipPath(
  clipper: LoginCliper(),
  child: LoginBodyWidget(),
),

<span class="hljs-comment">// 登录页面剪裁曲线</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginCliper</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CustomClipper</span><<span class="hljs-title">Path</span>> </span>&#123;
  <span class="hljs-comment">// 第一个点</span>
  Point p1 = Point(<span class="hljs-number">0.0</span>, <span class="hljs-number">54.0</span>);
  Point c1 = Point(<span class="hljs-number">20.0</span>, <span class="hljs-number">25.0</span>);
  Point c2 = Point(<span class="hljs-number">81.0</span>, <span class="hljs-number">-8.0</span>);
  <span class="hljs-comment">// 第二个点</span>
  Point p2 = Point(<span class="hljs-number">160.0</span>, <span class="hljs-number">20.0</span>);
  Point c3 = Point(<span class="hljs-number">216.0</span>, <span class="hljs-number">38.0</span>);
  Point c4 = Point(<span class="hljs-number">280.0</span>, <span class="hljs-number">73.0</span>);
  <span class="hljs-comment">// 第三个点</span>
  Point p3 = Point(<span class="hljs-number">280.0</span>, <span class="hljs-number">44.0</span>);
  Point c5 = Point(<span class="hljs-number">280.0</span>, <span class="hljs-number">-11.0</span>);
  Point c6 = Point(<span class="hljs-number">330.0</span>, <span class="hljs-number">8.0</span>);

  <span class="hljs-meta">@override</span>
  Path getClip(Size size) &#123;
    <span class="hljs-comment">// 第四个点</span>
    Point p4 = Point(size.width, <span class="hljs-number">.0</span>);

    Path path = Path();
    <span class="hljs-comment">// 移动到起始点</span>
    path.moveTo(p1.x, p1.y);
    <span class="hljs-comment">// 第 1 段三阶贝塞尔曲线</span>
    path.cubicTo(c1.x, c1.y, c2.x, c2.y, p2.x, p2.y);
    <span class="hljs-comment">// 第 2 段三阶贝塞尔曲线</span>
    path.cubicTo(c3.x, c3.y, c4.x, c4.y, p3.x, p3.y);
    <span class="hljs-comment">// 第 3 段三阶贝塞尔曲线</span>
    path.cubicTo(c5.x, c5.y, c6.x, c6.y, p4.x, p4.y);
    <span class="hljs-comment">// 右下角</span>
    path.lineTo(size.width, size.height);
    <span class="hljs-comment">// 左下角</span>
    path.lineTo(<span class="hljs-number">0</span>, size.height);
    <span class="hljs-comment">// 闭合</span>
    path.close();
    <span class="hljs-keyword">return</span> path;
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">bool</span> shouldReclip(<span class="hljs-keyword">covariant</span> CustomClipper<Path> oldClipper) &#123;
    <span class="hljs-keyword">return</span> oldClipper.hashCode != <span class="hljs-keyword">this</span>.hashCode;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">最终效果</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/999089c97cb446509622a77f2e6b0bd7~tplv-k3u1fbpfcp-zoom-1.image" alt="img_14.png" loading="lazy" referrerpolicy="no-referrer"><br></p>
<h2 data-id="heading-11">源码</h2>
<blockquote>
<p>base 分支：定义了基础全局样式、图片，自己练习使用
master 分支：视频内容对应的完整代码</p>
</blockquote>
<ul>
<li><a href="https://github.com/yy1300326388/flutter_drink_login_app" target="_blank" rel="nofollow noopener noreferrer">GitHub-flutter_drink_login_app（居然提供源码，我反手就是一个 Star）</a></li>
</ul>
<h2 data-id="heading-12">视频</h2>
<blockquote>
<p>建议克隆下来 base 分支代码，按照视频自己动手敲几遍，才可以变成自己的东西
动手实战是快速学习的最好方法</p>
</blockquote>
<ul>
<li><a href="https://www.bilibili.com/video/BV1zK4y1o75R/" target="_blank" rel="nofollow noopener noreferrer">BiliBili-(视频内容首发站点）</a></li>
</ul>
<h2 data-id="heading-13">关于我</h2>
<ul>
<li>15 年～18 年，使用 <code>Android</code> 原生做智能硬件相关的  App 研发</li>
<li>18 年 5 月，一次偶然的机会接触到了 <code>Flutter</code> ，然后开始自学，可以看 <a href="https://github.com/yy1300326388/weather_flutter" target="_blank" rel="nofollow noopener noreferrer">weather_flutter</a> 是我练习 Flutter 的入门实战项目（我现在依然觉得他非常适合 Flutter 入门练习使用）</li>
<li>18 年 8 月，顶着巨大的压力（Flutter 当时还没有 Release 1.0）开始使用 Flutter 开发企业级项目，并且开发维护了十几个 Flutter 插件包（因为当时插件资源非常的匮乏）</li>
<li>截止目前主导并参与上线了 4 款企业级 <code>Flutter</code> App，当前正在负责的一款 App 累计用户 <code>120W+</code>，使用 <code>Flutter</code> 得到了极佳的体验</li>
</ul>
<h2 data-id="heading-14">致谢</h2>
<ul>
<li>感谢 <code>Elizabeth Arostegui</code> 提供的非常漂亮的设计图，这是她的 <a href="https://www.figma.com/@coloripop" target="_blank" rel="nofollow noopener noreferrer">Figma 主页</a></li>
<li>如果你也有很棒的设计图，那么可以联系我制作出 App 分享给大家</li>
</ul>
<h2 data-id="heading-15">🎁 掘金官方活动 🎁</h2>
<ul>
<li>推荐<code>本文</code>到沸点，<code>掘金徽章、100元京东卡、掘金搪瓷杯、五折小册码</code>，好礼拿不停</li>
<li><a href="https://juejin.cn/post/6953434669589200903" target="_blank">查看活动详情</a></li>
</ul>
<h3 data-id="heading-16">本文推荐语示例</h3>
<ul>
<li>示例 1</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">【好文一起看】为这篇文章点赞👍👍👍，有很多 Flutter Widget 的基础和进阶用法，把这些 Widget 灵活巧妙的组合在一起，完成了超级漂亮的欢迎、登录页面，快和我一起来围观吧 #好文推荐#
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>示例 2</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">【好文一起看】在 Flutter 上贝塞尔曲线居然可以这么简单了🙀，文章超详细的注释和配图，让我很轻松就理解了优美的贝塞尔曲线剪裁，最重要还附带视频和源码，强烈推荐 👍👍👍 #好文推荐#
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其他推荐语，由你尽情发挥吧</p>
</blockquote>
<blockquote>
<p>👏 欢迎点赞➕关注➕转发，有任何问题随时在下面👇评论，我会第一时间回复哦</p>
</blockquote></div>  
</div>
            