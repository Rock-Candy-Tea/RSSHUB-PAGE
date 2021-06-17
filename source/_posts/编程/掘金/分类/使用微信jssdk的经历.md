
---
title: '使用微信jssdk的经历'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be2bd19c23274d53b6eefe86e21e7352~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 23:49:24 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be2bd19c23274d53b6eefe86e21e7352~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">为什么使用jssdk</h1>
<p>最近工作业务有碰到页面需要嵌入在微信浏览器当中需要自定义分享功能，以及微信浏览页跳到对应的小程序，在网上查了写资料，好像只能借助这个完成，我个人理解是这样，那没办法了，开整！</p>
<h3 data-id="heading-1">引入使用（引入的方式看个人习惯以及项目的搭建）</h3>
<ol>
<li>方式一</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//前提是npm install weixin-js-sdk</span>
    <span class="hljs-comment">//缺陷:如果你是小程序项目考虑体积的话，这些配置不算主包核心内容，也会占用主包的体积的</span>
    <span class="hljs-keyword">const</span> wx = <span class="hljs-built_in">require</span>(<span class="hljs-string">'weixin-js-sdk'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>方式二</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">    在根目录，index.html文件 用script引入  <span class="hljs-comment">//此方案也不太建议，跟上面大同小异，如果你的项目需要借助一些第三方的包来用的话，不方便维护</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>方式三（个人觉得比较适合的方式）</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">在官网把项目拷贝到自己的项目当中，因为我做的项目属于小程序有分包机制，这些功能也是在分包开发的，所以这种方式觉得比较适合

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be2bd19c23274d53b6eefe86e21e7352~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>引入在输出一下，当你看到下图的时候表示你是引入没问题的了，这个地方注意一个巨坑-引入的版本建议在1.6.0左右了，因为我最先引入的1.3左右的版本，1.3版本很多东西都不能用，分享这些api都不支持！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3bccc377a3d49ae9bd747edaada6ed8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">初期排坑：</h3>
<p>在引用 官方文件的时候源码this问题，如果你引入报下图错误，那应该就是这个坑了，其实这也不算源码自己本身的问题，执行环境不一样，</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a63a251a07a4d29aa17809ce5e7dc06~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官网源码：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f40fd8a8d4fa4da38423dcdf7d168ec2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>把this改成window即可，因为我这样引入this应该是指向的vue的根对象的，实际源码想要的指向应该是window,如果在 全局使用 srcipt引入应该不会报这个问题！</p>
<h3 data-id="heading-3">正常使用</h3>
<p>以为引入正常那使用不就是 看看官网api就行了吗，实际好像不是这样，吐槽一下这个微信jssdk的api不是很友好，有些地方讲的也不怎么完善，建议先看一遍文档在去写，官网地址：<a href="https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html#111" target="_blank" rel="nofollow noopener noreferrer">developers.weixin.qq.com/doc/offiacc…</a></p>
<p>使用jssdk需要后台的配合，大概意思就是后台给你提供密钥，你拿到密钥配置 jssdk的config，包括配置白名单这些，都是需要做的！</p>
<pre><code class="hljs language-js copyable" lang="js">config的配置
<span class="hljs-keyword">const</span> wx = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./jweixin-1.6.0'</span>)

<span class="hljs-keyword">const</span> SERVICE_ENV = process.env.SERVICE_ENV <span class="hljs-comment">//判断环境</span>
<span class="hljs-comment">// 所有的分享渠道</span>
<span class="hljs-keyword">const</span> shareList = [
  <span class="hljs-comment">// 1.4版本分享给朋友及分享到QQ</span>
  <span class="hljs-string">'updateAppMessageShareData'</span>,
  <span class="hljs-comment">// 1.4版本分享到朋友圈及分享到QQ空间</span>
  <span class="hljs-string">'updateTimelineShareData'</span>
]
<span class="hljs-comment">// 开启debug</span>
<span class="hljs-keyword">const</span> isDebug = <span class="hljs-literal">false</span>
<span class="hljs-keyword">const</span> weixinSdk = &#123;
  <span class="hljs-function"><span class="hljs-title">finishConfig</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> url = location.href.split(<span class="hljs-string">'#'</span>)[<span class="hljs-number">0</span>] <span class="hljs-comment">//拿到当前页面url（这样拿有个缺陷，如果不是哈希表的这种方式可能拿不到）</span>
      <span class="hljs-keyword">const</span> refreshTicket = <span class="hljs-literal">false</span>
      <span class="hljs-comment">//调用后台接口，一般是需要把当前url传给后台，这一步不是我们自己后台要求的，应该是微信的后台要求的！</span>
      getSdk(&#123; url, refreshTicket &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (res.code === <span class="hljs-number">1</span>) &#123;
          <span class="hljs-keyword">const</span> wxConfig = res.data
          wx.config(&#123;
            <span class="hljs-attr">debug</span>: SERVICE_ENV === <span class="hljs-string">'production'</span> ? <span class="hljs-literal">false</span> : isDebug,
            <span class="hljs-comment">// 必填，公众号的唯一标识</span>
            <span class="hljs-attr">appId</span>: wxConfig.appId,
            <span class="hljs-comment">// 必填，生成签名的时间戳</span>
            <span class="hljs-attr">timestamp</span>: wxConfig.time || <span class="hljs-number">0</span>,
            <span class="hljs-comment">// 必填，生成签名的随机串</span>
            <span class="hljs-attr">nonceStr</span>: wxConfig.nonceStr,
            <span class="hljs-comment">// 必填，签名，见附录1</span>
            <span class="hljs-attr">signature</span>: wxConfig.signature,
            <span class="hljs-comment">// 必填，需要使用的JS接口列表</span>
            <span class="hljs-attr">jsApiList</span>: shareList || [],
            <span class="hljs-attr">openTagList</span>: [<span class="hljs-string">'wx-open-launch-weapp'</span>]
          &#125;)
          wx.ready(<span class="hljs-function">() =></span> &#123;
            resolve(wx)
          &#125;)
        &#125;
      &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>, err)
      &#125;)
    &#125;)
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> weixinSdk
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置好了 ，此时我们就可以使用了，主要用到了俩个地方，网页自定义分享，使用微信的开放标签</p>
<ol>
<li>微信网页自定义 分享，这个地方调了蛮长时间主要俩个坑，因为是本地联调，配置的时候是配置的测试环境地址，所以本地是拉不起分享，在微信开饭工具网页开发的能看到报错信息，</li>
</ol>
<p>当你看到控制台输出你配置的信息不是ok的时候 ，但是有你配置的分享信息，这个时候挂载是没有问题的，是属于 正常的因为你本地的地址调 jssdk没有配置白名单，把写的代码发到测试环境，测试即可！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79c82ef53a804954b200a75e4267dd5f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> weixinSdk <span class="hljs-keyword">from</span> <span class="hljs-string">'../components/enSdk'</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getSdk</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> wx = <span class="hljs-built_in">this</span>.wx = <span class="hljs-keyword">await</span> weixinSdk.finishConfig()
        <span class="hljs-keyword">const</span> url = location.href
        <span class="hljs-keyword">const</span> shareData = &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'xxx'</span>, <span class="hljs-comment">// 分享标题</span>
          <span class="hljs-attr">desc</span>: <span class="hljs-string">'xxx'</span>, <span class="hljs-comment">// 分享描述</span>
          <span class="hljs-attr">link</span>: url, <span class="hljs-comment">// 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致</span>
          <span class="hljs-attr">imgUrl</span>: <span class="hljs-string">'xxx'</span> <span class="hljs-comment">// 分享图标</span>
        &#125;
        wx.updateAppMessageShareData(shareData)
        wx.updateTimelineShareData(shareData)
      &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p>坑二：使用wx-open-launch-weapp开放标签，官网列子使用云函数配合的好像，当时并不适用我项目，列子地址：<a href="https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/staticstorage/jump-miniprogram.html" target="_blank" rel="nofollow noopener noreferrer">developers.weixin.qq.com/miniprogram…</a></p>
<p>我的需求大概是一个商品列表需要用到商品列表，在网上找了一些大佬使用的demo还不错，但是都不怎么使用，大部分都不是动态熏染的！
这个坑是耽误时间最久的基本上很多钟方式都试过，最好还是用了原生添加dom方式，用script包起来以后是不支持动态熏染了，试了用v-html也不行，好像必须要用script标签，试了很多次都绕不过去！</p>
<pre><code class="hljs language-js copyable" lang="js">网上列子：
<wx-open-launch-weapp
                style=<span class="hljs-string">"width:100%;display:block;height:100%;"</span>
                username=<span class="hljs-string">"微信原始id"</span>
                path=<span class="hljs-string">"'pages/index/index'"</span>>
                <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/wxtag-template"</span>></span><span class="handlebars"><span class="xml">
                  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
                  <span class="hljs-selector-class">.imgset</span> &#123;
                  <span class="hljs-attribute">width</span>:<span class="hljs-number">100%</span>;
                  <span class="hljs-attribute">height</span>:<span class="hljs-number">100%</span>;
                  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">24</span>rpx;
                  &#125;
                  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span>></span>跳转小程序<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                </span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
              </wx-open-launch-weapp>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>大概的思路就是动态创建wx-open-launch-weapp和里面你需要熏染的一些结构，我这个需求是熏染一个列表，一些图片，结构不是很复杂，在网上页看了很多人家写的，可能自己没理解到真谛把，试了都不太行， 这种最原始的方法觉得是可以的，平时项目都是vue框架用多了，感觉原生js写起来费劲，但是关键时候原生js  YYDS!</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//实战列子</span>
<span class="hljs-comment">//html结构</span>
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"test-imgs"</span>> </div>

<span class="hljs-comment">//js结构</span>
<span class="hljs-comment">//方法在后台接口返回成功赋值以后直接调用即可</span>
<span class="hljs-function"><span class="hljs-title">getTemplate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> tempDom = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.test-imgs'</span>)
        tempDom.innerHTML = <span class="hljs-string">''</span>
        <span class="hljs-comment">//拿到后台返回的数据对数据进行处理</span>
        <span class="hljs-built_in">this</span>.wonderfulActivityList.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
          <span class="hljs-keyword">const</span> gh_id = configSet.weixinId || <span class="hljs-string">'gh_xxxxxx'</span>
          <span class="hljs-keyword">const</span> scriptDom = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>)
          scriptDom.type = <span class="hljs-string">'text/wxtag-template'</span>
          scriptDom.text = <span class="hljs-string">`<div style="height:100%;width:100%;text-align:center;">
        <img src="<span class="hljs-subst">$&#123;item.adPicUrl&#125;</span>" style="width:100%;height:100%;border-radius: 12px;"/>
        </div>`</span>

          <span class="hljs-keyword">const</span> weappDom = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'wx-open-launch-weapp'</span>)
          weappDom.style = <span class="hljs-string">'width:100%;display:block;height:100%;'</span>
          weappDom.setAttribute(<span class="hljs-string">'username'</span>, gh_id)
          weappDom.setAttribute(<span class="hljs-string">'path'</span>, item.adLinkUrl || <span class="hljs-string">'pages/index/index'</span>)
          weappDom.appendChild(scriptDom)

          <span class="hljs-keyword">const</span> divDom = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
          divDom.setAttribute(<span class="hljs-string">'class'</span>, <span class="hljs-string">'recommend-img-box'</span>)
          divDom.appendChild(weappDom)

          tempDom.appendChild(divDom)
        &#125;)
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">总结：使用了微信的这个第三方小相对来说收获挺多，希望看到文章的你有些许收获，本人第一次 写文章，写的比较拉稀，但是总体方向还是在的，以前也碰到过不少坑，所以现在碰到一写问题记录下来方便自己不碰同样的坑！</h3></div>  
</div>
            