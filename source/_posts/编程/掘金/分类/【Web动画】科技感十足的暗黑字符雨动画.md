
---
title: '【Web动画】科技感十足的暗黑字符雨动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://user-images.githubusercontent.com/8554143/127498604-2dc65906-b730-4e8f-b5f5-e10160007024.gif'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 18:41:28 GMT
thumbnail: 'https://user-images.githubusercontent.com/8554143/127498604-2dc65906-b730-4e8f-b5f5-e10160007024.gif'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文将使用纯 CSS，带大家一步一步实现一个这样的科幻字符跳动背景动画。类似于这样的字符雨动画：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/127498604-2dc65906-b730-4e8f-b5f5-e10160007024.gif" alt="Digital Char Rain Animation" loading="lazy" referrerpolicy="no-referrer"></p>
<p>或者是类似于这样的：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/127498966-dd59fc85-49a6-4741-859d-2b9b65757563.gif" alt="CodePen Home
Matrix digital rain (animated version) By yuanchuan" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运用在一些类似科技主题的背景之上，非常的添彩。</p>
<h2 data-id="heading-0">文字的竖排</h2>
<p>首先第一步，就是需要实现文字的竖向排列：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2c8c465c8064cf097ec4d7ae4dd9ff8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一步非常的简单，可能方法也很多，这里我简单罗列一下：</p>
<ol>
<li>使用控制文本排列的属性 <code>writing-mode</code> 进行控制，可以通过 <code>writing-mode: vertical-lr</code> 等将文字进行竖向排列，但是对于数字和英文，将会旋转 90° 展示：</li>
</ol>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>1234567890ABC<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>中文或其他字符ォヶ<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">p</span> &#123;
    writing-mode: vertical-lr; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3ff65b3bfc8401eb44fe7f5582ca601~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然这种情况下，英文字符的展示不太满足我们的需求。</p>
<ol start="2">
<li>控制容器的宽度，控制每行只能展示 1 个中文字符。</li>
</ol>
<p>这个方法算是最简单便捷的方法了，但是由于英文的特殊性，要让连续的长字符串自然的换行，我们还需要配合 <code>word-break: break-all</code> ：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">word-break</span>: break-all;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下，满足需求：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdc4ab2467194668b4b5abce118ed596~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">使用 CSS 实现随机字符串的选取</h2>
<p>为了让我们的效果更加自然。每一行的字符的选取最好是随机的。</p>
<p>但是要让 CSS 实现随机生成每一行的字符可太难了。所以这里我们请出 CSS 预处理器 SASS/LESS 。</p>
<p>而且由于不太可能利用 CSS 给单个标签内，譬如 <code><p></code> 标签插入字符，所以我们把标签内的字符展示，放在每个 <code><p></code> 元素的伪元素 <code>::before</code> 的 <code>content</code> 当中。</p>
<p>我们可以提前设置好一组字符串，然后利用 SASS function 随机生成每一次元素内的 <code>content</code>，伪代码如下：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-SASS copyable" lang="SASS">$str: 'ぁぃぅぇぉかきくけこんさしすせそた◁▣▤▥▦▧♂♀♥☻►◄▧▨♦ちつってとゐなにぬねのはひふへほゑまみむめもゃゅょゎをァィゥヴェォカヵキクケヶコサシスセソタチツッテトヰンナニヌネノハヒフヘホヱマミムメモャュョヮヲㄅㄉㄓㄚㄞㄢㄦㄆㄊㄍㄐㄔㄗㄧㄛㄟㄣㄇㄋㄎㄑㄕㄘㄨㄜㄠㄤㄈㄏㄒㄖㄙㄩㄝㄡㄥabcdefghigklmnopqrstuvwxyz123456789%@#$<>^&*_+';
$length: str-length($str);

@function randomChar() &#123;
    $r: random($length);
    @return str-slice($str, $r, $r);
&#125;

@function randomChars($number) &#123;
    $value: '';

    @if $number > 0 &#123;
        @for $i from 1 through $number &#123;
            $value: $value + randomChar();
        &#125;
    &#125;
    @return $value;
