
---
title: '_SSD系列_ 共享桌面，3分钟自己实现一个吧，还送麦克风声音哦'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f384dd2534d1408583891fcf81003fb8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 18:10:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f384dd2534d1408583891fcf81003fb8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>关于【SSD系列】：<br>
<strong>前端一些有意思的内容，旨在3-10分钟里， 500-1000字，有所获，又不为所累。</strong><br>
共享桌面程序，哇，高大尚耶！其实不然，让我带你3分钟实现桌面共享程序，还能听到对面说话哦。</p>
<h2 data-id="heading-1">效果演示和源码</h2>
<p>两个Tab标签，一个是分享者，一个是观众。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiangwenhu%2FjuejinBlogsCodes%2Ftree%2Fmaster%2FshareYourDesktop" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiangwenhu/juejinBlogsCodes/tree/master/shareYourDesktop" ref="nofollow noopener noreferrer">分享桌面源码</a><br>
<strong>顺便问一下，怎么把声音保存到gif图里面去？？？？</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f384dd2534d1408583891fcf81003fb8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="deskShare.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">思路</h2>
<pre><code class="hljs language-js copyable" lang="js">
用户<span class="hljs-number">1</span> ==> Screen Capture API  ===>  Web RTC  ===>  User2 Video 标签播放

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其核心 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen_Capture_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Screen_Capture_API" ref="nofollow noopener noreferrer">Screen Capture API</a> +  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWebRTC_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WebRTC_API" ref="nofollow noopener noreferrer">WebRTC API</a>, 我们一起来了解一波。</p>
<h2 data-id="heading-3"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen_Capture_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Screen_Capture_API" ref="nofollow noopener noreferrer">Screen Capture API</a> - 屏幕捕捉API</h2>
<p>MDN解释：</p>
<blockquote>
<p>屏幕捕获API，对现有的媒体捕获和流API进行了补充，让用户选择一个屏幕或屏幕的一部分（如一个窗口）作为媒体流进行捕获。然后，该流可以被记录或通过网络与他人共享。</p>
</blockquote>
<p>先看动态，再看代码：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed6481e886f14a9aa30c931dc7b31e71~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="desk1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>仅仅只需 <code>10</code> 余行代码，就可以把桌面展示在网页面里面是不是很酷。</p>
<pre><code class="hljs language-js copyable" lang="js">    <video id=<span class="hljs-string">"deskVideo"</span> autoplay controls></video>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        (<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">captureDesk</span>(<span class="hljs-params"></span>) </span>&#123;
            deskVideo.srcObject = <span class="hljs-keyword">await</span> navigator.mediaDevices.getDisplayMedia(&#123;
                <span class="hljs-attr">video</span>: &#123;
                    <span class="hljs-attr">cursor</span>: <span class="hljs-string">"always"</span>
                &#125;,
                <span class="hljs-attr">audio</span>: <span class="hljs-literal">false</span>
            &#125;);
        &#125;)();
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWebRTC_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WebRTC_API" ref="nofollow noopener noreferrer">Web RTC</a></h2>
<p>MDN</p>
<blockquote>
<p><strong>WebRTC</strong> (Web Real-Time Communications) 是一项实时通讯技术，它允许网络应用或者站点，在不借助中间媒介的情况下，建立浏览器之间点对点（Peer-to-Peer）的连接，实现视频流和（或）音频流或者其他任意数据的传输。</p>
</blockquote>
<p>我们明白其是点对点传输技术，解决传输问题就行。</p>
<h2 data-id="heading-5">实现</h2>
<p>遵循SSD系列的准则： 3-10分钟里， 500-1000字，有所获，又不为所累。
我自行实现，字数会超，而且还要有中转服务器。罢了，借助声网吧。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.agora.io%2Fcn" target="_blank" rel="nofollow noopener noreferrer" title="https://www.agora.io/cn" ref="nofollow noopener noreferrer">声网 agora</a>, 为什么是他，因为他一个月免费 <strong>10000</strong> 分钟， 做测试和个人使用是完全够了的。 其底层的基本原理上面已经说过了，核心就是
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen_Capture_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Screen_Capture_API" ref="nofollow noopener noreferrer">Screen Capture API</a> + <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWebRTC_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WebRTC_API" ref="nofollow noopener noreferrer">Web RTC</a>。</p>
<p>当然声网还支持摄像头，麦克风等等其他流的推送，摄像头和麦克风是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDevices" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices" ref="nofollow noopener noreferrer">MediaDevices</a>相关的内容不做过多的解释。</p>
<h3 data-id="heading-6">注册账号</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsso.agora.io%2Fcn%2Fv4%2Fsignup" target="_blank" rel="nofollow noopener noreferrer" title="https://sso.agora.io/cn/v4/signup" ref="nofollow noopener noreferrer">声网管理台登录或者注册</a>，链接地址已给，自行操作即可。</p>
<h3 data-id="heading-7">创建应用</h3>
<p>详情参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.agora.io%2Fcn%2FInteractive%2520Broadcast%2Frun_demo_live_web%3Fplatform%3DWeb" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.agora.io/cn/Interactive%20Broadcast/run_demo_live_web?platform=Web" ref="nofollow noopener noreferrer">跑通示例项目</a>, 里面有详细的步骤教你创建应用，以及获得<strong>AppID</strong>和<strong>Token</strong></p>
<h3 data-id="heading-8">SDK下载</h3>
<p>去这里下载 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.agora.io%2Fcn%2FAll%2Fdownloads%3Fplatform%3DWeb" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.agora.io/cn/All/downloads?platform=Web" ref="nofollow noopener noreferrer">Agora SDK下载</a></p>
<h3 data-id="heading-9">分享者代码编写</h3>
<p>这里有一个参数理解一下：</p>
<ol>
<li>appId： 应用ID</li>
<li>channel:  渠道，你可以理解为房间</li>
<li>token：票证</li>
<li>uid: 用户ID</li>
<li>role: 用户角色，有主播和观众两种</li>
</ol>
<p>核心代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">startBasicLive</span>(<span class="hljs-params"></span>) </span>&#123;
    rtc.client = AgoraRTC.createClient(&#123; <span class="hljs-attr">mode</span>: <span class="hljs-string">"live"</span>, <span class="hljs-attr">codec</span>: <span class="hljs-string">"vp8"</span> &#125;); <span class="hljs-comment">// 初始化客户端</span>
    rtc.client.setClientRole(options.role);  <span class="hljs-comment">// 设置角色</span>

    <span class="hljs-keyword">const</span> uid = <span class="hljs-keyword">await</span> rtc.client.join(options.appId, options.channel, options.token, options.uid);       
    rtc.localAudioTrack = <span class="hljs-keyword">await</span> AgoraRTC.createMicrophoneAudioTrack(); <span class="hljs-comment">// 麦克风</span>
    rtc.localVideoTrack = <span class="hljs-keyword">await</span> AgoraRTC.createScreenVideoTrack();  <span class="hljs-comment">// 桌面</span>

    <span class="hljs-comment">// 将这些音视频轨道对象发布到频道中。</span>
    <span class="hljs-keyword">await</span> rtc.client.publish([rtc.localAudioTrack, rtc.localVideoTrack]);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"publish success!"</span>);
&#125;
btnShareDesk.onclick = startBasicLive; <span class="hljs-comment">// 注册点击事件</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">观众端代码编写</h3>
<p>核心代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">startBasicLive</span>(<span class="hljs-params"></span>) </span>&#123;
    rtc.client = AgoraRTC.createClient(&#123; <span class="hljs-attr">mode</span>: <span class="hljs-string">"live"</span>, <span class="hljs-attr">codec</span>: <span class="hljs-string">"vp8"</span> &#125;);
    rtc.client.setClientRole(options.role);

    rtc.client.on(<span class="hljs-string">"user-published"</span>, <span class="hljs-keyword">async</span> (user, mediaType) => &#123;
         <span class="hljs-comment">// 开始订阅远端用户。</span>
        <span class="hljs-keyword">await</span> rtc.client.subscribe(user, mediaType);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"subscribe success"</span>, mediaType);

        <span class="hljs-comment">// 表示本次订阅的是视频。</span>
        <span class="hljs-keyword">if</span> (mediaType === <span class="hljs-string">"video"</span>) &#123;
            <span class="hljs-comment">// 订阅完成后，从 `user` 中获取远端视频轨道对象。</span>
            <span class="hljs-keyword">const</span> remoteVideoTrack = user.videoTrack;
            <span class="hljs-comment">// 动态插入一个 DIV 节点作为播放远端视频轨道的容器。</span>
            <span class="hljs-keyword">const</span> playerContainer = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
            <span class="hljs-comment">// 给这个 DIV 节点指定一个 ID，这里指定的是远端用户的 UID。</span>
            playerContainer.id = user.uid.toString();
            playerContainer.style.width = <span class="hljs-string">"640px"</span>;
            playerContainer.style.height = <span class="hljs-string">"480px"</span>;
            <span class="hljs-built_in">document</span>.body.append(playerContainer);

            <span class="hljs-comment">// 订阅完成，播放远端音视频。</span>
            <span class="hljs-comment">// 传入 DIV 节点，让 SDK 在这个节点下创建相应的播放器播放远端视频。</span>
            remoteVideoTrack.play(playerContainer);
        &#125;

        <span class="hljs-comment">// 表示本次订阅的是音频。</span>
        <span class="hljs-keyword">if</span> (mediaType === <span class="hljs-string">"audio"</span>) &#123;
            <span class="hljs-comment">// 订阅完成后，从 `user` 中获取远端音频轨道对象。</span>
            <span class="hljs-keyword">const</span> remoteAudioTrack = user.audioTrack;
            <span class="hljs-comment">// 播放音频因为不会有画面，不需要提供 DOM 元素的信息。</span>
            remoteAudioTrack.play();
        &#125;
    &#125;);   
    <span class="hljs-keyword">const</span> uid = <span class="hljs-keyword">await</span> rtc.client.join(options.appId, options.channel, options.token, <span class="hljs-literal">null</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"uid"</span>, uid);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">demo完整的代码</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiangwenhu%2FjuejinBlogsCodes%2Ftree%2Fmaster%2FshareYourDesktop" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiangwenhu/juejinBlogsCodes/tree/master/shareYourDesktop" ref="nofollow noopener noreferrer">分享桌面源码</a></p>
<h3 data-id="heading-12">小结</h3>
<p>是不是很简单，一切都看起来没那么难，这样，你才容易入坑啊。</p>
<h2 data-id="heading-13">写在最后</h2>
<p>写作不易，你的一赞一评就是我前行的最大动力。</p>
<h2 data-id="heading-14">参考引用</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWebRTC_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WebRTC_API" ref="nofollow noopener noreferrer">Web RTC</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen_Capture_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Screen_Capture_API" ref="nofollow noopener noreferrer">Screen Capture API</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDevices" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices" ref="nofollow noopener noreferrer">Media Devices</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.agora.io%2Fcn%2FInteractive%2520Broadcast%2Fstart_live_web_ng%3Fplatform%3DWeb" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.agora.io/cn/Interactive%20Broadcast/start_live_web_ng?platform=Web" ref="nofollow noopener noreferrer">实现视频直播</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.agora.io%2Fcn%2FInteractive%2520Broadcast%2Frun_demo_live_web%3Fplatform%3DWeb" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.agora.io/cn/Interactive%20Broadcast/run_demo_live_web?platform=Web" ref="nofollow noopener noreferrer">跑通示例项目</a></p>
</blockquote></div>  
</div>
            