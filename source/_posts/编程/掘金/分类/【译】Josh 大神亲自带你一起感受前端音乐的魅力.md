
---
title: '【译】Josh 大神亲自带你一起感受前端音乐的魅力'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be552edb37de43e68a920e930ea5a683~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 19:01:05 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be552edb37de43e68a920e930ea5a683~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文地址：<a href="https://www.joshwcomeau.com/react/announcing-use-sound-react-hook/" target="_blank" rel="nofollow noopener noreferrer">www.joshwcomeau.com/react/annou…</a></p>
<p>作者：Josh Comeau、 译者：林鸿鹄</p>
<p>未经授权禁止转载。</p>
<h2 data-id="heading-0">读前须知</h2>
<blockquote>
<p>本篇译文涉及到的部分 <strong>音频demo</strong> 需要前往到 <a href="https://www.joshwcomeau.com/react/announcing-use-sound-react-hook/" target="_blank" rel="nofollow noopener noreferrer"><strong>原文</strong></a> 进行尝试。</p>
<p><strong>强力推荐去试试看哦～ （需翻墙）</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be552edb37de43e68a920e930ea5a683~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-1"><strong>介绍</strong></h2>
<p>可能因为我是一个音频工程师，本人很期待能在浏览器里听到更多的音效。</p>
<p>我知道这时候会有一大堆的人反驳我，很大部分原因是曾经音频在浏览器里被乱用，从而导致一部分人觉得在浏览器听到声音是一件很讨厌的事情。</p>
<p>早期遇到音频往往是在以下情况：</p>
<ul>
<li>老的浏览器里使用 MIDI 文件作为背景音乐 🎺</li>
<li>黑客病毒类曾用音效来达到一些邪恶的目的，来获取用户的注意力，让诈骗更可信 😈</li>
<li>还有自动播放视频等等 😬</li>
</ul>
<p>但是我认为这个想法还是可以拯救一下的。我相信音效可以强调用户的行为，增强给用户的反馈、给枯燥的用户行为增添一些快乐。当声音被高雅地使用后，产品会更加地真实、更加地栩栩如生。</p>
<p>给项目添加音效并不是一个新主意：例如网页游戏，或手机app上一直有在使用音效来提升用户交互的体验。实际上，web 才是个奇葩，我能想到的所有数字媒体都有用到音效吧？你们说是不是？</p>
<p>当我搭建这个博客的时候，我就想要开始这个试验。在我这个博客里，当你和很多 UI 组件互动的时候都会发出声音哦～</p>
<h3 data-id="heading-2"><strong>去试试看吧！</strong></h3>
<p>你可以尝试点击<a href="https://www.joshwcomeau.com/react/announcing-use-sound-react-hook/" target="_blank" rel="nofollow noopener noreferrer"><strong>博客的右上角</strong></a> （需翻墙）</p>
<p>或尝试一下原文的在线代码编辑区，真的非常有意思！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/742f5b061c744015a1e9c70e4a0bd8cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为音效在浏览器上真的是太少太少了，所以体验的时候你会感觉特别的吸引人的"耳球"。所以只要把声音用在正确的项目里，这会是一个绝对的秘密武器，给 everybody 带来大大滴惊喜！</p>
<p>为了让你们比较方便的开始，我把这个博客的 hook，<code>use-sound</code>， 发布到 NPM 上了。本篇博客会尽快得让你们知道它可以做什么，我还会分享一些如何在 web 中正确使用音效的技巧。</p>
<blockquote>
<p><strong>直接看文档？</strong></p>
<p>如果你想直接用这个 hook，你可以 <a href="https://github.com/joshwcomeau/use-sound" target="_blank" rel="nofollow noopener noreferrer"><strong>直接跳到这个 GITHUB 链接</strong></a> 哦～</p>
</blockquote>
<h2 data-id="heading-3">概述</h2>
<p><code>use-sound</code> 是一个 react hook 让你可以播放音效。这里是一个比较简单的例子：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> useSound <span class="hljs-keyword">from</span> <span class="hljs-string">'use-sound'</span>;
<span class="hljs-keyword">import</span> boopSfx <span class="hljs-keyword">from</span> <span class="hljs-string">'../../sounds/boop.mp3'</span>; <span class="hljs-comment">// 导入你自己的音频</span>
<span class="hljs-keyword">const</span> BoopButton = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [play] = useSound(boopSfx);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;play&#125;</span>></span>Boop!<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useSound</code> 会异步加载10kb的第三方依赖包 <a href="https://howlerjs.com/" target="_blank" rel="nofollow noopener noreferrer"><strong>Howler</strong></a>，但对你的包只加大约1kb。</p>
<p>它提供了一大堆很赞的东西，包括：</p>
<ul>
<li>提早停止声音，或者暂停/重播声音。</li>
<li>加载一个雪碧音频，然后分裂成很多独立的声音。</li>
<li>让声音加速或减速。</li>
<li>拥有一大堆事件！</li>
<li>还有好多好多 Howler 所实现的高级东西。</li>
</ul>
<p>假如你想看更多复杂的使用方式或 API详情，你可以 <a href="https://github.com/joshwcomeau/use-sound" target="_blank" rel="nofollow noopener noreferrer"><strong>点击此处查看文档</strong></a>。</p>
<h2 data-id="heading-4">让我们开始吧！</h2>
<h3 data-id="heading-5">安装</h3>
<p>第一步我们要做的是通过 NPM 或者 Yarn 来进行安装包：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 用 YARN</span>
yarn add use-sound
<span class="hljs-comment"># 或，用 NPM</span>
npm install use-sound
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">导入</h3>
<p>这个包只导出一个默认的 hook，<code>useSound</code>：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> useSound <span class="hljs-keyword">from</span> <span class="hljs-string">'use-sound'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用这个 hook 之前，你还需要导入你的音频文件。</p>
<p>如果你是使用 <code>create-react-app</code>/Gatsby 这样的脚手架，你应该可以像导入图片或其他media一样的方式来导入 MP3 文件：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> boopSfx <span class="hljs-keyword">from</span> <span class="hljs-string">'../../sounds/boop.mp3'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你在捣鼓自己的 Webpack 配置，你可以用到 <a href="https://v4.webpack.js.org/loaders/file-loader/" target="_blank" rel="nofollow noopener noreferrer"><strong>file-loader</strong></a> 使 <code>.mp3</code> 格式的文件成为随意的文件类型。</p>
<h2 data-id="heading-7">前端好声音！</h2>
<p>知道如何安装依赖和写代码只是成功的一半；我们还需要准备好优美动听的音乐才行！</p>
<p>我最喜欢的资源是 <a href="https://freesound.org/" target="_blank" rel="nofollow noopener noreferrer"><strong>freesound.org</strong></a>。几乎博客的所有音频都来自于这个网站。你需要先注册一个账号来下载他们的资源，所有东西都是免费的喔。</p>
<blockquote>
<p>请做好寻找音乐的准备。网站里很多里面的声音都录的不是很清晰，</p>
<p>可能就是大海捞针的感觉 嘻嘻 毕竟是免费的</p>
</blockquote>
<h3 data-id="heading-8">准备音频</h3>
<p>很多来自 freesound.org 的音频我们都需要先处理一下：</p>
<ul>
<li>比如说一些和弦，音频播放时是断断续续的。你需要把他们裁剪一下，达到触发声音后就立马能听到的效果。</li>
<li>假如一些音频音量一会儿高一会儿低的，你还得调整音频的音量调成一致哦。</li>
<li>下载下来的音频格式可能不同，你还需要转成 MP3 的格式～</li>
</ul>
<p>完成以上几点，你播放的音频才会完美哟～</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e7b07339cc34dcdb539a6f1f258ff7e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以使用一个免费，开源，跨平台的音频编辑器来编辑你下载的音频</p>
<p>我推荐你们使用 <a href="https://www.audacityteam.org/" target="_blank" rel="nofollow noopener noreferrer"><strong>Audacity</strong></a>（该地址需要翻墙下载）</p>
<p>译者在百度找到了这个下载地址：<strong><a href="https://audacity.onl/" target="_blank" rel="nofollow noopener noreferrer">audacity.onl/</a></strong></p>
<p>当然学习怎么使用 Audacity 不是这个博客的重点，但是外面还是有很多免费的资源来学习如何使用它。</p>
<blockquote>
<p><strong>为什么一定要使用 MP3?</strong></p>
<p>在好久以前，还没有一个哪里都支持的音频格式；大家常用 MP3，AIFF，或是 WAV，在不同的环境下加载不同的文件。</p>
<p>开心的是， MP3 当今被所有主流的 <a href="https://caniuse.com/mp3" target="_blank" rel="nofollow noopener noreferrer"><strong>浏览器支持</strong></a>，包括 Internet Explorer 9。和其他格式相比，MP3 可以很好的被压缩成更小的文件大小。</p>
<p>所以我强推 MP3！</p>
</blockquote>
<h2 data-id="heading-9">音频 🔊 & 辅助功能 ♿️ & 可用性</h2>
<p>即使音频被网页所支持，我注意到有一部分用户不会在乎它的存在，他们可能更喜欢静静地呆着。</p>
<p>对于那些视力损伤的人群一般都会使用屏幕朗读软件来访问网页。如果我们给网页放置过多的音效，可能会导致这类用户在聆听朗读的内容时，被这些音效所打扰到。</p>
<p>以上原因所致，在你的页面上放置一个静音按钮 🔕 是非常重要的。而且把静音<a href="https://www.joshwcomeau.com/react/persisting-react-state-in-localstorage/" target="_blank" rel="nofollow noopener noreferrer">"<strong>状态保持</strong>"</a>住也是至关重要的，这样用户就不再需要反复地设置是否需要静音啦！</p>
<p>相反的，对于听力有障碍的用户而言，他们察觉不到声音是否被触发了。因此，我们绝不能仅通过音频来传递重要的信息。如果你在使用音效来作为反馈用户的途径，请也确保拥有视觉上的反馈。这样、网页才能100%在没声音的情况下保持可用性。</p>
<blockquote>
<p><strong>状态保持 Sticky</strong> 是作者的另外一篇文章，</p>
<p>假如同学们感兴趣可以在评论区点赞留言，小编抽空再翻译一下～</p>
</blockquote>
<h2 data-id="heading-10">小试牛刀</h2>
<p><a href="https://www.joshwcomeau.com/react/announcing-use-sound-react-hook/" target="_blank" rel="nofollow noopener noreferrer">请前往作者的博客尝试不同在线的 demo 吧～</a></p>
<p><strong>请不要忘记打开本地设备的声音哦～</strong></p>
<h3 data-id="heading-11">1. Checkbox</h3>
<p>当我点击这个 checkbox 的时候，我已经颅内升天了(゜-゜)つ！！如果有鼠标的或触控板的话，请尝试一次飞快的点击，然后再尝试一次缓慢的点击，听听他们的音效。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d08c8cb4045c45a199ddadadc2cca1a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [isChecked, setIsChecked] = React.useState(
    <span class="hljs-literal">false</span>
  );

  <span class="hljs-keyword">const</span> [playActive] = useSound(
    <span class="hljs-string">'/sounds/pop-down.mp3'</span>,
    &#123; <span class="hljs-attr">volume</span>: <span class="hljs-number">0.25</span> &#125;
  );
  <span class="hljs-keyword">const</span> [playOn] = useSound(
    <span class="hljs-string">'/sounds/pop-up-on.mp3'</span>,
    &#123; <span class="hljs-attr">volume</span>: <span class="hljs-number">0.25</span> &#125;
  );
  <span class="hljs-keyword">const</span> [playOff] = useSound(
    <span class="hljs-string">'/sounds/pop-up-off.mp3'</span>,
    &#123; <span class="hljs-attr">volume</span>: <span class="hljs-number">0.25</span> &#125;
  );

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Checkbox</span>
      <span class="hljs-attr">name</span>=<span class="hljs-string">"demo-checkbox"</span>
      <span class="hljs-attr">checked</span>=<span class="hljs-string">&#123;isChecked&#125;</span>
      <span class="hljs-attr">size</span>=<span class="hljs-string">&#123;24&#125;</span>
      <span class="hljs-attr">label</span>=<span class="hljs-string">"I agree to self-isolate"</span>
      <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;()</span> =></span> setIsChecked(!isChecked)&#125;
      onMouseDown=&#123;playActive&#125;
      onMouseUp=&#123;() => &#123;
        isChecked ? playOff() : playOn();
      &#125;&#125;
    /></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2. 互动音频</h3>
