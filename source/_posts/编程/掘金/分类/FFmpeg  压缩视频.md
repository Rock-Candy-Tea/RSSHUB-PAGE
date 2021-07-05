
---
title: 'FFmpeg  压缩视频'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e610eec079334be6834dc06d7ce16df5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 19:33:08 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e610eec079334be6834dc06d7ce16df5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前不久~</p>
<p>老姐：老弟，我学生快要中考了，我想将他们的点滴视频和图片整理成一个鼓励他们的短片。</p>
<p>我：那你整呗～</p>
<p>老姐：我不会，你来。</p>
<p>我：你自己的学生，我n年前不就跟你说过，拖拉拽就完事了，怎么还是我来。</p>
<p>老姐：没时间，要带娃，跟班。</p>
<p>我：那你发素材过来吧。</p>
<blockquote>
<p>A Few Moments Later</p>
</blockquote>
<p>老姐：我发了邮箱，你自己根据图片，文档内容和records制作一个视频。</p>
<blockquote>
<p>一看素材，图片200+，文档5+，视频2+... 我都要无语了，还要自己将素材串联成故事，扑通一下就跪下了，灵感才是难点啊~</p>
</blockquote>
<p>我：(强忍心酸)好的。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e610eec079334be6834dc06d7ce16df5~tplv-k3u1fbpfcp-watermark.image" alt="heart-rending-story.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">完成工具</h3>
<p>嗯～ 既然已经把视频的任务接了，那么，就捣鼓起来吧。</p>
<p>因为俺是一个早十晚八的程序员，能够完全自控的时间也就是那点周末时间了。殊不知，花了我两个周末的时间。</p>
<blockquote>
<p>如何成片讲故事的灵感至少耗费了我半天～momo</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2249d9d53381469d8e9365de36bd36a6~tplv-k3u1fbpfcp-watermark.image" alt="spend_two_week.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>全程两个工具疯狂切换：</p>
<ul>
<li>
<p><a href="https://www.apple.com/final-cut-pro/" target="_blank" rel="nofollow noopener noreferrer">Final Cut Pro</a>视频剪辑软件</p>
</li>
<li>
<p><a href="https://www.apple.com.cn/imovie/" target="_blank" rel="nofollow noopener noreferrer">iMovie</a>视频剪辑软件</p>
</li>
</ul>
<p>之所以选择这两款剪辑软件，一是熟悉，二是里面的模版比较友好，满足我目前一切需求。</p>
<p>比如<code>iMovie</code>的成片模版：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e377b5e3c4d4cfc9671c51149b94a9e~tplv-k3u1fbpfcp-watermark.image" alt="trailers.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过四天的捣鼓后，喜提成品：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5001ad81a45484a93a9e2c9596f88b7~tplv-k3u1fbpfcp-watermark.image" alt="cheerUp647.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，屁颠屁颠发过去给老姐<code>邀功</code>🙈</p>
<p>可是</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2311edc78add418493269425d96731af~tplv-k3u1fbpfcp-watermark.image" alt="send-limit-100.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">FFmpeg压缩视频</h3>
<p>这小事情，我将清晰度和尺寸降一降，总还行吧。然而，经过一阵捣鼓，还是没能达到目标啊～</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1984c5288344c86b1c51a9160df4ca8~tplv-k3u1fbpfcp-watermark.image" alt="cheerUp254.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哎，借助网上现成的压缩产品吧～</p>
<p>于是乎百度和谷歌了段时间:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec52e43e93fe46c3945e68f107ca25f0~tplv-k3u1fbpfcp-watermark.image" alt="compress-video.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然而尝试了两三个，不是一开始需要会员，就是免费帮你压缩1/3的视频。</p>
<p><code>cut cut cut</code>掉，怎么可以为了压缩一个视频，就购买一个会员呢？</p>
<p><strong>众里寻他千百度 蓦然回首 那人却在 灯火阑珊处</strong></p>
<p><a href="http://ffmpeg.org/about.html" target="_blank" rel="nofollow noopener noreferrer">FFmpeg</a>可以满足我方需求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84ebd9a3282c49fcac035ee3f8bb1e34~tplv-k3u1fbpfcp-watermark.image" alt="about-ffmpeg.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，我们要怎么使用它呢？</p>
<h4 data-id="heading-2">安装</h4>
<p>这里，我使用的是<code>homebrew</code>进行安装。</p>
<pre><code class="hljs language-bash copyable" lang="bash">brew install ffmpeg
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他安装方法，感兴趣的可自行尝试～</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22f054e8f8b64f4eb10acfb388bb2176~tplv-k3u1fbpfcp-watermark.image" alt="ffmpeg-version.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">使用</h4>
<p><code>FFmpeg</code>使用起来很简单。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ ffmpeg -i input.mp4 output.avi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你要个性化参数配置的话，可以参考<a href="http://ffmpeg.org/ffmpeg.html" target="_blank" rel="nofollow noopener noreferrer">官方的文档</a>。</p>
<p>嗯，这里简单的输出就已经满足个人需求了<code>$ ffmpeg -i cheerUp.mp4 cheerUp-wechat.mp4</code>，执行上面的命令行之后，你会在控制台上看到一串串的字节流日志打印出来，喝杯咖啡等待会即可。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efb35fe8052d41ad9253af03d6a68acf~tplv-k3u1fbpfcp-watermark.image" alt="tranform-movie.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成✅视频的压缩转换后，查看成品：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/184506c388a849aca255c03a890d5d16~tplv-k3u1fbpfcp-watermark.image" alt="target-done.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很好，满足需求。这次可以邀功了！</p>
<blockquote>
<p>因为视频播放的gif图上传上去模糊，这里切掉了gif图视频对比。前后对比的视频清晰度差异不大，完全可以接受。如果感兴趣，读者可以自行尝试后，对比前后的视频效果。</p>
</blockquote>
<h3 data-id="heading-4">后话</h3>
<p>然而，甲方还是甲方啊。需求改版了妥妥好几次～</p>
<blockquote>
<p>下面是邮箱传输视频备份版本</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f5cd646cf564ab48b22ee813f94050f~tplv-k3u1fbpfcp-watermark.image" alt="give-movies.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>值得欣慰的是，那帮兔崽子有点喜欢视频。</p>
<p>Anyway</p>
<p>祝你们<strong>金榜题名</strong>！</p></div>  
</div>
            