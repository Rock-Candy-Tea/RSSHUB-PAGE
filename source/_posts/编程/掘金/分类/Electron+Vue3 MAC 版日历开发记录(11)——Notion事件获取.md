
---
title: 'Electron+Vue3 MAC 版日历开发记录(11)——Notion事件获取'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 07:01:52 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第11天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关于 Notion 的使用，估计大家都不陌生，最近他们专门为 <code>Developer</code> 开放了 <code>API</code>，具体看<a href="https://developers.notion.com/" target="_blank" rel="nofollow noopener noreferrer">developers.notion.com/</a>。</p>
<p>本项目在开发的时候，也想过如果结合开源，让其他伙伴也用起来，那事件的数据放在哪合适，因为本身事件包含的字段和结构相对复杂，总不能用 Vuex state 去关联。同时，也不想着把大家的数据放到我的服务器数据库中，相对开源项目，大家还是想着独立性更高。</p>
<p>所以，基于以上的思考，再结合之前用过一段时间的 Notion，发现可以以全新的 Notion API，尝试将数据同步到自己的 Notion 中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/191c4f075621411a852bed5532449e37~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">使用 Notion API</h2>
<h3 data-id="heading-1">1. 创建 integration.</h3>
<ul>
<li>Go to <a href="https://www.notion.com/my-integrations" target="_blank" rel="nofollow noopener noreferrer">www.notion.com/my-integrat…</a>.</li>
<li>Click the "+ New integration" button.</li>
<li>Give your integration a name - I chose "Vacation Planner".</li>
<li>Select the workspace where you want to install this integration.</li>
<li>Click "Submit" to create the integration.</li>
<li>Copy the "Internal Integration Token" on the next page and save it somewhere secure, e.g. a password manager.</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52477b96a3c5474faf6cb9e3fe1e4769~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点下一步会生成一个：<code>Internal Integration Token</code>，这里需要注意的是你的 integrations 是不是公开的。</p>
<p>创建好的个人 Integration 查看链接：<a href="https://www.notion.so/my-integrations" target="_blank" rel="nofollow noopener noreferrer">www.notion.so/my-integrat…</a>。</p>
<h3 data-id="heading-2">2. Share a database with your integration</h3>
<p>在我们的 workspace 创建一个用于存储事件数据的数据库： <code>/table</code>，然后再点 <code>share</code> 把数据库分享给我们创建的 <code>integration</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a54013b55ef4e08a5e884e318643109~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时，需要拿到此 table 的 32 位 ID，后面需要用到。</p>
<h3 data-id="heading-3">Step 3: 创建数据并获取</h3>
<p>根据 FullCalendar 提供的事件 Demo 和字段，我们直接在 Notion table 上模拟几条事件数据：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2e53584b5b64999ab244631683c77c9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们使用 Postman 模拟获取数据：</p>
<pre><code class="copyable">  curl -X POST 'https://api.notion.com/v1/databases/577b3228cd1*******87d601/query' \
  -H 'Authorization: Bearer secret_OeWua2be357D**********' \
  -H 'Notion-Version: 2021-05-13' \
  -H "Content-Type: application/json"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f8bc734249f473ea254d9e09f49f430~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，我们拿到的 <code>json</code> 中的 <code>result</code> 已经拿到了这三条数据了。</p>