&#125;

p:nth-child(1)::before &#123;
    content: randomChars(25);
&#125;
p:nth-child(2)::before &#123;
    content: randomChars(25);
&#125;
p:nth-child(3)::before &#123;
    content: randomChars(25);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单解释下上面的代码：</p>
<ol>
<li><code>$str</code> 定义了一串随机字符串，<code>$length</code> 表示字符串的长度</li>
<li>randomChar() 中利用了 SASS 的 <code>random()</code> 方法，每次随机选取一个 0 - <code>$length</code> 的整形数，记为 <code>$r</code>，再利用 SASS 的 <code>str-slice</code> 方法，每次从 <code>$str</code> 中选取一个下标为 <code>$r</code> 的随机字符</li>
<li>randomChars() 就是循环调用 randomChar() 方法，从 <code>$str</code> 中随机生成一串字符串，长度为传进去的参数 <code>$number</code></li>
</ol>
<p>这样，每一列的字符，每次都是不一样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5559b74b934745a2a04da20f02368e30~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>当然，上述的方法我认为不是最好的，CSS 的伪元素的 <code>content</code> 是支持字符编码的，譬如 <code>content: '\3066';</code> 会被渲染成字符 <code>て</code>，这样，通过设定字符区间，配合 SASS function 可以更好的生成随机字符，但是我尝试了非常久，SASS function 生成的最终产物会在 <code>\</code> 和 <code>3066</code> 这样的数字间添加上空格，无法最终通过字符编码转换成字符，最终放弃...</p>
</blockquote>
<h2 data-id="heading-2">使用 CSS 实现打字效果</h2>
<p>OK，继续，接下来我们要使用 CSS 实现打字效果，就是让字符一个一个的出现，像是这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ce21d61a2a64f8e805c7b58d7d97a58~tplv-k3u1fbpfcp-zoom-1.image" alt="纯 CSS 实现文字输入效果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里借助了 animation 的 <code>steps</code> 的特性实现，也就是逐帧动画。</p>
<p>从左向右和从上向下原理是一样的，以从左向右为例，假设我们有 26 个英文字符，我们已知 26 个英文字符组成的字符串的长度，那么我们只需要设定一个动画，让它的宽度变化从 <code>0 - 100%</code> 经历 26 帧即可，配合 <code>overflow: hidden</code>，steps 的每一帧即可展出一个字符。</p>
<p>当然，这里需要利用一些小技巧，我们如何通过字符的数量知道字符串的长度呢？</p>
<p>划重点：<strong>通过等宽字体的特性，配合 CSS 中的 <code>ch</code> 单位</strong>。</p>
<blockquote>
<p>如果不了解什么是等宽字体族，可以看看我的这篇文章 -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS%2Fissues%2F6" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS/issues/6" ref="nofollow noopener noreferrer">《你该知道的字体 font-family》</a>。</p>
</blockquote>
<p>CSS 中，<code>ch</code> 单位表示数字 “0” 的宽度。如果字体恰巧又是等宽字体，即每个字符的宽度是一样的，此时 <code>ch</code> 就能变成每个英文字符的宽度，那么 <code>26ch</code> 其实也就是整个字符串的长度。</p>
<p>利用这个特性，配合 animation 的 <code>steps</code>，我们可以轻松的利用 CSS 实现打字动画效果：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Pure CSS Typing animation.<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">h1</span> &#123;
    <span class="hljs-attribute">font-family</span>: monospace;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">26ch</span>;
    <span class="hljs-attribute">white-space</span>: nowrap;
    <span class="hljs-attribute">overflow</span>: hidden;
    <span class="hljs-attribute">animation</span>: typing <span class="hljs-number">3s</span> <span class="hljs-built_in">steps</span>(<span class="hljs-number">26</span>, end);
&#125;

