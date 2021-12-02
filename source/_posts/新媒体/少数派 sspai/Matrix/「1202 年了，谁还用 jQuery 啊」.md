
---
title: '「1202 年了，谁还用 jQuery 啊」'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/11/28/927f8baef9042d94f21feeb1ae60c811.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Sat, 27 Nov 2021 19:04:12 GMT
thumbnail: 'https://cdn.sspai.com/2021/11/28/927f8baef9042d94f21feeb1ae60c811.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-1eaafa2a><div class="content wangEditor-txt minHeight" data-v-1eaafa2a><p>在很久很久以前，工程师们通过 jQuery 操作 DOM 来在网页上实现一些交互。</p><p>后来，工程师们捣鼓出了框架。React 和 Vue 之类的前端框架让工程师们可以专注于描述数据和 UI 之间的关系，而不是直接去操作它们。渐渐地，没有人用 jQuery 了。</p><p>但万一我还是需要操作 DOM 呢？</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/11/28/927f8baef9042d94f21feeb1ae60c811.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/11/28/927f8baef9042d94f21feeb1ae60c811.png" referrerpolicy="no-referrer"></figure><p>几个月前我做了一个<a href="https://github.com/xingrz/awsl" target="_blank">脚本</a>，可以给网页版微博增加一些一键转发，可以给网页版微博增加一些一键转发<s>（一键 awsl）</s>的功能。由于涉及到大量直接操作 DOM 的需求，让我不得不又考虑引入 jQuery 来简化这些操作。</p><p>且慢。</p><p><strong>1202 年了，谁还用 jQuery 啊。</strong></p><p>于是我开始思考，1202 年了，如果我需要一个「jQuery」那么它应该具备什么特性？</p><ul><li>现代的模块化系统，而不是像 jQuery 那样直接暴露一个全局的 <code>$</code></li><li>必须是 TypeScript，JS 之光。<s>裸写 JavaScript 的都是恶魔。</s></li><li>Less is more</li></ul><p>一顿编码之后，我做出来一个原型。我将它取名叫 <a href="https://github.com/xingrz/dro" target="_blank">dro</a>。其实本来想叫 tquery 的，已经被抢注了。至于为啥叫 dro，我也忘了。<s>但是它足够短。</s></p><h3>基础查询</h3><pre class="language-javascript"><code>import &#123; $, $$ &#125; from 'dro';
const container = $<HTMLElement>(document, '.foo');
const children = $$(document, '.foo a');</code></pre><p>我认为像 jQuery 那样 <code>$()</code> 永远返回一个数组是为了简化问题而带来更多问题。所以参照以前使用 MooTools 的经历，决定用 <code>$()</code> 和 <code>$$()</code> 来区分需要得到一个元素还是多个元素的场景（本质上就只是 <code>querySelector</code> 和 <code>querySelectorAll</code> 的 alias 罢了）。</p><p>你还注意到，dro 利用了 TypeScript 的泛型。<code>$()</code> 可以带上泛型参数来取得这个类型的结果。比如 <code>$<HTMLInputElement>(document, '#username')</code>。</p><h3>批量查询</h3><pre class="language-javascript"><code>import &#123; $H &#125; from 'dro';

interface MyForm &#123;
  username: HTMLInputElement;
  password: HTMLInputElement;
  submit: HTMLElement;
&#125;