<p>有时候你只希望声音在互动的时候被播放。 注意到下面这个 demo 声音只在 hover 的时候被播放：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7699bd064c1f40d886d51473613ebf09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> soundUrl = <span class="hljs-string">'/sounds/rising-pops.mp3'</span>;
  <span class="hljs-comment">// 你可以通过更换资源 'rising-pops' 成下面的音频资源听听看哟～</span>
  <span class="hljs-comment">// - fanfare</span>
  <span class="hljs-comment">// - dun-dun-dun</span>
  <span class="hljs-comment">// - guitar-loop</span>
  <span class="hljs-keyword">const</span> [play, &#123; stop &#125;] = useSound(
    soundUrl,
    &#123; <span class="hljs-attr">volume</span>: <span class="hljs-number">0.5</span> &#125;
  );

  <span class="hljs-keyword">const</span> [isHovering, setIsHovering] = React.useState(
    <span class="hljs-literal">false</span>
  );

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>
      <span class="hljs-attr">onMouseEnter</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
        setIsHovering(true);
        play();
      &#125;&#125;
      onMouseLeave=&#123;() => &#123;
        setIsHovering(false);
        stop();
      &#125;&#125;
    >
      <span class="hljs-tag"><<span class="hljs-name">ButtonContents</span> <span class="hljs-attr">isHovering</span>=<span class="hljs-string">&#123;isHovering&#125;</span>></span>
        Hover over me!
      <span class="hljs-tag"></<span class="hljs-name">ButtonContents</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">3. 逐步升高的音阶</h3>