<span class="hljs-keyword">@keyframes</span> typing &#123;
    <span class="hljs-number">0</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">26ch</span>;
     &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就可以得到如下结果啦：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db1dc255137644c6b8c830ad0a666725~tplv-k3u1fbpfcp-zoom-1.image" alt="纯 CSS 实现文字输入效果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完整的代码你可以戳这里：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2FChokcoco%2Fpen%2FWXGoGB" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/Chokcoco/pen/WXGoGB" ref="nofollow noopener noreferrer">CodePen Demo -- 纯 CSS 实现文字输入效果</a></p>
<h3 data-id="heading-3">改造成竖向打字效果</h3>
<p>接下来，我们就运用上述技巧，改造一下。将一个横向的打字效果改造成竖向的打字效果。</p>
<p>核心的伪代码如下：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS">$str: <span class="hljs-string">'ぁぃぅぇぉかきくけこんさしすせそた◁▣▤▥▦▧♂♀♥☻►◄▧▨♦ちつってとゐなにぬねのはひふへほゑまみむめもゃゅょゎをァィゥヴェォカヵキクケヶコサシスセソタチツッテトヰンナニヌネノハヒフヘホヱマミムメモャュョヮヲㄅㄉㄓㄚㄞㄢㄦㄆㄊㄍㄐㄔㄗㄧㄛㄟㄣㄇㄋㄎㄑㄕㄘㄨㄜㄠㄤㄈㄏㄒㄖㄙㄩㄝㄡㄥabcdefghigklmnopqrstuvwxyz123456789%@#$<>^&*_+'</span>;
$length: <span class="hljs-built_in">str-length</span>($str);

<span class="hljs-keyword">@function</span> randomChar() &#123;
    $r: <span class="hljs-built_in">random</span>($length);
    <span class="hljs-keyword">@return</span> str-slice($str, $r, $r);
&#125;

<span class="hljs-keyword">@function</span> randomChars($number) &#123;
    $value: <span class="hljs-string">''</span>;

    <span class="hljs-keyword">@if</span> $number > <span class="hljs-number">0</span> &#123;
        <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through $number &#123;
            $value: $value + <span class="hljs-built_in">randomChar</span>();
        &#125;
    &#125;
    <span class="hljs-keyword">@return</span> $value;
&#125;

<span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">word-break</span>: break-all;
&#125;

<span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">::before</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-built_in">randomChars</span>(<span class="hljs-number">20</span>);
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">animation</span>: typing <span class="hljs-number">4s</span> <span class="hljs-built_in">steps</span>(<span class="hljs-number">20</span>, end) infinite;
&#125;

<span class="hljs-keyword">@keyframes</span> typing &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-number">25%</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就实现了竖向的打字效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/831c4c69f17446beb6c070043b420963~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，这样看上去比较整齐划一，缺少了一定的随机，也就缺少了一定的美感。</p>
<p>基于此，我们进行 2 点改造：</p>
<ol>
<li>基于动画的时长 <code>animation-time</code>、和动画的延迟 <code>animation-delay</code>，增加一定幅度内的随机</li>
<li>在每次动画的末尾或者过程中，重新替换伪元素的 <code>content</code>，也就是重新生成一份 <code>content</code></li>
</ol>
<p>可以借助 SASS 非常轻松的实现这一点，核心的 SASS 代码如下：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS">$n: <span class="hljs-number">3</span>;
$animationTime: <span class="hljs-number">3</span>;
$perColumnNums: <span class="hljs-number">20</span>;

