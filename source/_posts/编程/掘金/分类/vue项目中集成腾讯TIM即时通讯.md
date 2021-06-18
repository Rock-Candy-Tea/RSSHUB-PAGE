
---
title: 'vue项目中集成腾讯TIM即时通讯'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61e33cf304be43e48a766202c31cf8b2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 23:28:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61e33cf304be43e48a766202c31cf8b2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">上图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61e33cf304be43e48a766202c31cf8b2~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bdc480e1cd2491388bba21b976888e1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">前言</h2>
<p>项目需要做个客服功能，用户端小程序，客服人员web端，于是用到了腾讯的tim</p>
<h2 data-id="heading-2">准备工作</h2>
<ol>
<li>
<p>在腾讯云官网上创建应用，获取到相应的SDKAppID和相应的秘钥信息</p>
</li>
<li>
<p>安装SDK</p>
</li>
</ol>
<p>（1） web项目使用命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// IM Web SDK</span>
npm install tim-js-sdk --save
<span class="hljs-comment">// 发送图片、文件等消息需要的 COS SDK</span>
npm install cos-js-sdk-v5 --save

<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2） 小程序项目使用命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// IM 小程序 SDK</span>
npm install tim-wx-sdk --save
<span class="hljs-comment">// 发送图片、文件等消息需要的 COS SDK</span>
npm install cos-wx-sdk-v5 --save

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>
<p>main.js中引入</p>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> TIM <span class="hljs-keyword">from</span> <span class="hljs-string">'tim-js-sdk'</span>;
<span class="hljs-comment">// import TIM from 'tim-wx-sdk'; // 微信小程序环境请取消本行注释，并注释掉 import TIM from 'tim-js-sdk';</span>
<span class="hljs-keyword">import</span> COS <span class="hljs-keyword">from</span> <span class="hljs-string">'cos-js-sdk-v5'</span>;
<span class="hljs-comment">// import COS from 'cos-wx-sdk-v5'; // 微信小程序环境请取消本行注释，并注释掉 import COS from 'cos-js-sdk-v5';</span>

<span class="hljs-comment">// 创建 SDK 实例，TIM.create() 方法对于同一个 SDKAppID 只会返回同一份实例</span>
<span class="hljs-keyword">let</span> options = &#123;
  <span class="hljs-attr">SDKAppID</span>: <span class="hljs-number">0</span> <span class="hljs-comment">// 接入时需要将0替换为您的即时通信应用的 SDKAppID</span>
&#125;;
<span class="hljs-keyword">let</span> tim = TIM.create(options); <span class="hljs-comment">// SDK 实例通常用 tim 表示</span>
<span class="hljs-comment">// 设置 SDK 日志输出级别，详细分级请参见 setLogLevel 接口的说明</span>
tim.setLogLevel(<span class="hljs-number">0</span>); <span class="hljs-comment">// 普通级别，日志量较多，接入时建议使用</span>
<span class="hljs-comment">// tim.setLogLevel(1); // release级别，SDK 输出关键信息，生产环境时建议使用</span>

