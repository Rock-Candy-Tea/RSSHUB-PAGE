
---
title: '仿gitee贡献日历图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9569'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:22:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=9569'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>不干活，摸鱼，就是玩..</p>
</blockquote>
<p>项目不着急的时候就想搞点新花样给自己网站上增点彩，于是乎便看上了 <strong>gitee</strong> 上的贡献日历，一开始还真没想着自己搞，嫌麻烦想找现成，但是 <strong>goo</strong> 一圈了之后又回到了原点，虽然有那几个类似，但都不是我想要设计 <strong>UI</strong> 效果，经常逛豆瓣看电影或者设置想看的书的时候，个人书影栏目会有一个那样的展示日历，效果符合预期，开整。</p>
<h1 data-id="heading-0">功能需求</h1>
<ol>
<li>需要有一个横向日历展示（...）。</li>
<li>日历需要展示 <code>hover</code> 当天的日期和发文次数。</li>
<li>倒叙排列的日历需要去掉前后多余的日期，且有一个开始的时间。</li>
<li>日历需要年份展示，且有横向滚动监听年份变化处理。</li>
</ol>
<p>目前好像就只有四个比较突出的功能点，一些不重要的细节就不写在上面了，为了实现上面的功能，我就上面展开一些思考的问题。</p>
<ul>
<li>从布局的角度去考虑怎么设计？</li>
<li>如何去做日历的倒叙排列？</li>
<li>一个月中的开始时段和结束时段的前后日期如何去处理？</li>
<li>怎么去监听日历的横向滚动变化，从而设置年份的变化？</li>
</ul>
<p>这是我开始写之前面对这几个问题，也折腾的几天，下面针对着这几个问题一个个击破。</p>
<h2 data-id="heading-1">从css的布局的角度去考虑怎么设计？</h2>
<p>从 <strong>gitee</strong> 上f12看到的代码写法是 <code>div</code> 式的布局，但是看另外的 <strong>goo</strong> 到的是使用的 <code>svg</code> 格式的写法。两者有优缺点， <code>div</code> 布局简单粗暴，要多少个就写多少个，但缺点是很多繁杂的 <code>dom</code> 操作和遍历；而 <code>svg</code> 则是需要定位来布局，缺点是计算定位的距离等。 <code>svg</code> 我没尝试过，计算搞来搞去头大，索性就直接用 <code>div</code> 加 <code>flex</code> 梭哈得了。 容器布局基本长这样：</p>
<pre><code class="copyable"><div class="git">
  <div class="git-box">
    <div class="git-left"></div>
    <div class="git-right">
      <div class="git-wrap">
        <div class="git-content">
          <div class="month">
            <div class="year">年份</div>
            <div class="title">月份</div>
            <div class="week">
              <div class="day">1号</div>
            </div>
            <div class="week"></div>
          </div>
        </div>
        <div class="git-year">2021</div>
      </div>
    </div>
  </div>
  <div class="git-color"></div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>布局很好理解，一个容器里面，包含左边的日期周几，右边的滚动的容器，里面包含需要滚动的月份，其中月份里面会有 <code>title</code> 和 <code>year</code> 年份设定，为了之后获取方便。设定好布局结构之后就开始写我们常用的插件模式啦。这里有个细节的布局是，<strong>为了不让滚动条在容器内影响美观，特意在多写了一个盒子，撑开父级的高度，让滚动条居于容器外部</strong>。</p>
