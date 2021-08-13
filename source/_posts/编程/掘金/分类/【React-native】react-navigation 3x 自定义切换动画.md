
---
title: '【React-native】react-navigation 3.x 自定义切换动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6995042083367206925'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 21:36:06 GMT
thumbnail: 'https://juejin.cn/post/6995042083367206925'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<blockquote>
<p>继我们接入了react-navigation 作为导航，并且实现android从右往左滑，那我现在又想各个页面切换的时候动画自定义，那该怎么搞？</p>
</blockquote>
<blockquote>
<p>这就需要我们对 <strong>router</strong> 的配置文件进行更改了，<strong>总体思路就是，跳转时传入一个参数（暂且叫 transitionType），然后在router文件中根据此参数来进行不同的动画跳转</strong>，废话不多说，让我们开搞</p>
</blockquote>
<hr>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 自定义动画参数，通过在跳转页面中增加 transitionType: '类型' 来进行动画设置，默认 forHorizontal（从右往左）
 * <span class="hljs-doctag">@param </span>sceneProps 路由参数获取源
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;*&#125;</span></span>
 * <span class="hljs-doctag">@constructor</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TransitionConfiguration</span>(<span class="hljs-params">sceneProps</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123;scene&#125; = sceneProps;
    <span class="hljs-keyword">const</span> &#123;route&#125; = scene;
    <span class="hljs-keyword">const</span> params = route.params || &#123;&#125;;
    <span class="hljs-keyword">const</span> transitionType = params.transitionType;
    <span class="hljs-keyword">if</span> (transitionType && transitionType !== <span class="hljs-string">''</span>) &#123;
        <span class="hljs-keyword">return</span> StackViewStyleInterpolator[transitionType];
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> StackViewStyleInterpolator.forHorizontal;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，底部的参数配置需要更改，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">transitionConfig: <span class="hljs-function">(<span class="hljs-params">sceneProps</span>) =></span> (&#123;
     <span class="hljs-comment">/**
       * 1、从右向左：  forHorizontal；
       * 2、从下向上：  forVertical；
       * 3、安卓那种的从下向上： forFadeFromBottomAndroid；
       * 4、无动画：  forInitial。
       */</span>
     <span class="hljs-attr">screenInterpolator</span>: TransitionConfiguration(sceneProps),
     &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995042083367206925" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样一来，我们跳转的时候就根据不同的参数来呈现不同的动画了。</p>
<p>使用（如下为跳转动画android从底部往上）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.props.navigation.push(<span class="hljs-string">'VersionInfo'</span>, &#123;<span class="hljs-attr">transitionType</span>: <span class="hljs-string">'forFadeToBottomAndroid'</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995042083367206925" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，目前支持的动画如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f525e07b60e4dc4a8ba05c0ceaacc89~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995042083367206925" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>如果输入不存在的参数，则默认是 forFade</strong></p>
<hr>
<p>实现效果如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1542e83062c74fcaaccd0ae07c980c71~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995042083367206925" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p> 项目地址：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsupervons%2FExploreRN" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/supervons/ExploreRN" ref="nofollow noopener noreferrer">github.com/supervons/E…</a></p></div>  
</div>
            