
---
title: '惊呆了，鼠标选一下就触发复制(document.copy )？原来是这样'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b064c1cf2f4e7da3024d603dd46860~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 01:18:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b064c1cf2f4e7da3024d603dd46860~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>背景：我们某系统，有一个禁止复制的功能，如果没有复制权限，复制的时候会弹出一个toast。本质上就是<code>document.oncopy = () => &#123; ... &#125;</code>。有一天，有一个用户反馈说，她一进页面就无限弹出禁止复制的toast，而且是动一下就弹一下，系统根本无法使用</p>
</blockquote>
<h1 data-id="heading-0">现场复现</h1>
<p>用户只是简单的说了几句，大家都表示不可思议，都表示这不可能。最后屏幕共享的时候，果然如此，简直让人怀疑人生。一用鼠标选中了文本，页面就弹出不能复制，大概是这样的表现:</p>
<p><img alt="de.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b064c1cf2f4e7da3024d603dd46860~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>选择文字的时候不手动复制都会触发copy</strong></p>
<blockquote>
<p>当时的录屏因为保密原因，不能对外公开。大概的情况就是这样，上面是我知道怎么复现自己本地跑demo录的屏，接下来会用同样的方式以第三者视角来逐步复述当时的问题排查过程</p>
</blockquote>
<h1 data-id="heading-1">远程控制排查问题</h1>
<p>首先打开控制台，把document.copy改写一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> cp =  <span class="hljs-built_in">document</span>.oncopy.bind(<span class="hljs-built_in">document</span>);
<span class="hljs-built_in">document</span>.oncopy = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
    cp();
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果发现，选一下竟然真的还是弹出toast和打印了1</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aff4c3ef18c2469597ae68079f85f347~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>接下来加了个断点，还是会触发，一样的过程，看起来也没啥区别。于是，开始怀疑用户的插件，瞄了一眼，没有任何可疑的插件，然后把她的Chrome扩展全部关掉，依然会复现</p>
<blockquote>
<p>初步结论：oncopy行为的触发，和插件无关</p>
</blockquote>
<p>此时想起一句话：90%可以通过重启解决，9%可以通过重装解决，1%只能通过买新电脑解决</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82354192afa74a858b85b8384bda647f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>电脑重启了，继续远程控制。还是一样的问题，我说要不你多打开其他网站试试，任何网站都行。小姐姐还是很耐心的一个个操作给我看：“你看什么页面都ok，就你这有问题”。于是我随便试了几个页面，打开控制台输入oncopy，然后就立刻复现问题：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.oncopy = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>"你看呐，所有的页面都有同样的问题～ 你再随便试多几个页面看看" ——其实我在查资料，看看是不是有我知识盲区之外的</p>
<blockquote>
<p>第二步结论：任何页面都会有问题，所以问题的根源不在于页面层面的，是更高层面上的</p>
</blockquote>
<p>资料也没查到类似的问题，大概无奈的看着她操作了几分钟，我也一句话都没有说，对着电脑发呆。突然萌生一个念头：系统上的个性化设定</p>
<p>check了一下输入法，搜狗，应该无影响。但是，在对方频繁操作中，有一个若隐若现的小logo引起我注意</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33bb30f9d5cb404ea5aee3bccbc9be1f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/805ba3b1664d4cf0bc3e5dad6b4b4bc4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/892f859f970646f3ab47eadb2c6f362a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>🧑‍🔧:“我发现你这有一个小logo，是干嘛的”</p>
<p>👩‍🦰:“一个翻译工具”</p>
<p>🧑‍🔧:“多动动看看，我想看清楚一点”</p>
<p>👩‍🦰:“你看，放在这里，它就会翻译屏幕上的单词”</p>
<p>🧑‍🔧:“那你试一下翻译其他软件如ppt呢”</p>
<p>👩‍🦰:“居然也可以喔”</p>
<p>🧑‍🔧:“那关掉这个翻译软件，再回来看看页面呢”</p>
<p>👩‍🦰:“好像没问题了”</p>
<p>🧑‍🔧:“嗯，那就是这个软件的问题。我看有一个自动翻译你鼠标所在的英文的功能，这个功能的实现方式可能是：你鼠标放到英文上，它会触发系统的copy事件，可能是直接帮你复制或者是背后帮你按下按键。你再打开这个应用，先把这个功能关了吧”</p>
<p>👩‍🦰:“哦，我知道了，有一个划词搜索的功能，应该跟他有关”</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b285bb0d9ec448fb90d45c044d828732~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>关掉后，问题是解决了，还是很好奇：你这软件叫什么，我也下载来玩玩</p>
<blockquote>
<p>真凶就是《欧路词典》，它会在你选中文本的时候自动触发复制，拿到英文文案去搜索那个单词的信息——顾名思义划词搜索</p>
</blockquote>
<h1 data-id="heading-2">下载来玩玩</h1>
<p>下载回来开启，自己写了一个简单的demo，果然都复现了</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> C: React.FC = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> ref = React.useRef<HTMLDivElement>(<span class="hljs-literal">null</span>);
  React.useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">document</span>.oncopy = (): <span class="hljs-function"><span class="hljs-params">boolean</span> =></span> &#123;
      Toast.error(<span class="hljs-string">'禁止复制'</span>);<span class="hljs-comment">// 仅仅一个toast，随便找个ui库吧</span>
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;;
    <span class="hljs-built_in">document</span>.onclick = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
      ref.current!.innerHTML += <span class="hljs-string">'你点击了页面<br />'</span>;
    &#125;;
    <span class="hljs-keyword">const</span> handleKeydown = (e): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
      ref.current!.innerHTML += <span class="hljs-string">`你按下了<span class="hljs-subst">$&#123;e.key&#125;</span><br />`</span>;
    &#125;;
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'keydown'</span>, handleKeydown);
    <span class="hljs-keyword">return</span> (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
      <span class="hljs-built_in">document</span>.oncopy = <span class="hljs-literal">null</span>;
      <span class="hljs-built_in">document</span>.onclick = <span class="hljs-literal">null</span>;
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'keydown'</span>, handleKeydown);
    &#125;;
  &#125;, []);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">pre</span>></span>
        我说 你是人间的四月天； 笑响点亮了四面风； 轻灵在春的光艳中交舞着变。 你是四月早天里的云烟，
        黄昏吹着风的软，星子在 无意中闪，细雨点洒在花前。
      <span class="hljs-tag"></<span class="hljs-name">pre</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        操作记录
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照预期，如果不开欧路词典，我们复制页面的内容，将会弹出toast禁止复制，如下：</p>
<p><img alt="de.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7f9334fd7fa4b5baad244e7c7a99891~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>开启了欧路词典，表现是这样：</p>
<p><img alt="de.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8eb3ff32ab8b44eab64cb7af6d9dbd0b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>问题因此转化为，如何区分出欧路词典的copy</p>
<h1 data-id="heading-3">解决方案</h1>
<p>我们使用一种最简单的方式，按下command(key为Meta)不弹起的时候，生产key的队列，当最后一个按下的是c，则消费生产者队列，往前搜索有没有按过command</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> Cpn: React.FC = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> ref = React.useRef<HTMLDivElement>(<span class="hljs-literal">null</span>);
  <span class="hljs-keyword">const</span> providerQuene = React.useRef<string[]>([]);

  <span class="hljs-keyword">const</span> triggerCopy = React.useCallback(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 消费生产者队列的数据</span>
    <span class="hljs-keyword">const</span> last = providerQuene.current.pop();
    <span class="hljs-comment">// 如果最后按下的是c，而且键盘不弹起，往前找是不是按下过command</span>
    <span class="hljs-keyword">if</span> (last === <span class="hljs-string">'c'</span> && providerQuene.current.includes(<span class="hljs-string">'Meta'</span>)) &#123;
      Toast.error(<span class="hljs-string">'禁止复制'</span>);
    &#125;
  &#125;, [providerQuene]);
  React.useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">document</span>.oncopy = (): <span class="hljs-function"><span class="hljs-params">boolean</span> =></span> &#123;
      triggerCopy();
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;;
    <span class="hljs-built_in">document</span>.onclick = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
      ref.current!.innerHTML += <span class="hljs-string">'你点击了页面<br />'</span>;
    &#125;;
    <span class="hljs-keyword">const</span> handleKeydown = (e: KeyboardEvent): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (e.key === <span class="hljs-string">'Meta'</span>) &#123;
        providerQuene.current.push(<span class="hljs-string">'Meta'</span>);
      &#125;
      <span class="hljs-keyword">if</span> (e.key === <span class="hljs-string">'c'</span>) &#123;
        providerQuene.current.push(<span class="hljs-string">'c'</span>);
      &#125;
      ref.current!.innerHTML += <span class="hljs-string">`你按下了<span class="hljs-subst">$&#123;e.key&#125;</span><br />`</span>;
    &#125;;
    <span class="hljs-keyword">const</span> handleKeyUp = (&#123; key &#125;: KeyboardEvent): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
      key === <span class="hljs-string">'Meta'</span> && (providerQuene.current = []); <span class="hljs-comment">// meta键弹起，清理生产者队列</span>
    &#125;;
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'keydown'</span>, handleKeydown);
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'keyup'</span>, handleKeyUp);
    <span class="hljs-keyword">return</span> (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
      <span class="hljs-built_in">document</span>.oncopy = <span class="hljs-literal">null</span>;
      <span class="hljs-built_in">document</span>.onclick = <span class="hljs-literal">null</span>;
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'keydown'</span>, handleKeydown);
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'keyup'</span>, handleKeyUp);
    &#125;;
  &#125;, []);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">pre</span>></span>
        我说 你是人间的四月天； 笑响点亮了四面风； 轻灵在春的光艳中交舞着变。 你是四月早天里的云烟，
        黄昏吹着风的软，星子在 无意中闪，细雨点洒在花前。
      <span class="hljs-tag"></<span class="hljs-name">pre</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        操作记录
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>以上所有的操作都是在mac的Chrome浏览器下，safari看起来没问题。其他浏览器或者windows的兼容性问题，都可以用类似的方式去处理</p>
</blockquote>
<h1 data-id="heading-4">最后</h1>
<blockquote>
<p>字节跳动互娱前端招人啦，互娱研发部门负责抖音、抖音火山版、直播、音乐、影像等多款明星产品的研发，技术氛围浓厚，团队年轻人多，充满挑战和机会，有想法的小伙伴简历可以投 <strong><a href="mailto:1756770934@qq.com">1756770934@qq.com</a></strong> 哦</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            