<p>我在点赞的按钮上加了一个很有意思的技巧：每次点击的音频音阶，都会比上一次的点击的要更高一点。我是这么实现的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/270731927437425fa7101b9618d9dd55~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> soundUrl = <span class="hljs-string">'/sounds/glug-a.mp3'</span>;

  <span class="hljs-keyword">const</span> [playbackRate, setPlaybackRate] = React.useState(<span class="hljs-number">0.75</span>);

  <span class="hljs-keyword">const</span> [play] = useSound(soundUrl, &#123;
    playbackRate,
    <span class="hljs-attr">volume</span>: <span class="hljs-number">0.5</span>,
  &#125;);

  <span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">() =></span> &#123;
    setPlaybackRate(playbackRate + <span class="hljs-number">0.1</span>);
    play();
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">role</span>=<span class="hljs-string">"img"</span> <span class="hljs-attr">aria-label</span>=<span class="hljs-string">"Heart"</span>></span>
        💖
      <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">4. 播放/暂停 按钮</h3>
<p>你可以用这个播放按钮搞一个新的网易音音乐了哈哈哈。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb09b5d4ca64f6399bbf9ad1d3aa191~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> soundUrl = <span class="hljs-string">'/sounds/guitar-loop.mp3'</span>;

  <span class="hljs-keyword">const</span> [play, &#123; stop, isPlaying &#125;] = useSound(soundUrl);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">PlayButton</span>
      <span class="hljs-attr">active</span>=<span class="hljs-string">&#123;isPlaying&#125;</span>
      <span class="hljs-attr">size</span>=<span class="hljs-string">&#123;60&#125;</span>
      <span class="hljs-attr">iconColor</span>=<span class="hljs-string">"var(--color-background)"</span>
      <span class="hljs-attr">idleBackgroundColor</span>=<span class="hljs-string">"var(--color-text)"</span>
      <span class="hljs-attr">activeBackgroundColor</span>=<span class="hljs-string">"var(--color-primary)"</span>
      <span class="hljs-attr">play</span>=<span class="hljs-string">&#123;play&#125;</span>
      <span class="hljs-attr">stop</span>=<span class="hljs-string">&#123;stop&#125;</span>
    /></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">5. 雪碧音频</h3>
<p>如果你的组件打算用很多音效，我建议你使用雪碧音频哦～ 雪碧音频是一个音频文件集合了很多不同的音效。把音频都结合成一个单独文件后，我们可以写出更优美的代码，此外防止很多并行的 HTTP 请求。</p>
<p>这里我们用了一个雪碧音频搭建了一个打碟机！尝试点击这些按钮，或者点击你键盘上的1234听听看吧！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdffccb88f0a4192b2e3414a32f69b22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> soundUrl = <span class="hljs-string">'/sounds/909-drums.mp3'</span>;

  <span class="hljs-keyword">const</span> [play] = useSound(soundUrl, &#123;
    <span class="hljs-attr">sprite</span>: &#123;
      <span class="hljs-attr">kick</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">350</span>],
      <span class="hljs-attr">hihat</span>: [<span class="hljs-number">374</span>, <span class="hljs-number">160</span>],
      <span class="hljs-attr">snare</span>: [<span class="hljs-number">666</span>, <span class="hljs-number">290</span>],
      <span class="hljs-attr">cowbell</span>: [<span class="hljs-number">968</span>, <span class="hljs-number">200</span>],
    &#125;
  &#125;);

  <span class="hljs-comment">// Custom hook that listens for 'keydown',</span>
  <span class="hljs-comment">// and calls the appropriate handler function.</span>
  useKeyboardBindings(&#123;
    <span class="hljs-number">1</span>: <span class="hljs-function">() =></span> play(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'kick'</span> &#125;),
    <span class="hljs-number">2</span>: <span class="hljs-function">() =></span> play(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'hihat'</span> &#125;),
    <span class="hljs-number">3</span>: <span class="hljs-function">() =></span> play(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'snare'</span> &#125;),
    <span class="hljs-number">4</span>: <span class="hljs-function">() =></span> play(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'cowbell'</span> &#125;),
  &#125;)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span>
        <span class="hljs-attr">aria-label</span>=<span class="hljs-string">"kick"</span>
        <span class="hljs-attr">onMouseDown</span>=<span class="hljs-string">&#123;()</span> =></span> play(&#123; id: 'kick' &#125;)&#125;
      >
        1
      <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span>
        <span class="hljs-attr">aria-label</span>=<span class="hljs-string">"hihat"</span>
        <span class="hljs-attr">onMouseDown</span>=<span class="hljs-string">&#123;()</span> =></span> play(&#123; id: 'hihat' &#125;)&#125;
      >
        2
      <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span>
        <span class="hljs-attr">aria-label</span>=<span class="hljs-string">"snare"</span>
        <span class="hljs-attr">onMouseDown</span>=<span class="hljs-string">&#123;()</span> =></span> play(&#123; id: 'snare' &#125;)&#125;
      >
        3
      <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Button</span>
        <span class="hljs-attr">aria-label</span>=<span class="hljs-string">"cowbell"</span>
        <span class="hljs-attr">onMouseDown</span>=<span class="hljs-string">&#123;()</span> =></span> play(&#123; id: 'cowbell' &#125;)&#125;
      >
        4
      <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多关于雪碧音频的详情 <a href="https://github.com/joshwcomeau/use-sound#sprites" target="_blank" rel="nofollow noopener noreferrer"><strong>查看 API 文档</strong></a></p>
<h2 data-id="heading-16">百万种可行性</h2>
<p>在网页中探索声音的过程深深触动着我，因为实在是有太多尚未开发的领域了！！我在网页上尝试音频有一段时间了，但我感觉我仅仅只是触碰到了表面而已。</p>
<p>现在你有了开始试验的工具，我希望能鼓励到你去尝试一下，看看你能走多远 😁</p>
<p>你可以通过 <a href="https://github.com/joshwcomeau/use-sound" target="_blank" rel="nofollow noopener noreferrer"><strong>GitHub</strong></a> 了解更多关于 <code>use-sound</code> 这个 hook 噢～ 快去行动起来吧～</p></div>  
</div>
            