
---
title: 'Electron+Vue3 MAC 版日历开发记录(7)——Menubar   时间显示'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 05:42:06 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天开始说到了 Mac Menubar 的功能显示了。</p>
<h2 data-id="heading-0">开篇之前</h2>
<p>Mac 有一个不太起眼却又非常有价值的地方——顶部菜单右边的 Menubar。事实上，Mac 的 Menubar 设计绝不是仅仅和 Windows 一样的展示常驻后台的程序，它依托于顶部 Menubar 的「任何情况都会存在」的特性。扩展了 Mac 下与其他应用的交互，从简单的展示到快捷的操作，用好 Menubar 是可以有效提升 Mac 效率。</p>
<p>所以，一样的，我也想在开发的 Mac 日历也有这样的展示功能。</p>
<h2 data-id="heading-1">Electron Tray</h2>
<p>这里就不得不先介绍 Electron's Tray。</p>
<blockquote>
<p>含义：添加图标和上下文菜单到系统通知区
官方文档：<a href="https://www.electronjs.org/docs/api/tray" target="_blank" rel="nofollow noopener noreferrer">www.electronjs.org/docs/api/tr…</a></p>
</blockquote>
<p>在本项目中，主要借鉴 <a href="https://github.com/mzdr/timestamp" target="_blank" rel="nofollow noopener noreferrer">Timestamp</a>，封装成 <code>TrayService</code>：</p>
<pre><code class="copyable">import type &#123; Rectangle&#125; from 'electron';
import &#123; Tray, nativeImage&#125; from 'electron';
export default class TrayService &#123;
  tray: Tray;
  label: string;
  clickHandler: any;

  constructor() &#123;
    this.label = '';
    const icon = nativeImage.createEmpty();
    this.tray = new Tray(icon);
    this.tray.on('click', () => (this.clickHandler || (() => &#123;&#125;))());
  &#125;

  getBounds(): Rectangle &#123;
    return this.tray.getBounds();
  &#125;

  getLabel(): string &#123;
    return this.label;
  &#125;

  setLabel(label: string): this &#123;
    if (this.tray.isDestroyed()) &#123;
      return this;
    &#125;

    this.tray.setTitle((this.label = label));
    return this;
  &#125;

  onClick(fn: any): void &#123;
    this.clickHandler = fn;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里主要介绍代码：</p>
<ol>
<li>因为我没设计好这个产品的 Icon，所以这里先置空；</li>
<li>Label 的内容有外部控制，今天主要是显示「农历 星期 时间」三个元素信息，之后还会有更复杂的内如呈现 (<strong>这里先保密</strong>)；</li>
<li><code>click</code> 事件，这个好理解，只要点击 Tray，Electron 显示或者消失;</li>
<li>因为要做到日历的 Electron 显示在 Menubar 正下方，所以需要借助 <code>getBounds()</code> 值，具体查看文档：<a href="https://www.electronjs.org/docs/api/tray#traygetbounds-macos-windows" target="_blank" rel="nofollow noopener noreferrer">www.electronjs.org/docs/api/tr…</a></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd2797cc6774a63b7d3fc1e96b0d836~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Electron 显示</h2>
<p>完成了 <code>TrayService</code>，现在需要把 Electron 显示在其正下方。</p>
<pre><code class="copyable">// Tray 点击事件，获取 getBounds()，为 Election 显示服务
this.trayService.onClick(() => &#123;
  const bounds = this.trayService.getBounds();
  const currentMousePosition = screen.getCursorScreenPoint();
  const currentDisplay = screen.getDisplayNearestPoint(
    currentMousePosition,
  );
  this.setPosition(bounds.x + bounds.width / 2, currentDisplay.workArea.y);

  if (this.isVisible()) &#123;
    this.hide();
  &#125; else &#123;
    this.show();
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看 <code>this.setPosition()</code> 方法：</p>
<pre><code class="copyable">setPosition(x: number, y: number, centerToX = true): this &#123;
this.window.setPosition(
  centerToX ? Math.round(x - this.window.getSize()[0] / 2) : x,
  y,
);
return this;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">内容输出</h2>
<p>万事具备，只欠我们需要展示的内容。今天只是动态显示：「农历 星期 时间」。</p>
<p>为了配合动态实时显示效果，需要借助定时器功能，这里封装为：<code>ClockService</code>，直接看代码：</p>
<pre><code class="copyable">'use strict';

import &#123; app &#125; from 'electron';
const Moment = require('moment');
import LunarService from './LunarService';

export default class ClockService &#123;
  format: any;
  onTickHandler: any;
  intervalId: any;
  constructor() &#123;
    Moment.locale(app.getLocale());
    // this.setFormat("MM/DD HH:mm:ss");
    // lll
    this.setFormat('MMMDo dddd HH:mm:ss');
    this.start();
  &#125;

  start(): this &#123;
    if (typeof this.onTickHandler !== 'function') &#123;
      this.onTickHandler = () => &#123;&#125;;
    &#125;

    this.intervalId = setInterval(() => this.onTickHandler(this), 1000);

    return this;
  &#125;

  stop(): this &#123;
    if (this.intervalId) &#123;
      this.intervalId = clearInterval(this.intervalId);
    &#125;

    return this;
  &#125;

  onTick(callback: any): this &#123;
    this.onTickHandler = callback;

    return this;
  &#125;

  getFormat(): any &#123;
    return this.format;
  &#125;

  setFormat(format: any): this &#123;
    if (typeof format !== 'string') &#123;
      return this;
    &#125;

    this.format = format;

    return this;
  &#125;

  toString(): string &#123;
    const lunarService = new LunarService();
    const dayTextInChinese = lunarService.showNongliData(true);
    return dayTextInChinese + ' ' + Moment().format(this.getFormat());
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信大家都能理解这功能的含义了。在定时器执行时，实时拿到显示的内容，填充到 Tray 的 <code>Label</code> 上：</p>
<pre><code class="copyable">this.clockService.onTick((clock: &#123; toString: () => string; &#125;) => &#123;
  this.trayService.setLabel(clock.toString());
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以具体只看上面的 <code>clock.toString()</code> 函数了，显示农历数据 + <code>Moment()</code> 值。</p>
<p>这个「农历数据」和日历每个日期里展示的一致，看之前笔记的应该不陌生了：</p>
<pre><code class="copyable">showNongliData(changeShowFestivals: boolean): string &#123;

if (changeShowFestivals) &#123;
  const solarFestivals = this.solar.getFestivals();

  if (solarFestivals.length > 0) &#123;
    return solarFestivals.join(' ');
  &#125;

  const lunarFestivals = this.lunar.getFestivals();

  if (lunarFestivals.length > 0) &#123;
    return lunarFestivals.join(' ');
  &#125;
&#125;

return this.lunar.getJieQi() ||
`$&#123;this.lunar.getMonthInChinese()&#125;月$&#123;this.lunar.getDayInChinese()&#125;`;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">小结</h2>
<p>哦了，最后，我们 <code>yarn watch</code> 直接看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9280e9011ee545ba901705013ead52c0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于 Memubar 上内容的显示，有待于下一步不断的挖掘。</p>
<blockquote>
<p>注：随着时间的推移，发现 Timestamps 使用了新的时间组件：<a href="https://date-fns.org/" target="_blank" rel="nofollow noopener noreferrer">date-fns</a>，可能下一阶段我也会参考使用这个，目前阶段因为 FullCalendar 也是使用的 Moment.js，所以我还是沿用使用这个组件，尽可能减少第三方的引入和减小软件的体积。</p>
</blockquote>
<p>今天算是开始涉猎 Electron 的开发了，至于更多的 Electron 功能我们继续折腾，未完待续！</p>
<p>这个项目的所有记录基本放进专栏里了，欢迎查看：
<a href="https://juejin.cn/column/6968672386895839269" target="_blank">Electron+Vue3 MAC 版日历开发记录</a></p></div>  
</div>
            