
---
title: 'flutter web 对接微信支付 JsApi'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/529af8132ef34955b3af049191db3785~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 18:47:32 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/529af8132ef34955b3af049191db3785~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">flutter web 对接微信支付</h1>
<p>flutter web 已经支持稳定版，根据公司要求，需要开发公众号，项目中需要对接微信支付，在网上看了下这类，资料比较少，so: 我整理下我调试的心得，提供给大家参考。</p>
<h4 data-id="heading-1">1. 微信公众号支付对接前提准备</h4>
<ul>
<li>申请微信商户号</li>
<li>申请微信服务号</li>
</ul>
<h4 data-id="heading-2">2. 微信公众号配置（只针对前端需要配置的）</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/529af8132ef34955b3af049191db3785~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
网页授权，主要是为了获取code ,一般为首页地址。或者支付页面地址（不推荐）</p>
<h4 data-id="heading-3">3. 支付对接整体流程</h4>
<ul>
<li>获取微信code</li>
<li>用获取到的code 请求后台Api 获取openID</li>
<li>创建订单信息</li>
<li>拉起微信支付</li>
</ul>
<h4 data-id="heading-4">4. 获取微信code</h4>
<ul>
<li>调用微信微信获取code方法,需要插件：<code>url_launcher</code> <code>url_encoder</code></li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    <span class="hljs-built_in">Uri</span> u = <span class="hljs-built_in">Uri</span>.parse(js.context[<span class="hljs-string">'location'</span>][<span class="hljs-string">'href'</span>]);
    <span class="hljs-built_in">String</span> code = u.queryParameters[<span class="hljs-string">'code'</span>]!=null?u.queryParameters[<span class="hljs-string">'code'</span>]:<span class="hljs-string">'0'</span>;
    <span class="hljs-built_in">String</span> state = u.queryParameters[<span class="hljs-string">'state'</span>]!=null?u.queryParameters[<span class="hljs-string">'state'</span>]:<span class="hljs-string">'0'</span>;

    <span class="hljs-keyword">if</span>(code ==<span class="hljs-string">'0'</span>&&state == <span class="hljs-string">'0'</span>)&#123;
      <span class="hljs-comment">// Util.showMsg('code is 0');</span>
      _getWxCode();
    &#125;<span class="hljs-keyword">else</span>&#123;
      _getOpenId(code);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-dart copyable" lang="dart">  _getWxCode() <span class="hljs-keyword">async</span>&#123;
    <span class="hljs-keyword">final</span> url = <span class="hljs-string">'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx2db21c1fd1f97062&response_type=code&scope=snsapi_base&state=1&redirect_uri=<span class="hljs-subst">$&#123;urlEncode(text: <span class="hljs-string">"https://xxx.xxxx.xxx/xxxx/xxxx"</span>)&#125;</span>#wechat_redirect'</span>;
    <span class="hljs-built_in">print</span>(url);
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">await</span> canLaunch(url)) &#123;
      <span class="hljs-keyword">await</span> launch(url);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-string">'Could not launch <span class="hljs-subst">$url</span>'</span>;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>redirect_uri:获取code授权地址，一般为<a href="https://xxx.xxxx.xxx/xxxx/xxx?code=%27xxxxx%27&state=1" target="_blank" rel="nofollow noopener noreferrer">xxx.xxxx.xxx/xxxx/xxx?co…</a>, 在获取code和配置微信公众号网页授权的时候会发现，我们flutter生成路由的url过程中，会带有<code>#/</code>标识，而我们在配置的时候，微信官会提示我们带<code>#/</code>的url不合法，我们尝试把<code>#/</code>去调发现,页面为404，所以我们要解决这个问题也就是<code>#/</code>去掉也能访问。我们把路由方式改为：Path模式<code>setUrlStrategy(PathUrlStrategy());</code>,具体请看：<a href="https://api.flutter.dev/flutter/flutter_web_plugins/PathUrlStrategy-class.html" target="_blank" rel="nofollow noopener noreferrer">api.flutter.dev/flutter/flu…</a></p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() <span class="hljs-keyword">async</span> &#123;
  WidgetsFlutterBinding.ensureInitialized();
  setUrlStrategy(PathUrlStrategy());
  <span class="hljs-keyword">await</span> SpUtil.getInstance();
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">if</span> (Platform.isAndroid) &#123;
      SystemUiOverlayStyle systemUiOverlayStyle = SystemUiOverlayStyle(
        statusBarColor: Colors.transparent,
      ).copyWith(statusBarBrightness: Brightness.dark);
      SystemChrome.setSystemUIOverlayStyle(systemUiOverlayStyle);
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;&#125;

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => TabbarSelectedIndexProvider()),
        ChangeNotifierProvider(create: (_) => UserInfoProvider()),
        ChangeNotifierProvider(create: (_) => ShoppingCartProvider()),
      ],
      child: MyApp(),
    ),
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时我们不带#/也可以访问。但是在加载<a href="https://xxx.xxxx.xxx/xxxx/xxx?code=%27xxxxx%27&state=1" target="_blank" rel="nofollow noopener noreferrer">xxx.xxxx.xxx/xxxx/xxx?co…</a>
url的时候会发现为空白页面，这个时候需要后台人员配置Nginx，让该url带参也可以访问就OK了。</p>
<h4 data-id="heading-5">5.获取openID</h4>
<pre><code class="hljs language-dart copyable" lang="dart">  _getOpenId(<span class="hljs-built_in">String</span> code) <span class="hljs-keyword">async</span>&#123;
    BaseEntity baseEntity = <span class="hljs-keyword">await</span> DioManager().postForm(AppApi.getWxOpenid,data: &#123;<span class="hljs-string">'code'</span>: code&#125;);
    <span class="hljs-keyword">if</span> (baseEntity.code == DioManager.successCode) &#123;
      openId = baseEntity.result[<span class="hljs-string">'openId'</span>];
    &#125; <span class="hljs-keyword">else</span> &#123;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">6.下单</h4>
<pre><code class="hljs language-dart copyable" lang="dart">  _weChatPayOrder(<span class="hljs-built_in">String</span> openid) <span class="hljs-keyword">async</span>&#123;
    BaseEntity baseEntity = <span class="hljs-keyword">await</span> DioManager().postForm(AppApi.weChatPayOrder,data: &#123;<span class="hljs-string">'amount'</span>: _textEditingController.text,<span class="hljs-string">'openid'</span>: openid,<span class="hljs-string">'equipment'</span>:<span class="hljs-string">'web'</span>&#125;);
    <span class="hljs-keyword">if</span> (baseEntity.code == DioManager.successCode) &#123;
    <span class="hljs-comment">///<span class="markdown">调用js代码拉起微信支付</span></span>
      <span class="hljs-keyword">var</span> request = js.context.callMethod(<span class="hljs-string">"onBridgeReady"</span>,[baseEntity.result[<span class="hljs-string">'appId'</span>],baseEntity.result[<span class="hljs-string">'timeStamp'</span>],baseEntity.result[<span class="hljs-string">'nonceStr'</span>],baseEntity.result[<span class="hljs-string">'package'</span>],baseEntity.result[<span class="hljs-string">'signType'</span>],baseEntity.result[<span class="hljs-string">'paySign'</span>]]);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'result--------><span class="hljs-subst">$&#123;baseEntity.message&#125;</span>'</span>);
      <span class="hljs-comment">/// <span class="markdown">失败</span></span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">7.编辑js代码调起微信</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85f8dec0e5354f1c933ef78ac0584f6e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onBridgeReady</span>(<span class="hljs-params">appId,timeStamp,nonceStr,package,signType,paySign</span>)</span>&#123;
   alert(<span class="hljs-string">"发起请求："</span>);<span class="hljs-comment">// 测试用flutter 是否成功调用js</span>
    WeixinJSBridge.invoke(
        <span class="hljs-string">'getBrandWCPayRequest'</span>, &#123;
            <span class="hljs-string">"appId"</span>:appId,     <span class="hljs-comment">//公众号名称，由商户传入</span>
            <span class="hljs-string">"timeStamp"</span>:timeStamp,         <span class="hljs-comment">//时间戳，自1970年以来的秒数</span>
            <span class="hljs-string">"nonceStr"</span>:nonceStr, <span class="hljs-comment">//随机串</span>
            <span class="hljs-string">"package"</span>:package,
            <span class="hljs-string">"signType"</span>:signType,         <span class="hljs-comment">//微信签名方式：</span>
            <span class="hljs-string">"paySign"</span>:paySign <span class="hljs-comment">//微信签名</span>
        &#125;,
        <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>)</span>&#123;
            <span class="hljs-keyword">if</span>(res.err_msg == <span class="hljs-string">"get_brand_wcpay_request:ok"</span> )&#123;
                <span class="hljs-comment">// 使用以上方式判断前端返回,微信团队郑重提示：</span>
                <span class="hljs-comment">//res.err_msg将在用户支付成功后返回ok，但并不保证它绝对可靠。</span>
                <span class="hljs-keyword">return</span> <span class="hljs-string">"true"</span>;
            &#125;
            <span class="hljs-keyword">else</span>
                <span class="hljs-keyword">return</span> <span class="hljs-string">"false"</span>;
        &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            