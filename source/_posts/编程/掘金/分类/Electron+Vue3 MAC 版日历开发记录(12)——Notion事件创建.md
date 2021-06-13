
---
title: 'Electron+Vue3 MAC 版日历开发记录(12)——Notion事件创建'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 07:28:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第12天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过昨天的动手 (<a href="https://juejin.cn/post/6972551210993713188" target="_blank">Electron+Vue3 MAC 版日历开发记录(11)——Notion事件获取</a>)，关于 Notion 的使用，估计大家都不陌生。</p>
<p>今天我们将继续学习使用 Notion API，用于创建「事件」。</p>
<h2 data-id="heading-0">Notion API 使用</h2>
<p>要创建一条 Event 事件记录，在 Notion 里对应的是一条 Page。</p>
<blockquote>
<p>Pages are used as items inside a database, and each page's properties must conform to it's parent database's schema. In other words, if you're viewing a database as a table, a page's properties define all the values in a single row.</p>
<p>可查看<a href="https://developers.notion.com/docs/working-with-databases" target="_blank" rel="nofollow noopener noreferrer">具体教程</a></p>
</blockquote>
<p>下面我们借助 <code>Postman</code> 向服务 <code>post</code>一条记录，具体如下 (在截稿之前，我把<code>event_id</code>属性移除了)：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6de14a2c3c745df8b7c7b37351a3286~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>结果直接返回 <code>page object</code>，同时在 Notion 后台也能看到此条记录：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/265f70ddfcac4f1bae40b22c26e1912c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在列表中也能看到这条记录了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/678d70bb8e8d44c3a644bde7e5688a59~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">创建 <code>postEvent</code> 函数</h2>
<p>根据 Postman 的模拟，我们直接用代码实现：</p>
<pre><code class="copyable">// EventService.ts
'use strict';
import axios from 'axios';
import wrapper from 'axios-cache-plugin';
export default class EventService &#123;
  headers: any;
  constructor() &#123;
    this.headers = &#123;
      'Notion-Version': import.meta.env.VITE_NOtion_VERSION,
      'Authorization': 'Bearer '+ import.meta.env.VITE_NOTION_KEY,
    &#125;;
  &#125;

  /**
   * 提交title和start、end 到 Notion API
   */
  async postEvent(
    title: string,
    start: Date,
    end: Date,
    ) &#123;
      const http = wrapper(axios, &#123;
        maxCacheSize: 15,
      &#125;);
      const res = await http(&#123;
        url: import.meta.env.VITE_NOTION_PAGE_API,
        method: 'post',
        headers: this.headers,
        data: &#123;
          'parent': &#123; 'type': 'database_id', 'database_id': import.meta.env.VITE_NOTION_DATABASE_ID &#125;,
          'properties': &#123;
            'title': &#123;
              'type': 'rich_text',
              'rich_text': [&#123;
                'type': 'text',
                'text': &#123; 'content': title &#125;,
              &#125;],
            &#125;,
            'start': &#123;
              'type': 'date',
              'date': &#123; 'start': start &#125;,
            &#125;,
            'end': &#123;
              'type': 'date',
              'date': &#123; 'start': end &#125;,
            &#125;,
          &#125;,
        &#125;,
      &#125;);

      return res.data;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码就很简单了，只要提供 <code>event</code> 的 <code>title</code>、<code>start</code>、<code>end</code> 三个字段即可。</p>
<p>其中我们在 <code>env</code> 增加了：</p>
<pre><code class="copyable">// .env
VITE_NOtion_VERSION=2021-05-13
VITE_NOTION_DATABASE_API=https://api.notion.com/v1/databases/
VITE_NOTION_PAGE_API=https://api.notion.com/v1/pages
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">增加创建页面</h2>
<p>之前我一直使用 <code>Sidebar</code> 组件，这里我使用了对话框组件 (<a href="https://primefaces.org/primevue/showcase/#/dialog" target="_blank" rel="nofollow noopener noreferrer"><code>Dialog</code></a>)：</p>
<pre><code class="copyable">// EventCreateDialog.vue

<template>
  <Dialog
    v-model:visible="eventDialogVisible"
    :modal="true"
    @click="$emit('update:visibleFullDialog', eventDialogVisible)"
  >
    <template #header>
      <h3>创建事件</h3>
    </template>
    <div class="p-fluid">
      <div class="p-field">
        <label for="eventInput">事件内容</label>
        <InputText
          id="eventInput"
          v-model="eventText"
          type="text"
        />
      </div>
    </div>
    <div class="p-fluid p-formgrid p-grid">
      <Calendar
        id="range"
        v-model="dates"
        date-format="MM d,yy"
        ::minDate="Date()"
        selection-mode="range"
        :inline="true"
      />
    </div>
    <template #footer>
      <Button
        label="取消"
        icon="pi pi-times"
        class="p-button-text"
        @click="$emit('update:visibleFullDialog', false)"
      />
      <Button
        label="确定"
        icon="pi pi-check"
        autofocus
        @click="add"
      />
    </template>
  </Dialog>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码不用多说了，直接看界面效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6db834467ec4d0d827eb4c5826e7a28~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里主要还用到了 <code>Calendar</code> 组件，关键用到的属性是：<code>selection-mode="range"</code>，可以手动选择事件的时间段，这样可以减少一个控件，直接拿到 <code>start</code> 和 <code>end</code> 两个值：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce8680c06f0c495f8a375939edd44c09~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了数据了，就直接调用函数：</p>
<pre><code class="copyable">add(): void &#123;
  const start: Date = this.dates[0];
  const end: Date = this.dates[1] == null ? this.dates[0] : this.dates[1];

  this.eventService.postEvent(this.eventText, start, end)
    .then(() => &#123;
      this.dates = [];
      this.eventText = '';
    &#125;);
  this.$emit('update:visibleFullDialog', false);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">增加 Menu 入口</h2>
<p>由于功能越来越多，需要操作的动作和入口也持续增多，所以我把之前的「设置」按钮变成了<a href="https://primefaces.org/primevue/showcase/#/menu" target="_blank" rel="nofollow noopener noreferrer">「目录」功能</a>，具体看代码：</p>
<pre><code class="copyable">// FullCalendarMain.vue

<event-create-dialog
  v-model:visibleFullDialog="visibleFullDialog"
/>
<Menu
  id="overlay_tmenu"
  ref="menu"
  :model="items"
  :popup="true"
/>

...

items: [
    &#123;
      label:'操作',
      icon:'pi pi-fw pi-pencil',
      items:[
        &#123;
          label:'创建事件',
          icon:'pi pi-fw pi-plus',
          command: this.goCreateEventView,
        &#125;,
        &#123;
          label:'设置',
          icon:'pi pi-fw pi-cog',
          command: this.goSettingView,
        &#125;,
        &#123;
          separator:true,
        &#125;,
        &#123;
          label:'退出应用',
          icon:'pi pi-fw pi-power-off',
          command: this.quit,
        &#125;,
      ],
    &#125;,
],

...

goCreateEventView(): void &#123;
  this.visibleFullDialog = true;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>入口如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d5b9ee8e064abab2d0bcd6761d9319~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">小结</h2>
<p>好了，从目录中增加创建事件的入口，到事件创建界面，到网络请求，最后验证数据是否保存到 Notion 数据库中，到此，基本完成了 <code>增加事件功能</code>。增加一条记录后，页面和 Notion 后台能实时看到效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ebac7d7296a4307a03a39c2c7317f72~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c94da98834ef4fbab9413156e26ac448~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于整个过程中的边界问题都需要接下来一一处理，如：Event 事件功能如何与「亲朋好友的生日提醒」等相结合；如何把 Event 事件展示在其他页面上；以及删除 Event 事件和同步更新到 Notion 里。未完待续！</p>
<blockquote>
<p>这个项目的所有记录基本放进专栏里了，欢迎查看：
<a href="https://juejin.cn/column/6968672386895839269" target="_blank">Electron+Vue3 MAC 版日历开发记录</a>
最近有伙伴问代码链接：代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            