
---
title: 'HarmonyOS学习路之开发篇——公共事件与通知（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/235559ced1a24f6b87063ccae87d233f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 01:31:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/235559ced1a24f6b87063ccae87d233f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：后端、大前端双赛道投稿，2万元奖池等你挑战！」</p>
<h2 data-id="heading-0">通知</h2>
<p>HarmonyOS提供了应用的通知功能，即在应用外层通过使用应用图标进行一些事件的通知。常见的使用场景：</p>
<ul>
<li>显示接收到短消息、即时消息等。</li>
<li>显示应用的推送消息，如广告、版本更新等。</li>
<li>显示当前正在进行的事件，如播放音乐、导航、下载等。</li>
</ul>
<h2 data-id="heading-1">接口说明</h2>
<p>通知相关基础类包含NotificationSlot、NotificationRequest和NotificationHelper。基础类之间的关系如下所示：</p>
<p>图1 通知基础类关系图
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/235559ced1a24f6b87063ccae87d233f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>NotificationSlot</li>
</ul>
<p>NotificationSlot可以对提示音、振动、锁屏显示和重要级别等进行设置。一个应用可以创建一个或多个NotificationSlot，在发布通知时，通过绑定不同的NotificationSlot，实现不同用途。</p>
<p>NotificationSlot的级别目前支持如下几种， 由低到高：</p>
<blockquote>
<ul>
<li><strong>LEVEL_NONE</strong>： 表示通知不发布。</li>
<li><strong>LEVEL_MIN</strong>：表示通知可以发布，但是不显示在通知栏，不自动弹出，无提示音；该级别不适用于前台服务的场景。</li>
<li><strong>LEVEL_LOW</strong>：表示通知可以发布且显示在通知栏，不自动弹出，无提示音。</li>
<li><strong>LEVEL_DEFAULT</strong>：表示通知发布后可在通知栏显示，不自动弹出，触发提示音。</li>
<li><strong>LEVEL_HIGH</strong>：表示通知发布后可在通知栏显示，自动弹出，触发提示音。</li>
</ul>
</blockquote>
<ul>
<li>NotificationRequest</li>
</ul>
<p>NotificationRequest用于设置具体的通知对象，包括设置通知的属性，如：通知的分发时间、小图标、大图标、自动删除等参数，以及设置具体的通知类型，如普通文本、长文本等。</p>
<blockquote>
<p><strong>具体的通知类型</strong>：目前支持六种类型，包括普通文本NotificationNormalContent、长文本NotificationLongTextContent、图片NotificationPictureContent、多行NotificationMultiLineContent、社交NotificationConversationalContent、媒体NotificationMediaContent。</p>
</blockquote>
<ul>
<li>NotificationHelper</li>
</ul>
<p>NotificationHelper封装了发布、更新、删除通知等静态方法。</p>
<h2 data-id="heading-2">效果演示</h2>
<p>[video(video-8u5LpZne-1625130916502)(type-csdn)(url-<a href="https://live.csdn.net/v/embed/168000)(image-https://vedu.csdnimg.cn/723740ccebc14e3ea2e40ba39233abc4/snapshots/0b92cb1f7eee4a218c317f28721c41db-00003.jpg)(title-HarmonyOS%E9%80%9A%E7%9F%A5Demo%E6%BC%94%E7%A4%BA" target="_blank" rel="nofollow noopener noreferrer">live.csdn.net/v/embed/168…</a>)]</p>
<h2 data-id="heading-3">开发步骤</h2>
<p>通知的开发指导分为创建NotificationSlot、发布通知和取消通知等开发场景。</p>
<h3 data-id="heading-4">第一步、初始化NotificationSlot</h3>
<pre><code class="hljs language-java copyable" lang="java">
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String SLOT_ID = <span class="hljs-string">"high"</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String SLOT_NAME = <span class="hljs-string">"Order notification"</span>;
<span class="hljs-comment">//--------------------</span>
 ....
 <span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStart</span><span class="hljs-params">(Intent intent)</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onStart(intent);
        <span class="hljs-keyword">super</span>.setUIContent(ResourceTable.Layout_main_ability_slice);
        ...
        defineNotificationSlot(Const.SLOT_ID, Const.SLOT_NAME, NotificationSlot.LEVEL_HIGH);