const form = $H<MyForm>(document, &#123;
  username: '.my-form input.user',
  password: '.my-form input.pass',
  submit: '.my-form button[type="submit"]',
&#125;);

console.log(form?.username.value);</code></pre><p>我写那个脚本的时候发现了一个需求。我经常需要同时 query 多个元素，并且一一对它们判空。有些时候，它们也不是简单的 HTMLElement，而是 HTMLInputElement 之类带有更多特性的元素。于是我带来了 <code>$H()</code> 这个函数。</p><p>它同样利用了 TypeScript 的泛型特性。你需要先声明一个 interface 来描述你需要的字段和对应的类型，然后通过参数传给函数。同时传给函数的还有对应 interface 中每个字段的 CSS selector（利用 TypeScript 的特性，编辑器会提示你需要哪些字段，确保没有遗漏或拼错）。</p><p>如果 interface 中声明的元素通过对应的 CSS selector 全部能得到，那么 <code>$H()</code> 会返回这个对象。否则，只要任意一个 CSS selector 不满足，返回 <code>null</code>。</p><h3>其它一些 HTML 操作函数</h3><pre class="language-javascript"><code>import &#123; append, create, html, attrs, style, on &#125; from 'dro';

append(document.body, () => &#123;
  const el = create('div');
  html(el, 'foo');
  attrs(el, &#123;
    'class': 'foo',
  &#125;);
  style(el, &#123;
    'margin-top': '200px',
  &#125;);
  on(el, 'click', () => console.log('lol!'));
  return el;
&#125;);</code></pre><p>这一部分只满足了我自己开发那个脚本时的需求。以后可能会增改。</p><p>这里的 <code>append()</code> 传入的不是一个已经创建好的元素，而是一个 creator 闭包。这是因为我不希望这个需要被 append 到某处的元素创建过程中用到的一些变量被暴露到外面来。</p><h3>总结</h3><p>以上就是我对 dro 的一些设计思路。目前这个库仅作为原型发布。可能将来某一天想法成熟了，会作为一个严肃项目进行维护。当然，也可能咕咕咕…</p><p>感谢阅读。</p></div><!----></div><div style="border:1px solid transparent;" data-v-1eaafa2a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-1eaafa2a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>7</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>3</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-5152" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E3%80%8C1202%20%E5%B9%B4%E4%BA%86%EF%BC%8C%E8%B0%81%E8%BF%98%E7%94%A8%20jQuery%20%E5%95%8A%E3%80%8D%E3%80%91%E5%9C%A8%E5%BE%88%E4%B9%85%E5%BE%88%E4%B9%85%E4%BB%A5%E5%89%8D%EF%BC%8C%E5%B7%A5%E7%A8%8B%E5%B8%88%E4%BB%AC%E9%80%9A%E8%BF%87jQuery%E6%93%8D%E4%BD%9CDOM%E6%9D%A5%E5%9C%A8%E7%BD%91%E9%A1%B5%E4%B8%8A%E5%AE%9E%E7%8E%B0%E4%B8%80%E4%BA%9B%E4%BA%A4%E4%BA%92%E3%80%82%E5%90%8E%E6%9D%A5%EF%BC%8C%E5%B7%A5%E7%A8%8B%E5%B8%88%E4%BB%AC%E6%8D%A3%E9%BC%93%E5%87%BA%E4%BA%86%E6%A1%86%E6%9E%B6%E3%80%82React%E5%92%8CVue%E4%B9%8B%E7%B1%BB%E7%9A%84%E5%89%8D%E7%AB%AF%E6%A1%86%E6%9E%B6%E8%AE%A9%E5%B7%A5%E7%A8%8B%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-3339" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E3%80%8C1202%20%E5%B9%B4%E4%BA%86%EF%BC%8C%E8%B0%81%E8%BF%98%E7%94%A8%20jQuery%20%E5%95%8A%E3%80%8D%E3%80%91%E5%9C%A8%E5%BE%88%E4%B9%85%E5%BE%88%E4%B9%85%E4%BB%A5%E5%89%8D%EF%BC%8C%E5%B7%A5%E7%A8%8B%E5%B8%88%E4%BB%AC%E9%80%9A%E8%BF%87jQuery%E6%93%8D%E4%BD%9CDOM%E6%9D%A5%E5%9C%A8%E7%BD%91%E9%A1%B5%E4%B8%8A%E5%AE%9E%E7%8E%B0%E4%B8%80%E4%BA%9B%E4%BA%A4%E4%BA%92%E3%80%82%E5%90%8E%E6%9D%A5%EF%BC%8C%E5%B7%A5%E7%A8%8B%E5%B8%88%E4%BB%AC%E6%8D%A3%E9%BC%93%E5%87%BA%E4%BA%86%E6%A1%86%E6%9E%B6%E3%80%82React%E5%92%8CVue%E4%B9%8B%E7%B1%BB%E7%9A%84%E5%89%8D%E7%AB%AF%E6%A1%86%E6%9E%B6%E8%AE%A9%E5%B7%A5%E7%A8%8B%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            