<span class="hljs-keyword">@for</span> $i from <span class="hljs-number">0</span> through $n &#123;
    $<span class="hljs-attribute">content</span>: <span class="hljs-built_in">randomChars</span>($perColumnNums);
    $contentNext: <span class="hljs-built_in">randomChars</span>($perColumnNums);
    $delay: <span class="hljs-built_in">random</span>($n);
    $randomAnimationTine: #&#123;$animationTime + <span class="hljs-built_in">random</span>(<span class="hljs-number">20</span>) / <span class="hljs-number">10</span> - <span class="hljs-number">1</span>&#125;s;

    <span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$<span class="hljs-selector-tag">i</span>&#125;)<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: $content;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">animation</span>: typing-#&#123;$i&#125; $randomAnimationTine steps(<span class="hljs-number">20</span>, end) #&#123;$delay * <span class="hljs-number">0.1s</span> * -<span class="hljs-number">1</span>&#125; infinite;
    &#125;

    <span class="hljs-keyword">@keyframes</span> typing-#&#123;$<span class="hljs-selector-tag">i</span>&#125; &#123;
        <span class="hljs-number">0%</span> &#123;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
        &#125;
        <span class="hljs-number">25%</span> &#123;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        &#125;
        <span class="hljs-number">100%</span> &#123;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">content</span>: $contentNext;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看效果，已经有不错的改观：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/127734113-37703e90-67fc-477d-995f-478267447e80.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，上述由横向打字转变为竖向打字效果其实是有一些不一样的。在现有的竖向排列规则下，无法通过 ch 配合字符数拿到实际的竖向高度。所以这里有一定的取舍，实际放慢动画来看，没个字的现出不一定是完整的。</p>
<p>当然，在快速的动画效果下几乎是察觉不到的。</p>
<h2 data-id="heading-4">增加光影与透明度变化</h2>
<p>最后一步，就是增加光影及透明度的变化。</p>
<p>最佳的效果是要让每个新出现的字符保持亮度最大，同时已经出现过的字符亮度慢慢减弱。</p>
<p>但是由于这里我们无法精细操控每一个字符，只能操控每一行字符，所以在实现方式上必须另辟蹊径。</p>
<p>最终的方式是借用了另外一个伪元素进行同步的遮罩以实现最终的效果。下面我们就来一步一步看看过程。</p>
<h3 data-id="heading-5">给文字增添亮色及高光</h3>
<p>第一步就是给文字增添亮色及高光，这点非常容易，就是选取一个黑色底色下的亮色，并且借助 <code>text-shadow</code> 让文字发光。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">::before</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">179</span>, <span class="hljs-number">255</span>, <span class="hljs-number">199</span>);
    <span class="hljs-attribute">text-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">1px</span> <span class="hljs-number">#fff</span>, <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">2px</span> <span class="hljs-number">#fff</span>, <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> currentColor, <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">10px</span> currentColor;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看效果，左边是白色字符，中间是改变字符颜色，右边是改变了字体颜色并且添加了字体阴影的效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfc67604df4c4462a4e4686b226ed15c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">给文字添加同步遮罩</h3>
<p>接下来，就是在文字动画的行进过程中，同步添加一个黑色到透明的遮罩，尽量还原让每个新出现的字符保持亮度最大，同时已经出现过的字符亮度慢慢减弱。</p>
<p>这个效果的示意图大概是这样的，这里我将文字层和遮罩层分开，并且底色从黑色改为白色，方便理解：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/127735480-e7df1317-e0f2-4b84-8a22-59ea76a9d775.gif" alt="蒙层遮罩原理图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大概的遮罩的层的伪代码如下，用到了元素的另外一个伪元素：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">9</span>), transparent <span class="hljs-number">75%</span>, transparent);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">100%</span> <span class="hljs-number">220%</span>;
    <span class="hljs-attribute">background-repeat</span>: no-repeat;
    <span class="hljs-attribute">animation</span>: mask <span class="hljs-number">4s</span> infinite linear;
&#125;

<span class="hljs-keyword">@keyframes</span> mask &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">220%</span>;
    &#125; 
    <span class="hljs-number">30%</span> &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">0%</span>;
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">0%</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好，合在一起的最终效果大概就是这样：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/127735820-9ac92c0a-8f83-4b65-ba14-3ab7c51586a5.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过调整 <code>@keyframes mask</code> 的一些参数，可以得到不一样的字符渐隐效果，需要一定的调试。</p>
<h2 data-id="heading-7">完整代码及效果</h2>
<p>OK，拆解了一下主要的步骤，最后上一下完整代码，应用了 Pug 模板引擎和 SASS 语法。</p>
<p>完整代码加起来不过 100 行。</p>
<pre><code class="hljs language-Pug copyable" lang="Pug">.g-container
    -for(var i=0; i<50; i++)
        p
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-SCSS copyable" lang="SCSS"><span class="hljs-keyword">@import</span> url(<span class="hljs-string">'https://fonts.googleapis.com/css2?family=Inconsolata:wght@200&display=swap'</span>);

