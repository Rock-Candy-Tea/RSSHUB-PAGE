
---
title: 'Electron+Vue3 MAC 版日历开发记录(30)——告一段落'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 07:35:46 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第30天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>终于到最后一天了，反观这一个月，自己没想到能够坚持下来，每天都挺忙的，也逼着自己没天晚上，不看电视，不玩游戏，不做一些没意义的事情，把所有时间用回来，第一件事就是把当天的记录整理出来，有时候都是一边写代码一边往 Markdown 编辑器粘贴 (这里感谢下 MWeb 这款编辑器，让我省心太多了)。</p>
<p>今天还是有点水，主要还是放在 Warning 的优化上，看看今晚还剩下 21 个 Warning。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edeb3c0dc5fc4a8ea4ad6143c056e262~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看 VSCode 也能看出具体在哪行代码上：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ca46673dc8f4b17934a207350225af6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>相比于之前的 50 多个，已然少了很多了，着实有点小开心～</p>
<h2 data-id="heading-0">优化 events</h2>
<p>具体看看这个案例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/009dbaa28bad4ed78b67b17e603a21fe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实这个 events 数组在子组件里，我们有引用到 FullCalendar 里定义的 Type：</p>
<pre><code class="copyable">// FullcalendarSub.vue

import type &#123;
  CalendarApi,
  CalendarOptions,
  DateSelectArg,
  EventClickArg,
  EventInput,
  EventSourceInput,
  DateRangeInput,
  DateInput,
  DayCellContentArg,
&#125; from '@fullcalendar/vue3';

  props: &#123;
    changeShowFestivals: Boolean,
    changeShowWeather: Boolean,
    events: &#123;
      type: Array,
      default: [] as EventInput[],
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以这里需要追本溯源找到从 Notion API 返回的数据做类型转变。刚巧，我们的 EventService 返回的结果也没加 return type。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bd66d28a1594388a8db4bb835535495~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以可以一并重构了。</p>
<p>先看看 EventInput 追踪代码：</p>
<pre><code class="copyable">declare const EVENT_REFINERS: &#123;
    extendedProps: Identity<Dictionary>;
    start: Identity<DateInput>;
    end: Identity<DateInput>;
    date: Identity<DateInput>;
    allDay: BooleanConstructor;
    id: StringConstructor;
    groupId: StringConstructor;
    title: StringConstructor;
    url: StringConstructor;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中包含了这几个参数，所以我们可以直接 <code>as</code>：</p>
<pre><code class="copyable">// EventService.ts

import type &#123; EventInput &#125; from '@fullcalendar/vue3';


  list2Events(results: []): EventInput[] &#123;
    const events = results.map((element: any) => &#123;
      return &#123;
        'id': element.id,
        'title': element.properties?.title?.rich_text[0].plain_text,
        'start': element.properties?.start?.date.start,
        'end': element.properties?.end?.date.start,
      &#125; as EventInput;
    &#125;);

    return events;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再回到 Main 页面，我们重新在 data 中去定义我们的 events：</p>
<pre><code class="copyable">// FullCalendarMain.vue

  data() &#123;
    return &#123;
      location: &#123;&#125;,
      changeShowFestivals: false,
      changeShowWeather: false,
      visibleFullDateView: false,
      date: new Date(),
      visibleECSub: false,
      events: [] as EventInput[],
      event: null as EventInput,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>yarn lint</code> 看看：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14aebe5fe74143f3b9f694e9a5208dab~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>瞬间少了几个了。</p>
<h2 data-id="heading-1">小结</h2>
<p>这两天确实坚持到了极限了，本来还想继续优化，把所有的 warning 都消灭了，但有点顶了。估计从明天开始需要好好休息放空几天了。</p>
<p>这一阶段告一段落！！！</p>
<blockquote>
<p>代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            