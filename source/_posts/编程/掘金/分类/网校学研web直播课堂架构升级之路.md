
---
title: '网校学研web直播课堂架构升级之路'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba04e268e23f483fb87f1d8c6938496f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 00:52:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba04e268e23f483fb87f1d8c6938496f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述</h2>
<p>首先，web的免安装，即用即走的特性，再加上没有版本的限制，可以快速迭代或者试错，特别的适合一些业务场景，例如创新性业务，快速迭代业务，关于web能不能支撑直播业务，web直播性能行不行，带着这两个疑问，我们对web直播能力做了探索。通过读这篇文章你可以了解到到web、h5、小程序是否能够做直播，以下探索基于网校学研大班直播体系。</p>
<h2 data-id="heading-1">web1.0版本横空出世</h2>
<p>背景是产品侧提出讲座业务要重构，这时候天时地利人和都占有了，快速组建团队，耗时1个多月，做出了支持rtmp视频播放、即时聊天、投票、献礼物等功能，简单，够用。但天有不测风云，由于这样那样的原因，最终项目也没有上线，夭折了。你以为就此草草收场，那不是我们的脾气，继续发动每一个人的小宇宙。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba04e268e23f483fb87f1d8c6938496f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">web1.1版本初生牛犊不怕虎</h2>
<p>这个版本最大的亮点是要跟PC客户端进行功能追齐，那摆在我们面前有三个大坑需要填，一个是web的AI能力，一个是连麦中的rtc能力，还有一个是web的课堂互动拉齐。</p>
<p>首先解决最难的，AI能力，通过探索，我们借助hark插件进行收音，</p>
<pre><code class="copyable">this._speechEvents = hark(this._stream)
  
this._speechEvents.on('speaking', () => &#123;
      // createLog('检测到说话')
    &#125;)
 
    this._speechEvents.on('stopped_speaking', () => &#123;
      // createLog('检测到停止说话')
    &#125;)
 
    this._speechEvents.on('volume_change', (db) => &#123;
      
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动work使用了lamejs，使用AudioContext,在收集声音时给encodeMp3Worker发消息，转成buffer传给AI，完成了AI语音识别能力，图像识别还没有完成，理论上也能实现。</p>
<pre><code class="copyable">const audioCtx = this._audioCtx = new AudioCtx()
   this._audioStream = audioCtx.createMediaStreamSource(this._stream)
   this._audioRecorder = audioCtx.createScriptProcessor(16384, 1, 1)
   this._audioRecorder.onaudioprocess = (e) => &#123;
     const buffer = e.inputBuffer.getChannelData(0)
     this._encodeMp3Worker.postMessage(&#123;
       type: 'encode',
       payload: buffer
     &#125;)
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>AI插件地址OpenAI:<code>@xes/web-live-framework/libs/openai/index</code><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fba8c749d52f49938d085bfd7483e81a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二个，集成rtc能力。这块我们直接复用了集团直播中台的rtc sdk，快速孵化了我们的业务。RTC SDK<code>@xes/weblive-framework/components/base/players/libs/rtcengine_js_xueersi-1.5.0</code><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33c5a0b788864742b03f6623d960ae91~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三个，与PC端功能拉齐。这个是一个消耗体力的事情，首先了解客户端开发的样子，其次拆分任务，分工开发。这也给项目带来很大的问题，很多人参与，质量把控难度大，这个时候是一个代码量暴增的时期。虽然有CR，依然没有摆脱被重构的命运，这也许就是一个大型项目的宿命。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a55db4e536d142ed9b25f79563d615aa~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3c7fa871ff34fbabf32ae3490b41c1d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">web直播2.0粉墨登场</h2>
<p>重构的原因：开发之间矛盾出现，问题频出，开始互相不信任；代码风格差异大，理解成本增加；重复代码多。为了解决团队合作问题，为了解决项目体验与稳定性，为了让项目能继续活着，开启了第一版本的重构。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08bdee2fcd69487b925de746e85757b2~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
首先，设计了直播框架，将播放器，聊天，信令通道，日志，消息管理中心，收敛到直播框架中，直播框架发布以npm包进行版本管理，并且直播框架设计了一些base类，约定了一些类的基本方法，例如互动base，消息处理base，初始化base，业务通过重载，实现了自己的业务功能。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27d299c2b9e24239b0c41d9556afb4fe~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21f43dfcba3e4c6fb1366d13de9d9ff0~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
这次的重构产出的直播框架，后来快速孵化了PHP大会项目，海外PC端直播项目，轻直播半身直播项目、小程序直播等，这次的重构还是蛮成功的。<a href="https://npm.xesv5.com/?token=eyJpdiI6IlFWaU9sZkFVeTloanROM0ljZGl3R0E9PSIsInZhbHVlIjoiMG1KR2J0UksyTGpySXMyZ2RqY3FBbEMxTUJBZFpCamtJb2Q3ajB0WVBYNXUralZZMkdwY0R1VkZsWjhac3lSWm5zUUJkWW5RYXZSZ01sdW1NQTExOFV0clRuU0ZTcytuYU9JeXVaUWR3Q1E9IiwibWFjIjoiOTIxMDEwMDQ2NzA0ZDU3Y2IzMjA3ZDFiMTAyZmZhNjE4MDliYjRiNDIwYjNiNWNiMTJlN2I5N2VjMWJiYWMzMyJ9#/detial?name=%40xes%2Fweb-live-framework" target="_blank" rel="nofollow noopener noreferrer">web直播框架地址@xes/weblive-framework</a>，支持RTMP播放器、RTC播放器、涂鸦、小程序直播，h5-rtc直播。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4688b227394364b2e1b5ef39dbfcdb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
你以为这就完事了，并不是，现阶段直播项目单页面应用，已经发展出了61个模块，30余中互动。其中一些互动也到了不得不重构的时候了。</p>
<h2 data-id="heading-4">web直播2.1版本到来</h2>
<p>这个版本主要是一个模块的重构，主要是对信令处理模块进行了处理，其次对未来课件、语音答题、语音测评进行了模块的重构，升级eslint。<br>
1、对未来课件、语音答题等互动通过开发中间类来实例化不同互动，解决了互动组件的耦合性问题<br>
2、对信令消息处理模块将控制逻辑与业务实现做了拆分<br>
3、统一eslint：<code>@xes/eslint-cof</code><br>
互动消息处理模块新的流程图：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baa3849801094824b065ff2e1c327016~tplv-k3u1fbpfcp-zoom-1.image" alt="图片名称" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">总结</h2>
<p>1、经过不断的技术探索，文章开始的问题有了答案：web是可以做直播的，在一些场景还具有一定优势<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bd645f9e1b94a50b480f85f89521eb2~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
2、从我们自测的数据来看（待线上数据的检验）,大部分指标与native表现相近。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1aee443899a14b81a43cc46b4c36e174~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">写在最后</h2>
<p>特别感谢所有参与web直播开发的小伙伴们，你们有着极客精神。</p>
<p>关于直播相关的技术欢迎交流，一起进步，未来想做h5直播与小程序直播。</p></div>  
</div>
            