<span class="hljs-variable">$str</span>: <span class="hljs-string">'ぁぃぅぇぉかきくけこんさしすせそた◁▣▤▥▦▧♂♀♥☻►◄▧▨♦ちつってとゐなにぬねのはひふへほゑまみむめもゃゅょゎをァィゥヴェォカヵキクケヶコサシスセソタチツッテトヰンナニヌネノハヒフヘホヱマミムメモャュョヮヲㄅㄉㄓㄚㄞㄢㄦㄆㄊㄍㄐㄔㄗㄧㄛㄟㄣㄇㄋㄎㄑㄕㄘㄨㄜㄠㄤㄈㄏㄒㄖㄙㄩㄝㄡㄥabcdefghigklmnopqrstuvwxyz123456789%@#$<>^&*_+'</span>;
<span class="hljs-variable">$length</span>: str-length(<span class="hljs-variable">$str</span>);
<span class="hljs-variable">$n</span>: <span class="hljs-number">50</span>;
<span class="hljs-variable">$animationTime</span>: <span class="hljs-number">4</span>;
<span class="hljs-variable">$perColumnNums</span>: <span class="hljs-number">25</span>;

<span class="hljs-keyword">@function</span> randomChar() &#123;
    <span class="hljs-variable">$r</span>: random(<span class="hljs-variable">$length</span>);
    <span class="hljs-keyword">@return</span> str-slice(<span class="hljs-variable">$str</span>, <span class="hljs-variable">$r</span>, <span class="hljs-variable">$r</span>);
&#125;

<span class="hljs-keyword">@function</span> randomChars(<span class="hljs-variable">$number</span>) &#123;
    <span class="hljs-variable">$value</span>: <span class="hljs-string">''</span>;

    <span class="hljs-keyword">@if</span> <span class="hljs-variable">$number</span> > <span class="hljs-number">0</span> &#123;
        <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">1</span> through <span class="hljs-variable">$number</span> &#123;
            <span class="hljs-variable">$value</span>: <span class="hljs-variable">$value</span> + randomChar();
        &#125;
    &#125;
    <span class="hljs-keyword">@return</span> <span class="hljs-variable">$value</span>;
&#125;

<span class="hljs-selector-tag">body</span>, <span class="hljs-selector-tag">html</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#000</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">overflow</span>: hidden;
&#125;

<span class="hljs-selector-class">.g-container</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100vw</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: space-between;
    <span class="hljs-attribute">flex-wrap</span>: nowrap;
    <span class="hljs-attribute">flex-direction</span>: row;
    <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'Inconsolata'</span>, monospace, sans-serif;
&#125;

<span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">5vh</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
    <span class="hljs-attribute">text-align</span>: center;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">5vh</span>;
    <span class="hljs-attribute">word-break</span>: break-all;
    <span class="hljs-attribute">white-space</span>: pre-wrap;
    
    &<span class="hljs-selector-pseudo">::before</span>,
    &<span class="hljs-selector-pseudo">::after</span> &#123;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">overflow</span>: hidden;
    &#125;
&#125;