<p>说到写插件这个地方，我多说一句，最近在面试的过程中也会问有没有自己写过插件，这时候有很多人都说没有写过，说写过一写组件的封装，这其实是考验面试着自己的学习能力和动手能力，简单的功能组件封装是很浅的一部分（复杂的当我没说...），至少也要自己动手做过一些。这里我就写一个简单的插件封装格式，不会的同志可以直接照葫芦画瓢，搞里头！</p>
<p>基本格式如下：</p>
<pre><code class="copyable">(function(window)&#123;
  // params 标示传过来的参数
  var Git = function(params) &#123;
    // 可以使用 extend 重新拷贝一份
    this.extend(this.params, params)
  &#125;
​
  Git.prototype = &#123;
    // 这里就是默认参数啦，如果new 的过程没有传入参数，就是用这里的参数即可
    params: &#123;
      data: null
    &#125;,
    ...
    // 简单的拷贝
    extend: function (a, b) &#123;
      for (var key in b) &#123;
        if (b.hasOwnProperty(key)) &#123;
          a[key] = b[key]
        &#125;
      &#125;
      return a
    &#125;
  &#125;
​
  window.Git = Git;
&#125;)(window)
​
// 这样就可以在外面直接， new Git()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在好了，布局和插件格式都已经处理完成，开撸！</p>
<h2 data-id="heading-2">如何去做日历的倒叙排列？</h2>
<p>在做排序之前，我想到一个问题。优先看到是今天的日期，滚动到后面看到的是开始的节点，如果是倒着排列，那么必然日历也要倒着排列，因为从 <code>querySelectorAll('.day')</code> 获取的日期的时候就是从前往后获取的而不是从后面开始获取，所以日历也需要倒着排列。</p>
<p>接下来要获取一下今天的日期到开始的日期的时间月份差，这样就可以知道要循环几次的月份，再循环的过程中，使用 <code>insertAdjacentHTML</code> 的方法传入参数是 <code>afterbegin</code> ,在文档的最前面添加<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FElement%2FinsertAdjacentHTML" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Element/insertAdjacentHTML" ref="nofollow noopener noreferrer">MDN地址</a> 。
获取循环得到的时间</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取开始日期的时间</span>
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(startDate)
<span class="hljs-comment">// 设置当前月份的Date，跟随月份递增</span>
date.setMonth(date.getMonth() + i);
<span class="hljs-keyword">var</span> year = date.getFullYear();
<span class="hljs-keyword">var</span> month = date.getMonth();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取当前月份的是从哪个日期开始的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> setCurrentDate = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(year, month, <span class="hljs-number">1</span>);
<span class="hljs-keyword">var</span> firstDay = setCurrentDate.getDay();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置每个月的月份，这里使用的是索引 0，而不是 i 是因为倒叙的关系，只获取第一个 dom 元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">element.querySelectorAll(<span class="hljs-string">'.title'</span>)[<span class="hljs-number">0</span>].innerHTML = monthMap[month]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在获取一年之中的月份日期数，这里有一个需要判断的地方是，闰年2月为28的情况。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> months = [<span class="hljs-number">31</span>, <span class="hljs-built_in">this</span>.isLeapYear(year) ? <span class="hljs-number">29</span> : <span class="hljs-number">28</span>, <span class="hljs-number">31</span>, <span class="hljs-number">30</span>, <span class="hljs-number">31</span>, <span class="hljs-number">30</span>, <span class="hljs-number">31</span>, <span class="hljs-number">31</span>, <span class="hljs-number">30</span>, <span class="hljs-number">31</span>, <span class="hljs-number">30</span>, <span class="hljs-number">31</span>];
<span class="hljs-comment">// 判断 平年闰年[四年一闰，百年不闰，四百年再闰]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isLeapYear</span>(<span class="hljs-params">year</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (year % <span class="hljs-number">4</span> === <span class="hljs-number">0</span>) && (year % <span class="hljs-number">100</span> !== <span class="hljs-number">0</span> || year % <span class="hljs-number">400</span> === <span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取一个月内有多少周 （一周7天，所以要除以7），这样就可以设置对应月份里面 week</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> weeks = <span class="hljs-built_in">Math</span>.ceil((firstDay + months[month]) / <span class="hljs-number">7</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">一个月中的开始时段和结束时段的前后日期如何去处理？</h2>
<p>有了当月的开始时间，那也必然要获取到上个月的时间天数了，这样才可以把当月之前上个月的日期给补上。比如说，这个7月开始的时间1号对应的是第一周的周四，那么获取上个月的是时间只有30天，那就可以在周三的时候30循环--直到27号，这样的话最后的一周可以去掉。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> lastMonth = (month - <span class="hljs-number">1</span> >= <span class="hljs-number">0</span>) ? (months[month - <span class="hljs-number">1</span>]) : <span class="hljs-number">31</span>;
<span class="hljs-comment">// 设置每个月有多少周，最后减一是为了去掉最后一周，因为在第一周的时候加上了上个月的时间</span>
<span class="hljs-comment">// 这里有个注意的地方是，如果当月的最后一天如果是周日，就不需要再去减掉最后一周，可以直接显示出来</span>
<span class="hljs-comment">// 这里的len 是表示最后需要截止多少日</span>
date.setMonth(date.getMonth() + <span class="hljs-number">1</span>);
<span class="hljs-keyword">var</span> lastDay = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(date.setDate(<span class="hljs-number">0</span>)).getDay();
<span class="hljs-keyword">var</span> len = <span class="hljs-number">0</span>;
<span class="hljs-keyword">if</span> (i !== diffMonth - <span class="hljs-number">1</span> && lastDay !== <span class="hljs-number">6</span>) &#123;
  weeks = weeks - <span class="hljs-number">1</span>;
  len = <span class="hljs-number">0</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
  len = <span class="hljs-number">7</span> - lastDay;
&#125;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>; j < weeks; j++) &#123;
  <span class="hljs-keyword">var</span> whtml = <span class="hljs-string">'<div class="week">'</span> +
    <span class="hljs-string">'<div class="day less"></div>'</span> +
    <span class="hljs-string">'<div class="day less"></div>'</span> +
    <span class="hljs-string">'<div class="day less"></div>'</span> +
    <span class="hljs-string">'<div class="day less"></div>'</span> +
    <span class="hljs-string">'<div class="day less"></div>'</span> +
    <span class="hljs-string">'<div class="day less"></div>'</span> +
    <span class="hljs-string">'<div class="day less"></div>'</span> +
    <span class="hljs-string">'</div>'</span>
  element.querySelectorAll(<span class="hljs-string">'.month'</span>)[<span class="hljs-number">0</span>].insertAdjacentHTML(<span class="hljs-string">'beforeEnd'</span>, whtml)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>以上的过程都走完了，就会的到一个 <code>month</code> 的节点，再通过这个节点去找到下面所有的 <code>day</code> 节点，最后再通过反向操作逐个添加相应的属性和对比数据。具体看代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> days = element.querySelectorAll(<span class="hljs-string">'.month'</span>)[<span class="hljs-number">0</span>].querySelectorAll(<span class="hljs-string">'.day'</span>);
<span class="hljs-comment">// 保存临时变量使用</span>
<span class="hljs-keyword">var</span> _firstDay = firstDay;
<span class="hljs-keyword">var</span> _month = month;
<span class="hljs-keyword">var</span> _year = year;
<span class="hljs-comment">// 每日的日期</span>
<span class="hljs-keyword">var</span> day = <span class="hljs-number">0</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> m = days.length; m > len; m--) &#123;
  day++
  <span class="hljs-keyword">var</span> d = --_firstDay;
  <span class="hljs-comment">// 因为是倒叙，所以就减 1 来获取索引</span>
  <span class="hljs-keyword">var</span> dayIndex = m - <span class="hljs-number">1</span>;
  <span class="hljs-comment">// 获取上个月的最后一周的时间段 天数 </span>
  <span class="hljs-keyword">var</span> lastDays = dayIndex - firstDay;
  <span class="hljs-comment">// 给当月的 1号 的前面加上 上个月的日期</span>
  <span class="hljs-keyword">if</span> (m > days.length - firstDay) &#123;
    <span class="hljs-comment">// 去掉第一个月的第一周里面的上一个月的末尾日期</span>
    <span class="hljs-keyword">if</span> (i === <span class="hljs-number">0</span>) &#123;
      days[dayIndex].classList.add(<span class="hljs-string">'none'</span>)
    &#125;
    <span class="hljs-comment">// 当时间到 12 月时需要重新设置一下年份和月份</span>
    <span class="hljs-keyword">if</span> (month === <span class="hljs-number">0</span>) &#123;
      _month = <span class="hljs-number">12</span>
      _year = year - <span class="hljs-number">1</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      _month = month
      _year = year
    &#125;
    <span class="hljs-keyword">var</span> num = <span class="hljs-built_in">this</span>.parseDate(days[dayIndex], _year, _month, lastMonth - d)
    days[dayIndex].setAttribute(<span class="hljs-string">'data-time'</span>, _year + <span class="hljs-string">'-'</span> + _month + <span class="hljs-string">'-'</span> + (lastMonth - d))
    days[dayIndex].setAttribute(<span class="hljs-string">'data-tit'</span>, num + <span class="hljs-string">'次发文：'</span> + _year + <span class="hljs-string">'-'</span> + _month + <span class="hljs-string">'-'</span> + (lastMonth - d))
  &#125;
  <span class="hljs-keyword">if</span> (!days[lastDays]) <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">var</span> num = <span class="hljs-built_in">this</span>.parseDate(days[lastDays], year, month + <span class="hljs-number">1</span>, day)
  days[lastDays].setAttribute(<span class="hljs-string">'data-time'</span>, year + <span class="hljs-string">'-'</span> + (month + <span class="hljs-number">1</span>) + <span class="hljs-string">'-'</span> + day)
  days[lastDays].setAttribute(<span class="hljs-string">'data-tit'</span>, num + <span class="hljs-string">'次发文：'</span> + year + <span class="hljs-string">'-'</span> + (month + <span class="hljs-number">1</span>) + <span class="hljs-string">'-'</span> + day)
  <span class="hljs-comment">// 去掉最后一个月之中从当前日期往后的日期</span>
  <span class="hljs-keyword">if</span> (i === diffMonth - <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">if</span> (day > currentDate.getDate()) &#123;
      days[lastDays].classList.add(<span class="hljs-string">'none'</span>)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>parseDate</code> 是比较函数，根据传值过来的 <code>data</code> 数据和日期比较，如果时间相等就添加次数加 1，最后返回次数，添加到自定义属性中，方便后续的获取。
在使用自定义属性时，为了使鼠标可以 <code>hover</code> 展示数据就使用了伪类处理，通过 <code>attr()</code> 函数来获取的节点上的相关属性，这样也方便操作不需要重新在 <code>JS</code> 中写提示相关的代码。有一个小细节，这里在赋值 <code>setAttribute('data-tit', '我是一只小小鸟！')</code> 属性去通过 <code>attr()</code> 获取时，我本想是加入换行的字符，但是不管如何去操作都不得成功。通过查阅资料和操作得知，只有直接写在节点上的属性加上 \A 才可以实现换行，这里我用的另外一个方法，那就是在content 中获取两个属性，中间用 \A 把这两个拼接起来，结果是完美的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1</span>
<div data-tit=<span class="hljs-string">"哈哈哈\A啦啦啦"</span>></div>
<span class="hljs-comment">// 2</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">data-tit</span>=<span class="hljs-string">"哈哈哈"</span> <span class="hljs-attr">data-time</span>=<span class="hljs-string">"啦啦啦"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">::before</span> &#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-built_in">attr</span>(data-tit)
&#125;
// 这里不需要加上 + 号
<span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">::after</span> &#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-built_in">attr</span>(data-tit)<span class="hljs-string">"\A"</span><span class="hljs-built_in">attr</span>(data-time)
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">怎么去监听日历的横向滚动变化，从而设置年份的变化？</h2>
<p>最后一步监听滚动的变化也好处理，写一个监听事件，然后获取这个节点滚动的 <code>scrollLeft</code> 属性。先把每一个年份出现的节点距离左边的距离拿到放进一个数组里面，在滚动的时候去监听滚动的具体来判断是哪个年份的中间，最后添加其给定的样式即可。具体代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> allMonths = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'.month'</span>);
<span class="hljs-keyword">var</span> yearList = [];
<span class="hljs-keyword">var</span> listWidth = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> q = <span class="hljs-number">0</span>; q < allMonths.length; q++) &#123;
  <span class="hljs-keyword">var</span> item = allMonths[q]
  <span class="hljs-keyword">if</span> (item.querySelector(<span class="hljs-string">'.year'</span>).getAttribute(<span class="hljs-string">'data-year'</span>)) &#123;
    listWidth.push(item.offsetLeft);
    yearList.push(item);
  &#125;
