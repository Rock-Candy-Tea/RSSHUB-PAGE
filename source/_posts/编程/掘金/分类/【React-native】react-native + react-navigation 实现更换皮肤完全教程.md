
---
title: '【React-native】react-native + react-navigation 实现更换皮肤完全教程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dafdb76902f4b7890a7bf25774ba530~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 21:44:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dafdb76902f4b7890a7bf25774ba530~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>想实现一个更换 app 整体色调（导航头，tabBar 以及按钮）的功能，比如在晚上可以换成黑色保护眼睛，亦或者选用户自己喜欢的颜色。</p>
</blockquote>
<p><strong>先放具体的实现效果图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dafdb76902f4b7890a7bf25774ba530~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995043903258755086" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-0">整体思路</h2>
<ol>
<li>在 App.js 中，添加一个全局变量 screenProps，把颜色变量放在其中，然后再添加监听，当颜色改变时，触发监听，修改 state 中的颜色值，达到颜色重新渲染。</li>
<li>在 router 配置文件中，配置颜色从 screenProps 中获取。</li>
<li>换肤页面调用替换颜色方法，触发监听。</li>
</ol>
<h2 data-id="heading-1">核心依赖版本</h2>
<pre><code class="copyable">"react-native": "0.60.5",
"react-navigation": "^3.11.1"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995043903258755086" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-2">具体实现</h2>
<h3 data-id="heading-3">一，入口文件中添加全局变量及监听</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Created by supervons 2019/08/02
 *
 * App 入口文件
 * App entry file
 *
 * https://github.com/supervons/ExploreRN
 *
 * <span class="hljs-doctag">@format</span>
 * <span class="hljs-doctag">@flow</span>
 */</span>

<span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-comment">// 导航路由表</span>
<span class="hljs-keyword">import</span> RootStack <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/routers/index'</span>;
<span class="hljs-keyword">import</span> &#123; View, DeviceEventEmitter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">color</span>: <span class="hljs-string">'#f4511E'</span>
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 添加全局监听颜色变化</span>
    DeviceEventEmitter.addListener(<span class="hljs-string">'theme_change'</span>, <span class="hljs-function"><span class="hljs-params">params</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">color</span>: params
      &#125;);
    &#125;);
  &#125;

  render(): * &#123;
    <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">flex:</span> <span class="hljs-attr">1</span> &#125;&#125;></span>
            <span class="hljs-tag"><<span class="hljs-name">RootStack</span>
              <span class="hljs-attr">screenProps</span>=<span class="hljs-string">&#123;&#123;</span>
                <span class="hljs-attr">themeColor:</span> <span class="hljs-attr">this.state.color</span>
              &#125;&#125;
            /></span>
          <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995043903258755086" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里讲下， 是路由配置，在下一步中会修改。</p>
<h3 data-id="heading-4">二，修改 router 配置文件</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Tabs = createMaterialTopTabNavigator(
  &#123;
    <span class="hljs-attr">MainPage</span>: &#123;
      <span class="hljs-attr">screen</span>: MainPage,
      <span class="hljs-attr">navigationOptions</span>: <span class="hljs-function">(<span class="hljs-params">&#123; navigation, screenProps &#125;</span>) =></span> (&#123;
        <span class="hljs-comment">// 涉及到换肤的属性，改为 screenProps.themeColor</span>
        ...
      &#125;)
    &#125;
  &#125;)

<span class="hljs-keyword">const</span> Router = createStackNavigator(
  &#123;
    <span class="hljs-attr">Login</span>: &#123;
      <span class="hljs-comment">// 登录界面</span>
      <span class="hljs-attr">screen</span>: Login
    &#125;,
    <span class="hljs-attr">MainPage</span>: &#123;
      <span class="hljs-attr">screen</span>: Tabs
    &#125;
  &#125;,
  &#123;
    <span class="hljs-comment">// 定义配置</span>
    <span class="hljs-attr">initialRouteName</span>: <span class="hljs-string">'Login'</span>, <span class="hljs-comment">//设置初始路由为登录界面</span>
    <span class="hljs-attr">headerMode</span>: <span class="hljs-string">'screen'</span>,
    <span class="hljs-attr">defaultNavigationOptions</span>: <span class="hljs-function">(<span class="hljs-params">&#123; navigation, screenProps &#125;</span>) =></span> (&#123;
      <span class="hljs-comment">// screenProps 即可获取全局变量 themeColor</span>
      <span class="hljs-attr">headerStyle</span>: &#123;
        <span class="hljs-attr">backgroundColor</span>: screenProps.themeColor <span class="hljs-comment">// <----- 看这里</span>
      &#125;,
      <span class="hljs-attr">headerTintColor</span>: <span class="hljs-string">'#ffffff'</span>,
      <span class="hljs-attr">headerTitleStyle</span>: &#123;
        <span class="hljs-attr">fontWeight</span>: <span class="hljs-string">'bold'</span>
      &#125;
    &#125;)
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995043903258755086" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">三，在页面调用方法，触发监听</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">DeviceEventEmitter.emit(<span class="hljs-string">'theme_change'</span>, <span class="hljs-string">'black'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995043903258755086" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是的，你没看错，一行代码就触发了换肤。</p>
<p>当然，如果你想保留换肤，还需要存储到后台数据库，然后下次在用户进入 app 从后台拉取配置，就达到了永久换肤了。</p>
<hr>
<h3 data-id="heading-6">项目地址</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsupervons%2FExploreRN" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/supervons/ExploreRN" ref="nofollow noopener noreferrer">github.com/supervons/E…</a>，欢迎关注 star~</p></div>  
</div>
            