<span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">0</span> through <span class="hljs-variable">$n</span> &#123;
    <span class="hljs-variable">$content</span>: randomChars(<span class="hljs-variable">$perColumnNums</span>);
    <span class="hljs-variable">$contentNext</span>: randomChars(<span class="hljs-variable">$perColumnNums</span>);
    <span class="hljs-variable">$delay</span>: random(<span class="hljs-variable">$n</span>);
    <span class="hljs-variable">$randomAnimationTine</span>: #&#123;<span class="hljs-variable">$animationTime</span> + random(<span class="hljs-number">20</span>) / <span class="hljs-number">10</span> - <span class="hljs-number">1</span>&#125;s;
  
    <span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$i&#125;)<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-variable">$content</span>;
        <span class="hljs-attribute">color</span>: rgb(<span class="hljs-number">179</span>, <span class="hljs-number">255</span>, <span class="hljs-number">199</span>);
        <span class="hljs-attribute">text-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">1px</span> <span class="hljs-number">#fff</span>, <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">2px</span> <span class="hljs-number">#fff</span>, <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> currentColor, <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">10px</span> currentColor;
        <span class="hljs-attribute">animation</span>: typing-#&#123;<span class="hljs-variable">$i</span>&#125; <span class="hljs-variable">$randomAnimationTine</span> steps(<span class="hljs-number">20</span>, end) #&#123;<span class="hljs-variable">$delay</span> * <span class="hljs-number">0.1s</span> * -<span class="hljs-number">1</span>&#125; infinite;
        <span class="hljs-attribute">z-index</span>: <span class="hljs-number">1</span>;
    &#125;

    <span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$i&#125;)<span class="hljs-selector-pseudo">::after</span> &#123;
        <span class="hljs-variable">$alpha</span>: random(<span class="hljs-number">40</span>) / <span class="hljs-number">100</span> + <span class="hljs-number">0.6</span>;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
        <span class="hljs-attribute">background</span>: linear-gradient(rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-variable">$alpha</span>), rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-variable">$alpha</span>), rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-variable">$alpha</span>), transparent <span class="hljs-number">75%</span>, transparent);
        <span class="hljs-attribute">background-size</span>: <span class="hljs-number">100%</span> <span class="hljs-number">220%</span>;
        <span class="hljs-attribute">background-repeat</span>: no-repeat;
        <span class="hljs-attribute">animation</span>: mask <span class="hljs-variable">$randomAnimationTine</span> infinite #&#123;(<span class="hljs-variable">$delay</span> - <span class="hljs-number">2</span>) * <span class="hljs-number">0.1s</span> * -<span class="hljs-number">1</span>&#125; linear;
        <span class="hljs-attribute">z-index</span>: <span class="hljs-number">2</span>;
    &#125;

    <span class="hljs-keyword">@keyframes</span> typing-#&#123;<span class="hljs-variable">$i</span>&#125; &#123;
        0% &#123;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
        &#125;
        25% &#123;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        &#125;
        100% &#123;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">content</span>: <span class="hljs-variable">$contentNext</span>;
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> mask&#123;
    0% &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">220%</span>;
    &#125; 
    30% &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">0%</span>;
    &#125;
    100% &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">0%</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果也就是题图所示：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/127797308-fa170070-6e7a-4cae-baf3-2d8c6c4ae05c.gif" alt="Digital Char Rain Animation" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完整的代码及演示效果你可以戳这里：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2FChokcoco%2Fpen%2FbGWvNme" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/Chokcoco/pen/bGWvNme" ref="nofollow noopener noreferrer">CodePen Demo -- Digital Char Rain Animation</a></p>
<h2 data-id="heading-8">最后</h2>
<p>灵感源自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyuanchuan" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yuanchuan" ref="nofollow noopener noreferrer">袁川</a> 老师的这个效果 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fyuanchuan%2Fpen%2FYoqWeR" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/yuanchuan/pen/YoqWeR" ref="nofollow noopener noreferrer">CodePen Demo -- Matrix digital rain</a>，原效果使用了 JavaScript· 实现，本文利用纯 CSS 进行了演绎。</p>
<p>更多精彩 CSS 效果可以关注我的 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fcsscoco.com%2Finspiration%2F%23%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://csscoco.com/inspiration/#/" ref="nofollow noopener noreferrer">CSS 灵感</a></p>
<p>好了，本文到此结束，希望对你有帮助 :)</p>
<p>想 Get 到最有意思的 CSS 资讯，千万不要错过我的公众号 -- <strong>iCSS前端趣闻</strong> 😄</p>
<p>更多精彩 CSS 技术文章汇总在我的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS" ref="nofollow noopener noreferrer">Github -- iCSS</a> ，持续更新，欢迎点个 star 订阅收藏。</p>
<p>如果还有什么疑问或者建议，可以多多交流，原创文章，文笔有限，才疏学浅，文中若有不正之处，万望告知。</p></div>  
</div>
            