...
    &#125;
<span class="hljs-comment">//---------------------</span>
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">defineNotificationSlot</span><span class="hljs-params">(String id, String name, <span class="hljs-keyword">int</span> importance)</span> </span>&#123;
        <span class="hljs-comment">// 创建notificationSlot对象</span>
        NotificationSlot notificationSlot = <span class="hljs-keyword">new</span> NotificationSlot(id, name, importance);
        <span class="hljs-comment">// 设置振动提醒</span>
        notificationSlot.setEnableVibration(<span class="hljs-keyword">true</span>);
        <span class="hljs-comment">// 设置锁屏模式</span>
        notificationSlot.setLockscreenVisibleness(NotificationRequest.VISIBLENESS_TYPE_PUBLIC);
        Uri uri = Uri.parse(Const.SOUND_URI);
        notificationSlot.setSound(uri);
        <span class="hljs-keyword">try</span> &#123;
            NotificationHelper.addNotificationSlot(notificationSlot);
        &#125; <span class="hljs-keyword">catch</span> (RemoteException ex) &#123;
            HiLog.error(LABEL_LOG, <span class="hljs-string">"%&#123;public&#125;s"</span>, <span class="hljs-string">"defineNotificationSlot remoteException."</span>);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">第二步、发布通知</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">publishNotification</span><span class="hljs-params">(String title, String text)</span> </span>&#123;
       <span class="hljs-comment">//构建NotificationRequest对象，应用发布通知前，通过NotificationRequest的setSlotId()方法与NotificationSlot绑定，使该通知在发布后都具备该对象的特征</span>
        notificationId = <span class="hljs-number">0x1000001</span>;
        NotificationRequest request = <span class="hljs-keyword">new</span> NotificationRequest(notificationId).setSlotId(Const.SLOT_ID)
            .setTapDismissed(<span class="hljs-keyword">true</span>);
        <span class="hljs-comment">//调用setContent()设置通知的内容</span>
        request.setContent(createNotificationContent(title, text));
        IntentAgent intentAgent = createIntentAgent(MainAbility.class.getName(),
            IntentAgentConstant.OperationType.START_ABILITY);
        request.setIntentAgent(intentAgent);
        <span class="hljs-comment">//调用publishNotification()发布通知</span>
        <span class="hljs-keyword">try</span> &#123;
            NotificationHelper.publishNotification(request);
        &#125; <span class="hljs-keyword">catch</span> (RemoteException ex) &#123;
            HiLog.error(LABEL_LOG, <span class="hljs-string">"%&#123;public&#125;s"</span>, <span class="hljs-string">"publishNotification remoteException."</span>);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">第三步、取消通知</h3>
<p>取消通知分为取消指定单条通知和取消所有通知，应用只能取消自己发布的通知。</p>
<ul>
<li>调用cancelNotification()取消指定的单条通知。</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">cancel</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            NotificationHelper.cancelNotification(notificationId);
        &#125; <span class="hljs-keyword">catch</span> (RemoteException ex) &#123;
            HiLog.error(LABEL_LOG, <span class="hljs-string">"%&#123;public&#125;s"</span>, <span class="hljs-string">"cancel remoteException."</span>);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>调用cancelAllNotifications()取消所有通知</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">cancelAll</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            NotificationHelper.cancelAllNotifications();
        &#125; <span class="hljs-keyword">catch</span> (RemoteException ex) &#123;
            HiLog.error(LABEL_LOG, <span class="hljs-string">"%&#123;public&#125;s"</span>, <span class="hljs-string">"cancelAll remoteException."</span>);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            