<p>再打开看每一条数据结构：</p>
<pre><code class="copyable">&#123;
    "object": "page",
    "id": "72ba9-9b57-4859-9ab3-d7eaf",
    "created_time": "2021-06-11T03:31:41.534Z",
    "last_edited_time": "2021-06-11T14:31:00.000Z",
    "parent": &#123;
        "type": "database_id",
        "database_id": "5778-cd15-4117-8243-0fe601"
    &#125;,
    "archived": false,
    "properties": &#123;
        "title": &#123;
            "id": "Whai",
            "type": "rich_text",
            "rich_text": [
                &#123;
                    "type": "text",
                    "text": &#123;
                        "content": "使用 Notion API 存储数据",
                        "link": null
                    &#125;,
                    "annotations": &#123;
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    &#125;,
                    "plain_text": "使用 Notion API 存储数据",
                    "href": null
                &#125;
            ]
        &#125;,
        "event_id": &#123;
            "id": "jv^r",
            "type": "number",
            "number": 2
        &#125;,
        "end": &#123;
            "id": "p:bR",
            "type": "date",
            "date": &#123;
                "start": "2021-06-12",
                "end": null
            &#125;
        &#125;,
        "start": &#123;
            "id": "wh^E",
            "type": "date",
            "date": &#123;
                "start": "2021-06-12",
                "end": null
            &#125;
        &#125;,
        "id": &#123;
            "id": "title",
            "type": "title",
            "title": [
                &#123;
                    "type": "text",
                    "text": &#123;
                        "content": "2",
                        "link": null
                    &#125;,
                    "annotations": &#123;
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    &#125;,
                    "plain_text": "2",
                    "href": null
                &#125;
            ]
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体根据每个属性的 type 获取对应的值。</p>
<h3 data-id="heading-4">4. 代码实现</h3>
<p>具体实现，我们看 <code>EventService.ts</code>:</p>
<pre><code class="copyable">'use strict';
import axios from 'axios';
import wrapper from 'axios-cache-plugin';
export default class EventService &#123;
  async getEvents() &#123;
    const http = wrapper(axios, &#123;
      maxCacheSize: 15,
      ttl: 60000, //ms
    &#125;);
    http.__addFilter(/weatherdata/);

    const headers = &#123;
      'Notion-Version': '2021-05-13',
      'Authorization': 'Bearer '+ import.meta.env.VITE_NOTION_KEY
    &#125;;

    const res = await http(&#123;
      url: import.meta.env.VITE_NOTION_DATABASE_API + import.meta.env.VITE_NOTION_DATABASE_ID + '/query',
      method: 'post',
      headers: headers,
    &#125;);

    return this.list2Events(res.data.results);
  &#125;

  // &#123;"id": 5,"title": "Conference","start": "2021-04-11","end": "2021-04-13"&#125;,
  list2Events(results: []) &#123;
    const events = results.map((element) => &#123;
      return &#123;
        'id': element.properties.event_id.number,
        'title': element.properties.title.rich_text[0].plain_text,
        'start': element.properties.start.date.start,
        'end': element.properties.end?.date.start,
      &#125;
    &#125;);

    return events;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码没对异常情况做处理，基本通过正常逻辑将 <code>Notion</code> 数据转为 Event 数据。</p>
<h2 data-id="heading-5">显示</h2>
<p>有了数据以后，就可以在页面上呈现了，看过之前代码的伙伴肯定不陌生了：</p>
<pre><code class="copyable">// FullcalendarSub.vue
<template>
  <Fullcalendar
    ref="fullcalendar"
    :events="events"
    :options="calendarOptions"
  />
</template>

...

import EventService from '../../../services/EventService';

...

setup() &#123;
    onMounted(() => &#123;
      eventService.value.getEvents().then((data) => (events.value = data));
    &#125;);
    
    const events = ref([]);
    const eventService = ref(new EventService());
    return &#123;
      events,
      eventService,
    &#125;;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果显示如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce126f66fb7344aea34873320ec5dfab~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">小结</h2>
<p>今天主要代码功能是：同步 <code>Notion database</code> 数据到日历上呈现。</p>
<p>明天我们继续在客户端创建 <code>Event</code>，并保存到 <code>Notion</code> 上。</p>
<blockquote>
<p>所有用到的 <code>Internal Integration Token</code>、<code>database_id</code> 等数据都保存到 <code>.env</code> 里。</p>
</blockquote>
<p>未完待续！</p>
<blockquote>
<p>这个项目的所有记录基本放进专栏里了，欢迎查看：</p>
</blockquote>
<p><a href="https://juejin.cn/column/6968672386895839269" target="_blank">Electron+Vue3 MAC 版日历开发记录</a></p>
<blockquote>
<p>最近有伙伴问代码链接：代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            