<span class="hljs-comment">// 将腾讯云对象存储服务 SDK （以下简称 COS SDK）注册为插件，IM SDK 发送文件、图片等消息时，需要用到腾讯云的 COS 服务</span>
wx.$app = tim
wx.$app.registerPlugin(&#123;<span class="hljs-string">'cos-wx-sdk'</span>: COS&#125;)
wx.store = store
wx.TIM = TIM
 wx.dayjs = dayjs
 dayjs.locale(<span class="hljs-string">'zh-cn'</span>)
<span class="hljs-keyword">let</span> $bus = <span class="hljs-keyword">new</span> Vue()
Vue.prototype.TIM = TIM
Vue.prototype.$type = TYPES
Vue.prototype.$store = store
Vue.prototype.$bus = $bus
<span class="hljs-comment">// 监听事件 收到离线消息和会话列表同步完毕通知</span>
tim.on(TIM.EVENT.SDK_READY, onReadyStateUpdate, <span class="hljs-built_in">this</span>)
<span class="hljs-comment">// 收到SDK进入not ready状态通知,此时SDK无法正常工作</span>
tim.on(TIM.EVENT.SDK_NOT_READY, onReadyStateUpdate, <span class="hljs-built_in">this</span>)
<span class="hljs-comment">// 收到被踢下线通知</span>
tim.on(TIM.EVENT.KICKED_OUT, kickOut, <span class="hljs-built_in">this</span>)
<span class="hljs-comment">// 出错统一处理</span>
tim.on(TIM.EVENT.ERROR, onError, <span class="hljs-built_in">this</span>)
<span class="hljs-comment">// 收到推送的消息,遍历event.data获取消息列表数据并渲染到页面</span>
tim.on(TIM.EVENT.MESSAGE_RECEIVED, messageReceived, <span class="hljs-built_in">this</span>)
<span class="hljs-comment">// 更新会话列表</span>
tim.on(TIM.EVENT.CONVERSATION_LIST_UPDATED, convListUpdate, <span class="hljs-built_in">this</span>)
<span class="hljs-comment">// 更新群组列表</span>
tim.on(TIM.EVENT.GROUP_LIST_UPDATED, groupListUpdate, <span class="hljs-built_in">this</span>)
<span class="hljs-comment">// 更新黑名单</span>
tim.on(TIM.EVENT.BLACKLIST_UPDATED, blackListUpdate, <span class="hljs-built_in">this</span>)
<span class="hljs-comment">// 网络状态变化</span>
tim.on(TIM.EVENT.NET_STATE_CHANGE, netStateChange, <span class="hljs-built_in">this</span>)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onReadyStateUpdate</span> (<span class="hljs-params">&#123; name &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> isSDKReady = (name === TIM.EVENT.SDK_READY)
  <span class="hljs-keyword">if</span> (isSDKReady) &#123;
  <span class="hljs-comment">//用户信息</span>
    wx.$app.getMyProfile().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      store.commit(<span class="hljs-string">'updateMyInfo'</span>, res.data)
  uni.setStorageSync(<span class="hljs-string">'name'</span>, res.data.nick);
  <span class="hljs-built_in">console</span>.log(name,<span class="hljs-string">'updateMyInfo'</span>);
    &#125;)
    <span class="hljs-comment">//黑名单列表，存入vuex中</span>
    wx.$app.getBlacklist().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      store.commit(<span class="hljs-string">'setBlacklist'</span>, res.data)
    &#125;)
  &#125;
  store.commit(<span class="hljs-string">'setSdkReady'</span>, isSDKReady)
&#125;
<span class="hljs-comment">//被踢下线函数,被踢下线之后需要设置重新登录</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">kickOut</span> (<span class="hljs-params">event</span>) </span>&#123;
  store.dispatch(<span class="hljs-string">'resetStore'</span>)
  wx.showToast(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'你已被踢下线'</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-string">'none'</span>,
    <span class="hljs-attr">duration</span>: <span class="hljs-number">1500</span>
  &#125;)
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    wx.reLaunch(&#123;
      <span class="hljs-attr">url</span>: <span class="hljs-string">'../account/login'</span>
    &#125;)
  &#125;, <span class="hljs-number">500</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onError</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-comment">// 网络错误不弹toast && sdk未初始化完全报错</span>
  <span class="hljs-keyword">if</span> (event.data.message && event.data.code && event.data.code !== <span class="hljs-number">2800</span> && event.data.code !== <span class="hljs-number">2999</span>) &#123;
    store.commit(<span class="hljs-string">'showToast'</span>, &#123;
      <span class="hljs-attr">title</span>: event.data.message,
      <span class="hljs-attr">duration</span>: <span class="hljs-number">2000</span>
    &#125;)
  &#125;
&#125;
<span class="hljs-comment">//</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkoutNetState</span> (<span class="hljs-params">state</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (state) &#123;
    <span class="hljs-keyword">case</span> TIM.TYPES.NET_STATE_CONNECTED:
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'已接入网络'</span>, <span class="hljs-attr">duration</span>: <span class="hljs-number">2000</span> &#125;
    <span class="hljs-keyword">case</span> TIM.TYPES.NET_STATE_CONNECTING:
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'当前网络不稳定'</span>, <span class="hljs-attr">duration</span>: <span class="hljs-number">2000</span> &#125;
    <span class="hljs-keyword">case</span> TIM.TYPES.NET_STATE_DISCONNECTED:
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'当前网络不可用'</span>, <span class="hljs-attr">duration</span>: <span class="hljs-number">2000</span> &#125;
    <span class="hljs-attr">default</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
  &#125;
&#125;
<span class="hljs-comment">//网络状态变化函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">netStateChange</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(event.data.state)
  store.commit(<span class="hljs-string">'showToast'</span>, checkoutNetState(event.data.state))
&#125;
<span class="hljs-comment">//消息收发</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">messageReceived</span> (<span class="hljs-params">event</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(event,<span class="hljs-string">'main.js'</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < event.data.length; i++) &#123;
    <span class="hljs-keyword">let</span> item = event.data[i]
    <span class="hljs-keyword">if</span> (item.type === TYPES.MSG_GRP_TIP) &#123;
      <span class="hljs-keyword">if</span> (item.payload.operationType) &#123;
        $bus.$emit(<span class="hljs-string">'groupNameUpdate'</span>, item.payload)
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (item.type === TYPES.MSG_CUSTOM) &#123;
      <span class="hljs-keyword">if</span> (isJSON(item.payload.data)) &#123;
        <span class="hljs-keyword">const</span> videoCustom = <span class="hljs-built_in">JSON</span>.parse(item.payload.data)
<span class="hljs-built_in">console</span>.log(item,<span class="hljs-string">'首页信息'</span>)
        <span class="hljs-keyword">if</span> (videoCustom.version === <span class="hljs-number">3</span>) &#123;
          <span class="hljs-keyword">switch</span> (videoCustom.action) &#123;
            <span class="hljs-comment">// 对方呼叫我</span>
            <span class="hljs-keyword">case</span> <span class="hljs-number">0</span>:
              <span class="hljs-keyword">if</span> (!store.getters.isCalling) &#123;
                <span class="hljs-keyword">let</span> url = <span class="hljs-string">`call?args=<span class="hljs-subst">$&#123;item.payload.data&#125;</span>&&from=<span class="hljs-subst">$&#123;item.<span class="hljs-keyword">from</span>&#125;</span>&&to=<span class="hljs-subst">$&#123;item.to&#125;</span>&&name=`</span>+uni.getStorageSync(<span class="hljs-string">'name'</span>)+<span class="hljs-string">'&&nick='</span>+<span class="hljs-string">''</span>;
<span class="hljs-built_in">console</span>.log(url,<span class="hljs-string">'url'</span>)
                wx.navigateTo(&#123;url&#125;)
              &#125; <span class="hljs-keyword">else</span> &#123;
                $bus.$emit(<span class="hljs-string">'isCalling'</span>, item)
              &#125;
              <span class="hljs-keyword">break</span>
            <span class="hljs-comment">// 对方取消</span>
            <span class="hljs-keyword">case</span> <span class="hljs-number">1</span>:
              wx.navigateBack(&#123;
                <span class="hljs-attr">delta</span>: <span class="hljs-number">1</span>
              &#125;)
              <span class="hljs-keyword">break</span>
            <span class="hljs-comment">// 对方拒绝</span>
            <span class="hljs-keyword">case</span> <span class="hljs-number">2</span>:
              $bus.$emit(<span class="hljs-string">'onRefuse'</span>)
              <span class="hljs-keyword">break</span>
            <span class="hljs-comment">// 对方不接1min</span>
            <span class="hljs-keyword">case</span> <span class="hljs-number">3</span>:
              wx.navigateBack(&#123;
                <span class="hljs-attr">delta</span>: <span class="hljs-number">1</span>
              &#125;)
              <span class="hljs-keyword">break</span>
            <span class="hljs-comment">// 对方接听</span>
            <span class="hljs-keyword">case</span> <span class="hljs-number">4</span>:
              $bus.$emit(<span class="hljs-string">'onCall'</span>, videoCustom)
              <span class="hljs-keyword">break</span>
            <span class="hljs-comment">// 对方挂断</span>
            <span class="hljs-keyword">case</span> <span class="hljs-number">5</span>:
              $bus.$emit(<span class="hljs-string">'onClose'</span>)
              <span class="hljs-keyword">break</span>
            <span class="hljs-comment">// 对方正在通话中</span>
            <span class="hljs-keyword">case</span> <span class="hljs-number">6</span>:
              $bus.$emit(<span class="hljs-string">'onBusy'</span>)
              <span class="hljs-keyword">break</span>
            <span class="hljs-attr">default</span>:
              <span class="hljs-keyword">break</span>
          &#125;
        &#125;
      &#125;
    &#125;
  &#125;
  store.dispatch(<span class="hljs-string">'onMessageEvent'</span>, event)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convListUpdate</span> (<span class="hljs-params">event</span>) </span>&#123;
  store.commit(<span class="hljs-string">'updateAllConversation'</span>, event.data)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">groupListUpdate</span> (<span class="hljs-params">event</span>) </span>&#123;
  store.commit(<span class="hljs-string">'updateGroupList'</span>, event.data)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">blackListUpdate</span> (<span class="hljs-params">event</span>) </span>&#123;
  store.commit(<span class="hljs-string">'updateBlacklist'</span>, event.data)
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">最后</h2>
<p>其余的代码不多做描述，直接看demo源码。
需要源码的可以联系本人qq:392716797</p></div>  
</div>
            