&#125;
<span class="hljs-comment">// 偏移量，最好 0 - 10 之间</span>
<span class="hljs-keyword">var</span> distance = <span class="hljs-number">8</span>;
<span class="hljs-built_in">this</span>.addEvent(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.git-wrap'</span>), <span class="hljs-string">'scroll'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-keyword">var</span> scrollX = e.target.scrollLeft;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < listWidth.length; i++) &#123;
    <span class="hljs-keyword">var</span> width1 = listWidth[i];
    <span class="hljs-keyword">var</span> width2 = listWidth[i + <span class="hljs-number">1</span>];
    <span class="hljs-keyword">if</span> (scrollX > width1 && scrollX < width2) &#123;
      <span class="hljs-keyword">if</span> (width2 - scrollX < TITLE_WIDTH + distance) &#123;
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.git-year'</span>).innerHTML = yearList[i + <span class="hljs-number">1</span>].querySelector(<span class="hljs-string">'.year'</span>).getAttribute(<span class="hljs-string">'data-year'</span>)
        yearList[i + <span class="hljs-number">1</span>].querySelector(<span class="hljs-string">'.year'</span>).classList.add(<span class="hljs-string">'active'</span>)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.git-year'</span>).innerHTML = yearList[i].querySelector(<span class="hljs-string">'.year'</span>).getAttribute(<span class="hljs-string">'data-year'</span>)
        yearList[i + <span class="hljs-number">1</span>].querySelector(<span class="hljs-string">'.year'</span>).classList.remove(<span class="hljs-string">'active'</span>)
      &#125;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">结束</h1>
<p>完结撒花🎉
以上差不多都算是完成了本次的代码插件化，有很多也是边做边查，一开始不是很顺利，但是做的这个过程痛并快乐，一是奇怪的姿势又涨了一点，二是又可以把做的分享给大家。</p>
<p>纯JS手写，懒得用es6了，写的不好，轻一点...</p>
<p>代码实地<a href="https://link.juejin.cn/?target=https%3A%2F%2Fluszy.com%2Fhome%2Farchives.html" target="_blank" rel="nofollow noopener noreferrer" title="https://luszy.com/home/archives.html" ref="nofollow noopener noreferrer">查看</a>，已上传 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FZHOUYUANN%2Fgit-calendar" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ZHOUYUANN/git-calendar" ref="nofollow noopener noreferrer">github</a> ，觉得还行给个鼓励。</p></div>  
</div>
            